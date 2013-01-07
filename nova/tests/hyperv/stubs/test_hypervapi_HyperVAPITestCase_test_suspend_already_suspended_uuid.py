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
            return '8c4c98a5-fca4-4c3e-8fb1-5e4aa82d6c70'
        elif self.__id__ == 3:
            return 'c5ffd686-0ace-49f2-8aa3-1b0e0b8e7848'
        elif self.__id__ == 4:
            return 'e64c66ad-0f27-44c8-9a1a-48fdf387b99d'
        elif self.__id__ == 5:
            return '531139a8-649e-4b09-b2d8-b290f4196132'
        elif self.__id__ == 6:
            return '35f221fa-4893-462e-bb76-6c7e6a2374ea'
        elif self.__id__ == 7:
            return 'b430f482-063a-43fd-84df-e72fcfdaadce'
        elif self.__id__ == 8:
            return 'c797b023-83c3-480e-9388-cd6ad00174dc'
        elif self.__id__ == 9:
            return '459ab3bd-232b-427c-b105-d396f716c0d0'
        elif self.__id__ == 10:
            return '800f8a6a-4065-48cb-a478-3190d8810ccb'
