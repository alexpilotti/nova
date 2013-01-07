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
            return 'fa50940f-808e-457b-8196-1be9026605d3'
        elif self.__id__ == 3:
            return 'ca2c9b66-be17-4501-a686-cdb73502e0bc'
        elif self.__id__ == 4:
            return '03ebf120-b3df-4f44-aa8a-8698716f31ff'
        elif self.__id__ == 5:
            return '6a980ff7-4672-499d-bb4f-35168034cd9c'
        elif self.__id__ == 6:
            return '9d20e46a-5f72-4ebb-9ce3-b7200d7d6edc'
        elif self.__id__ == 7:
            return '2d2526bf-0469-4218-acbb-9e6542f5e878'
        elif self.__id__ == 8:
            return 'f168458f-6638-4d20-a673-2c302f713272'
        elif self.__id__ == 9:
            return '542ca31e-78f9-40e5-ab2d-5f39130bfcd2'
        elif self.__id__ == 10:
            return '89dc36d7-3b2f-43b5-a621-99b7729b938f'
