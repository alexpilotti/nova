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

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__

    def __str__(self):
        if self.__id__ == 2:
            return '5276dd6f-fd3a-41da-8799-352039c91e80'
        elif self.__id__ == 3:
            return 'c28406b0-2728-4b79-afda-5be0c0f55099'
        elif self.__id__ == 4:
            return '1e73ad83-4828-4f95-92c0-caf0430fc713'
        elif self.__id__ == 5:
            return '2db2b60d-dcbf-451c-b550-83dfeb068c53'
        elif self.__id__ == 6:
            return '547f2602-93d4-40d5-b1e8-21775ca79561'
        elif self.__id__ == 7:
            return 'a5c2c5e4-c967-42b2-9434-7150203b17d8'
        elif self.__id__ == 8:
            return 'ca0617eb-d040-4008-a0b7-561358e1e071'
        elif self.__id__ == 9:
            return 'f6bc9888-b4e9-4f3b-9027-e91290155372'
        elif self.__id__ == 10:
            return '81c6465e-c9fc-40df-832d-7be5fdc33ff6'
        elif self.__id__ == 11:
            return 'd2f216ef-4d56-4189-92e6-73abd638fe8e'
        elif self.__id__ == 12:
            return '8bf956f4-f8ff-4da5-aec8-ed8f97145b2b'
