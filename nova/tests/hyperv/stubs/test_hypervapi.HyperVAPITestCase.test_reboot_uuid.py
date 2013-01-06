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
            return '86c0c8f6-4bf6-4119-9370-40cd6a22c7c3'
        elif self.__id__ == 3:
            return '44f0b5ae-be36-4bbb-b5b1-ed22a71874a4'
        elif self.__id__ == 4:
            return 'd9eb5322-8324-4920-8b22-ab63412c4644'
        elif self.__id__ == 5:
            return '5175fe8a-0ba3-4ead-9531-b5f919ac2782'
        elif self.__id__ == 6:
            return '2801e697-5d13-4860-9de4-7f75cb15d5e6'
        elif self.__id__ == 7:
            return 'c6bbd940-7b90-4b0e-a157-b7f67890b2ea'
        elif self.__id__ == 8:
            return '00c65f44-e575-4e7e-afe4-c9cd19872f11'
        elif self.__id__ == 9:
            return '26c98482-0503-499e-aa54-2aa70b27895a'
        elif self.__id__ == 10:
            return '20777aa5-e181-4b51-ade4-508910bc0589'
