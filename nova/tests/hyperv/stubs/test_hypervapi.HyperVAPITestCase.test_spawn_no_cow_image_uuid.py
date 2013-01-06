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

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__

    def __str__(self):
        if self.__id__ == 2:
            return 'c5bc7261-2aee-4b17-a240-9f30b5f57aa0'
        elif self.__id__ == 3:
            return '2d73339c-18f6-4374-a826-b4535b4f6e57'
        elif self.__id__ == 4:
            return 'b116a527-3c6f-4450-a00c-d659e5a1a72b'
        elif self.__id__ == 5:
            return 'a5df871b-7929-497a-9548-69b407fcfb7e'
        elif self.__id__ == 6:
            return 'e7a5d28d-f8cd-4c4a-bca4-079f295e3526'
        elif self.__id__ == 7:
            return '2bb5a703-46ff-4e21-9634-8bb266a63f8d'
        elif self.__id__ == 8:
            return 'b416c43b-ec9c-490d-8938-890d4dd05ac0'
        elif self.__id__ == 9:
            return 'a21d652b-01d9-45ec-95e1-6d4cfd7a843f'
        elif self.__id__ == 10:
            return 'd2a5ce28-6805-41af-8023-c986c22ea5f3'
