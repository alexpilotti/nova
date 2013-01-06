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
            return '80d55410-354e-4fd8-8f6b-432f9be8258b'
        elif self.__id__ == 3:
            return '0da52bd3-345d-405b-9b89-b37fb480b0ac'
        elif self.__id__ == 4:
            return '491c811c-dd70-4ee6-aa2a-c160ba0d08f5'
        elif self.__id__ == 5:
            return '4871bed0-61aa-4994-9103-6129818c98f1'
        elif self.__id__ == 6:
            return '921314f5-4c1e-4d24-a613-a04a663ac422'
        elif self.__id__ == 7:
            return '50f92a71-dec4-4b8a-a2cd-a18ef4b612c0'
        elif self.__id__ == 8:
            return '6b325303-2281-4dc7-b403-9cf9ed050a49'
        elif self.__id__ == 9:
            return '928f6868-98ce-42c1-9aeb-92f71e9fa2e1'
        elif self.__id__ == 10:
            return 'ad668e59-e53b-4857-a924-7ce6c9f35fb1'
