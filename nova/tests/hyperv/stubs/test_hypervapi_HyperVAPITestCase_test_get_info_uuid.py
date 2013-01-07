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
            return 'e1ea28f0-2279-46c2-bee1-4e09d613d272'
        elif self.__id__ == 3:
            return 'd473b61d-00ff-42d3-9416-4688326bf742'
        elif self.__id__ == 4:
            return '71bdf236-dbcd-4d06-90a9-815bd3233056'
        elif self.__id__ == 5:
            return '0f11dba6-29e6-4b4a-9933-a7c1c7924bf3'
        elif self.__id__ == 6:
            return '34a561a2-4866-4526-91c0-0a8e86e99969'
        elif self.__id__ == 7:
            return 'eaeb529c-256d-430d-8584-30589296e025'
        elif self.__id__ == 8:
            return '5c4069e6-b856-4db9-8891-d5cc5a255e87'
        elif self.__id__ == 9:
            return '70389fd2-0f9e-466f-94a2-0ae5909fe7ab'
        elif self.__id__ == 10:
            return '7600ea53-bfa0-42ae-a413-841c89f75b81'
