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
            return '405cb363-3a3a-4369-8995-5c3cf53350f1'
        elif self.__id__ == 3:
            return '1a6ce3d6-279f-4348-8f9b-765d7ee55dd2'
        elif self.__id__ == 4:
            return '05b05278-e2d8-4eb8-b570-3bbcb4697c60'
        elif self.__id__ == 5:
            return '5b5509db-ea1c-4069-a624-03686a48fa05'
        elif self.__id__ == 6:
            return 'de12a0c4-51c7-495b-b995-c5842989127d'
        elif self.__id__ == 7:
            return '0cb79cc5-828e-4ab1-9cd6-673ab680ea66'
        elif self.__id__ == 8:
            return '33f87ad3-5ebb-49f5-815c-8d8344bcdfe4'
        elif self.__id__ == 9:
            return '35faeff9-20bb-4323-ba58-1e968184d3d9'
        elif self.__id__ == 10:
            return '97e3d11b-d431-42eb-b117-82495720e5b8'
