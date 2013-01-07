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
    elif _uuid4_count_0 == 10:
        v = UUID(12)
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
            return '81f8b976-3c30-4d1c-8c7a-091e55c1ca9d'
        elif self.__id__ == 3:
            return 'ec10c996-9271-4b26-a0c7-ad2b60223b93'
        elif self.__id__ == 4:
            return 'b10fc8c3-9453-402e-a0ef-9ef712a185fe'
        elif self.__id__ == 5:
            return 'ee223cf9-7f5e-4127-b3eb-773ce7168025'
        elif self.__id__ == 6:
            return '3f69f372-12f8-4ea6-99bb-96c7a4239c13'
        elif self.__id__ == 7:
            return '63bfbcd6-d7df-4094-af0f-6ebb0fba6f84'
        elif self.__id__ == 8:
            return 'b26b5b15-b849-4166-bee6-9653b04347b0'
        elif self.__id__ == 9:
            return '665c008a-1428-4141-89ff-0b07b2627913'
        elif self.__id__ == 10:
            return '5fabfcab-ccc2-4ff8-9190-8546611a2301'
        elif self.__id__ == 11:
            return '4a71002d-c902-415d-abff-f2f1b9897420'
        elif self.__id__ == 12:
            return '51e43592-286f-41c9-9edc-f0322b7dec76'
