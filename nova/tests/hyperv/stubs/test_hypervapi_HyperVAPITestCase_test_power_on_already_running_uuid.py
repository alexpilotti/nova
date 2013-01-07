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
            return '07b101c7-adde-43f6-a620-2c4e2fabcf49'
        elif self.__id__ == 3:
            return 'c358ab86-4828-49c6-9de6-bda439654f26'
        elif self.__id__ == 4:
            return 'a1c81b03-458a-45ad-952a-f1c7364e1337'
        elif self.__id__ == 5:
            return 'f5c5fd3e-bf3f-4142-ac36-37de962b8251'
        elif self.__id__ == 6:
            return '765e220e-e80e-46f6-afc9-a6de20ba0818'
        elif self.__id__ == 7:
            return '7e90efd3-8452-452c-8c4c-3ac66f820650'
        elif self.__id__ == 8:
            return 'ecc391b9-6108-4253-a9af-03d4fa791020'
        elif self.__id__ == 9:
            return '6bc51417-83c6-4008-a8a8-1cab2026ed5f'
        elif self.__id__ == 10:
            return 'ecfb4198-a2af-4c37-9f30-a0a6e55c4892'
