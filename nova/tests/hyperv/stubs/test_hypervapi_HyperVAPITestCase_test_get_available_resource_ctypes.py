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


class LibraryLoader(object):

    def __init__(self, instance_id=1, *args, **kwargs):
        self.__instance_id__ = instance_id

    @property
    def __id__(self):
        return self.__instance_id__

    @property
    def kernel32(self):
        if self.__id__ == 2:
            v = WinDLL(3)
            return v
        elif self.__id__ == 5:
            v = WinDLL(6)
            return v
        elif self.__id__ == 8:
            v = WinDLL(9)
            return v
        elif self.__id__ == 11:
            v = WinDLL(12)
            return v
        elif self.__id__ == 14:
            v = WinDLL(15)
            return v
        elif self.__id__ == 17:
            v = WinDLL(18)
            return v
        elif self.__id__ == 20:
            v = WinDLL(21)
            return v
        elif self.__id__ == 23:
            v = WinDLL(24)
            return v
        elif self.__id__ == 26:
            v = WinDLL(27)
            return v
        elif self.__id__ == 29:
            v = WinDLL(30)
            return v
        elif self.__id__ == 32:
            v = WinDLL(33)
            return v

    @kernel32.setter
    def kernel32(self, value):
        pass


class WinDLL(object):

    def __init__(self, instance_id=1, *args, **kwargs):
        self.__instance_id__ = instance_id

    @property
    def __id__(self):
        return self.__instance_id__

    @property
    def IsProcessorFeaturePresent(self):
        if self.__id__ == 3:
            v = _FuncPtr(4)
            return v
        elif self.__id__ == 6:
            v = _FuncPtr(7)
            return v
        elif self.__id__ == 9:
            v = _FuncPtr(10)
            return v
        elif self.__id__ == 12:
            v = _FuncPtr(13)
            return v
        elif self.__id__ == 15:
            v = _FuncPtr(16)
            return v
        elif self.__id__ == 18:
            v = _FuncPtr(19)
            return v
        elif self.__id__ == 21:
            v = _FuncPtr(22)
            return v
        elif self.__id__ == 24:
            v = _FuncPtr(25)
            return v
        elif self.__id__ == 27:
            v = _FuncPtr(28)
            return v
        elif self.__id__ == 30:
            v = _FuncPtr(31)
            return v
        elif self.__id__ == 33:
            v = _FuncPtr(34)
            return v

    @IsProcessorFeaturePresent.setter
    def IsProcessorFeaturePresent(self, value):
        pass


class _FuncPtr(object):

    def __init__(self, instance_id=1, *args, **kwargs):
        self.__instance_id__ = instance_id

    @property
    def __id__(self):
        return self.__instance_id__

    def __call__(*p):
        if len(p) == 1 and p[0] == 3:
            return 1
        elif len(p) == 1 and p[0] == 6:
            return 1
        elif len(p) == 1 and p[0] == 7:
            return 0
        elif len(p) == 1 and p[0] == 8:
            return 1
        elif len(p) == 1 and p[0] == 9:
            return 1
        elif len(p) == 1 and p[0] == 10:
            return 1
        elif len(p) == 1 and p[0] == 12:
            return 1
        elif len(p) == 1 and p[0] == 13:
            return 1
        elif len(p) == 1 and p[0] == 17:
            return 1
        elif len(p) == 1 and p[0] == 20:
            return 0
        elif len(p) == 1 and p[0] == 21:
            return 0
