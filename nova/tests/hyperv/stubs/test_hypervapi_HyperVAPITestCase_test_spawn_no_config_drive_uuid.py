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
            return '2d08a0b0-31c0-41f3-8108-e87569b1591b'
        elif self.__id__ == 3:
            return 'c8bf9a17-70ba-45cd-9550-ddf096d56de5'
        elif self.__id__ == 4:
            return 'edcc0614-b734-4e5a-89e0-370b1f25dbf1'
        elif self.__id__ == 5:
            return '16c65add-1007-4066-9d13-e1a636faa05d'
        elif self.__id__ == 6:
            return 'b9e622f7-8617-48b7-9e23-b66046a39103'
        elif self.__id__ == 7:
            return '434089b0-38a1-4222-a39a-0589b0273524'
        elif self.__id__ == 8:
            return '158eee15-3cdb-4e63-bddc-0723aaa3a2e5'
        elif self.__id__ == 9:
            return 'afcf95d9-f4c4-4706-a89e-3f238b5719f3'
        elif self.__id__ == 10:
            return '56a1b5e2-31f5-4e22-83e8-965ca97ae001'
