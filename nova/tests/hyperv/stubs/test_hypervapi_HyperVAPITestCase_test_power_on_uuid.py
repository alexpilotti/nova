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
            return '2f35331e-c669-46af-9f31-a893a7e3db2a'
        elif self.__id__ == 3:
            return 'dec6d080-3b06-47b0-bd5a-fce265813340'
        elif self.__id__ == 4:
            return 'f5253828-075c-4042-8ea6-e67ff030903a'
        elif self.__id__ == 5:
            return '9de0c733-c249-4e58-8faf-d4ab20d36a7b'
        elif self.__id__ == 6:
            return 'ed3fc03c-5994-4c64-937a-ff6edfe29b90'
        elif self.__id__ == 7:
            return '0ae743df-22c6-42e3-8bc9-7f9f10370b63'
        elif self.__id__ == 8:
            return 'e0d9a8ea-e946-495d-bd5c-d926dffc4738'
        elif self.__id__ == 9:
            return '264260d3-d4ee-4d9b-9936-811eebf8a987'
        elif self.__id__ == 10:
            return 'b5c51f43-b789-4d18-8735-63dd2d09527e'
