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

    def __init__(self, *args, **kwargs):
        pass

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__


    def __str__(self):
        if self.__id__ == 2:
            return '7d456c14-0817-4ba0-8dde-6853694fe457'
        elif self.__id__ == 3:
            return '41e2f0e1-b202-402a-8fc4-d3b9d2af54e1'
        elif self.__id__ == 4:
            return '9c71a7f7-85ad-4775-810c-2efea36a2c94'
        elif self.__id__ == 5:
            return '34fda82e-81f4-4759-8fca-bf3afd350868'
        elif self.__id__ == 6:
            return '1f06b9aa-625b-4d6a-9531-2076a4b08fcf'
        elif self.__id__ == 7:
            return 'cc4258a1-5d61-439b-bae3-27c03063c0be'
        elif self.__id__ == 8:
            return 'e2580c06-cdd7-4355-820a-01664c9d54eb'
        elif self.__id__ == 9:
            return '10e90b77-e2a7-47a3-aa3c-b847cc4ed7e3'
        elif self.__id__ == 10:
            return 'd900a4c2-2436-4c85-88ac-e6fe427b3cb5'
