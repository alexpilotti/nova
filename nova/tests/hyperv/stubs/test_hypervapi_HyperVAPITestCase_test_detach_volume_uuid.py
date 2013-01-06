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
            return '17c25ba4-1c3a-4769-a44a-f0f6c89e02db'
        elif self.__id__ == 3:
            return '4cb4740c-aa7a-450c-84aa-86830c9be793'
        elif self.__id__ == 4:
            return '2f6dae28-e08d-4070-9898-2d4b3918982a'
        elif self.__id__ == 5:
            return '40722a0c-46f2-4c7c-a921-477faf7b6d1d'
        elif self.__id__ == 6:
            return '8be3cad2-beab-481a-89e7-a54ea28bdcdf'
        elif self.__id__ == 7:
            return 'e0f16d06-d10e-4e78-abeb-7c43d7ec4ff1'
        elif self.__id__ == 8:
            return '2217e215-a762-41cb-90ac-3f11519f411b'
        elif self.__id__ == 9:
            return '448d1651-04a5-451b-8a2c-3611db77d466'
        elif self.__id__ == 10:
            return 'beca3ac8-daa7-4e95-b011-fccca72b615a'
        elif self.__id__ == 11:
            return 'cca8f7cf-ed9f-41f7-9577-7039711322e4'
