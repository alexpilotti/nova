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
    elif _uuid4_count_0 == 9:
        v = UUID(11)
    elif _uuid4_count_0 == 10:
        v = UUID(12)
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
            return '4978e512-aa2d-492f-ac9f-09ed770c00d8'
        elif self.__id__ == 3:
            return '67115e69-108d-47ec-b80c-98d3662585af'
        elif self.__id__ == 4:
            return '78204352-a67d-498d-ae9d-4506646877f4'
        elif self.__id__ == 5:
            return '63dc76e2-d664-4d96-9163-702a5b068c26'
        elif self.__id__ == 6:
            return '1a0635fb-502a-4f56-ad31-814c5749c0b9'
        elif self.__id__ == 7:
            return 'e37d849f-e021-4ce3-b4c8-188bd95e2bf7'
        elif self.__id__ == 8:
            return '879e3f0a-ec4b-4f9c-841c-6e073f058e57'
        elif self.__id__ == 9:
            return '8bd50d5b-9c32-4fc1-89e6-32b96cf2bca2'
        elif self.__id__ == 10:
            return 'bd8c8c95-a891-4f76-9ba3-fb5b91c04329'
        elif self.__id__ == 11:
            return '1bcba902-b889-4be0-9278-996e8b4452d2'
        elif self.__id__ == 12:
            return '3b04a56a-b96a-406a-9052-80d6b146e43e'
