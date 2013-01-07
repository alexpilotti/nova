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
            return 'd657c9de-3739-44c2-a2a2-677288877041'
        elif self.__id__ == 3:
            return 'b572a115-6608-4b91-9aa2-9114312508c2'
        elif self.__id__ == 4:
            return '00d427f8-62aa-4cae-8d8c-b3179e3ffb7c'
        elif self.__id__ == 5:
            return '3a6f61de-f38f-4548-b873-a0629a2b0bbc'
        elif self.__id__ == 6:
            return '29f28d1a-a664-42bb-9699-8420e6db8e30'
        elif self.__id__ == 7:
            return '8b85db39-c560-4098-ba8e-eda81562bc47'
        elif self.__id__ == 8:
            return '67a84eb4-221f-4cee-8f0f-47e423771947'
        elif self.__id__ == 9:
            return '13af39db-a47a-4368-8414-1828aa895ac8'
        elif self.__id__ == 10:
            return '379c567e-e83e-4265-8ee9-5f3b919b07db'
