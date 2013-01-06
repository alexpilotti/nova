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

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__

    def __str__(self):
        if self.__id__ == 2:
            return 'af19f0f2-a8f2-4ca5-915d-80b631ce62c3'
        elif self.__id__ == 3:
            return 'bd18fae9-0fe0-4fcb-8a53-9073e1e6fbc4'
        elif self.__id__ == 4:
            return 'e6f2952b-6615-4e3d-992c-d66723239b10'
        elif self.__id__ == 5:
            return '95ef2cd9-827f-4eca-acb4-37c58e00b8d6'
        elif self.__id__ == 6:
            return '7d3dcd36-5cdf-4d93-ac42-adad6c642522'
        elif self.__id__ == 7:
            return '9b90437d-a3b9-45af-9382-d94fa2a5aff0'
        elif self.__id__ == 8:
            return 'd948bd5a-6c97-4cb6-a23b-b09cbeed8f9a'
        elif self.__id__ == 9:
            return '303b9075-b298-405c-9209-f9ccaf6b6f73'
        elif self.__id__ == 10:
            return '4227d023-4ff2-4743-9c98-72612c6e7155'
        elif self.__id__ == 11:
            return 'cc10a30b-8530-475e-a804-d93710e2b834'
