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
            return 'e9f30752-115c-4d5f-ace3-9032e1a19c08'
        elif self.__id__ == 3:
            return 'e38537df-8e95-4f6b-a7a5-c4a0b0a8bfce'
        elif self.__id__ == 4:
            return '07cce40b-43d6-45cc-bfcb-f654a4e8c8e0'
        elif self.__id__ == 5:
            return '0dced33f-50a3-4062-a6a1-c4294e9f1804'
        elif self.__id__ == 6:
            return '4196ba98-1e88-4954-8a53-cd76f020617e'
        elif self.__id__ == 7:
            return '01f89c9d-48d3-44ef-b505-c5542d62a357'
        elif self.__id__ == 8:
            return 'b0fba93d-4fc7-4a37-8003-289b66b4d192'
        elif self.__id__ == 9:
            return 'ac474993-bad7-4bbc-abac-6a992f6bd7e4'
        elif self.__id__ == 10:
            return '601d0767-53fc-4d21-a1eb-012349f3bdd5'
        elif self.__id__ == 11:
            return '01f6daa3-6481-4abf-a280-a4d52017b14e'
