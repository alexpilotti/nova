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
            return '8271e765-499e-4317-88a1-a7ed2329ec34'
        elif self.__id__ == 3:
            return 'd78aa104-eb68-447a-896f-4cae77f0e614'
        elif self.__id__ == 4:
            return '4fa33f66-0698-429a-a6e3-5cc5388deae9'
        elif self.__id__ == 5:
            return '2bfe442f-9494-4108-a90a-83e32243aaf3'
        elif self.__id__ == 6:
            return 'd4466125-4c58-4209-92ff-39099dea0c70'
        elif self.__id__ == 7:
            return 'e39f78c7-070b-4556-a484-01c4f24b8722'
        elif self.__id__ == 8:
            return '2dc878db-ce7d-449c-9b3c-e8022999a52d'
        elif self.__id__ == 9:
            return 'a657081e-2bc7-4411-b0ec-5bf51ce237d2'
        elif self.__id__ == 10:
            return 'c26ea2c4-fc17-410f-912f-68b70ace332b'
        elif self.__id__ == 11:
            return '3f05ec5a-1f0f-42bb-9248-fb9ad9ab131c'
