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
            return '4a7c7e1d-c8c9-40c3-bab5-602a02effa1e'
        elif self.__id__ == 3:
            return '8b7d12b8-0b9e-4eb8-ae48-d585a995ef80'
        elif self.__id__ == 4:
            return 'f5647b9e-9949-4d74-9bb7-36c12b21fda9'
        elif self.__id__ == 5:
            return '2c6ba59a-ee52-42e3-a04d-1d98e417576b'
        elif self.__id__ == 6:
            return 'b28324ae-29c3-46e5-9e3e-fcde83c655e3'
        elif self.__id__ == 7:
            return '48ad703b-7b84-4d2b-8423-6551452d3dca'
        elif self.__id__ == 8:
            return 'a25e7f4a-2c37-4371-a60f-9c6de34ef65b'
        elif self.__id__ == 9:
            return '1c04eb02-8a31-48e7-a2c4-ccbd8b4a371b'
        elif self.__id__ == 10:
            return '73f5d148-227e-4bc4-801d-0a120407085f'
