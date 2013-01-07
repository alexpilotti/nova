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
            return '6554824d-e7e3-4e2d-b241-4dc72e3d8603'
        elif self.__id__ == 3:
            return '7df4cbe8-2aef-429b-a238-47c607bac168'
        elif self.__id__ == 4:
            return '52124d62-250a-48c1-9f52-c791f21a1890'
        elif self.__id__ == 5:
            return 'cae552d0-0dce-4a76-8f6a-ce3c46441ba9'
        elif self.__id__ == 6:
            return '03b7b69b-0f95-4c1c-8bf4-138751541c52'
        elif self.__id__ == 7:
            return 'eebff403-c51c-40ac-beac-6c9064e1aa9c'
        elif self.__id__ == 8:
            return '806d64cd-94b3-44d2-b486-33355a78815b'
        elif self.__id__ == 9:
            return '6c570f20-dcf3-49d9-b469-dd33e0c175ec'
        elif self.__id__ == 10:
            return 'a6a88967-30c7-47fb-8271-96c21931b062'
