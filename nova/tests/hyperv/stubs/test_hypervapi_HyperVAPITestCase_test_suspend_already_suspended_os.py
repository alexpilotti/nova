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


import sys
path = sys.modules[__name__]


def makedirs(name, mode=511):
    if name ==\
 'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_8c4c98a5-fca4-4c3e-8fb1\
-5e4aa82d6c70':
        return None
    elif name == 'C:\\Hyper-V\\test\\instances\\_base':
        return None


def join(a, *p):
    if len(p) == 1 and a == 'C:\\Hyper-V\\test\\instances' and p[0] ==\
 'openstack_unit_test_vm_8c4c98a5-fca4-4c3e-8fb1-5e4aa82d6c70':
        return\
 'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_8c4c98a5-fca4-4c3e-8fb1\
-5e4aa82d6c70'
    elif len(p) == 1 and a ==\
 'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_8c4c98a5-fca4-4c3e-8fb1\
-5e4aa82d6c70' and p[0] ==\
 'openstack_unit_test_vm_8c4c98a5-fca4-4c3e-8fb1-5e4aa82d6c70.vhd':
        return\
 'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_8c4c98a5-fca4-4c3e-8fb1\
-5e4aa82d6c70\\openstack_unit_test_vm_8c4c98a5-fca4-4c3e-8fb1-5e4aa82d6c70.vhd'
    elif len(p) == 1 and a == 'C:\\Hyper-V\\test\\instances' and p[0] ==\
 '_base':
        return 'C:\\Hyper-V\\test\\instances\\_base'
    elif len(p) == 1 and a == 'C:\\Hyper-V\\test\\instances\\_base' and p[0]\
 == '1.vhd':
        return 'C:\\Hyper-V\\test\\instances\\_base\\1.vhd'


def exists(path):
    if path ==\
 'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_8c4c98a5-fca4-4c3e-8fb1\
-5e4aa82d6c70':
        return False
    elif path ==\
 'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_8c4c98a5-fca4-4c3e-8fb1\
-5e4aa82d6c70\\openstack_unit_test_vm_8c4c98a5-fca4-4c3e-8fb1-5e4aa82d6c70.vhd\
':
        return False
    elif path == 'C:\\Hyper-V\\test\\instances\\_base':
        return False
    elif path == 'C:\\Hyper-V\\test\\instances\\_base\\1.vhd':
        return False
    elif path == 'C:\\Hyper-V\\test\\instances\\_base\\1.vhd':
        return False