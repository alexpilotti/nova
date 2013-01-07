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
            return 'b54f5cae-7aa7-4809-8ba7-7b51e7c9e03d'
        elif self.__id__ == 3:
            return '45647d00-e6a8-4be4-a2cb-c9daee1da121'
        elif self.__id__ == 4:
            return 'e49bff6c-95b4-45e5-a3d7-65eff0f80aea'
        elif self.__id__ == 5:
            return '1fa95e64-6d55-4b66-8a0f-747b433a5e11'
        elif self.__id__ == 6:
            return '0f32025b-86e2-4c9a-bf63-13009f038f54'
        elif self.__id__ == 7:
            return '13409b50-1d63-4186-8b44-880dcc00f9ef'
        elif self.__id__ == 8:
            return '390bc387-35fb-4345-bd9c-58bfe8addb9b'
        elif self.__id__ == 9:
            return '494ba91f-7bd6-4006-aea1-38698cc5d712'
        elif self.__id__ == 10:
            return '27b552a5-f516-4d02-8cbb-3fd1ca5c7ed2'
