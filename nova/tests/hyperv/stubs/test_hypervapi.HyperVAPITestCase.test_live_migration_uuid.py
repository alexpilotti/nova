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
            return '97a523fb-b4c9-4387-9a52-6f81dd456309'
        elif self.__id__ == 3:
            return '61c310ee-e874-4a64-9dde-1c2d4fc1dfd1'
        elif self.__id__ == 4:
            return '22c39333-3175-46c3-83fd-02c4c88354f1'
        elif self.__id__ == 5:
            return '62e291b1-c82b-43f3-9a6b-fb134ff7549b'
        elif self.__id__ == 6:
            return '9b8d3919-90e8-4743-af68-25bb3be943bc'
        elif self.__id__ == 7:
            return '1f2f5c80-b1b4-40ce-a1cc-cad769ef7e78'
        elif self.__id__ == 8:
            return 'bfeb0f97-1703-4333-a657-43029a879039'
        elif self.__id__ == 9:
            return '40b22d51-7f10-4b77-99bb-b8b5ff1acaab'
        elif self.__id__ == 10:
            return '946349ff-aefd-4bb5-8e43-f5b01e3e70b0'
