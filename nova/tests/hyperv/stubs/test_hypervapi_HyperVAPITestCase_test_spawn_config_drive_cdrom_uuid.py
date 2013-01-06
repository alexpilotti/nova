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
    elif _uuid4_count_0 == 9:
        v = UUID()
        v.__instance_id__ = 11
    elif _uuid4_count_0 == 10:
        v = UUID()
        v.__instance_id__ = 12
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
            return '15983892-548b-4b11-8d77-323bbf89fabc'
        elif self.__id__ == 3:
            return '8b11b9d9-b8cd-447e-8b8a-3567f3bfe49d'
        elif self.__id__ == 4:
            return 'd930b3ef-7fba-460b-88f1-d1b92cdf9bef'
        elif self.__id__ == 5:
            return '377321ee-fd75-416e-9b78-870063ed8e8f'
        elif self.__id__ == 6:
            return 'd616f68b-697f-4cd9-a96a-8fc35e5a6fff'
        elif self.__id__ == 7:
            return '1a3e162b-b380-4a1d-bfca-7335f0e5bf3c'
        elif self.__id__ == 8:
            return 'f1f23f75-e4d5-4765-9be9-e595aefd772d'
        elif self.__id__ == 9:
            return 'aef00cd8-7ee2-4934-bd75-99bdd7db02e1'
        elif self.__id__ == 10:
            return 'ba856a5b-b4a2-4481-a266-57c683cffc09'
        elif self.__id__ == 11:
            return '09adc9d5-04d4-443d-a86a-86f657c38a0b'
        elif self.__id__ == 12:
            return '3a5ed990-2680-4df8-a537-a657bedd24bf'
