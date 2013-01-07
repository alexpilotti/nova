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
            v = _wmi_namespace(2)
        elif _WMI_count_0 == 1:
            v = _wmi_namespace(7)
        _WMI_count_0 += 1
        return v
    elif moniker == '//./root/wmi':
        ret_value = None
        global _WMI_count_1
        if not '_WMI_count_1' in globals():
            _WMI_count_1 = 0
        if _WMI_count_1 == 0:
            v = _wmi_namespace(3)
        elif _WMI_count_1 == 1:
            v = _wmi_namespace(8)
        _WMI_count_1 += 1
        return v
    elif moniker == '//./root/cimv2':
        v = _wmi_namespace(4)
        return v
    elif moniker == '//./root/virtualization/v2':
        v = _wmi_namespace(9)
        return v


class _wmi_namespace(object):

    def __init__(self, instance_id=1, *args, **kwargs):
        self.__instance_id__ = instance_id

    @property
    def __id__(self):
        return self.__instance_id__

    @property
    def Msvm_VirtualSystemMigrationService(self):
        if self.__id__ == 9:
            v = _wmi_class(10)
            return v

    @Msvm_VirtualSystemMigrationService.setter
    def Msvm_VirtualSystemMigrationService(self, value):
        pass

    @property
    def Win32_OperatingSystem(self):
        if self.__id__ == 4:
            v = _wmi_class(5)
            return v

    @Win32_OperatingSystem.setter
    def Win32_OperatingSystem(self, value):
        pass

    def query(self, wql, instance_of=None, fields='[]'):
        if self.__id__ == 3 and wql == 'SELECT * FROM\
 MSiSCSIInitiator_SessionClass                     WHERE\
 TargetName=\'iqn.2010-10.org.openstack:volume-ccb39627-34fa-4f47-968b-6580d9d\
7ee2b\'':
            v = []
            return v


class _wmi_class(object):

    def __init__(self, instance_id=1, *args, **kwargs):
        self.__instance_id__ = instance_id

    @property
    def __id__(self):
        return self.__instance_id__

    def __call__(self, fields='[]', **where_clause):
        if self.__id__ == 5:
            v = []
            v1 = _wmi_object(6)
            v.append(v1)
            return v
        elif self.__id__ == 10:
            v = []
            v1 = _wmi_object(11)
            v.append(v1)
            return v


class _wmi_object(object):

    def __init__(self, instance_id=1, *args, **kwargs):
        self.__instance_id__ = instance_id

    @property
    def __id__(self):
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

    def associators(self, wmi_association_class='', wmi_result_class=''):
        if self.__id__ == 11 and wmi_association_class ==\
 'Msvm_ElementSettingData' and wmi_result_class ==\
 'Msvm_VirtualSystemMigrationServiceSettingData':
            v = []
            v1 = _wmi_object(12)
            v.append(v1)
            return v
