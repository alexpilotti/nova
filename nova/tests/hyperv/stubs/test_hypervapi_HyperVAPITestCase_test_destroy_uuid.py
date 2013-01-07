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
        v = UUID(2)
    elif _uuid4_count_0 == 1:
        v = UUID(3)
    elif _uuid4_count_0 == 2:
        v = UUID(4)
    elif _uuid4_count_0 == 3:
        v = UUID(5)
    elif _uuid4_count_0 == 4:
        v = UUID(6)
    elif _uuid4_count_0 == 5:
        v = UUID(7)
    elif _uuid4_count_0 == 6:
        v = UUID(8)
    elif _uuid4_count_0 == 7:
        v = UUID(9)
    elif _uuid4_count_0 == 8:
        v = UUID(10)
    _uuid4_count_0 += 1
    return v


class UUID(object):

    def __init__(self, instance_id=1, *args, **kwargs):
        self.__instance_id__ = instance_id

    @property
    def __id__(self):
        return self.__instance_id__

    def __str__(self):
        if self.__id__ == 2:
            return 'a8e40dc8-1b8a-4d04-b8b5-e223c8f63c2a'
        elif self.__id__ == 3:
            return '284955af-4827-46c8-b948-c922e13c5c43'
        elif self.__id__ == 4:
            return 'a2ec32b9-24bc-4fb6-aa16-6dda7842ba13'
        elif self.__id__ == 5:
            return '64225f90-bc72-4c1d-90eb-814d20b67782'
        elif self.__id__ == 6:
            return '8a1f5396-4b6f-42f3-bd3f-46f85a29903a'
        elif self.__id__ == 7:
            return 'e706635f-3d90-4f5e-81f2-6fda87f8d796'
        elif self.__id__ == 8:
            return 'c16af976-95a0-447c-86d2-0e629aacc9c9'
        elif self.__id__ == 9:
            return '06abcd6f-cc34-44e3-96ed-2cf40f13a85a'
        elif self.__id__ == 10:
            return '0b44b776-4164-4766-95c9-8837a6760365'
