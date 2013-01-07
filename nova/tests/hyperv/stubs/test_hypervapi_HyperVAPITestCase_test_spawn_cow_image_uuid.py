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
        v = UUID(2)
    elif _uuid4_count_0 == 1:
        v = UUID(3)
    elif _uuid4_count_0 == 2:
        v = UUID(4)
    elif _uuid4_count_0 == 3:
        v = UUID(5)
    elif _uuid4_count_0 == 4:
        v = UUID(6)
    elif _uuid4_count_0 == 5:
        v = UUID(7)
    elif _uuid4_count_0 == 6:
        v = UUID(8)
    elif _uuid4_count_0 == 7:
        v = UUID(9)
    elif _uuid4_count_0 == 8:
        v = UUID(10)
    _uuid4_count_0 += 1
    return v


class UUID(object):

    def __init__(self, instance_id=1, *args, **kwargs):
        self.__instance_id__ = instance_id

    @property
    def __id__(self):
        return self.__instance_id__

    def __str__(self):
        if self.__id__ == 2:
            return '7ce87aae-7958-4beb-b2ac-c79303c4e01a'
        elif self.__id__ == 3:
            return '250bb34e-0557-4f99-be35-3850667eb8b3'
        elif self.__id__ == 4:
            return '8cbdb69e-fe5a-4a81-b3a0-e9fce7a4c7cc'
        elif self.__id__ == 5:
            return '0bbd7d53-f964-4b75-a784-b070afd69ffd'
        elif self.__id__ == 6:
            return '835821e1-03b3-4d76-8907-3425a67c29a5'
        elif self.__id__ == 7:
            return '59f123dd-60dd-4b9b-b363-66353b3ce70a'
        elif self.__id__ == 8:
            return 'eb6490df-0555-49ff-a0aa-2544bb326fa7'
        elif self.__id__ == 9:
            return 'd53f6bad-f68a-441d-b810-d445f8deaea2'
        elif self.__id__ == 10:
            return 'f9642fa0-7242-41ba-aaa1-b7cdda7fa17a'
