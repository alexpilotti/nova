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
            return 'e8d0288a-15ba-4647-a714-1054db0f506d'
        elif self.__id__ == 3:
            return '23b7d04f-5fad-4305-9555-3e553fcf6510'
        elif self.__id__ == 4:
            return 'bc699e55-6fa2-40e4-bad1-7554e9e68631'
        elif self.__id__ == 5:
            return '18f851ad-fe9b-4304-8668-52d346e7f244'
        elif self.__id__ == 6:
            return '0f3ff39c-c0e5-4fe7-b440-d154558a8a2f'
        elif self.__id__ == 7:
            return '0fad52db-33a0-4959-8451-37a6cc1ddcab'
        elif self.__id__ == 8:
            return '49bef8a3-d697-4945-b8c4-0b19161aa540'
        elif self.__id__ == 9:
            return '1391d092-a332-47b6-8ca5-a3a2d5062fcf'
        elif self.__id__ == 10:
            return '7323b20a-06f9-422b-a807-a81cb10a7614'
