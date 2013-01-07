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
            return 'f20cbe84-2bc5-4fd7-9a02-d7a3be306ebc'
        elif self.__id__ == 3:
            return '214c8ba2-ee80-441b-bd18-04da6391ed1c'
        elif self.__id__ == 4:
            return '26555113-9b2b-4e18-8db5-fb94193f42eb'
        elif self.__id__ == 5:
            return 'e574cfc2-9328-42f7-943c-9baff65109f9'
        elif self.__id__ == 6:
            return '03fde2f5-099b-493a-a2a5-aca64f355bb1'
        elif self.__id__ == 7:
            return 'c70f0fb8-a95e-4660-8136-a5bb84145519'
        elif self.__id__ == 8:
            return '7fc13fc3-0ab1-48b8-9bfe-022a900e2f99'
        elif self.__id__ == 9:
            return '32ab334f-27d9-4994-b6fb-aa413ebb6a16'
        elif self.__id__ == 10:
            return 'a7146cc1-1da6-4277-b24c-e27d5762839d'
