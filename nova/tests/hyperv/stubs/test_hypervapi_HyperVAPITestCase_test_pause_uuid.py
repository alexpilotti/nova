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

    def __init__(self, *args, **kwargs):
        pass

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__


    def __str__(self):
        if self.__id__ == 2:
            return 'c05b4937-016d-44e0-ad50-8740c1a1cee9'
        elif self.__id__ == 3:
            return '5311a4db-2e40-4b14-9451-cfb511736543'
        elif self.__id__ == 4:
            return '31e92588-c455-4894-86e0-b4e83901e8ce'
        elif self.__id__ == 5:
            return 'a560b020-2734-4377-8dfc-1f200f9fe617'
        elif self.__id__ == 6:
            return '10c4a802-a0e5-4955-a146-cc77321cbefd'
        elif self.__id__ == 7:
            return 'a33fba28-8bdb-4299-91a8-d5d84799877f'
        elif self.__id__ == 8:
            return 'ea18d330-df44-4421-acf4-6232b43cba08'
        elif self.__id__ == 9:
            return '00d2f2bb-6011-4443-a13d-ab02acebea19'
        elif self.__id__ == 10:
            return 'ce77cb66-926c-44f4-889e-975c28f8dbe4'
