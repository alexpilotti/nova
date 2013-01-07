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
            return 'fe88a3b0-6f96-4fa7-bf46-ccfbbb618bf0'
        elif self.__id__ == 3:
            return '63352981-ce6b-4193-8d60-246c657baf20'
        elif self.__id__ == 4:
            return 'e161d6a6-e84a-43d3-9e98-0a78802eed2d'
        elif self.__id__ == 5:
            return '5184445f-413e-4a36-93f1-5cd1c57e0581'
        elif self.__id__ == 6:
            return 'e1249ea0-ef00-4863-995c-12ff64826f12'
        elif self.__id__ == 7:
            return '8897493e-8463-4352-a265-6e4917bc2564'
        elif self.__id__ == 8:
            return '64d9fae9-5932-4ed0-a2dd-4e29fd6204dc'
        elif self.__id__ == 9:
            return '63997476-5531-4f85-b0fe-cfa857d83f5d'
        elif self.__id__ == 10:
            return 'ec93f40e-bf11-4880-b47b-2983f6cef5d0'
