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
            return 'adeb3f8f-5ca5-4ddf-89d2-7d22d8b0ab7d'
        elif self.__id__ == 3:
            return 'b9dc2225-249c-4f35-938c-ccdde6480099'
        elif self.__id__ == 4:
            return 'd6f2f796-cd1b-446f-ba99-2572705a5260'
        elif self.__id__ == 5:
            return 'ce14bdf2-3267-4640-9b49-1c52496f49bd'
        elif self.__id__ == 6:
            return '72097355-50eb-477b-9223-9338802240f7'
        elif self.__id__ == 7:
            return 'e70f1dac-3bc7-403e-95f4-24c9c8b43570'
        elif self.__id__ == 8:
            return 'ffb1c156-7262-4a52-afd4-0dd474eef4a1'
        elif self.__id__ == 9:
            return '42a6f838-438d-41ab-acb0-3e426ad6a049'
        elif self.__id__ == 10:
            return 'd9f81bf8-a6d3-46de-8061-eac59e9813c8'
