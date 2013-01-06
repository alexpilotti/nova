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
            return 'a5d2f72a-7475-4e13-82e7-76f7a7d943a0'
        elif self.__id__ == 3:
            return '0e2f93d7-fe15-446d-aa37-5e571375eb88'
        elif self.__id__ == 4:
            return 'b3dbd42a-8da0-4659-ab91-0701733be7a2'
        elif self.__id__ == 5:
            return '5da947d4-23b3-481c-99c4-192448a9db45'
        elif self.__id__ == 6:
            return 'ed75482d-d60f-4801-9005-31ead4a2af32'
        elif self.__id__ == 7:
            return '2cbe07b1-064a-4766-bec9-87c09c74ccb9'
        elif self.__id__ == 8:
            return 'df94c23f-6b5c-4d0c-acbe-b93d398f2210'
        elif self.__id__ == 9:
            return 'a38d7a90-a536-4545-8cf8-62ae5779b310'
        elif self.__id__ == 10:
            return '536e8623-7549-4af8-9123-452a72d6b081'
