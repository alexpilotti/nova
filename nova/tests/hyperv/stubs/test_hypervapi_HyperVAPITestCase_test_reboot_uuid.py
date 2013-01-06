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
            return '23d7c640-4c90-4f36-a7d4-6c85be625326'
        elif self.__id__ == 3:
            return '6ab152cb-cb80-456b-b1eb-12ab57efa868'
        elif self.__id__ == 4:
            return '2eb194cb-8526-4517-9d62-d0d56e44e27c'
        elif self.__id__ == 5:
            return 'bd3a3c33-5fa1-4b4d-817d-28f1c8a88c23'
        elif self.__id__ == 6:
            return 'b56fa1c1-6ad2-4942-8242-580693e308be'
        elif self.__id__ == 7:
            return '49db9331-8c4c-4611-833f-dc8569213a15'
        elif self.__id__ == 8:
            return '83f97003-0c86-4ccf-b79e-2adc816660da'
        elif self.__id__ == 9:
            return '82a708ea-882c-46ed-8032-f6c397781349'
        elif self.__id__ == 10:
            return 'f242ed44-7e55-4670-9c14-2f71fa62970f'
