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
    elif _uuid4_count_0 == 9:
        v = UUID(11)
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
            return '82c326ef-3696-41c4-ad51-9fd855bd8fa7'
        elif self.__id__ == 3:
            return '7be3b636-13b8-4732-9d3c-5e20a07b70dd'
        elif self.__id__ == 4:
            return '031eb386-ead7-4906-9fab-92045cf253f6'
        elif self.__id__ == 5:
            return 'd30e8e8f-803a-48b5-9f80-b8316434233b'
        elif self.__id__ == 6:
            return '205ef3f7-5b1e-4bd0-837a-4bafca28dc24'
        elif self.__id__ == 7:
            return 'ee38578c-9952-4255-9d5f-ec357ff43694'
        elif self.__id__ == 8:
            return '156a72fd-5398-4979-8828-a227dabe7e09'
        elif self.__id__ == 9:
            return 'd396bcea-f2a9-4b4f-8632-8133757a3ba5'
        elif self.__id__ == 10:
            return '0750ac55-6d63-4d63-b214-03866d8be3f2'
        elif self.__id__ == 11:
            return '88188539-287b-4e7d-8eba-1255aefafb8b'
