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
    elif _uuid4_count_0 == 9:
        v = UUID(11)
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
            return '585d0ad8-1b54-490f-83cf-f773089a8be8'
        elif self.__id__ == 3:
            return 'ec4ac9d6-e1e6-434e-9018-5bbf0493c3d8'
        elif self.__id__ == 4:
            return 'f6f1e394-dff3-41dc-a7aa-e32f19eab258'
        elif self.__id__ == 5:
            return 'dc94e436-d985-4d6f-bb58-11d11db095e2'
        elif self.__id__ == 6:
            return '0ddb3993-d48c-4030-a0c0-a5cb6e87eadc'
        elif self.__id__ == 7:
            return 'ee5c621d-bdbc-4454-8881-a0fd2463e460'
        elif self.__id__ == 8:
            return 'cded883b-eb74-4331-ad13-6f6d3310c408'
        elif self.__id__ == 9:
            return 'c05e37c4-ca78-45ff-8959-d9f96a0d070f'
        elif self.__id__ == 10:
            return '2a2e6c05-dc9f-46cf-91cb-c9a41c85e245'
        elif self.__id__ == 11:
            return '6b187bd4-17b6-4629-ba35-676813869747'
