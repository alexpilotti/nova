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
 'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_2ccaa158-2156-46f0-a5a5\
-3032172e237e':
        return None
    elif name == 'C:\\Hyper-V\\test\\instances\\_base':
        return None
    elif name ==\
 'C:\\Hyper-V\\test\\instances\\export\\openstack_unit_test_vm_2ccaa158-2156-4\
6f0-a5a5-3032172e237e':
        return None


def isdir(*p):
    if len(p) == 1 and p[0] ==\
 'C:\\Hyper-V\\test\\instances\\export\\openstack_unit_test_vm_2ccaa158-2156-4\
6f0-a5a5-3032172e237e':
        return False


def basename(p):
    if p ==\
 'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_2ccaa158-2156-46f0-a5a5\
-3032172e237e\\openstack_unit_test_vm_2ccaa158-2156-46f0-a5a5-3032172e237e.vhd\
':
        return\
 'openstack_unit_test_vm_2ccaa158-2156-46f0-a5a5-3032172e237e.vhd'
    elif p == 'C:\\Hyper-V\\test\\instances\\_base\\1.vhd':
        return '1.vhd'


def join(a, *p):
    if len(p) == 1 and a == 'C:\\Hyper-V\\test\\instances' and p[0] ==\
 'openstack_unit_test_vm_2ccaa158-2156-46f0-a5a5-3032172e237e':
        return\
 'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_2ccaa158-2156-46f0-a5a5\
-3032172e237e'
    elif len(p) == 1 and a ==\
 'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_2ccaa158-2156-46f0-a5a5\
-3032172e237e' and p[0] ==\
 'openstack_unit_test_vm_2ccaa158-2156-46f0-a5a5-3032172e237e.vhd':
        return\
 'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_2ccaa158-2156-46f0-a5a5\
-3032172e237e\\openstack_unit_test_vm_2ccaa158-2156-46f0-a5a5-3032172e237e.vhd'
    elif len(p) == 1 and a == 'C:\\Hyper-V\\test\\instances' and p[0] ==\
 '_base':
        return 'C:\\Hyper-V\\test\\instances\\_base'
    elif len(p) == 1 and a == 'C:\\Hyper-V\\test\\instances\\_base' and p[0]\
 == '1.vhd':
        return 'C:\\Hyper-V\\test\\instances\\_base\\1.vhd'
    elif len(p) == 2 and a == 'C:\\Hyper-V\\test\\instances' and p[0] ==\
 'openstack_unit_test_vm_2ccaa158-2156-46f0-a5a5-3032172e237e' and p[1] ==\
 'openstack_unit_test_vm_2ccaa158-2156-46f0-a5a5-3032172e237e.vhd':
        return\
 'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_2ccaa158-2156-46f0-a5a5\
-3032172e237e\\openstack_unit_test_vm_2ccaa158-2156-46f0-a5a5-3032172e237e.vhd'
    elif len(p) == 2 and a == 'C:\\Hyper-V\\test\\instances' and p[0] ==\
 'export' and p[1] ==\
 'openstack_unit_test_vm_2ccaa158-2156-46f0-a5a5-3032172e237e':
        return\
 'C:\\Hyper-V\\test\\instances\\export\\openstack_unit_test_vm_2ccaa158-2156-4\
6f0-a5a5-3032172e237e'
    elif len(p) == 1 and a ==\
 'C:\\Hyper-V\\test\\instances\\export\\openstack_unit_test_vm_2ccaa158-2156-4\
6f0-a5a5-3032172e237e' and p[0] ==\
 'openstack_unit_test_vm_2ccaa158-2156-46f0-a5a5-3032172e237e.vhd':
        return\
 'C:\\Hyper-V\\test\\instances\\export\\openstack_unit_test_vm_2ccaa158-2156-4\
6f0-a5a5-3032172e237e\\openstack_unit_test_vm_2ccaa158-2156-46f0-a5a5-3032172e\
237e.vhd'
    elif len(p) == 1 and a ==\
 'C:\\Hyper-V\\test\\instances\\export\\openstack_unit_test_vm_2ccaa158-2156-4\
6f0-a5a5-3032172e237e' and p[0] == '1.vhd':
        return\
 'C:\\Hyper-V\\test\\instances\\export\\openstack_unit_test_vm_2ccaa158-2156-4\
6f0-a5a5-3032172e237e\\1.vhd'


def exists(path):
    if path ==\
 'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_2ccaa158-2156-46f0-a5a5\
-3032172e237e':
        return False
    elif path ==\
 'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_2ccaa158-2156-46f0-a5a5\
-3032172e237e\\openstack_unit_test_vm_2ccaa158-2156-46f0-a5a5-3032172e237e.vhd\
':
        return False
    elif path == 'C:\\Hyper-V\\test\\instances\\_base':
        return False
    elif path == 'C:\\Hyper-V\\test\\instances\\_base\\1.vhd':
        return False
    elif path == 'C:\\Hyper-V\\test\\instances\\_base\\1.vhd':
        return False
