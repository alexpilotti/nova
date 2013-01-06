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

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__

    def __str__(self):
        if self.__id__ == 2:
            return 'ab42abbf-e4d6-4b3f-a79b-a0699e194e91'
        elif self.__id__ == 3:
            return '3d5ac754-0c53-42da-8e5f-feecfcbb44ea'
        elif self.__id__ == 4:
            return '3cef9e87-1182-434b-aed2-fc541780822a'
        elif self.__id__ == 5:
            return '71a0407f-03b9-4841-8b9a-0c83dd2d4129'
        elif self.__id__ == 6:
            return '0bf3fd4d-3612-4069-a113-5f353c4b3f0c'
        elif self.__id__ == 7:
            return '690183db-27ab-478a-bce9-e96573849036'
        elif self.__id__ == 8:
            return 'dae8b035-b515-4747-b304-13ff21b88e4b'
        elif self.__id__ == 9:
            return '5d042dff-b326-48fb-aa30-12e1c455c770'
        elif self.__id__ == 10:
            return 'e5168c93-fe17-46c5-bc46-6732fd7add6a'
        elif self.__id__ == 11:
            return 'cde6ae00-1b61-43d0-82a1-a39ce1e389c9'
