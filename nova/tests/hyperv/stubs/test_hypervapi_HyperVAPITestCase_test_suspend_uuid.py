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
            return '5731f99b-bceb-4416-bb49-7a1a0962d5ac'
        elif self.__id__ == 3:
            return '484d5418-6d21-476c-a04e-df2349a989da'
        elif self.__id__ == 4:
            return '1461f7b4-6b35-44a8-9f0d-586456283043'
        elif self.__id__ == 5:
            return 'f939876b-407f-43f0-9432-ffa05db51b78'
        elif self.__id__ == 6:
            return '5dde4026-0393-4a85-8f9f-d2115be6a07c'
        elif self.__id__ == 7:
            return 'de561165-1272-4df6-b310-357e4b2fcfa1'
        elif self.__id__ == 8:
            return '9118d593-3635-46af-8d98-e9b1d71ffadd'
        elif self.__id__ == 9:
            return '68f26049-4d16-4e8a-8bdc-cd6f040937dc'
        elif self.__id__ == 10:
            return '6217c9de-9e45-4c5e-8d8a-05dce8d23e12'
