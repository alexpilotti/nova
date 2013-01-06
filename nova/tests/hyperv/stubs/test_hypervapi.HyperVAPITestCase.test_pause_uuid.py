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
            return '85ab3a47-94ec-4486-bbbd-57dac43705cb'
        elif self.__id__ == 3:
            return '55894f03-b582-4f12-8925-81dbc3f3cdb6'
        elif self.__id__ == 4:
            return '9ccfb947-f531-4856-8413-51c25074bb75'
        elif self.__id__ == 5:
            return '0b56311b-78f8-4fe0-b158-05d20c0034d3'
        elif self.__id__ == 6:
            return 'afd3b17a-a2c3-4118-b238-2cf4dd721267'
        elif self.__id__ == 7:
            return '8ce43f55-601f-4b95-93fb-2135c0b00f7c'
        elif self.__id__ == 8:
            return '046d0d92-716f-4ea2-823d-aeb19a122d77'
        elif self.__id__ == 9:
            return '7e5cac13-b47b-4ee0-a73e-8d07c646b454'
        elif self.__id__ == 10:
            return 'd013e562-def0-4da9-97ef-f9c5a28930df'
