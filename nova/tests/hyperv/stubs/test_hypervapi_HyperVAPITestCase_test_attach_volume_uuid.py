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
    elif _uuid4_count_0 == 9:
        v = UUID(11)
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
            return '67a39e13-209c-4108-8bd8-54c0ea5832bb'
        elif self.__id__ == 3:
            return 'b05f5e4a-8b68-4d41-afdd-4ec322e8f082'
        elif self.__id__ == 4:
            return 'ef8c4aac-5499-4d28-8d04-6a5a5ec7b3ff'
        elif self.__id__ == 5:
            return '4a94bb43-4fbd-40ab-b174-68f48097e0db'
        elif self.__id__ == 6:
            return '179f705a-d9dd-490f-b94d-81fc0cd54788'
        elif self.__id__ == 7:
            return '0b447533-4a42-4b70-95f7-eb0e317d47df'
        elif self.__id__ == 8:
            return '5dc852bd-4fc9-488e-9907-7c1f51940c4c'
        elif self.__id__ == 9:
            return '76eb2345-4700-4077-ba32-8d3a2d8f07ab'
        elif self.__id__ == 10:
            return 'a9196905-c530-4bb5-bf89-21584ec59c67'
        elif self.__id__ == 11:
            return '96a27d1d-74ad-4054-9450-1bb9887d15ea'
