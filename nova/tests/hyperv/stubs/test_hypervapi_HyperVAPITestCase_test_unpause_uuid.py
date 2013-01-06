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
            return 'b5f9ff50-f87c-477f-a813-35fd1b3239d3'
        elif self.__id__ == 3:
            return '4557e661-e58a-41d6-a83b-04881ed85985'
        elif self.__id__ == 4:
            return '73914065-b295-4594-839a-c7243f24bbd6'
        elif self.__id__ == 5:
            return '6f15cd41-1cda-4d74-89e1-7840369d61d7'
        elif self.__id__ == 6:
            return 'a56a03a7-9a2e-408c-baa9-895a17b93af9'
        elif self.__id__ == 7:
            return '784250dd-e10f-41bd-bc3f-e1604625ad19'
        elif self.__id__ == 8:
            return '7862ba50-d0ab-4652-a014-f1992cb585f9'
        elif self.__id__ == 9:
            return 'e80d3b00-112a-435b-9e68-680609d3a769'
        elif self.__id__ == 10:
            return 'c9e911a5-c441-4646-addd-0d5d56929338'
