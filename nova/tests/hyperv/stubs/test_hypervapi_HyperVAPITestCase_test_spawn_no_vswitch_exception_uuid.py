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
            return 'b79ebb6f-cccd-4975-96b4-3d614163faf0'
        elif self.__id__ == 3:
            return '187d436f-40e9-4f70-b2e6-ea707991785f'
        elif self.__id__ == 4:
            return '714ff188-7f72-48a1-843b-aef8d5c5e101'
        elif self.__id__ == 5:
            return '716e2f1b-ad8d-41f6-ac4f-5c49a13260ba'
        elif self.__id__ == 6:
            return '1567e892-00f4-417e-b064-105699d827ff'
        elif self.__id__ == 7:
            return 'b618cb0d-a0fc-4ee7-b4af-f44ae538a3f9'
        elif self.__id__ == 8:
            return '30ccfd1d-0420-40cb-b11d-5dc0fb3522b6'
        elif self.__id__ == 9:
            return '8c09fae4-6976-40a6-8617-e31c0cc0cb28'
        elif self.__id__ == 10:
            return 'b96cd55f-0649-421c-bd90-21a280eb5003'
        elif self.__id__ == 11:
            return 'af5d30e0-3ec1-4b0c-b2a4-6ddc2d383f39'
