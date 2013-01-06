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
            return 'd7c25f8a-2da4-48ae-b16e-6d13c224a8b4'
        elif self.__id__ == 3:
            return '1caba02f-06b4-450a-abfe-7e36a74db234'
        elif self.__id__ == 4:
            return '14127685-d8d0-4017-8433-c312dd06fcca'
        elif self.__id__ == 5:
            return '212135b9-70fb-4a23-b4dd-cde1b775c1ba'
        elif self.__id__ == 6:
            return '6b41fe34-3dfc-45cd-83eb-8bd3e086af50'
        elif self.__id__ == 7:
            return 'be249a15-ac58-41b2-9380-c2b9ce99ef30'
        elif self.__id__ == 8:
            return '512590bb-6da9-4267-b4d5-f1f5f5acd3dd'
        elif self.__id__ == 9:
            return '450c1070-08c2-4276-995a-a896511d4846'
        elif self.__id__ == 10:
            return '0fae32a7-5ee2-4b0e-ba7f-e71f817e1523'
