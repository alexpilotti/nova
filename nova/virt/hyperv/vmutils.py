# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 Cloudbase Solutions Srl / Pedro Navarro Perez
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
Utility class for VM related operations.
"""

from nova import log as logging
from nova import flags
import constants

FLAGS = flags.FLAGS
LOG = logging.getLogger(__name__)

class VMUtils(object):
    def __init__(self, wmi, os, uuid, time):
        self._wmi = wmi
        self._os = os        
        self._uuid = uuid
        self._time = time
                
    def lookup(self, conn, i):
        vms = conn.Msvm_ComputerSystem(ElementName=i)
        n = len(vms)
        if n == 0:
            return None
        elif n > 1:
            raise Exception(_('duplicate name found: %s') % i)
        else:
            return vms[0].ElementName

    #TODO: use the reactor to poll instead of sleep
    def check_job_status(self, jobpath):
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
        	
        while job.JobState == constants.WMI_JOB_STATE_RUNNING:
            self._time.sleep(0.1)
            job = self._wmi.WMI(moniker=job_wmi_path)
        if job.JobState != constants.WMI_JOB_STATE_COMPLETED:
            LOG.debug(_("WMI job failed: %s - %s - %s"), job.ErrorSummaryDescription, job.ErrorDescription, job.ErrorCode)
            return False
        desc = job.Description
        elap = job.ElapsedTime
        LOG.debug(_("WMI job succeeded: %(desc)s, Elapsed=%(elap)s ")
                % locals())
        return True
              
    def get_base_vhd_path(self, image_name):
        base_dir = self._os.path.join(FLAGS.instances_path, '_base')
        if not self._os.path.exists(base_dir):
            self._os.mkdir(base_dir)
        return self._os.path.join(base_dir, image_name + ".vhd")
        
    def clone_wmi_obj(self, conn, wmi_class, wmi_obj):
        """Clone a WMI object"""
        cl = conn.__getattr__(wmi_class)  # get the class
        newinst = cl.new()
        #Copy the properties from the original.
        for prop in wmi_obj._properties:
            if prop == "VirtualSystemIdentifiers":
                strguid=[]
                strguid.append(str(self._uuid.uuid4()))
                newinst.Properties_.Item(prop).Value=strguid
            else:
                newinst.Properties_.Item(prop).Value = \
                    wmi_obj.Properties_.Item(prop).Value
        return newinst
        
    def add_virt_resource(self, conn, res_setting_data, target_vm):
        """Add a new resource (disk/nic) to the VM"""
        vs_man_svc = conn.Msvm_VirtualSystemManagementService()[0]
        (job, new_resources, ret_val) = vs_man_svc.\
                    AddVirtualSystemResources([res_setting_data.GetText_(1)],
                                                target_vm.path_())
        success = True
        if ret_val == constants.WMI_JOB_STATUS_STARTED:
            success = self.check_job_status(job)
        else:
            success = (ret_val == 0)
        if success:
            return new_resources
        else:
            return None
       
    def remove_virt_resource(self, conn, res_setting_data, target_vm):
        """Add a new resource (disk/nic) to the VM"""
        vs_man_svc = conn.Msvm_VirtualSystemManagementService()[0]
        (job, ret_val) = vs_man_svc.\
                    RemoveVirtualSystemResources([res_setting_data.path_()],
                                                target_vm.path_())
        success = True
        if ret_val == constants.WMI_JOB_STATUS_STARTED:
            success = self.check_job_status(job)
        else:
            success = (ret_val == 0)
        return success
       