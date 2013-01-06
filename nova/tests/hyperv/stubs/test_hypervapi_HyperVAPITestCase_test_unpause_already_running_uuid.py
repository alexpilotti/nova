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
            return '5e78ae7c-b4ad-453d-a619-9c6c0ac2c9b9'
        elif self.__id__ == 3:
            return 'e7e44c4d-54ab-41a4-bec9-12515783868f'
        elif self.__id__ == 4:
            return '5ce6a9ed-427a-43b7-8a99-cf35ab0c7b8b'
        elif self.__id__ == 5:
            return 'a607f125-96de-4d36-bc4a-29494784a014'
        elif self.__id__ == 6:
            return '7e556da0-6435-4706-a987-f23751e852e4'
        elif self.__id__ == 7:
            return 'bd298d3b-2569-4c65-b0cf-905071904483'
        elif self.__id__ == 8:
            return '40da3bcb-b517-4566-a831-b09ef559aa18'
        elif self.__id__ == 9:
            return 'ed3435a2-bddc-4504-b760-8c502291fcab'
        elif self.__id__ == 10:
            return '2520e711-751b-4e51-a319-b7c134b819a6'
