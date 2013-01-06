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
            return '8f48846f-f6c3-4aae-b34c-84824d13810a'
        elif self.__id__ == 3:
            return '75ed1297-51b3-450c-b91d-f519440348c9'
        elif self.__id__ == 4:
            return '5aadf3b0-aa84-4775-956e-63d7fe0ebd0c'
        elif self.__id__ == 5:
            return 'cf8e49ca-6e25-4c06-bfbc-bfa269a19b1c'
        elif self.__id__ == 6:
            return '22f6b2c9-0716-473c-bd6d-d03de1b9da65'
        elif self.__id__ == 7:
            return 'f9e0f031-c938-4e79-afeb-b7e0499bba10'
        elif self.__id__ == 8:
            return '56a868db-daa2-4ad9-9136-327ad5df5158'
        elif self.__id__ == 9:
            return 'a278f7f6-2218-49d2-85fc-1f32034ca779'
        elif self.__id__ == 10:
            return '647aa305-966f-47a6-ba82-4a63d3ad3e7b'
