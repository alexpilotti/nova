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
        v = _wmi_namespace()
        v.__instance_id__ = 4
        return v
    elif moniker == '//./root/virtualization/v2':
        v = _wmi_namespace()
        v.__instance_id__ = 9
        return v
    elif moniker == '//./root/virtualization':
        v = _wmi_namespace()
        v.__instance_id__ = 13
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_StorageJob.InstanceID="0BEFDB81-9829\
-4393-B210-66CB75254BA9"':
        ret_value = None
        global _WMI_count_5
        if not '_WMI_count_5' in globals():
            _WMI_count_5 = 0
        if _WMI_count_5 == 0:
            v = _wmi_object()
            v.__instance_id__ = 16
        elif _WMI_count_5 == 1:
            v = _wmi_object()
            v.__instance_id__ = 17
        elif _WMI_count_5 == 2:
            v = _wmi_object()
            v.__instance_id__ = 18
        elif _WMI_count_5 == 3:
            v = _wmi_object()
            v.__instance_id__ = 19
        elif _WMI_count_5 == 4:
            v = _wmi_object()
            v.__instance_id__ = 20
        elif _WMI_count_5 == 5:
            v = _wmi_object()
            v.__instance_id__ = 21
        elif _WMI_count_5 == 6:
            v = _wmi_object()
            v.__instance_id__ = 22
        elif _WMI_count_5 == 7:
            v = _wmi_object()
            v.__instance_id__ = 23
        elif _WMI_count_5 == 8:
            v = _wmi_object()
            v.__instance_id__ = 24
        elif _WMI_count_5 == 9:
            v = _wmi_object()
            v.__instance_id__ = 25
        _WMI_count_5 += 1
        return v


class _wmi_namespace(object):

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__

    @property
    def Msvm_VirtualSystemMigrationService(self):
        if self.__id__ == 9:
            v = _wmi_class()
            v.__instance_id__ = 10
            return v

    @Msvm_VirtualSystemMigrationService.setter
    def Msvm_VirtualSystemMigrationService(self, value):
        pass

    @property
    def Win32_OperatingSystem(self):
        if self.__id__ == 4:
            v = _wmi_class()
            v.__instance_id__ = 5
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
        elif self.__id__ == 13 and wql == 'Select * from\
 Msvm_ImageManagementService':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 14
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
        elif self.__id__ == 10:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 11
            v.append(v1)
            return v


class _wmi_object(object):

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__

    @property
    def EnableVirtualSystemMigration(self):
        if self.__id__ == 12:
            return True

    @EnableVirtualSystemMigration.setter
    def EnableVirtualSystemMigration(self, value):
        pass

    @property
    def Version(self):
        if self.__id__ == 6:
            return u'6.2.9200'

    @Version.setter
    def Version(self, value):
        pass

    @property
    def CreateDynamicVirtualHardDisk(self):
        if self.__id__ == 14:
            v = _wmi_method()
            v.__instance_id__ = 15
            return v

    @CreateDynamicVirtualHardDisk.setter
    def CreateDynamicVirtualHardDisk(self, value):
        pass

    @property
    def MigrationServiceListenerIPAddressList(self):
        if self.__id__ == 11:
            v = ()
            v1 = u'192.168.209.172'
            v += (v1,)
            v1 = u'fe80::100:7f:fffe'
            v += (v1,)
            v1 = u'fe80::9885:23c5:f327:c587'
            v += (v1,)
            v1 = u'fe80::5efe:192.168.209.172'
            v += (v1,)
            return v

    @MigrationServiceListenerIPAddressList.setter
    def MigrationServiceListenerIPAddressList(self, value):
        pass

    @property
    def JobState(self):
        if self.__id__ == 16:
            return 4
        elif self.__id__ == 17:
            return 4
        elif self.__id__ == 18:
            return 4
        elif self.__id__ == 19:
            return 4
        elif self.__id__ == 20:
            return 4
        elif self.__id__ == 21:
            return 4
        elif self.__id__ == 22:
            return 4
        elif self.__id__ == 23:
            return 4
        elif self.__id__ == 24:
            return 4
        elif self.__id__ == 25:
            ret_value = None
            if not hasattr(self, '_JobState_count_9'):
                self._JobState_count_9 = 0
            if self._JobState_count_9 == 0:
                v = 7
            elif self._JobState_count_9 == 1:
                v = 7
            self._JobState_count_9 += 1
            return v

    @JobState.setter
    def JobState(self, value):
        pass

    def associators(self, wmi_association_class='', wmi_result_class=''):
        if self.__id__ == 11 and wmi_association_class ==\
 'Msvm_ElementSettingData' and wmi_result_class ==\
 'Msvm_VirtualSystemMigrationServiceSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 12
            v.append(v1)
            return v


class _wmi_method(object):

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__

    def __call__(self, *args, **kwargs):
        if len(args) == 0 and self.__id__ == 15 and\
 kwargs.get('MaxInternalSize') == 3145728 and kwargs.get('Path') ==\
 'C:\\Hyper-V\\test\\instances\\_base\\1.vhd':
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_StorageJob.InstanceID="0BEFDB81-\
9829-4393-B210-66CB75254BA9"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v
