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
            return '57a6166a-6140-4523-9183-ad92f4f8d1dd'
        elif self.__id__ == 3:
            return '6b5f26ee-f2a7-4b31-934a-2305721994bf'
        elif self.__id__ == 4:
            return '5f3efca2-0b07-4ec9-83c1-14f7a91d63a6'
        elif self.__id__ == 5:
            return 'add0b121-aff1-47ee-b2eb-21b79a9c41b8'
        elif self.__id__ == 6:
            return '3f3f48c2-0b5c-444e-b3d5-5cfea7534752'
        elif self.__id__ == 7:
            return 'fa0ad860-dea5-48d0-ab2c-6cc80c6245a4'
        elif self.__id__ == 8:
            return '6cc403ca-4653-4ac2-a44d-e2605b2d64d4'
        elif self.__id__ == 9:
            return '2c831a9f-723a-4be5-9f18-dcc2104a159b'
        elif self.__id__ == 10:
            return 'a73772ba-13aa-4708-9cbd-3707bcc93339'
