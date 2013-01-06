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
            return 'ef74bbb3-525d-42ac-a8c3-c1a0835a452f'
        elif self.__id__ == 3:
            return '55bd80e9-076c-417a-9750-d6bab7908057'
        elif self.__id__ == 4:
            return '0f805ecb-3c0a-464c-8dfe-9515962d6499'
        elif self.__id__ == 5:
            return 'b424004c-9aa7-4656-a3fd-ea28e13d5eae'
        elif self.__id__ == 6:
            return '3a02b60a-f301-483c-aa5d-2740c2a2e6b8'
        elif self.__id__ == 7:
            return '3c83d847-6330-4ac0-81b2-db161cc0de49'
        elif self.__id__ == 8:
            return 'dde5d88f-f3c6-4dcb-a1c5-41c165fc19b7'
        elif self.__id__ == 9:
            return '8409615a-9fcc-4a33-bb51-ac10c698132e'
        elif self.__id__ == 10:
            return 'd236329e-ab94-42e4-9d96-bfc32f59dd3e'
