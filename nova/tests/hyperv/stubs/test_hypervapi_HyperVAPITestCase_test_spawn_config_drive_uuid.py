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
    elif _uuid4_count_0 == 9:
        v = UUID()
        v.__instance_id__ = 11
    elif _uuid4_count_0 == 10:
        v = UUID()
        v.__instance_id__ = 12
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
            return 'ac388e12-d662-48a1-b444-fa15482b40ff'
        elif self.__id__ == 3:
            return '16f58b29-0128-40ac-82c7-3cc882d3b072'
        elif self.__id__ == 4:
            return '1f63fa7b-7324-438c-b782-b31ffcb31e04'
        elif self.__id__ == 5:
            return '4a31dce2-6f33-4a30-ab84-ffb8125f87a9'
        elif self.__id__ == 6:
            return 'febfe438-d0ef-48e6-aa0f-160f992c99c4'
        elif self.__id__ == 7:
            return '1414d447-0fb4-44e2-b08c-c74c65576c44'
        elif self.__id__ == 8:
            return 'ad2c672b-41f1-4561-b70a-8dc9a688dce1'
        elif self.__id__ == 9:
            return '4b57acd0-1ac3-455b-b7d9-d82f20baba38'
        elif self.__id__ == 10:
            return '348c2dcc-e3c4-45cc-80e5-996d697d7826'
        elif self.__id__ == 11:
            return 'c4d15567-93e0-42f2-836b-bc77443b8a79'
        elif self.__id__ == 12:
            return 'ee51ffa3-007a-4d1e-8368-dfe54ed42eea'
