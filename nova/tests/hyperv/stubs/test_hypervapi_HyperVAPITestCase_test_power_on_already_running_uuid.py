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
            return 'e6d398eb-c6c0-4b22-b163-febe6c1ca04f'
        elif self.__id__ == 3:
            return 'f96254fb-e1b7-458f-9fd9-4580483e93f2'
        elif self.__id__ == 4:
            return 'a91da09f-32d9-405e-bdfe-e8db32740ffe'
        elif self.__id__ == 5:
            return 'f34a8a61-d197-4c11-a8ad-78ebaee2d6b0'
        elif self.__id__ == 6:
            return '375a9df3-4db9-4159-9f8c-f7ed7420c778'
        elif self.__id__ == 7:
            return 'ec9bab22-4727-4a4d-9b17-4ef8ca83d082'
        elif self.__id__ == 8:
            return '762bc18c-3a92-4412-b04b-f51d4165c1aa'
        elif self.__id__ == 9:
            return '4c21883d-a2a5-4024-a68e-f8227ad0708a'
        elif self.__id__ == 10:
            return '5c73844f-f5a3-4346-b533-fcbd3fc09b68'
