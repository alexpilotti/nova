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

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__

    def __str__(self):
        if self.__id__ == 2:
            return '590db1b1-4a09-4d66-ad75-d725c60b2d64'
        elif self.__id__ == 3:
            return '24168230-19ca-4f1c-aff1-59f64994967f'
        elif self.__id__ == 4:
            return 'e4c4f74a-1727-4e76-b9b7-b578c6cc31ba'
        elif self.__id__ == 5:
            return '640d098d-eac1-49d4-8e5b-f02cff14c51d'
        elif self.__id__ == 6:
            return '2f701fa4-da71-4a09-aaa3-25f852241578'
        elif self.__id__ == 7:
            return 'dde20be2-9481-4dae-b7ef-adf1f28fccf1'
        elif self.__id__ == 8:
            return '061807b4-5a8c-4037-9465-bb7e4e6abfa9'
        elif self.__id__ == 9:
            return '9522a33b-51ae-49a9-bb08-0cb45644202e'
        elif self.__id__ == 10:
            return 'd1b5e08d-f8ef-4b72-9a1e-db11929b3730'
