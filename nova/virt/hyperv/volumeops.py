# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 Pedro Navarro Perez
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Management class for Storage-related functions (attach, detach, etc).
"""
import uuid
import time

from nova import flags
from nova import log as logging
from nova import utils
from _winreg import (HKEY_LOCAL_MACHINE, KEY_ALL_ACCESS,
                     OpenKey, CloseKey, QueryValueEx)

LOG = logging.getLogger(__name__)

FLAGS = flags.FLAGS

WMI_JOB_STATUS_STARTED = 4096

WMI_JOB_STATUS_STARTED = 4096
WMI_JOB_STATE_RUNNING = 4
WMI_JOB_STATE_COMPLETED = 7

class VolumeOps(object):
    """
    Management class for Volume-related tasks
    """

    def __init__(self,wmi):
        self._initiator = None
        self._wmi = wmi
        self._cim_conn = wmi.WMI(moniker='//./root/cimv2')
        self._wmi_conn = wmi.WMI(moniker='//./root/wmi')
        self._conn = wmi.WMI(moniker='//./root/virtualization')
    
    def attach_volume(self, connection_info, instance_name, mountpoint):
        LOG.debug(_("Attach_volume: %(connection_info)s, %(instance_name)s,"
        " %(mountpoint)s") % locals())
        data = connection_info['data']
        target_lun = data['target_lun']
        target_iqn = data['target_iqn']
        target_portal = data['target_portal']
        separator = target_portal.find(':')
        target_address = target_portal[:separator]
        target_port = target_portal[separator + 1:]
        #Adding target portal to iscsi initiator. Sending targets
        utils.execute('iscsicli.exe','AddTargetPortal',target_address,target_port,'*',
                      '*','*','*','*','*','*','*','*','*','*','*',close_fds=False)
        #Listing targets
        utils.execute('iscsicli.exe','LisTargets',close_fds=False)
        #Sending login
        utils.execute('iscsicli.exe','qlogintarget',target_iqn, close_fds=False)
        #Waiting the disk to be mounted. Research this
        time.sleep(2)
        #Getting the mounted disk
        mounted_disk = self._get_mounted_disk_from_lun(target_iqn, target_lun)
        #Find the SCSI controller for the vm
        vms = self._conn.MSVM_ComputerSystem(ElementName=instance_name)
        vm = vms[0]
        vmsettings = vm.associators(
                wmi_result_class='Msvm_VirtualSystemSettingData')
        rasds = vmsettings[0].associators(
                wmi_result_class='MSVM_ResourceAllocationSettingData')
        ctrller = [r for r in rasds
                   if r.ResourceSubType == 'Microsoft Synthetic SCSI Controller']
        #Getting the physical disk mounted
        diskdflt = self._conn.query(
                "SELECT * FROM Msvm_ResourceAllocationSettingData \
                WHERE ResourceSubType LIKE 'Microsoft Physical Disk Drive'\
                AND InstanceID LIKE '%Default%'")[0]
        diskdrive = self._clone_wmi_obj(
                'Msvm_ResourceAllocationSettingData', diskdflt)
        diskdrive.Address = self._get_free_controller_slot(ctrller[0])
        diskdrive.Parent = ctrller[0].path_()
        diskdrive.HostResource = [mounted_disk[0].path_()]
        new_resources = self._add_virt_resource(diskdrive, vm)
        if new_resources is None:
            raise Exception(_('Failed to add volume to VM %s'),
                                             instance_name)
    def _get_free_controller_slot (self, scsi_controller):
        #Getting volumes mounted in the SCSI controller
        volumes = self._conn.query(
                "SELECT * FROM Msvm_ResourceAllocationSettingData \
                WHERE ResourceSubType LIKE 'Microsoft Physical Disk Drive'\
                AND Parent = '" +  scsi_controller.path_() + "'")
        #Slots starts from 0, so the lenght of the disks gives us the free slot
        return len (volumes)
        
    def detach_volume(self, connection_info, instance_name, mountpoint):
        LOG.debug(_("Detach_volume: %(connection_info)s, %(instance_name)s,"
        " %(mountpoint)s") % locals())
        data = connection_info['data']
        target_lun = data['target_lun']
        target_iqn = data['target_iqn']
        #Getting the mounted disk
        mounted_disk = self._get_mounted_disk_from_lun(target_iqn, target_lun)
        physical_list = self._conn.query(
                "SELECT * FROM Msvm_ResourceAllocationSettingData \
                WHERE ResourceSubType LIKE 'Microsoft Physical Disk Drive'")
        physical_disk = 0
        for phydisk in physical_list:
            host_resource_list = phydisk.HostResource
            if host_resource_list == None:
                continue
            host_resource = str(host_resource_list[0].lower())
            mounted_disk_path = str(mounted_disk[0].path_().lower())
            LOG.debug(_("Mounted disk to detach is: %s"),mounted_disk_path)
            LOG.debug(_("host_resource disk detached is: %s"),host_resource)   
            if host_resource == mounted_disk_path:
                physical_disk = phydisk
        LOG.debug(_("Physical disk detached is: %s"),physical_disk)           
        vms = self._conn.MSVM_ComputerSystem(ElementName=instance_name)
        vm = vms[0]
        remove_result = self._remove_virt_resource(physical_disk, vm)
        if remove_result is False:
            raise Exception(_('Failed to remove volume from VM %s'),instance_name)
        #Sending logout
        initiator_session = self._wmi_conn.query(
                "SELECT * FROM MSiSCSIInitiator_SessionClass \
                WHERE TargetName='" + target_iqn + "'")[0]
        session_id = initiator_session.SessionId
        utils.execute('iscsicli.exe','logouttarget',session_id, close_fds=False)
    
    def get_volume_connector(self, instance):
        if not self._initiator:
            self._initiator = self._get_iscsi_initiator()
            if not self._initiator:
                LOG.warn(_('Could not determine iscsi initiator name'),
                         instance=instance)
        return {
            'ip': FLAGS.my_ip,
            'initiator': self._initiator,
        }
    
    def _get_iscsi_initiator(self):
        computer_system = self._cim_conn.Win32_ComputerSystem()[0]
        hostname = computer_system.name
        keypath = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\iSCSI\Discovery"
        try:
            key = OpenKey(HKEY_LOCAL_MACHINE, keypath, 0, KEY_ALL_ACCESS)
            temp = QueryValueEx(key, 'DefaultInitiatorName')
            initiator_name = str(temp[0])
            CloseKey(key) 
        except:
            LOG.info(_("The ISCSI initiator name can't be found. Choosing the default one"))
            computer_system = self._cim_conn.Win32_ComputerSystem()[0]
            initiator_name = "iqn.1991-05.com.microsoft:" + hostname.lower()
        return {
            'ip': FLAGS.my_ip,
            'initiator': initiator_name,
        }
    
    def _get_mounted_disk_from_lun(self,target_iqn,target_lun):
        initiator_session = self._wmi_conn.query(
                "SELECT * FROM MSiSCSIInitiator_SessionClass \
                WHERE TargetName='" + target_iqn + "'")[0]
        session_id = initiator_session.SessionId
        devices = initiator_session.Devices
        device_number = None
        for device in devices:
            LOG.debug(_("device.InitiatorName: %s"),device.InitiatorName)
            LOG.debug(_("device.TargetName: %s"),device.TargetName)
            LOG.debug(_("device.ScsiPortNumber: %s"),device.ScsiPortNumber)
            LOG.debug(_("device.ScsiPathId: %s"),device.ScsiPathId)
            LOG.debug(_("device.ScsiTargetId): %s"),device.ScsiTargetId)
            LOG.debug(_("device.ScsiLun: %s"),device.ScsiLun)
            LOG.debug(_("device.DeviceInterfaceGuid :%s"),device.DeviceInterfaceGuid)
            LOG.debug(_("device.DeviceInterfaceName: %s"),device.DeviceInterfaceName)
            LOG.debug(_("device.LegacyName: %s"),device.LegacyName)
            LOG.debug(_("device.DeviceType: %s"),device.DeviceType)
            LOG.debug(_("device.DeviceNumber %s"),device.DeviceNumber)
            LOG.debug(_("device.PartitionNumber :%s"),device.PartitionNumber)
            scsi_lun = device.ScsiLun
            if scsi_lun == target_lun:
                device_number = device.DeviceNumber
        if device_number == None:
            raise Exception(_('Unable to find a mounted disk for'
                  ' instance %(instance_name)s') % locals())
        LOG.debug(_("Device number : %s"),device_number)
        LOG.debug(_("Target lun : %s"),target_lun)
        #Finding Mounted disk drive
        mounted_disk = self._conn.query(
                "SELECT * FROM Msvm_DiskDrive WHERE DriveNumber='" + str(device_number) + "'")
        return mounted_disk
    
    def disconnect_volume(self, physical_drive_path):
        #Get the session_id of the ISCSI connection
        session_id = self._get_session_id_from_mounted_disk(physical_drive_path)
        #Logging out the target
        utils.execute('iscsicli.exe','logouttarget',session_id, close_fds=False)

    def _get_session_id_from_mounted_disk(self, physical_drive_path):
        drive_number = self._get_drive_number_from_disk_path(physical_drive_path)
        LOG.debug(_("Drive number to disconnect is: %s"),drive_number)
        initiator_sessions = self._wmi_conn.query(
                "SELECT * FROM MSiSCSIInitiator_SessionClass")
        for initiator_session in initiator_sessions:
            devices = initiator_session.Devices
            for device in devices:
                deviceNumber = str(device.DeviceNumber)
                LOG.debug(_("DeviceNumber : %s"),deviceNumber) 
                if deviceNumber ==  drive_number:
                    return initiator_session.SessionId
    
    def _get_drive_number_from_disk_path(self, disk_path):
        LOG.debug(_("Disk path to parse: %s"),disk_path)
        start_device_id = disk_path.find('"',disk_path.find('DeviceID'))
        LOG.debug(_("start_device_id: %s"),start_device_id)
        end_device_id = disk_path.find('"', start_device_id +1)
        LOG.debug(_("end_device_id: %s"),end_device_id)
        deviceID = disk_path[start_device_id + 1:end_device_id]
        return deviceID[deviceID.find("\\")+2:]
                
    def _clone_wmi_obj(self, wmi_class, wmi_obj):
        """Clone a WMI object"""
        cl = self._conn.__getattr__(wmi_class)  # get the class
        newinst = cl.new()
        #Copy the properties from the original.
        for prop in wmi_obj._properties:
            if prop == "VirtualSystemIdentifiers":
                strguid=[]
                strguid.append(str(uuid.uuid4()))
                newinst.Properties_.Item(prop).Value=strguid
            else:
                newinst.Properties_.Item(prop).Value = \
                    wmi_obj.Properties_.Item(prop).Value
        return newinst
    
    #Move to utils class
    def _add_virt_resource(self, res_setting_data, target_vm):
        """Add a new resource (disk/nic) to the VM"""
        vs_man_svc = self._conn.Msvm_VirtualSystemManagementService()[0]
        (job, new_resources, ret_val) = vs_man_svc.\
                    AddVirtualSystemResources([res_setting_data.GetText_(1)],
                                                target_vm.path_())
        success = True
        if ret_val == WMI_JOB_STATUS_STARTED:
            success = self._check_job_status(job)
        else:
            success = (ret_val == 0)
        if success:
            return new_resources
        else:
            return None
    
    def _remove_virt_resource(self, res_setting_data, target_vm):
        """Add a new resource (disk/nic) to the VM"""
        vs_man_svc = self._conn.Msvm_VirtualSystemManagementService()[0]
        (job, ret_val) = vs_man_svc.\
                    RemoveVirtualSystemResources([res_setting_data.path_()],
                                                target_vm.path_())
        success = True
        if ret_val == WMI_JOB_STATUS_STARTED:
            success = self._check_job_status(job)
        else:
            success = (ret_val == 0)
        return success
    
    def _check_job_status(self, jobpath):
        """Poll WMI job state for completion"""
        #Jobs have a path of the form:
        #\\WIN-P5IG7367DAG\root\virtualization:Msvm_ConcreteJob.InstanceID=
        #"8A496B9C-AF4D-4E98-BD3C-1128CD85320D"
        ##inst_id = jobpath.split('=')[1].strip('"')
        ##jobs = self._conn.Msvm_ConcreteJob(InstanceID=inst_id)
        ##if len(jobs) == 0:
        ##    return False
        ##job = jobs[0]
        job_wmi_path = jobpath.replace('\\','/')
        job = self._wmi.WMI(moniker=job_wmi_path)
            
        while job.JobState == WMI_JOB_STATE_RUNNING:
            time.sleep(0.1)
            job = self._wmi.WMI(moniker=job_wmi_path)
        if job.JobState != WMI_JOB_STATE_COMPLETED:
            LOG.debug(_("WMI job failed: %s - %s - %s"), job.ErrorSummaryDescription, job.ErrorDescription, job.ErrorCode)
            return False
        desc = job.Description
        elap = job.ElapsedTime
        LOG.debug(_("WMI job succeeded: %(desc)s, Elapsed=%(elap)s ")
                % locals())
        return True
                    
        
