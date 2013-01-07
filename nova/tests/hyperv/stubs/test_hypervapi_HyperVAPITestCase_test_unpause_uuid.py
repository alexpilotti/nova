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
            return '10bfc386-c072-4446-8a76-ff06d6ddae66'
        elif self.__id__ == 3:
            return '87410674-de59-482b-b82b-1659aa60a4e5'
        elif self.__id__ == 4:
            return 'bd10a9e4-5b3d-49b5-83fc-06313de662dd'
        elif self.__id__ == 5:
            return '9712a0bd-c7ee-45cc-8709-531976822e3e'
        elif self.__id__ == 6:
            return 'a7e9bb56-c88c-459a-a590-9124c55c2356'
        elif self.__id__ == 7:
            return '8b05a9fa-28c2-4b28-9b77-d9f79527b339'
        elif self.__id__ == 8:
            return 'a6f99c4a-9957-429d-8120-6094a4aded06'
        elif self.__id__ == 9:
            return '1f533389-4ab1-4c01-b1ec-d3c438efd600'
        elif self.__id__ == 10:
            return 'b386cb45-bf0b-4522-8c45-d20a9b1c4713'
