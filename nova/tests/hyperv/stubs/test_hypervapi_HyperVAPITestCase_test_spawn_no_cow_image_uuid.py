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
            return '0866fef5-e332-43b9-bc19-a992e98d8ee5'
        elif self.__id__ == 3:
            return '8561a879-fd02-454e-a2f6-47b251cb7f29'
        elif self.__id__ == 4:
            return '843f536c-524f-4ad1-b465-4ecc8b719009'
        elif self.__id__ == 5:
            return 'baa8a73c-eedf-44db-904f-ae8dcbe5987b'
        elif self.__id__ == 6:
            return '7d9a8222-820a-4b7a-89e3-1e3eb0c1d82b'
        elif self.__id__ == 7:
            return '8a72657b-cdb7-4f00-a8ec-dd0cc3502323'
        elif self.__id__ == 8:
            return 'f74095ab-7096-43fe-97c9-f053f5b32e61'
        elif self.__id__ == 9:
            return 'f003ae6b-bf68-44e7-be3a-d863ec67a419'
        elif self.__id__ == 10:
            return '7d70b10c-bc3b-4d7e-827d-b799880225fa'
