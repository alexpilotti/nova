# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright (c) 2010 Cloud.com, Inc
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
A connection to Hyper-V .
Uses Windows Management Instrumentation (WMI) calls to interact with Hyper-V
Hyper-V WMI usage:
    http://msdn.microsoft.com/en-us/library/cc723875%28v=VS.85%29.aspx
The Hyper-V object model briefly:
    The physical computer and its hosted virtual machines are each represented
    by the Msvm_ComputerSystem class.

    Each virtual machine is associated with a
    Msvm_VirtualSystemGlobalSettingData (vs_gs_data) instance and one or more
    Msvm_VirtualSystemSettingData (vmsetting) instances. For each vmsetting
    there is a series of Msvm_ResourceAllocationSettingData (rasd) objects.
    The rasd objects describe the settings for each device in a VM.
    Together, the vs_gs_data, vmsettings and rasds describe the configuration
    of the virtual machine.

    Creating new resources such as disks and nics involves cloning a default
    rasd object and appropriately modifying the clone and calling the
    AddVirtualSystemResources WMI method
    Changing resources such as memory uses the ModifyVirtualSystemResources
    WMI method

Using the Python WMI library:
    Tutorial:
        http://timgolden.me.uk/python/wmi/tutorial.html
    Hyper-V WMI objects can be retrieved simply by using the class name
    of the WMI object and optionally specifying a column to filter the
    result set. More complex filters can be formed using WQL (sql-like)
    queries.
    The parameters and return tuples of WMI method calls can gleaned by
    examining the doc string. For example:
    >>> vs_man_svc.ModifyVirtualSystemResources.__doc__
    ModifyVirtualSystemResources (ComputerSystem, ResourceSettingData[])
                 => (Job, ReturnValue)'
    When passing setting data (ResourceSettingData) to the WMI method,
    an XML representation of the data is passed in using GetText_(1).
    Available methods on a service can be determined using method.keys():
    >>> vs_man_svc.methods.keys()
    vmsettings and rasds for a vm can be retrieved using the 'associators'
    method with the appropriate return class.
    Long running WMI commands generally return a Job (an instance of
    Msvm_ConcreteJob) whose state can be polled to determine when it finishes

