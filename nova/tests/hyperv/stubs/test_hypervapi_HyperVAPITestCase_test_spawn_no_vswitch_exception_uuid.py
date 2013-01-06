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
            return '0eb22b88-f36e-4ce1-ab7e-6b0a40c3fc2d'
        elif self.__id__ == 3:
            return 'bad45503-0183-4188-a60b-d3e33c943bdc'
        elif self.__id__ == 4:
            return '944f8dba-47ec-4134-b431-c98205e8879d'
        elif self.__id__ == 5:
            return 'd878f46f-e615-41df-b2f2-d358b963b451'
        elif self.__id__ == 6:
            return '94603540-0ec3-476d-ac0d-8d75da25fd46'
        elif self.__id__ == 7:
            return 'b8d32e7c-78b0-4269-b305-864d359e5a62'
        elif self.__id__ == 8:
            return '9e0237db-b853-407b-ba6d-c380819e3cbc'
        elif self.__id__ == 9:
            return '994e005c-dcd4-44b1-8f12-66901745e781'
        elif self.__id__ == 10:
            return 'be35c835-1684-4ec3-8375-78be77fde10c'
        elif self.__id__ == 11:
            return 'ec07bc1e-a5fd-47df-a163-ef72ca50c7d7'
