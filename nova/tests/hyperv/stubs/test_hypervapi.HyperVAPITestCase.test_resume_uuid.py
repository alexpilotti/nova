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
            return '8e61a5f0-a997-4642-993d-5b2933bad05f'
        elif self.__id__ == 3:
            return '74cdc93a-7d74-4cb8-a5bb-c49e54bef612'
        elif self.__id__ == 4:
            return 'f2a281be-6ac3-4812-bd29-6b1521a4c3c1'
        elif self.__id__ == 5:
            return 'abe394a6-f252-453a-96f1-870e598aed69'
        elif self.__id__ == 6:
            return 'a358ae28-ffa5-4190-9992-b708ea903af7'
        elif self.__id__ == 7:
            return '48ea39e3-aa79-4754-9313-233c115bb6e1'
        elif self.__id__ == 8:
            return '43110d36-e027-4580-b3c4-79df15daf6c4'
        elif self.__id__ == 9:
            return 'dec2f6b5-b878-4fcb-9f9b-64c483774fd0'
        elif self.__id__ == 10:
            return 'c376b985-dec2-4468-8fba-0a442805b2c2'
