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
            return '29e58ba9-c5c2-4c8a-9cea-e051bded0026'
        elif self.__id__ == 3:
            return 'aa86a95c-c754-4b6e-a587-2eb9c83a79c6'
        elif self.__id__ == 4:
            return '5f56bca5-cc02-45f8-bcb9-5dbfe3b76801'
        elif self.__id__ == 5:
            return 'fa47520c-5851-4623-884f-7474b57a2a03'
        elif self.__id__ == 6:
            return '70eb8b4c-6f0e-466a-a256-f6a3dab1931e'
        elif self.__id__ == 7:
            return '3f5dbbf8-15d5-4db1-987a-6fa83af77f7e'
        elif self.__id__ == 8:
            return '38abeafd-051a-4399-a656-e79250dad0cb'
        elif self.__id__ == 9:
            return '8012d1d5-fe84-4d4f-8c14-1f5efedccebb'
        elif self.__id__ == 10:
            return '80bdc839-32cd-480c-96eb-351a07177d2d'
