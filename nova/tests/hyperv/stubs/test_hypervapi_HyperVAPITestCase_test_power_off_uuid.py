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
            return '5a7fc31c-9c1a-4a36-90c3-e0d4b7df8dce'
        elif self.__id__ == 3:
            return '4d206b83-9f61-468b-bb4f-5c305f6e1487'
        elif self.__id__ == 4:
            return '84208e58-d982-4a5e-aff0-31c960873acb'
        elif self.__id__ == 5:
            return '8aced857-d2ca-4bc7-bfd5-4ab0b55eabc9'
        elif self.__id__ == 6:
            return '40a2f852-e60e-4dc9-85dd-74f232f140bb'
        elif self.__id__ == 7:
            return 'e664c04c-0c22-49e4-bb07-9ead40df2062'
        elif self.__id__ == 8:
            return '775cee8c-08ff-4fde-89ae-13a53c8281e6'
        elif self.__id__ == 9:
            return '01767fac-5f59-4414-a7f7-41b4f10e9d2f'
        elif self.__id__ == 10:
            return 'fc6dbef6-cf60-4551-b015-dfb55bb93494'
