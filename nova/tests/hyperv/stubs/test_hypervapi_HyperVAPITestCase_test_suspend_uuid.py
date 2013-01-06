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


def uuid4():
    ret_value = None
    global _uuid4_count_0
    if not '_uuid4_count_0' in globals():
        _uuid4_count_0 = 0
    if _uuid4_count_0 == 0:
        v = UUID()
        v.__instance_id__ = 2
    elif _uuid4_count_0 == 1:
        v = UUID()
        v.__instance_id__ = 3
    elif _uuid4_count_0 == 2:
        v = UUID()
        v.__instance_id__ = 4
    elif _uuid4_count_0 == 3:
        v = UUID()
        v.__instance_id__ = 5
    elif _uuid4_count_0 == 4:
        v = UUID()
        v.__instance_id__ = 6
    elif _uuid4_count_0 == 5:
        v = UUID()
        v.__instance_id__ = 7
    elif _uuid4_count_0 == 6:
        v = UUID()
        v.__instance_id__ = 8
    elif _uuid4_count_0 == 7:
        v = UUID()
        v.__instance_id__ = 9
    elif _uuid4_count_0 == 8:
        v = UUID()
        v.__instance_id__ = 10
    _uuid4_count_0 += 1
    return v


class UUID(object):

    def __init__(self, *args, **kwargs):
        pass

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__


    def __str__(self):
        if self.__id__ == 2:
            return '34dcc778-36a6-4390-a46e-dad9110caf97'
        elif self.__id__ == 3:
            return '35173df8-aa02-439a-be41-f3e1cff02b7a'
        elif self.__id__ == 4:
            return 'd57302f0-503d-4f0f-bec3-e4016f529b3b'
        elif self.__id__ == 5:
            return '6b169be2-8e4a-41a0-acfc-281a75fb28d0'
        elif self.__id__ == 6:
            return 'b9b72390-202f-444a-ae58-93219f307f9c'
        elif self.__id__ == 7:
            return '3b36def8-b8f9-4899-859e-316f59250649'
        elif self.__id__ == 8:
            return '9252502c-5999-4cf7-8327-a34b29eb2e3d'
        elif self.__id__ == 9:
            return '1de6be59-09bc-44df-8a1a-925b3dd248c8'
        elif self.__id__ == 10:
            return '3ad5cde7-607e-494a-b901-483c7fe06b81'
