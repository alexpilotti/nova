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
            return '593f5f6a-e9b7-48d9-bef0-c96b3b8a77b0'
        elif self.__id__ == 3:
            return '3987c451-edb6-4a11-9757-662226212e81'
        elif self.__id__ == 4:
            return '112d3b8a-e0f6-4b13-8d0f-f13189b444cc'
        elif self.__id__ == 5:
            return 'c3121c93-4cdc-4399-a575-53cb8dd60b5d'
        elif self.__id__ == 6:
            return 'e0f60c3e-9211-4ccb-bd53-f6fa0c61b914'
        elif self.__id__ == 7:
            return '6edd8eb4-53d4-4af2-8786-278ac9211b2c'
        elif self.__id__ == 8:
            return 'b7533706-faa7-4226-81af-a13547c352b2'
        elif self.__id__ == 9:
            return '6f0d4cec-b103-4a98-8284-68d1c6a60d8e'
        elif self.__id__ == 10:
            return '0f908e83-076c-4476-ad5c-6f003e5dc62a'
