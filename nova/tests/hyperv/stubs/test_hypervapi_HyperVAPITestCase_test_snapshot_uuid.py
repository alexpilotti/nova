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
            return '2ccaa158-2156-46f0-a5a5-3032172e237e'
        elif self.__id__ == 3:
            return 'b97ab18a-23dd-4942-808a-441b1104ce8a'
        elif self.__id__ == 4:
            return 'dd1cc97a-a0b4-4e02-9d7b-0609c09ce282'
        elif self.__id__ == 5:
            return '0e87cf89-f5f5-46c2-966a-a5257c7d85c8'
        elif self.__id__ == 6:
            return '06d33e4f-1792-4164-935b-75ba26108d3a'
        elif self.__id__ == 7:
            return '36013ee7-8108-45b2-826b-59ecdfe348d9'
        elif self.__id__ == 8:
            return '822827ca-f8a6-4ffd-917d-b1b712181fc2'
        elif self.__id__ == 9:
            return '6cafaf68-96e2-4e06-943a-c2b86f1078a6'
        elif self.__id__ == 10:
            return '240dd9e4-e4ed-41d3-ab3f-9691b8f6220f'
        elif self.__id__ == 11:
            return 'ca9d1cc0-e130-467a-864b-493edcf8e00a'
