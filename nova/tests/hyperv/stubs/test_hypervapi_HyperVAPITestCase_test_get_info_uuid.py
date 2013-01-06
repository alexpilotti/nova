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
            return '429af6a7-195b-4300-9d77-fa1cabc1bd59'
        elif self.__id__ == 3:
            return 'ce9cb79d-edb8-40d3-83a5-ebc10ba7c175'
        elif self.__id__ == 4:
            return '3f08fad0-a7d6-498d-bca9-cfc5bc60e3cd'
        elif self.__id__ == 5:
            return '2f1d150e-7a69-4467-b847-f3490f28dcd5'
        elif self.__id__ == 6:
            return '55f87773-7b1f-4fdb-b230-0ce16730b835'
        elif self.__id__ == 7:
            return '390e07d6-56ab-4682-9364-787ee8061c71'
        elif self.__id__ == 8:
            return 'bda8e037-3720-47b0-ae22-64fd717b2d5f'
        elif self.__id__ == 9:
            return '1d39e175-e1c1-4202-b201-5a40bcd43f14'
        elif self.__id__ == 10:
            return 'ea11e057-17e2-4052-9d24-754007332135'
