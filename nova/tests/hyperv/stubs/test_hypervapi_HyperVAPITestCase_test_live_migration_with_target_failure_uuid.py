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
            return 'e0fcfead-58c5-44c5-938f-a050ef7d9284'
        elif self.__id__ == 3:
            return 'ae21195a-7415-42c3-8cab-a5139d959ef0'
        elif self.__id__ == 4:
            return 'b4144737-0893-4257-8834-3a522378c536'
        elif self.__id__ == 5:
            return '6e2778ba-f706-4367-9b90-0ed053fa5072'
        elif self.__id__ == 6:
            return '770adaf9-f971-48d0-84b2-10250840576d'
        elif self.__id__ == 7:
            return 'd9851fff-c5d3-45cd-9e7c-c9cb1c1473b4'
        elif self.__id__ == 8:
            return '75da7c69-e774-4db8-b5b9-2e1ec0c46c63'
        elif self.__id__ == 9:
            return '58bc32d8-a3ca-411a-accd-54cc557d755f'
        elif self.__id__ == 10:
            return '1fad5d23-a8ff-4f5a-a995-30c601ff9988'
