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
            return 'f946e117-6439-4fa5-8583-5d40c3aab81f'
        elif self.__id__ == 3:
            return 'cb96b714-6a55-45cf-b7da-5871f914d067'
        elif self.__id__ == 4:
            return 'a53eae6e-1064-4def-807a-a6f30385809b'
        elif self.__id__ == 5:
            return 'b086c293-07ca-4f65-bf14-7869a50a966d'
        elif self.__id__ == 6:
            return '77815025-cf02-4988-8d26-03f38af9c356'
        elif self.__id__ == 7:
            return '7374f53d-5321-44a0-a4d3-ff0fd6899ba9'
        elif self.__id__ == 8:
            return 'b3e05079-9059-4200-ad1c-5675c101aaf1'
        elif self.__id__ == 9:
            return 'bd1f4212-dc3a-4093-9b82-ef00f959ee2b'
        elif self.__id__ == 10:
            return '309b9f79-9c87-47a7-ac30-4e0f2caba01d'
