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
            return 'fbae78d4-0c5a-4c43-9b3e-c3aacd72b401'
        elif self.__id__ == 3:
            return 'f5cc2bcc-a195-4e61-847e-8974fdcaa722'
        elif self.__id__ == 4:
            return '39cc380f-74ac-49c9-8714-352388be54f4'
        elif self.__id__ == 5:
            return '1331d281-fe2b-4379-a094-27599c38662a'
        elif self.__id__ == 6:
            return '1e38f86e-4025-41c1-ab81-5b3d965dbea7'
        elif self.__id__ == 7:
            return '61acc9eb-7a8b-43c1-8d30-9bbfafe249c5'
        elif self.__id__ == 8:
            return '8e5fac59-5c62-4a5a-95d9-bd6c1ab8c83d'
        elif self.__id__ == 9:
            return 'c509604b-85ce-4b0b-959b-5279815c086c'
