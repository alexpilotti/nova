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
            return 'f1b2123c-0c77-47b3-840e-e16a9e5cc205'
        elif self.__id__ == 3:
            return 'b89dc74f-5395-4a13-88b4-fd5f8d941f92'
        elif self.__id__ == 4:
            return '5cc5dc46-a977-45f8-afc7-dd2bfea198de'
        elif self.__id__ == 5:
            return '5eabbae6-0f3d-4267-aa58-ddf09b2110d5'
        elif self.__id__ == 6:
            return '6396c766-9d32-404f-b0c3-94ca30e7207f'
        elif self.__id__ == 7:
            return '99772e86-442d-4b12-b399-32bffe2245b1'
        elif self.__id__ == 8:
            return 'cadd80c1-6f94-4ae6-9ded-812d898422ed'
        elif self.__id__ == 9:
            return '297edfab-7b2d-4acc-adb3-42c01b35eb12'
        elif self.__id__ == 10:
            return '3313cad1-528d-436f-9f13-41a4784f7864'
