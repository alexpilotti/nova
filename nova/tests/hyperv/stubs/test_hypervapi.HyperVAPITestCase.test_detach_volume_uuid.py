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
            return '9a3dd9aa-7471-4746-8dca-4b7eeabeda40'
        elif self.__id__ == 3:
            return '1544b3c3-f3b3-48bb-862f-8210ffc0bf0c'
        elif self.__id__ == 4:
            return 'efbe6500-ce52-4965-b84a-58c0850e5524'
        elif self.__id__ == 5:
            return 'd1033b1e-21f9-4fa5-aeb0-f3880b61f1ff'
        elif self.__id__ == 6:
            return '4175090f-0890-4ef9-8104-4476361070f7'
        elif self.__id__ == 7:
            return '89b9b84d-53de-4824-942e-9ce21d819c99'
        elif self.__id__ == 8:
            return 'ad88d02b-0710-49dc-9082-3304bd910ca3'
        elif self.__id__ == 9:
            return '100cba29-6dc7-4b7e-a643-d0057b554c4a'
        elif self.__id__ == 10:
            return 'b0f454c7-1643-43fb-9bc5-a3baef69be2b'
