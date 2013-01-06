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
            return '2b7b33e0-3c3b-41c0-a3a9-6ff8ba23314d'
        elif self.__id__ == 3:
            return '7596ad1c-76eb-486d-a42b-cf8a591db099'
        elif self.__id__ == 4:
            return '305f4226-342b-4642-a282-dd9d8366b6ef'
        elif self.__id__ == 5:
            return '41666e16-4910-46fb-93de-c5ee9f5ce1cb'
        elif self.__id__ == 6:
            return 'db305a6b-6871-40e6-b452-eb25c4e890f5'
        elif self.__id__ == 7:
            return '3b8d52b0-5203-4ca1-b58d-12947a51380d'
        elif self.__id__ == 8:
            return '3bc12b47-ec24-4744-a28b-2ae38bf176ee'
        elif self.__id__ == 9:
            return '4d94e1d9-fd53-45a3-a149-ff1fc91372ac'
        elif self.__id__ == 10:
            return '149a4174-6704-4566-b714-318aec841c6c'
