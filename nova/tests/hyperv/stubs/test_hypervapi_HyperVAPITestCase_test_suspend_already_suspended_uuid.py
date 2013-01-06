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
            return 'a646cece-4ae6-4074-8585-e430b37ebb98'
        elif self.__id__ == 3:
            return '65022352-a999-4378-afee-05922b914efe'
        elif self.__id__ == 4:
            return 'cce5b494-0ccf-4b36-b412-35b4e2e04a16'
        elif self.__id__ == 5:
            return 'e17423b7-0c8e-486c-8b45-ed20f944172a'
        elif self.__id__ == 6:
            return '6e30ccce-e818-4ab9-a786-ff14ba3b8612'
        elif self.__id__ == 7:
            return 'a361b672-9759-411a-bc12-a34e44ee3a8e'
        elif self.__id__ == 8:
            return '8b73b761-505d-4959-8549-d2454a1cd291'
        elif self.__id__ == 9:
            return 'd944840c-a49a-44b9-b9f4-f28dc73cd66b'
        elif self.__id__ == 10:
            return '09c31249-2436-4055-ba34-73f9a49ed5cf'
