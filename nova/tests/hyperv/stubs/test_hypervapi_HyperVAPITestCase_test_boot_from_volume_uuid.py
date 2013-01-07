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
            return '387799c4-c4cd-491f-99f3-9d7b3dad5593'
        elif self.__id__ == 3:
            return 'bbc84cfc-7f02-4a2b-af5e-05a232564e8d'
        elif self.__id__ == 4:
            return '6cf5bc07-6819-4f1e-b0ff-82db6271596c'
        elif self.__id__ == 5:
            return '04fb8104-eed4-4c7d-b560-3ee50248fd26'
        elif self.__id__ == 6:
            return 'ad44f84f-aa24-48e5-8ec3-520beb4222a4'
        elif self.__id__ == 7:
            return 'a0e0b8a0-8839-4589-b22e-c0cf197fbebc'
        elif self.__id__ == 8:
            return 'f29935f2-7352-45ca-a7ca-52b41a9ff5a3'
        elif self.__id__ == 9:
            return '7d2effab-137b-4397-be90-a99b385ad3db'
