# vim: tabstop=4 shiftwidth=4 softtabstop=4
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

'''
This file contains auto generated mock classes and functions.
'''


class type(object):

    def __init__(self, instance_id=1, *args, **kwargs):
        self.__instance_id__ = instance_id

    @property
    def __id__(self):
        return self.__instance_id__

    def __call__(*p):
        if len(p) == 0 and str(instance_md) ==\
 '<nova.api.metadata.base.InstanceMetadata instance at 0x0E690FA8>':
            v = ConfigDriveBuilder(3)
            return v


def required_by(instance):
    if str(instance) == '{\'vm_state\': \'building\', \'project_id\':\
 \'fake\', \'user_id\': \'fake\', \'name\':\
 \'openstack_unit_test_vm_81f8b976-3c30-4d1c-8c7a-091e55c1ca9d\',\
 \'kernel_id\': \'1\', \'ramdisk_id\': \'1\', \'launch_time\':\
 \'2013-01-06T22:59:34Z\', \'mac_addresses\': [{\'address\':\
 \'de:ad:be:ef:be:ef\'}], \'memory_mb\': 512, \'instance_type\': {\'root_gb\':\
 0, \'name\': \'m1.tiny\', \'memory_mb\': 512, \'vcpus\': 1, \'rxtx_factor\':\
 1, \'flavorid\': 1}, \'vcpus\': 1, \'root_gb\': 0, \'image_ref\': \'1\',\
 \'task_state\': \'scheduling\', \'reservation_id\': \'r-jc0i5zyk\', \'id\':\
 1, \'uuid\': \'b10fc8c3-9453-402e-a0ef-9ef712a185fe\'}':
        return True


class ConfigDriveBuilder(object):

    def __init__(self, instance_id=1, *args, **kwargs):
        self.__instance_id__ = instance_id

    @property
    def __id__(self):
        return self.__instance_id__

    def cleanup(self):
        if self.__id__ == 3:
            return None

    def make_drive(self, path):
        if self.__id__ == 3 and path ==\
 'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_81f8b976-3c30-4d1c-8c7a\
-091e55c1ca9d\\configdrive.iso':
            return None
