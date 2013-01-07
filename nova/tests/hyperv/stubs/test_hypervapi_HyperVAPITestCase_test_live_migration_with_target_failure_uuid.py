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
            return 'ac172f02-305d-48c3-a153-99d634a07e1f'
        elif self.__id__ == 3:
            return '7ed53151-c798-40d6-89fc-f9f43059fbfe'
        elif self.__id__ == 4:
            return '76cb9ce1-47ef-46cf-86d7-f9b577ba78f7'
        elif self.__id__ == 5:
            return '6c1975e1-3f20-407e-bb36-20112aaf08f3'
        elif self.__id__ == 6:
            return 'f95b92e4-b083-411e-a512-63962ba2f853'
        elif self.__id__ == 7:
            return '2b18c380-1aeb-40c8-8475-aaf7e5f52ab8'
        elif self.__id__ == 8:
            return '7790c8c9-4048-466a-9f13-b535a524d2ce'
        elif self.__id__ == 9:
            return '73f6e404-99e7-42e5-845c-ad240f504daf'
        elif self.__id__ == 10:
            return '750b98f2-72dc-4e5b-a7c0-75063a3bc6fc'
