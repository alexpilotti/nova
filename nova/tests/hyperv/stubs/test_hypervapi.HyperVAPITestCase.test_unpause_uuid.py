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
            return '30a2d910-8b96-4c9a-8d5c-6e1930d9eb20'
        elif self.__id__ == 3:
            return '0f03304b-f9ab-4a25-8e27-c566427ab372'
        elif self.__id__ == 4:
            return 'ea15212b-74e8-4bfa-a2d1-424b9efb1938'
        elif self.__id__ == 5:
            return '39d760bd-c0c0-495f-a45f-ef2b849ba687'
        elif self.__id__ == 6:
            return '292cb804-dcdb-4de9-9a7b-492c74ac5cc0'
        elif self.__id__ == 7:
            return '60658a0f-485f-442a-8233-4d8fba09f1b4'
        elif self.__id__ == 8:
            return '9c65510a-29a5-484a-b59d-b31e4c9a0454'
        elif self.__id__ == 9:
            return '8d04b440-22d7-4f92-8d01-bd14120b8aa9'
        elif self.__id__ == 10:
            return '6a94f92b-5a25-47de-97b9-ce87511f3639'
