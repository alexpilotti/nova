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
            return '44f3c9f0-32c7-4f7d-ba2c-0ccc1df1c5e5'
        elif self.__id__ == 3:
            return 'abb00aa5-f559-4a57-8dc9-756ad3ac8687'
        elif self.__id__ == 4:
            return '5987f521-0799-4a3c-8a8e-e4068071265f'
        elif self.__id__ == 5:
            return '2c164698-6ef1-4f3e-8bcf-d531f621addd'
        elif self.__id__ == 6:
            return 'df808f97-ab5f-402a-89c2-73f308cdabd5'
        elif self.__id__ == 7:
            return '7d1b4e90-e439-4667-8459-f11051e5adcf'
        elif self.__id__ == 8:
            return '73793ac0-c202-42d8-81b0-dd8466c426cc'
        elif self.__id__ == 9:
            return 'bd14c479-0f47-4972-95c6-4aa88b2a3d53'
        elif self.__id__ == 10:
            return '97cf8b08-9ce2-40a0-957e-f3ae925596b4'
