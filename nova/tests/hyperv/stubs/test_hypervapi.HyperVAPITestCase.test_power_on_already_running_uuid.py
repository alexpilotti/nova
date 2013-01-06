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
            return '7d3045fc-bf23-4b95-b09b-d7d8ae23d6b2'
        elif self.__id__ == 3:
            return 'd750f27b-e4f5-418e-b8cc-96bf3748423a'
        elif self.__id__ == 4:
            return '1ed7c1cd-7c68-4785-a4a1-c4bde6b09d74'
        elif self.__id__ == 5:
            return 'add9fecd-78b7-4ee1-afe6-2ae4c8b7b86a'
        elif self.__id__ == 6:
            return 'f3f87ac4-1ec6-4cf6-b805-4304743c81d4'
        elif self.__id__ == 7:
            return 'd48caccb-2ac7-4de6-8273-9de2e9c01a97'
        elif self.__id__ == 8:
            return '34cecae8-5d21-4f0b-8296-987a6093cf4e'
        elif self.__id__ == 9:
            return '7aa2fd55-bbf0-47f4-900c-88cd32203bb4'
        elif self.__id__ == 10:
            return 'e714d508-2083-4705-b0b0-1250f4425217'
