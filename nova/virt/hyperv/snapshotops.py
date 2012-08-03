# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 Cloudbase Solutions Srl
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
Management class for VM snapshot operations.
"""
from nova import log as logging
from nova import flags
from nova import exception
from nova.virt.hyperv import baseops
from xml.etree import ElementTree
import constants

FLAGS = flags.FLAGS
LOG = logging.getLogger(__name__)

class SnapshotOps(baseops.BaseOps):
    def __init__(self, wmi, vmutils, glance, os, shutil):
        super(SnapshotOps, self).__init__(wmi)
        
        self._vmutils = vmutils
        self._os = os        
        self._shutil = shutil 
        self._glance = glance
    
    def snapshot(self, context, instance, name):
        """Create snapshot from a running VM instance."""
        vm = self._vmutils.lookup(self._conn, instance.name)
        if vm is None:
            raise exception.InstanceNotFound(instance=instance.name)
        vm = self._conn.Msvm_ComputerSystem(ElementName=instance.name)[0]                        
        vs_man_svc = self._conn.Msvm_VirtualSystemManagementService()[0]
        
        LOG.debug(_("Creating snapshot for instance %s"), instance.name)
        (job_path, ret_val, snap_setting_data) = vs_man_svc.CreateVirtualSystemSnapshot(vm.path_())
        if ret_val == constants.WMI_JOB_STATUS_STARTED:
            success = self._vmutils.check_job_status(job_path)
            if success:
                job_wmi_path = job_path.replace('\\','/')
                job = self._wmi.WMI(moniker=job_wmi_path)
                snap_setting_data = job.associators(wmi_result_class='Msvm_VirtualSystemSettingData')[0]                
        else:
            success = (ret_val == 0)            
        if not success:
            raise Exception(_('Failed to create snapshot for VM %s'), instance.name)
        
        export_folder = None
        f = None
        
        try:
            src_vhd_path = self._os.path.join(FLAGS.instances_path, instance.name, instance.name + ".vhd")            			

            image_man_svc = self._conn.Msvm_ImageManagementService()[0]
            
            LOG.debug(_("Getting info for VHD %s"), src_vhd_path)            
            (src_vhd_info, job_path, ret_val) = image_man_svc.GetVirtualHardDiskInfo(src_vhd_path)
            if ret_val == constants.WMI_JOB_STATUS_STARTED:
                success = self._vmutils.check_job_status(job_path)
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

            export_folder = self._os.path.join(FLAGS.instances_path, "export", instance.name)
            LOG.debug(_('Creating folder %s '), export_folder)
            if self._os.path.isdir(export_folder):
                self._shutil.rmtree(export_folder)
            self._os.mkdir(export_folder)

            dest_vhd_path = self._os.path.join(export_folder, self._os.path.basename(src_vhd_path))	
            LOG.debug(_('Copying VHD %s to %s'), src_vhd_path, dest_vhd_path)
            self._shutil.copyfile(src_vhd_path, dest_vhd_path)

            image_vhd_path = None
            if not src_base_disk_path:
                image_vhd_path = dest_vhd_path
            else:
                dest_base_disk_path = self._os.path.join(export_folder, self._os.path.basename(src_base_disk_path))	
                LOG.debug(_('Copying base disk %s to %s'), src_base_disk_path, dest_base_disk_path)
                self._shutil.copyfile(src_base_disk_path, dest_base_disk_path)

                LOG.debug(_("Reconnecting copied base disk %s and diff disk %s"), dest_base_disk_path, dest_vhd_path)            
                (job_path, ret_val) = image_man_svc.ReconnectParentVirtualHardDisk(ChildPath = dest_vhd_path, ParentPath = dest_base_disk_path, Force = True)
                if ret_val == constants.WMI_JOB_STATUS_STARTED:
                    success = self._vmutils.check_job_status(job_path)
                else:
                    success = (ret_val == 0)
                if not success:
                    raise Exception(_("Failed to reconnect base disk %s and diff disk %s"), dest_base_disk_path, dest_vhd_path)

                LOG.debug(_("Merging base disk %s and diff disk %s"), dest_base_disk_path, dest_vhd_path)            
                (job_path, ret_val) = image_man_svc.MergeVirtualHardDisk(SourcePath = dest_vhd_path, DestinationPath = dest_base_disk_path)
                if ret_val == constants.WMI_JOB_STATUS_STARTED:
                    success = self._vmutils.check_job_status(job_path)
                else:
                    success = (ret_val == 0)
                if not success:
                    raise Exception(_("Failed to merge base disk %s and diff disk %s"), dest_base_disk_path, dest_vhd_path)			
                image_vhd_path = dest_base_disk_path
			
            (glance_client, image_id) = self._glance.get_glance_client(context, name)            
            image_metadata = {"is_public": False,
                      "disk_format": "vhd",
                      "container_format": "bare",
                      "properties": {}}     
            f = open(image_vhd_path, 'rb')
            LOG.debug(_("Updating Glance image %s with content from merged disk %s"), image_id, image_vhd_path)                      
            glance_client.update_image(image_id, image_meta=image_metadata, image_data=f)

            LOG.debug(_("Snapshot image %s updated for VM %s"), image_id, instance.name)   
        finally:            
            LOG.debug(_("Removing snapshot %s"), name)
            (job_path, ret_val) = vs_man_svc.RemoveVirtualSystemSnapshot(snap_setting_data.path_())
            if ret_val == constants.WMI_JOB_STATUS_STARTED:
                success = self._vmutils.check_job_status(job_path)
            else:
                success = (ret_val == 0)            
            if not success:
                raise Exception(_('Failed to remove snapshot for VM %s'), instance.name)
            
            if f:
                f.close()
            
            if export_folder:
                LOG.debug(_('Removing folder %s '), export_folder)
                self._shutil.rmtree(export_folder)            
        