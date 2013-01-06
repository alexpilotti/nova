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
            return '1b56fa6e-fdae-45e3-b1d0-6f1551472a37'
        elif self.__id__ == 3:
            return '9c58dfb2-4e12-41de-9365-7ced20efcea4'
        elif self.__id__ == 4:
            return 'c0046ebb-792a-4df1-b043-dba8d211b489'
        elif self.__id__ == 5:
            return 'c842b500-16c0-464d-9bc0-fa321b3e3e3e'
        elif self.__id__ == 6:
            return 'e8257e09-7549-468b-9afa-5d00b7f17ec8'
        elif self.__id__ == 7:
            return '718c66de-5441-4839-b854-e29d708c335d'
        elif self.__id__ == 8:
            return 'c6ab9101-cc11-4846-b936-4d5c0322152b'
        elif self.__id__ == 9:
            return '609f296d-8d61-4c54-bee0-7b3481fd71b3'
        elif self.__id__ == 10:
            return '22128792-ad1b-4d6b-9093-bd5d01a81506'
