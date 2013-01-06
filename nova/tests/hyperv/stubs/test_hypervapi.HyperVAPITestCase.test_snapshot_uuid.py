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
            return 'd66dbe32-9e1c-4994-8884-70c064f3b8de'
        elif self.__id__ == 3:
            return '564ece5b-f970-44a7-92f0-dadc44299a70'
        elif self.__id__ == 4:
            return 'bc73cca6-7601-460a-b7c3-f8b4f27ae131'
        elif self.__id__ == 5:
            return '26166620-076d-41b1-b5f0-9bbde4ff29e3'
        elif self.__id__ == 6:
            return 'd7e792a2-ca61-4ebb-8502-dc1fa5fd3bae'
        elif self.__id__ == 7:
            return '1147a0fb-03f9-48de-87f7-2a83aa6051a2'
        elif self.__id__ == 8:
            return 'b79076bb-a6e3-4520-8e4a-3322b965305d'
        elif self.__id__ == 9:
            return 'c01ba1e9-7ed4-4761-bf30-c54945cd1ab9'
        elif self.__id__ == 10:
            return '23c3d986-b1c7-4a42-86b7-bfdae4431d15'
        elif self.__id__ == 11:
            return '381397fe-96c3-4020-847d-f7bc92c938c9'
