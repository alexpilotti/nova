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
            return '6fb85d6a-58a1-4db1-ac29-4969bcc6db91'
        elif self.__id__ == 3:
            return 'fc6259d5-3825-4e10-ae08-f267e104cd4e'
        elif self.__id__ == 4:
            return '5b9e4a96-98aa-4c20-bf4e-1bb4aa7c65ab'
        elif self.__id__ == 5:
            return 'f0fb575e-cd84-4f1c-934f-2b22aa4e69e2'
        elif self.__id__ == 6:
            return 'a0ad2779-b78b-4527-aac6-dee5604a22d6'
        elif self.__id__ == 7:
            return '20f0c64e-e332-4078-9c20-db12cd966778'
        elif self.__id__ == 8:
            return '429c999c-392d-4587-9adc-51c355fdd336'
        elif self.__id__ == 9:
            return '06d53f55-fd42-48b1-ad56-5d58af353c87'
        elif self.__id__ == 10:
            return '6a386ac7-fbc1-4a5a-838a-6fc2a7c7bb93'
