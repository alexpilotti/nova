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
import uuid
import shutil
import multiprocessing
import time
from nova import flags
from nova import log as logging
from nova.compute import power_state
from nova.virt import driver
from nova.virt import images
from nova import utils
from nova import db
from nova.virt.hyperv import volumeops
from nova.virt.hyperv import vmops
from nova.virt.hyperv import snapshotops
from nova.virt.hyperv import livemigrationops
from nova.virt.hyperv import vmutils
from nova.image import glance
import pythoncom


LOG = logging.getLogger(__name__)

wmi = None

def get_connection(read_only):
    global wmi
    if wmi is None:
        wmi = __import__('wmi')
    return HyperVConnection(read_only)


class HyperVConnection(driver.ComputeDriver):
    def __init__(self, read_only):
        super(HyperVConnection, self).__init__()

        vmutls = vmutils.VMUtils(wmi, os, uuid, time)
        
        self._volumeops = volumeops.VolumeOps(wmi, vmutils, time)        
        self._vmops = vmops.VMOps(wmi, vmutls, self._volumeops, images, db, os, multiprocessing, uuid)
        self._snapshotops = snapshotops.SnapshotOps(wmi, vmutls, glance, os, shutil)
        self._livemigrationops = livemigrationops.LiveMigrationOps(wmi, vmutls, self._volumeops, os)
        
    def init_host(self, host):
        #FIXME(chiradeep): implement this
        self._host = host

    def list_instances(self):
        return self._vmops.list_instances()

    def list_instances_detail(self):
        return self._vmops.list_instances_detail()

    def spawn(self, context, instance, image_meta, network_info, block_device_info=None):
        self._vmops.spawn(context, instance, image_meta, network_info, block_device_info)
            
    def reboot(self, instance, network_info, reboot_type):
        self._vmops.reboot(instance, network_info, reboot_type)
    
    def destroy(self, instance, network_info=None, cleanup=True):
        self._vmops.destroy(instance, network_info, cleanup)

    def get_info(self, instance):
        return self._vmops.get_info(instance)
        
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

    def update_available_resource(self, context, host):
        self._vmops.update_available_resource(context, host)

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
            
    def snapshot(self, context, instance, name):
        self._snapshotops.snapshot(context, instance, name)
        
    def pause(self, instance):
        self._vmops.pause(instance)

    def unpause(self, instance):
        self._vmops.unpause(instance)
 
    def suspend(self, instance):
        self._vmops.suspend(instance)

    def resume(self, instance):
        self._vmops.resume(instance)    

    def live_migration(self, context, instance_ref, dest, post_method, recover_method, block_migration=False):
        self._livemigrationops.live_migration(context, instance_ref, dest, post_method, recover_method, block_migration)

    def compare_cpu(self, cpu_info):
        return self._livemigrationops.compare_cpu(cpu_info)

    def pre_live_migration(self, context, instance, block_device_info):
        self._livemigrationops.pre_live_migration(context, instance, block_device_info)

    def post_live_migration_at_destination(self, ctxt, instance_ref, network_info, block_migration):
        self._livemigrationops.post_live_migration_at_destination(ctxt, instance_ref, network_info, block_migration)

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
