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

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__


    def __call__(*p):
        if len(p) == 0 and str(instance_md) ==\
 '<nova.api.metadata.base.InstanceMetadata instance at 0x0E07ED78>':
            v = ConfigDriveBuilder()
            v.__instance_id__ = 3
            return v




def required_by(instance):
    if str(instance) == '{\'vm_state\': \'building\', \'project_id\':\
 \'fake\', \'user_id\': \'fake\', \'name\':\
 \'openstack_unit_test_vm_5276dd6f-fd3a-41da-8799-352039c91e80\',\
 \'kernel_id\': \'1\', \'ramdisk_id\': \'1\', \'launch_time\':\
 \'2013-01-03T20:14:32Z\', \'mac_addresses\': [{\'address\':\
 \'de:ad:be:ef:be:ef\'}], \'memory_mb\': 512, \'instance_type\': {\'root_gb\':\
 0, \'name\': \'m1.tiny\', \'memory_mb\': 512, \'vcpus\': 1, \'rxtx_factor\':\
 1, \'flavorid\': 1}, \'vcpus\': 1, \'root_gb\': 0, \'image_ref\': \'1\',\
 \'task_state\': \'scheduling\', \'reservation_id\': \'r-93r191yi\', \'id\':\
 1, \'uuid\': \'1e73ad83-4828-4f95-92c0-caf0430fc713\'}':
        return True


class ConfigDriveBuilder(object):

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__

    def cleanup(self):
        if self.__id__ == 3:
            return None

    def make_drive(self, path):
        if self.__id__ == 3 and path ==\
 'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_5276dd6f-fd3a-41da-8799\
-352039c91e80\\configdrive.iso':
            return None
