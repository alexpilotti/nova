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

    def __init__(self, *args, **kwargs):
        pass

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__

    @property
    def kernel32(self):
        if self.__id__ == 2:
            v = WinDLL()
            v.__instance_id__ = 3
            return v
        elif self.__id__ == 5:
            v = WinDLL()
            v.__instance_id__ = 6
            return v
        elif self.__id__ == 8:
            v = WinDLL()
            v.__instance_id__ = 9
            return v
        elif self.__id__ == 11:
            v = WinDLL()
            v.__instance_id__ = 12
            return v
        elif self.__id__ == 14:
            v = WinDLL()
            v.__instance_id__ = 15
            return v
        elif self.__id__ == 17:
            v = WinDLL()
            v.__instance_id__ = 18
            return v
        elif self.__id__ == 20:
            v = WinDLL()
            v.__instance_id__ = 21
            return v
        elif self.__id__ == 23:
            v = WinDLL()
            v.__instance_id__ = 24
            return v
        elif self.__id__ == 26:
            v = WinDLL()
            v.__instance_id__ = 27
            return v
        elif self.__id__ == 29:
            v = WinDLL()
            v.__instance_id__ = 30
            return v
        elif self.__id__ == 32:
            v = WinDLL()
            v.__instance_id__ = 33
            return v

    @kernel32.setter
    def kernel32(self, value):
        pass


class WinDLL(object):

    def __init__(self, *args, **kwargs):
        pass

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__

    @property
    def IsProcessorFeaturePresent(self):
        if self.__id__ == 3:
            v = _FuncPtr()
            v.__instance_id__ = 4
            return v
        elif self.__id__ == 6:
            v = _FuncPtr()
            v.__instance_id__ = 7
            return v
        elif self.__id__ == 9:
            v = _FuncPtr()
            v.__instance_id__ = 10
            return v
        elif self.__id__ == 12:
            v = _FuncPtr()
            v.__instance_id__ = 13
            return v
        elif self.__id__ == 15:
            v = _FuncPtr()
            v.__instance_id__ = 16
            return v
        elif self.__id__ == 18:
            v = _FuncPtr()
            v.__instance_id__ = 19
            return v
        elif self.__id__ == 21:
            v = _FuncPtr()
            v.__instance_id__ = 22
            return v
        elif self.__id__ == 24:
            v = _FuncPtr()
            v.__instance_id__ = 25
            return v
        elif self.__id__ == 27:
            v = _FuncPtr()
            v.__instance_id__ = 28
            return v
        elif self.__id__ == 30:
            v = _FuncPtr()
            v.__instance_id__ = 31
            return v
        elif self.__id__ == 33:
            v = _FuncPtr()
            v.__instance_id__ = 34
            return v

    @IsProcessorFeaturePresent.setter
    def IsProcessorFeaturePresent(self, value):
        pass


class _FuncPtr(object):

    def __init__(self, *args, **kwargs):
        pass

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
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
