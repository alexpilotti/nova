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
            return 'f65363cb-0a0f-40ea-b826-24088908a5f7'
        elif self.__id__ == 3:
            return 'aaf1267b-fbc6-49fe-b84a-e72081546b49'
        elif self.__id__ == 4:
            return 'd6ce76f6-2b35-4564-9dda-952be64636f9'
        elif self.__id__ == 5:
            return 'a10333d1-1a52-4a29-942a-b7ec8c5ba302'
        elif self.__id__ == 6:
            return 'bb9b6efa-0087-4b65-9774-54521b99ad02'
        elif self.__id__ == 7:
            return '0ba8bf8f-5166-4e5e-9a33-b4aae6c3bd54'
        elif self.__id__ == 8:
            return '3247be57-b150-413d-aaaa-c8a048fff023'
        elif self.__id__ == 9:
            return 'fbaea9e8-7432-4ab1-9097-32b676327021'
        elif self.__id__ == 10:
            return '1c116448-cb95-4a32-a0b3-fc00f7f8f891'
        elif self.__id__ == 11:
            return 'e0e51f63-33b7-4385-bae5-843a2f9eebb1'
