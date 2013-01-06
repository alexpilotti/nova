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


def generate_uid(topic, size=8):
    if topic == 'r':
        return 'r-93r191yi'


def execute(*cmd, **kwargs):
    if len(cmd) == 8 and kwargs.get('attempts') == 1 and cmd[1] ==\
 'qemu-img.exe' and cmd[2] == 'convert' and cmd[3] == '-f' and cmd[4] == 'raw'\
 and cmd[5] == '-O' and cmd[6] == 'vpc' and cmd[7] ==\
 'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_5276dd6f-fd3a-41da-8799\
-352039c91e80\\configdrive.iso' and cmd[8] ==\
 'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_5276dd6f-fd3a-41da-8799\
-352039c91e80\\configdrive.vhd':
        v = ()
        v1 = ''
        v += (v1,)
        v1 = ''
        v += (v1,)
        return v
