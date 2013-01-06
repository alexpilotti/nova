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
            return '7080e213-a0bb-4c56-933f-16428976af3c'
        elif self.__id__ == 3:
            return 'e9d720a5-00cc-4a53-b332-2902c5065d49'
        elif self.__id__ == 4:
            return 'bf941539-b1c1-46bb-be1c-608c85bdc2b8'
        elif self.__id__ == 5:
            return '2128239a-82b0-4157-b4e7-1010376e327c'
        elif self.__id__ == 6:
            return 'b049a65c-af93-4a9e-9e90-f93e3f896fb9'
        elif self.__id__ == 7:
            return '39be47be-97a2-47c0-97aa-b9471cf20ae3'
        elif self.__id__ == 8:
            return '3f28b5b5-9699-4c66-b671-0e30908f9188'
        elif self.__id__ == 9:
            return '694c3110-71e1-4069-9f9e-fbbf15fd32d4'
        elif self.__id__ == 10:
            return '0c924148-a7bf-4282-9665-d805798724d0'