"""

import os
import time
import uuid
import platform
import shutil
import multiprocessing
import sys

from nova import exception
from nova import flags
from nova import log as logging
from nova.compute import power_state
from nova.virt import driver
from nova.virt import images
from nova import utils
from nova import db
from nova.openstack.common import cfg
from nova.virt.hyperv import volumeops
from nova.image import glance
from xml.etree import ElementTree


wmi = None

hyperv_opts = [
    cfg.StrOpt('vswitch_name',
                default=None,
                help='Default vSwitch Name, if none provided first external is used'),
    ]

FLAGS = flags.FLAGS
FLAGS.register_opts(hyperv_opts)


LOG = logging.getLogger(__name__)


HYPERV_POWER_STATE = {
    3: power_state.SHUTDOWN,
    2: power_state.RUNNING,
    32768: power_state.PAUSED,
    32769: power_state.SUSPENDED    
}


REQ_POWER_STATE = {
    'Enabled': 2,
    'Disabled': 3,
    'Reboot': 10,
    'Reset': 11,
    'Paused': 32768,
    'Suspended': 32769,
}


WMI_JOB_STATUS_STARTED = 4096
WMI_JOB_STATE_RUNNING = 4
WMI_JOB_STATE_COMPLETED = 7

def get_connection(read_only):
    global wmi
    if wmi is None:
        wmi = __import__('wmi')
    return HyperVConnection(read_only)


class HyperVConnection(driver.ComputeDriver):
    def __init__(self, read_only):
        super(HyperVConnection, self).__init__()
        self._conn = wmi.WMI(moniker='//./root/virtualization')
        self._cim_conn = wmi.WMI(moniker='//./root/cimv2')
        self._wmi_conn = wmi.WMI(moniker='//./root/wmi')

        version = self._get_windows_version()
        if version[0] >= 6 and version[1] >= 2:
            self._conn_v2 = wmi.WMI(moniker='//./root/virtualization/v2')
        else:
            self._conn_v2 = None

        self._volumeops = volumeops.VolumeOps(wmi)

    def _get_windows_version(self):
		return self._cim_conn.Win32_OperatingSystem()[0].Version.split('.')		

    def init_host(self, host):
        #FIXME(chiradeep): implement this
        self._host = host

    def list_instances(self):
        """ Return the names of all the instances known to Hyper-V. """
        vms = [v.ElementName \
                for v in self._conn.Msvm_ComputerSystem(['ElementName'], Caption="Virtual Machine")]
        return vms

    def list_instances_detail(self):
        # TODO(justinsb): This is a terrible implementation (1+N)
        instance_infos = []
        for instance_name in self.list_instances():
            info = self.get_info(instance_name)

            state = info['state']

            instance_info = driver.InstanceInfo(instance_name, state)
            instance_infos.append(instance_info)

        return instance_infos

    def spawn(self, context, instance, image_meta,
              network_info, block_device_info=None):
        """ Create a new VM and start it."""
        vm = self._lookup(instance.name)
        if vm is not None:
            raise exception.InstanceExists(name=instance.name)
        
        ebs_root = self._volumeops._volume_in_mapping(self._volumeops.get_default_root_device(),
                               block_device_info)
        
        #If is not a boot from volume spawn 
        if not (ebs_root):
            #Fetch the file, assume it is a VHD file.
            base_vhd_folder = os.path.join(FLAGS.instances_path, instance.name)
            if not os.path.exists(base_vhd_folder):
                    LOG.debug(_('Creating folder %s '), base_vhd_folder)
                    os.mkdir(base_vhd_folder)
            vhdfile = os.path.join(base_vhd_folder, instance.name + ".vhd")
            try:
                self._cache_image(self, fn=self._fetch_image,
                  context=context,
                  target=vhdfile,
                  fname=instance['image_ref'],
                  image_id=instance['image_ref'],
                  user=instance['user_id'],
                  project=instance['project_id'],
                  cow=FLAGS.use_cow_images)
            except Exception as exn:
                LOG.exception(_('cache image failed: %s'), exn)
                self.destroy(instance)
        
        try:
            self._create_vm(instance)

            if not ebs_root :
                self._create_disk(instance['name'], vhdfile)
            else:
                self._volumeops.attach_boot_volume(block_device_info,
                                             instance.name)
            
            #A SCSI controller for volumes connection is created 
            self._create_scsi_controller(instance['name'])
          
            for (network, mapping) in network_info:
                mac_address = mapping['mac'].replace(':', '')
                
            self._create_nic(instance['name'], mac_address)

            LOG.debug(_('Starting VM %s '), instance.name)
            self._set_vm_state(instance['name'], 'Enabled')
            LOG.info(_('Started VM %s '), instance.name)
        except Exception as exn:
            LOG.exception(_('spawn vm failed: %s'), exn)
            self.destroy(instance)

    def _create_vm(self, instance):
        """Create a VM but don't start it.  """
        vs_man_svc = self._conn.Msvm_VirtualSystemManagementService()[0]

        vs_gs_data = self._conn.Msvm_VirtualSystemGlobalSettingData.new()
        vs_gs_data.ElementName = instance['name']
        (job, ret_val) = vs_man_svc.DefineVirtualSystem(
                [], None, vs_gs_data.GetText_(1))[1:]
        if ret_val == WMI_JOB_STATUS_STARTED:
            success = self._check_job_status(job)
        else:
            success = (ret_val == 0)

        if not success:
            raise Exception(_('Failed to create VM %s'), instance.name)

        LOG.debug(_('Created VM %s...'), instance.name)
        vm = self._conn.Msvm_ComputerSystem(ElementName=instance.name)[0]

        vmsettings = vm.associators(
                          wmi_result_class='Msvm_VirtualSystemSettingData')
        vmsetting = [s for s in vmsettings
                        if s.SettingType == 3][0]  # avoid snapshots
        memsetting = vmsetting.associators(
                           wmi_result_class='Msvm_MemorySettingData')[0]
        #No Dynamic Memory, so reservation, limit and quantity are identical.
        mem = long(str(instance['memory_mb']))
        memsetting.VirtualQuantity = mem
        memsetting.Reservation = mem
        memsetting.Limit = mem

        (job, ret_val) = vs_man_svc.ModifyVirtualSystemResources(
                vm.path_(), [memsetting.GetText_(1)])
        LOG.debug(_('Set memory for vm %s...'), instance.name)
        procsetting = vmsetting.associators(
                wmi_result_class='Msvm_ProcessorSettingData')[0]
        vcpus = long(instance['vcpus'])
        procsetting.VirtualQuantity = vcpus
        procsetting.Reservation = vcpus
        procsetting.Limit = 100000  # static assignment to 100%

        if FLAGS.limit_cpu_features:
            procsetting.LimitProcessorFeatures = True

        (job, ret_val) = vs_man_svc.ModifyVirtualSystemResources(
                vm.path_(), [procsetting.GetText_(1)])
        LOG.debug(_('Set vcpus for vm %s...'), instance.name)
        
    def _create_scsi_controller (self,vm_name):
        """ Create an iscsi controller ready to mount volumes """
        LOG.debug(_('Creating a scsi controller for %(vm_name)s for volume '\
                'attaching') % locals())
        vms = self._conn.MSVM_ComputerSystem(ElementName=vm_name)
        vm = vms[0]
        scsicontrldefault = self._conn.query(
                "SELECT * FROM Msvm_ResourceAllocationSettingData \
                WHERE ResourceSubType = 'Microsoft Synthetic SCSI Controller'\
                AND InstanceID LIKE '%Default%'")[0]
        if scsicontrldefault is None:
            raise Exception(_('Controller not found'))
        scsicontrl = self._clone_wmi_obj(
                'Msvm_ResourceAllocationSettingData', scsicontrldefault)
        scsicontrl.VirtualSystemIdentifiers = ['{' + str(uuid.uuid4()) + '}']
        scsiresource = self._add_virt_resource(scsicontrl, vm)
        if scsiresource is None:
            raise Exception(_('Failed to add scsi controller to VM %s'),vm_name)      
        
    def _create_disk(self, vm_name, vhdfile):
        """Create a disk and attach it to the vm"""
        LOG.debug(_('Creating disk for %(vm_name)s by attaching'
                ' disk file %(vhdfile)s') % locals())
        #Find the IDE controller for the vm.
        vms = self._conn.MSVM_ComputerSystem(ElementName=vm_name)
        vm = vms[0]
        vmsettings = vm.associators(
                wmi_result_class='Msvm_VirtualSystemSettingData')
        rasds = vmsettings[0].associators(
                wmi_result_class='MSVM_ResourceAllocationSettingData')
        ctrller = [r for r in rasds
                   if r.ResourceSubType == 'Microsoft Emulated IDE Controller'\
                   and r.Address == "0"]
        #Find the default disk drive object for the vm and clone it.
        diskdflt = self._conn.query(
                "SELECT * FROM Msvm_ResourceAllocationSettingData \
                WHERE ResourceSubType LIKE 'Microsoft Synthetic Disk Drive'\
                AND InstanceID LIKE '%Default%'")[0]
        diskdrive = self._clone_wmi_obj(
                'Msvm_ResourceAllocationSettingData', diskdflt)
        #Set the IDE ctrller as parent.
        diskdrive.Parent = ctrller[0].path_()
        diskdrive.Address = 0
        #Add the cloned disk drive object to the vm.
        new_resources = self._add_virt_resource(diskdrive, vm)
        if new_resources is None:
            raise Exception(_('Failed to add diskdrive to VM %s'),
                                             vm_name)
        diskdrive_path = new_resources[0]
        LOG.debug(_('New disk drive path is %s'), diskdrive_path)
        #Find the default VHD disk object.
        vhddefault = self._conn.query(
                "SELECT * FROM Msvm_ResourceAllocationSettingData \
                 WHERE ResourceSubType LIKE 'Microsoft Virtual Hard Disk' AND \
                 InstanceID LIKE '%Default%' ")[0]

        #Clone the default and point it to the image file.
        vhddisk = self._clone_wmi_obj(
                'Msvm_ResourceAllocationSettingData', vhddefault)
        #Set the new drive as the parent.
        vhddisk.Parent = diskdrive_path
        vhddisk.Connection = [vhdfile]

        #Add the new vhd object as a virtual hard disk to the vm.
        new_resources = self._add_virt_resource(vhddisk, vm)
        if new_resources is None:
            raise Exception(_('Failed to add vhd file to VM %s'),
                                             vm_name)
        LOG.info(_('Created disk for %s'), vm_name)

    def _create_nic(self, vm_name, mac):
        """Create a (synthetic) nic and attach it to the vm"""
        LOG.debug(_('Creating nic for %s '), vm_name)
        #Find the vswitch that is connected to the physical nic.
        vms = self._conn.Msvm_ComputerSystem(ElementName=vm_name)
        extswitch = self._find_external_network()
        vm = vms[0]
        switch_svc = self._conn.Msvm_VirtualSwitchManagementService()[0]
        #Find the default nic and clone it to create a new nic for the vm.
        #Use Msvm_SyntheticEthernetPortSettingData for Windows or Linux with
        #Linux Integration Components installed.
        syntheticnics_data = self._conn.Msvm_SyntheticEthernetPortSettingData()
        default_nic_data = [n for n in syntheticnics_data
                            if n.InstanceID.rfind('Default') > 0]
        new_nic_data = self._clone_wmi_obj(
                'Msvm_SyntheticEthernetPortSettingData',
                default_nic_data[0])
        #Create a port on the vswitch.
        (new_port, ret_val) = switch_svc.CreateSwitchPort(vm_name, vm_name,
                                            "", extswitch.path_())
        if ret_val != 0:
            LOG.error(_('Failed creating a port on the external vswitch'))
            raise Exception(_('Failed creating port for %s'),
                    vm_name)
        ext_path = extswitch.path_()
        LOG.debug(_("Created switch port %(vm_name)s on switch %(ext_path)s")
                % locals())
        #Connect the new nic to the new port.
        new_nic_data.Connection = [new_port]
        new_nic_data.ElementName = vm_name + ' nic'
        new_nic_data.Address = mac
        new_nic_data.StaticMacAddress = 'True'
        new_nic_data.VirtualSystemIdentifiers = ['{' + str(uuid.uuid4()) + '}']
        #Add the new nic to the vm.
        new_resources = self._add_virt_resource(new_nic_data, vm)
        if new_resources is None:
            raise Exception(_('Failed to add nic to VM %s'),
                    vm_name)
        LOG.info(_("Created nic for %s "), vm_name)

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
   
    #TODO: use the reactor to poll instead of sleep
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
        job = wmi.WMI(moniker=job_wmi_path)
        	
        while job.JobState == WMI_JOB_STATE_RUNNING:
            time.sleep(0.1)
            job = wmi.WMI(moniker=job_wmi_path)
        if job.JobState != WMI_JOB_STATE_COMPLETED:
            LOG.debug(_("WMI job failed: %s - %s - %s"), job.ErrorSummaryDescription, job.ErrorDescription, job.ErrorCode)
            return False
        desc = job.Description
        elap = job.ElapsedTime
        LOG.debug(_("WMI job succeeded: %(desc)s, Elapsed=%(elap)s ")
                % locals())
        return True

    def _find_external_network(self):
        """Find the vswitch that is connected to the physical nic.
           Assumes only one physical nic on the host
        """
        #If there are no physical nics connected to networks, return.
        LOG.debug(_("Attempting to bind NIC to %s ")
                % FLAGS.vswitch_name)
        if FLAGS.vswitch_name:
            LOG.debug(_("Attempting to bind NIC to %s ")
                % FLAGS.vswitch_name)
            bound = self._conn.Msvm_VirtualSwitch(ElementName=FLAGS.vswitch_name)
        else:
            LOG.debug(_("No vSwitch specified, attaching to default"))
            self._conn.Msvm_ExternalEthernetPort(IsBound='TRUE')
        if len(bound) == 0:
            return None
        if FLAGS.vswitch_name:
            return self._conn.Msvm_VirtualSwitch(ElementName=FLAGS.vswitch_name)[0]\
            .associators(wmi_result_class='Msvm_SwitchPort')[0]\
            .associators(wmi_result_class='Msvm_VirtualSwitch')[0]
        else:
            return self._conn.Msvm_ExternalEthernetPort(IsBound='TRUE')\
            .associators(wmi_result_class='Msvm_SwitchPort')[0]\
            .associators(wmi_result_class='Msvm_VirtualSwitch')[0]

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

    def reboot(self, instance, network_info, reboot_type):
        """Reboot the specified instance."""
        vm = self._lookup(instance.name)
        if vm is None:
            raise exception.InstanceNotFound(instance_id=instance.id)
        self._set_vm_state(instance.name, 'Reboot')

    def destroy(self, instance, network_info=None, cleanup=True):
        """Destroy the VM. Also destroy the associated VHD disk files"""
        LOG.debug(_("Got request to destroy vm %s"), instance.name)
        vm = self._lookup(instance.name)
        if vm is None:
            return
        vm = self._conn.Msvm_ComputerSystem(ElementName=instance.name)[0]
        vs_man_svc = self._conn.Msvm_VirtualSystemManagementService()[0]
        #Stop the VM first.
        self._set_vm_state(instance.name, 'Disabled')
        vmsettings = vm.associators(
                         wmi_result_class='Msvm_VirtualSystemSettingData')
        rasds = vmsettings[0].associators(
                         wmi_result_class='MSVM_ResourceAllocationSettingData')
        disks = [r for r in rasds \
                    if r.ResourceSubType == 'Microsoft Virtual Hard Disk']
        diskfiles = []
        volumes = [r for r in rasds \
                    if r.ResourceSubType == 'Microsoft Physical Disk Drive']
        volumes_drives_list = []
        #collect the volumes information before destroying the VM.
        for volume in volumes:
            hostResources = volume.HostResource
            drive_path = hostResources[0]
            #Appending the Msvm_Disk path
            volumes_drives_list.append(drive_path)
        #Collect disk file information before destroying the VM.
        for disk in disks:
            diskfiles.extend([c for c in disk.Connection])
        #Nuke the VM. Does not destroy disks.
        (job, ret_val) = vs_man_svc.DestroyVirtualSystem(vm.path_())
        if ret_val == WMI_JOB_STATUS_STARTED:
            success = self._check_job_status(job)
        elif ret_val == 0:
            success = True
        if not success:
            raise Exception(_('Failed to destroy vm %s') % instance.name)
        #Disconnect volumes
        for volume_drive in volumes_drives_list:
            self._volumeops.disconnect_volume(volume_drive)
        #Delete associated vhd disk files.
        for disk in diskfiles:
            vhdfile = self._cim_conn.CIM_DataFile(Name=disk)
            for vf in vhdfile:
                vf.Delete()
                instance_name = instance.name
                LOG.debug(_("Del: disk %(vhdfile)s vm %(instance_name)s")
                        % locals())

    def get_info(self, instance):
        """Get information about the VM"""
        LOG.debug(_("get_info called for instance: %s"), instance.name)
        vm = self._lookup(instance.name)
        if vm is None:
            raise exception.InstanceNotFound(instance=instance.name)
        vm = self._conn.Msvm_ComputerSystem(ElementName=instance.name)[0]
        vs_man_svc = self._conn.Msvm_VirtualSystemManagementService()[0]
        vmsettings = vm.associators(
                       wmi_association_class='Msvm_SettingsDefineState',
                       wmi_result_class='Msvm_VirtualSystemSettingData')
        settings_paths = [v.path_() for v in vmsettings]
        #See http://msdn.microsoft.com/en-us/library/cc160706%28VS.85%29.aspx
        summary_info = vs_man_svc.GetSummaryInformation(
                                       [4, 100, 103, 105], settings_paths)[1]
        info = summary_info[0]
               
        LOG.debug(_("hyperv vm state: %s"), info.EnabledState)       
        state = str(HYPERV_POWER_STATE[info.EnabledState])
        memusage = str(info.MemoryUsage)
        numprocs = str(info.NumberOfProcessors)
        uptime = str(info.UpTime)

        LOG.debug(_("Got Info for vm %s: state=%s,"
                " mem=%s, num_cpu=%s,"
                " cpu_time=%s"), instance.name, state, memusage, numprocs, uptime)

        return {'state': state,
                'max_mem': info.MemoryUsage,
                'mem': info.MemoryUsage,
                'num_cpu': info.NumberOfProcessors,
                'cpu_time': info.UpTime}

    def _lookup(self, i):
        vms = self._conn.Msvm_ComputerSystem(ElementName=i)
        n = len(vms)
        if n == 0:
            return None
        elif n > 1:
            raise Exception(_('duplicate name found: %s') % i)
        else:
            return vms[0].ElementName

    def _set_vm_state(self, vm_name, req_state):
        """Set the desired state of the VM"""
        vms = self._conn.Msvm_ComputerSystem(ElementName=vm_name)
        if len(vms) == 0:
            return False
        (job, ret_val) = vms[0].RequestStateChange(REQ_POWER_STATE[req_state])
        success = False
        if ret_val == WMI_JOB_STATUS_STARTED:
            success = self._check_job_status(job)
        elif ret_val == 0:
            success = True
        elif ret_val == 32775:
            #Invalid state for current operation. Typically means it is
            #already in the state requested
            success = True
        if success:
            LOG.info(_("Successfully changed vm state of %(vm_name)s"
                    " to %(req_state)s") % locals())
        else:
            msg = _("Failed to change vm state of %(vm_name)s"
                    " to %(req_state)s") % locals()
            LOG.error(msg)
            raise Exception(msg)
        
    def attach_volume(self, connection_info, instance_name, mountpoint):
        """Attach volume storage to VM instance"""
        return self._volumeops.attach_volume(connection_info,
                                             instance_name,
                                             mountpoint)
        
    def detach_volume(self, connection_info, instance_name, mountpoint):
        """Detach volume storage to VM instance"""
        return self._volumeops.detach_volume(connection_info,
                                             instance_name,
                                             mountpoint)
    
    def get_volume_connector(self, instance):
        return self._volumeops.get_volume_connector(instance)
    
    def poll_rescued_instances(self, timeout):
        pass

    def get_vcpu_total(self):
        """Get vcpu number of physical computer.

        :returns: the number of cpu core.

        """

        # On certain platforms, this will raise a NotImplementedError.
        try:
            return multiprocessing.cpu_count()
        except NotImplementedError:
            LOG.warn(_("Cannot get the number of cpu, because this "
                       "function is not implemented for this platform. "
                       "This error can be safely ignored for now."))
            return 0

    def get_memory_mb_total(self):
        """Get the total memory size(MB) of physical computer.

        :returns: the total amount of memory(MB).

        """
	total_kb = self._cim_conn.query("SELECT TotalVisibleMemorySize FROM win32_operatingsystem")[0].TotalVisibleMemorySize
	total_mb = long(total_kb) / 1024
        return total_mb

    def get_local_gb_total(self):
        """Get the total hdd size(GB) of physical computer.

        :returns:
            The total amount of HDD(GB).
            Note that this value shows a partition where
            NOVA-INST-DIR/instances mounts.

        """
	#TODO: This binds to C only right now, need to bind to instance dir
	total_kb = self._cim_conn.query("SELECT Size FROM win32_logicaldisk WHERE DriveType=3")[0].Size
        total_gb = long(total_kb) / (1024 ** 3)
        return total_gb

    def get_vcpu_used(self):
        """ Get vcpu usage number of physical computer.

        :returns: The total number of vcpu that currently used.

        """

	#TODO figure out a way to count assigned VCPUs
	total_vcpu = 0
        return total_vcpu

    def get_memory_mb_used(self):
        """Get the free memory size(MB) of physical computer.

        :returns: the total usage of memory(MB).

        """

        if sys.platform.upper() not in ['LINUX2', 'LINUX3']:
            return 0

	total_kb = self._cim_conn.query("SELECT FreePhysicalMemory FROM win32_operatingsystem")[0].FreePhysicalMemory
	total_mb = long(total_kb) / 1024
        
        return  total_mb

    def get_local_gb_used(self):
        """Get the free hdd size(GB) of physical computer.

        :returns:
           The total usage of HDD(GB).
           Note that this value shows a partition where
           NOVA-INST-DIR/instances mounts.

        """

	#TODO: This binds to C only right now, need to bind to instance dir
	total_kb = self._cim_conn.query("SELECT FreeSpace FROM win32_logicaldisk WHERE DriveType=3")[0].FreeSpace
        total_gb = long(total_kb) / (1024 ** 3)
        return total_gb

    def get_hypervisor_version(self):
        """Get hypervisor version.

        :returns: hypervisor version (ex. 12003)
 
        """
 
        # NOTE(justinsb): getVersion moved between libvirt versions
        # Trying to do be compatible with older versions is a lost cause
        # But ... we can at least give the user a nice message
    
        platform_ver = platform.uname()[2]
        return platform_ver

    def update_available_resource(self, context, host):
        """Updates compute manager resource info on ComputeNode table.

        This method is called as an periodic tasks and is used only
        in live migration currently.

        :param ctxt: security context
        :param host: hostname that compute manager is currently running

        """

        try:
            service_ref = db.service_get_all_compute_by_host(context, host)[0]
        except exception.NotFound:
            raise exception.ComputeServiceUnavailable(host=host)

        # Updating host information
        # TODO implemented cpu_info
        dic = {'vcpus': self.get_vcpu_total(),
               'memory_mb': self.get_memory_mb_total(),
               'local_gb': self.get_local_gb_total(),
               'vcpus_used': self.get_vcpu_used(),
               'memory_mb_used': self.get_memory_mb_used(),
               'local_gb_used': self.get_local_gb_used(),
               'hypervisor_type': "hyperv",
               'hypervisor_version': self.get_hypervisor_version(),
               'cpu_info': "unknown",
               'service_id': service_ref['id'],
               'disk_available_least': 1}        

        compute_node_ref = service_ref['compute_node']
        if not compute_node_ref:
            LOG.info(_('Compute_service record created for %s ') % host)
            db.compute_node_create(context, dic)
        else:
            LOG.info(_('Compute_service record updated for %s ') % host)
            db.compute_node_update(context, compute_node_ref[0]['id'], dic)

    def update_host_status(self):
        """See xenapi_conn.py implementation."""
        pass

    def get_host_stats(self, refresh=False):
        """See xenapi_conn.py implementation."""
        pass

    def host_power_action(self, host, action):
        """Reboots, shuts down or powers up the host."""
        pass

    def set_host_enabled(self, host, enabled):
        """Sets the specified host's ability to accept new instances."""
        pass
    
    def _get_base_vhd_path(self, image_name):
        base_dir = os.path.join(FLAGS.instances_path, '_base')
        if not os.path.exists(base_dir):
            os.mkdir(base_dir)
        return os.path.join(base_dir, image_name + ".vhd")

    @staticmethod
    def _cache_image(self, fn, target, fname, cow=False, Size=None, *args, **kwargs):
        """Wrapper for a method that creates an image that caches the image.

        This wrapper will save the image into a common store and create a
        copy for use by the hypervisor.

        The underlying method should specify a kwarg of target representing
        where the image will be saved.

        fname is used as the filename of the base image.  The filename needs
        to be unique to a given image.

        If cow is True, it will make a CoW image instead of a copy.
        """
        @utils.synchronized(fname)
        def call_if_not_exists(base, fn, *args, **kwargs):
                if not os.path.exists(base):
                    fn(target=base, *args, **kwargs)
        
        if not os.path.exists(target):
            base = self._get_base_vhd_path(fname)
            
            if not os.path.exists(base):
                call_if_not_exists(base, fn, *args, **kwargs)
            
            LOG.debug("use_cow_image:%s", cow)
            if cow:
                
                image_service = self._conn.query("Select * from Msvm_ImageManagementService")[0]
                (job, ret_val) = image_service.CreateDifferencingVirtualHardDisk(Path=target, ParentPath=base)
                LOG.debug("Creating difference disk: JobID=%s, Source=%s, Target=%s", job, base, target)
                if ret_val == WMI_JOB_STATUS_STARTED:
                    success = self._check_job_status(job)
                else:
                    success = (ret_val == 0)

                if not success:
                    raise Exception(_('Failed to create Difference Disk from %s to %s'), base, target)

            else:
                call_if_not_exists(target, fn, *args, **kwargs)
                
    #Trying to use code directly from vish/libvirt for portability
    @staticmethod
    def _fetch_image(target, context, image_id, user, project, *args, **kwargs):
        """Grab image and optionally attempt to resize it"""
        images.fetch(context, image_id, target, user, project)
        
    def snapshot(self, context, instance, name):
        """Create snapshot from a running VM instance."""
        vm = self._lookup(instance.name)
        if vm is None:
            raise exception.InstanceNotFound(instance=instance.name)
        vm = self._conn.Msvm_ComputerSystem(ElementName=instance.name)[0]                        
        vs_man_svc = self._conn.Msvm_VirtualSystemManagementService()[0]
        
        LOG.debug(_("Creating snapshot for instance %s"), instance.name)
        (job_path, ret_val, snap_setting_data) = vs_man_svc.CreateVirtualSystemSnapshot(vm.path_())
        if ret_val == WMI_JOB_STATUS_STARTED:
            success = self._check_job_status(job_path)
            if success:
                job_wmi_path = job_path.replace('\\','/')
                job = wmi.WMI(moniker=job_wmi_path)
                snap_setting_data = job.associators(wmi_result_class='Msvm_VirtualSystemSettingData')[0]                
        else:
            success = (ret_val == 0)            
        if not success:
            raise Exception(_('Failed to create snapshot for VM %s'), instance.name)
        
        export_folder = None
        f = None
        
        try:
            src_vhd_path = os.path.join(FLAGS.instances_path, instance.name, instance.name + ".vhd")            			

            image_man_svc = self._conn.Msvm_ImageManagementService()[0]
            
            LOG.debug(_("Getting info for VHD %s"), src_vhd_path)            
            (src_vhd_info, job_path, ret_val) = image_man_svc.GetVirtualHardDiskInfo(src_vhd_path)
            if ret_val == WMI_JOB_STATUS_STARTED:
                success = self._check_job_status(job_path)
            else:
                success = (ret_val == 0)            
            if not success:
                raise Exception(_("Failed to reconnect base disk %s and diff disk %s"), dest_base_disk_path, dest_vhd_path)
            
            src_base_disk_path = None
            et = ElementTree.fromstring(src_vhd_info)
            for item in et.findall("PROPERTY"):
                if item.attrib["NAME"] == "ParentPath":
                    src_base_disk_path = item.find("VALUE").text
                    break
                                
            if not src_base_disk_path:
                raise Exception(_("Cannot find base disk for diff disk %s"), dest_vhd_path)
                                
            export_folder = os.path.join(FLAGS.instances_path, "export", instance.name)
            LOG.debug(_('Creating folder %s '), export_folder)
            if os.path.isdir(export_folder):
                shutil.rmtree(export_folder)
            os.mkdir(export_folder)

            dest_base_disk_path = os.path.join(export_folder, os.path.basename(src_base_disk_path))	
            LOG.debug(_('Copying base disk %s to %s'), src_base_disk_path, dest_base_disk_path)
            shutil.copyfile(src_base_disk_path, dest_base_disk_path)

            dest_vhd_path = os.path.join(export_folder, os.path.basename(src_vhd_path))	

            LOG.debug(_('Copying diff VHD %s to %s'), src_vhd_path, dest_vhd_path)
            shutil.copyfile(src_vhd_path, dest_vhd_path)

            LOG.debug(_("Reconnecting copied base disk %s and diff disk %s"), dest_base_disk_path, dest_vhd_path)            
            (job_path, ret_val) = image_man_svc.ReconnectParentVirtualHardDisk(ChildPath = dest_vhd_path, ParentPath = dest_base_disk_path)
            if ret_val == WMI_JOB_STATUS_STARTED:
                success = self._check_job_status(job_path)
            else:
                success = (ret_val == 0)            
            if not success:
                raise Exception(_("Failed to reconnect base disk %s and diff disk %s"), dest_base_disk_path, dest_vhd_path)            
                
            LOG.debug(_("Merging base disk %s and diff disk %s"), dest_base_disk_path, dest_vhd_path)            
            (job_path, ret_val) = image_man_svc.MergeVirtualHardDisk(SourcePath = dest_vhd_path, DestinationPath = dest_base_disk_path)
            if ret_val == WMI_JOB_STATUS_STARTED:
                success = self._check_job_status(job_path)
            else:
                success = (ret_val == 0)            
            if not success:
                raise Exception(_("Failed to merge base disk %s and diff disk %s"), dest_base_disk_path, dest_vhd_path)			
			
            (glance_client, image_id) = glance.get_glance_client(context, name)            
            image_metadata = {"is_public": False,
                      "disk_format": "vhd",
                      "container_format": "bare",
                      "properties": {}}     
            f = open(dest_base_disk_path, 'r')
            LOG.debug(_("Updating Glance image %s with content from merged disk %s"), image_id, dest_base_disk_path)                      
            glance_client.update_image(image_id, image_meta=image_metadata, image_data=f) 
                        
            status = None
            while True: 
                status = glance_client.get_image_meta(image_id).get("status")
                if status not in ["queued", "saving"]:
                    break;         
                time.sleep(2)                     
            if status != "active":
                raise Exception(_('Snapshot image update failed for VM %s'), instance.name)
                
            LOG.debug(_("Snapshot image %s updated for VM %s"), image_id, instance.name)   
        finally:            
            LOG.debug(_("Removing snapshot %s"), name)            
            (job_path, ret_val) = vs_man_svc.RemoveVirtualSystemSnapshot(snap_setting_data.path_())
            if ret_val == WMI_JOB_STATUS_STARTED:
                success = self._check_job_status(job_path)
            else:
                success = (ret_val == 0)            
            if not success:
                raise Exception(_('Failed to remove snapshot for VM %s'), instance.name)
            
            if f:
                f.close()
            
            if export_folder:
                LOG.debug(_('Removing folder %s '), export_folder)
                shutil.rmtree(export_folder)            
        
    def pause(self, instance):
        """Pause VM instance."""
        LOG.debug("Pause instance=%s", instance)
        self._set_vm_state(instance.name, 'Paused')

    def unpause(self, instance):
        """Unpause paused VM instance."""
        LOG.debug("Unpause instance=%s", instance)
        self._set_vm_state(instance.name, 'Enabled')
 
    def suspend(self, instance):
        """Suspend the specified instance."""
        LOG.debug("Suspend instance=%s", instance)
        self._set_vm_state(instance.name, 'Suspended')        

    def resume(self, instance):
        """Resume the suspended VM instance."""
        LOG.debug("Resume instance=%s", instance)        
        self._set_vm_state(instance.name, 'Enabled')        

    def _check_live_migration_config(self):
        if not self._conn_v2:
            raise Exception(_('Live migration is not supported by this version of Hyper-V')) 

        migration_svc =  self._conn_v2.Msvm_VirtualSystemMigrationService()[0]
        vsmssd = migration_svc.associators(wmi_association_class='Msvm_ElementSettingData', wmi_result_class='Msvm_VirtualSystemMigrationServiceSettingData')[0]
        if not vsmssd.EnableVirtualSystemMigration:
            raise Exception(_('Live migration is not enabled on this host'))
        if not migration_svc.MigrationServiceListenerIPAddressList:
            raise Exception(_('Live migration networks are not configured on this host')) 

    def live_migration(self, context, instance_ref, dest, post_method, recover_method, block_migration=False):
        LOG.debug("live_migration called: %s", instance_ref)

        try:
            self._check_live_migration_config()

            vm_name = self._lookup(instance_ref.name)
            if vm_name is None:
                raise exception.InstanceNotFound(instance=instance.name)
            vm = self._conn_v2.Msvm_ComputerSystem(ElementName=instance_ref.name)[0]			
            vm_settings = vm.associators(wmi_association_class='Msvm_SettingsDefineState', wmi_result_class='Msvm_VirtualSystemSettingData')[0]

            new_resource_setting_data = [];
            sasds	= vm_settings.associators(wmi_association_class='Msvm_VirtualSystemSettingDataComponent', wmi_result_class='Msvm_StorageAllocationSettingData')		
            for sasd in sasds:
                if sasd.ResourceType == 31 and sasd.ResourceSubType == "Microsoft:Hyper-V:Virtual Hard Disk":
                    #sasd.PoolId = ""
                    new_resource_setting_data.append(sasd.GetText_(1))

            LOG.debug("Getting live migration networks for remote host: %s", dest) 		
            _conn_v2_remote = wmi.WMI(moniker='//' + dest + '/root/virtualization/v2')		
            migration_svc_remote =  _conn_v2_remote.Msvm_VirtualSystemMigrationService()[0];	
            remote_ip_address_list = migration_svc_remote.MigrationServiceListenerIPAddressList

            # VirtualSystemAndStorage
            vsmsd = self._conn_v2.query('select * from Msvm_VirtualSystemMigrationSettingData where MigrationType = 32771')[0]
            vsmsd.DestinationIPAddressList = remote_ip_address_list
            migration_setting_data = vsmsd.GetText_(1)

            migration_svc =  self._conn_v2.Msvm_VirtualSystemMigrationService()[0];			

            LOG.debug("Starting live migration for instance: %s", instance_ref.name) 				
            (job_path, ret_val) = migration_svc.MigrateVirtualSystemToHost(ComputerSystem = vm.path_(), DestinationHost = dest, MigrationSettingData = migration_setting_data, NewResourceSettingData = new_resource_setting_data)
            if ret_val == WMI_JOB_STATUS_STARTED:
                success = self._check_job_status(job_path)
            else:
                success = (ret_val == 0)
            if not success:
                raise Exception(_('Failed to live migrate VM %s'), instance_ref.name)                
        except:
            with utils.save_and_reraise_exception():
                LOG.debug("Calling live migration recover_method for instance: %s", instance_ref.name) 
                recover_method(context, instance_ref, dest, block_migration)

        LOG.debug("Calling live migration post_method for instance: %s", instance_ref.name)
        post_method(context, instance_ref, dest, block_migration)

    def compare_cpu(self, cpu_info):
        LOG.debug("compare_cpu called: %s", cpu_info)
        return True;

    def pre_live_migration(self, context, instance, block_device_info):
        LOG.debug("pre_live_migration called: %s", instance.name)
        self._check_live_migration_config()

        if FLAGS.use_cow_images:
            ebs_root = self._volumeops._volume_in_mapping(self._volumeops.get_default_root_device(), block_device_info)
            if not ebs_root:
                base_vhd_path = self._get_base_vhd_path(instance.image_ref)
                if not os.path.exists(base_vhd_path):
                    self._fetch_image(base_vhd_path, context, instance.image_ref, instance.user_id, instance.project_id)

    def post_live_migration_at_destination(self, ctxt, instance_ref, network_info, block_migration):
        LOG.debug("post_live_migration_at_destination called: %s", instance_ref.name)

    def plug_vifs(self, instance, network_info):
        LOG.debug("plug_vifs called: %s", instance.name)

    def unplug_vifs(self, instance, network_info):
        LOG.debug("plug_vifs called: %s", instance.name)

    def ensure_filtering_rules_for_instance(self, instance_ref, network_info):
        LOG.debug("ensure_filtering_rules_for_instance called: %s", instance_ref.name)

    def unfilter_instance(self, instance, network_info):
        """Stop filtering instance"""
        LOG.debug("unfilter_instance called: %s", instance.name)

    def confirm_migration(self, migration, instance, network_info):
		"""Confirms a resize, destroying the source VM"""
		LOG.debug("confirm_migration called: %s", instance)

    def finish_revert_migration(self, instance, network_info):
		"""Finish reverting a resize, powering back on the instance"""
		LOG.debug("finish_revert_migration called: %s", instance)

    def finish_migration(self, context, migration, instance, disk_info, network_info, image_meta, resize_instance=False):
		"""Completes a resize, turning on the migrated instance"""
		LOG.debug("finish_migration called: %s", instance)

    def get_console_output(self, instance):
        LOG.debug("get_console_output called: %s", instance.name)
        return ''
