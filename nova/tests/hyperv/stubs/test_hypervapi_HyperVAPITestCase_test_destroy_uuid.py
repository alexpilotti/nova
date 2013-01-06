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
            return '8e9359cb-21f7-40c6-a1e6-c852b676ae62'
        elif self.__id__ == 3:
            return 'c89e66cd-6bb3-4e05-ba5a-e26400dc129d'
        elif self.__id__ == 4:
            return '850e2805-9d91-4fcf-93e7-55371844debe'
        elif self.__id__ == 5:
            return '54de1f98-1316-4225-acfe-3955c272f819'
        elif self.__id__ == 6:
            return '415f99c5-fc9f-488a-b1a9-8a3a4dc8d469'
        elif self.__id__ == 7:
            return 'c4255674-6fb0-40b7-8fb2-3f8172f32e33'
        elif self.__id__ == 8:
            return '1eb9d385-b2a0-4530-8149-670978de68be'
        elif self.__id__ == 9:
            return 'db2f0133-8ab2-4f7c-9ce5-85d0cff377c7'
        elif self.__id__ == 10:
            return '2593d10b-352f-479e-ade1-082ff26796a1'
