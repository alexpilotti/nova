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
            return '419ac48a-c4e3-4772-a9c1-af7b187f21a1'
        elif self.__id__ == 3:
            return '8766e771-4cfa-4ef3-8d2f-8936a31182cb'
        elif self.__id__ == 4:
            return '0904709e-c42b-4d75-a404-e26b8a2c2c41'
        elif self.__id__ == 5:
            return '124a4546-ca41-4f41-81ab-7ad054a3abc8'
        elif self.__id__ == 6:
            return '7678ac8e-88e5-4b0c-bc7e-7261660a29e7'
        elif self.__id__ == 7:
            return 'fdf5c091-2dd3-43fc-864f-cfcc0f11d6e5'
        elif self.__id__ == 8:
            return '073bc54e-d644-4e2c-9668-000738efb4a3'
        elif self.__id__ == 9:
            return 'a91e9b8c-8db6-4eb0-b59d-0f9f50806ca5'
        elif self.__id__ == 10:
            return '607efe9d-d90e-486e-b812-a0d926324767'
        elif self.__id__ == 11:
            return '15f22047-8a8b-4d81-aa4e-bf19be5a3733'
        elif self.__id__ == 12:
            return '62857f83-7691-4371-a9ef-f1a4b46b711b'
