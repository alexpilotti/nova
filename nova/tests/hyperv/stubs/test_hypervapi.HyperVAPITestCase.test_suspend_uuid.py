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
            return 'ffdfc592-0350-4024-9620-f8d0b8d7dd91'
        elif self.__id__ == 3:
            return '65f06e3a-c772-4663-9554-1d94d1f7b2e3'
        elif self.__id__ == 4:
            return '9becc834-3140-48c9-8f0d-fdbe4826df68'
        elif self.__id__ == 5:
            return 'cac7d133-e6c7-49ac-8655-ef368bc00d5f'
        elif self.__id__ == 6:
            return '8f4b8271-74f3-4bca-bacb-d25eb796f9a0'
        elif self.__id__ == 7:
            return '91d8bc4f-8947-491a-811e-420a4743fada'
        elif self.__id__ == 8:
            return '5f1ca0b7-5f3f-4832-b014-24795bb4124e'
        elif self.__id__ == 9:
            return '0937b7d2-3c75-43e4-8231-35e119fcc2d0'
        elif self.__id__ == 10:
            return 'd4061185-6305-4c8e-ba48-76ba26b46c41'
