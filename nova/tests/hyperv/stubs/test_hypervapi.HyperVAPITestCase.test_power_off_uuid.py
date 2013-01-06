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
            return 'f317c664-b994-4156-86c5-888238eece9e'
        elif self.__id__ == 3:
            return 'f9748e6e-0b01-4bab-97ac-1794192c75b7'
        elif self.__id__ == 4:
            return '6f8f430b-612c-478b-942d-b078ff78b259'
        elif self.__id__ == 5:
            return '00f43100-0943-42dc-9dcd-574abf5b77ab'
        elif self.__id__ == 6:
            return 'b0651b0f-3548-4049-8f51-26b86d344b71'
        elif self.__id__ == 7:
            return 'a563debb-b738-48c0-a337-d7a02c7af46b'
        elif self.__id__ == 8:
            return '5962e4b7-6968-4a6e-9f93-04d296f4aa9f'
        elif self.__id__ == 9:
            return 'cf8d1bc5-879c-466a-9aa4-1032d5745035'
        elif self.__id__ == 10:
            return 'e540a396-f728-4bd6-b761-f78f4c780dcd'
