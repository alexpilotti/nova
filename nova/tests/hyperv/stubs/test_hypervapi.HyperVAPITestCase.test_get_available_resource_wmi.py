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


def WMI(computer='', impersonation_level='', authentication_level='',
 authority='', privileges='', moniker='', wmi=None, namespace='', suffix='',
 user='', password='', find_classes=False, debug=False):
    if moniker == '//./Root/Microsoft/Windows/Storage':
        ret_value = None
        global _WMI_count_0
        if not '_WMI_count_0' in globals():
            _WMI_count_0 = 0
        if _WMI_count_0 == 0:
            v = _wmi_namespace()
            v.__instance_id__ = 2
        elif _WMI_count_0 == 1:
            v = _wmi_namespace()
            v.__instance_id__ = 7
        _WMI_count_0 += 1
        return v
    elif moniker == '//./root/wmi':
        ret_value = None
        global _WMI_count_1
        if not '_WMI_count_1' in globals():
            _WMI_count_1 = 0
        if _WMI_count_1 == 0:
            v = _wmi_namespace()
            v.__instance_id__ = 3
        elif _WMI_count_1 == 1:
            v = _wmi_namespace()
            v.__instance_id__ = 8
        _WMI_count_1 += 1
        return v
    elif moniker == '//./root/cimv2':
        ret_value = None
        global _WMI_count_2
        if not '_WMI_count_2' in globals():
            _WMI_count_2 = 0
        if _WMI_count_2 == 0:
            v = _wmi_namespace()
            v.__instance_id__ = 4
        elif _WMI_count_2 == 1:
            v = _wmi_namespace()
            v.__instance_id__ = 9
        _WMI_count_2 += 1
        return v


class _wmi_namespace(object):

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__

    @property
    def Win32_OperatingSystem(self):
        if self.__id__ == 4:
            v = _wmi_class()
            v.__instance_id__ = 5
            return v
        elif self.__id__ == 9:
            v = _wmi_class()
            v.__instance_id__ = 13
            return v

    @Win32_OperatingSystem.setter
    def Win32_OperatingSystem(self, value):
        pass

    def query(self, wql, instance_of=None, fields='[]'):
        if self.__id__ == 3 and wql == 'SELECT * FROM\
 MSiSCSIInitiator_SessionClass                     WHERE\
 TargetName=\'iqn.2010-10.org.openstack:volume-8957e088-dbee-4216-8056-978353a\
3e737\'':
            v = []
            return v
        elif self.__id__ == 9 and wql == 'SELECT FreeSpace,Size FROM\
 win32_logicaldisk WHERE DeviceID=\'C:\'':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 10
            v.append(v1)
            return v
        elif self.__id__ == 9 and wql == 'SELECT TotalVisibleMemorySize FROM\
 win32_operatingsystem':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 11
            v.append(v1)
            return v
        elif self.__id__ == 9 and wql == 'SELECT FreePhysicalMemory FROM\
 win32_operatingsystem':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 12
            v.append(v1)
            return v
        elif self.__id__ == 9 and wql == 'SELECT * FROM Win32_Processor WHERE\
 ProcessorType = 3':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 15
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 16
            v.append(v1)
            return v


class _wmi_class(object):

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__

    def __call__(self, fields='[]', **where_clause):
        if self.__id__ == 5:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 6
            v.append(v1)
            return v
        elif self.__id__ == 13:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 14
            v.append(v1)
            return v


class _wmi_object(object):

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__

    @property
    def FreeSpace(self):
        if self.__id__ == 10:
            return u'33580752896'

    @FreeSpace.setter
    def FreeSpace(self, value):
        pass

    @property
    def NumberOfLogicalProcessors(self):
        if self.__id__ == 15:
            return 1

    @NumberOfLogicalProcessors.setter
    def NumberOfLogicalProcessors(self, value):
        pass

    @property
    def Name(self):
        if self.__id__ == 15:
            return u'Intel(R) Core(TM) i7-2720QM CPU @ 2.20GHz'

    @Name.setter
    def Name(self, value):
        pass

    @property
    def FreePhysicalMemory(self):
        if self.__id__ == 12:
            return u'2146836'

    @FreePhysicalMemory.setter
    def FreePhysicalMemory(self, value):
        pass

    @property
    def NumberOfCores(self):
        if self.__id__ == 15:
            ret_value = None
            if not hasattr(self, '_NumberOfCores_count_0'):
                self._NumberOfCores_count_0 = 0
            if self._NumberOfCores_count_0 == 0:
                v = 1
            elif self._NumberOfCores_count_0 == 1:
                v = 1
            self._NumberOfCores_count_0 += 1
            return v

    @NumberOfCores.setter
    def NumberOfCores(self, value):
        pass

    @property
    def Version(self):
        if self.__id__ == 6:
            return u'6.2.9200'
        elif self.__id__ == 14:
            return u'6.2.9200'

    @Version.setter
    def Version(self, value):
        pass

    @property
    def TotalVisibleMemorySize(self):
        if self.__id__ == 11:
            return u'3145204'

    @TotalVisibleMemorySize.setter
    def TotalVisibleMemorySize(self, value):
        pass

    @property
    def Architecture(self):
        if self.__id__ == 15:
            return 9

    @Architecture.setter
    def Architecture(self, value):
        pass

    @property
    def Manufacturer(self):
        if self.__id__ == 15:
            return u'GenuineIntel'

    @Manufacturer.setter
    def Manufacturer(self, value):
        pass

    @property
    def Size(self):
        if self.__id__ == 10:
            return u'64055406592'

    @Size.setter
    def Size(self, value):
        pass
