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
            return 'debfdf91-51a1-4787-ace7-8ebd753bfa03'
        elif self.__id__ == 3:
            return '55f2e09c-851d-42bd-9636-1f5e5ae2adfd'
        elif self.__id__ == 4:
            return '85818823-31b3-4a60-9a37-51e131f27150'
        elif self.__id__ == 5:
            return '5f628726-0f63-4de1-b635-6d308dd2c1d5'
        elif self.__id__ == 6:
            return 'bdcfb436-dd41-417a-8f4e-90158ede5d55'
        elif self.__id__ == 7:
            return '5a00a282-2a23-44ba-82f0-7ae3faaa4568'
        elif self.__id__ == 8:
            return '552ed28d-7ecc-4b39-a06a-598cbbe0a4d0'
        elif self.__id__ == 9:
            return '845593c5-e64a-469b-ba61-0af8b285f4e5'
        elif self.__id__ == 10:
            return 'f797be73-6c84-4a32-a063-5eca8e241ddc'
