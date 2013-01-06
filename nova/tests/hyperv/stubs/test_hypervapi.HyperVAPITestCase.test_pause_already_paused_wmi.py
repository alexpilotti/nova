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
            v.__instance_id__ = 377
        _WMI_count_2 += 1
        return v
    elif moniker == '//./root/virtualization':
        ret_value = None
        global _WMI_count_3
        if not '_WMI_count_3' in globals():
            _WMI_count_3 = 0
        if _WMI_count_3 == 0:
            v = _wmi_namespace()
            v.__instance_id__ = 9
        elif _WMI_count_3 == 1:
            v = _wmi_namespace()
            v.__instance_id__ = 11
        _WMI_count_3 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_StorageJob.InstanceID="BF07D796-9509\
-44B9-A313-A2475E14FB7B"':
        ret_value = None
        global _WMI_count_4
        if not '_WMI_count_4' in globals():
            _WMI_count_4 = 0
        if _WMI_count_4 == 0:
            v = _wmi_object()
            v.__instance_id__ = 14
        elif _WMI_count_4 == 1:
            v = _wmi_object()
            v.__instance_id__ = 15
        elif _WMI_count_4 == 2:
            v = _wmi_object()
            v.__instance_id__ = 16
        elif _WMI_count_4 == 3:
            v = _wmi_object()
            v.__instance_id__ = 17
        elif _WMI_count_4 == 4:
            v = _wmi_object()
            v.__instance_id__ = 18
        elif _WMI_count_4 == 5:
            v = _wmi_object()
            v.__instance_id__ = 19
        elif _WMI_count_4 == 6:
            v = _wmi_object()
            v.__instance_id__ = 20
        elif _WMI_count_4 == 7:
            v = _wmi_object()
            v.__instance_id__ = 21
        elif _WMI_count_4 == 8:
            v = _wmi_object()
            v.__instance_id__ = 22
        _WMI_count_4 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_StorageJob.InstanceID="1DDDE39C-EF4D\
-4685-969C-816C3041DBD8"':
        ret_value = None
        global _WMI_count_5
        if not '_WMI_count_5' in globals():
            _WMI_count_5 = 0
        if _WMI_count_5 == 0:
            v = _wmi_object()
            v.__instance_id__ = 25
        elif _WMI_count_5 == 1:
            v = _wmi_object()
            v.__instance_id__ = 26
        elif _WMI_count_5 == 2:
            v = _wmi_object()
            v.__instance_id__ = 27
        elif _WMI_count_5 == 3:
            v = _wmi_object()
            v.__instance_id__ = 28
        elif _WMI_count_5 == 4:
            v = _wmi_object()
            v.__instance_id__ = 29
        elif _WMI_count_5 == 5:
            v = _wmi_object()
            v.__instance_id__ = 30
        elif _WMI_count_5 == 6:
            v = _wmi_object()
            v.__instance_id__ = 31
        elif _WMI_count_5 == 7:
            v = _wmi_object()
            v.__instance_id__ = 32
        elif _WMI_count_5 == 8:
            v = _wmi_object()
            v.__instance_id__ = 33
        _WMI_count_5 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_ConcreteJob.InstanceID="C9854C10-5CA\
F-4FC4-A092-16E0E8E4AED2"':
        ret_value = None
        global _WMI_count_6
        if not '_WMI_count_6' in globals():
            _WMI_count_6 = 0
        if _WMI_count_6 == 0:
            v = _wmi_object()
            v.__instance_id__ = 354
        elif _WMI_count_6 == 1:
            v = _wmi_object()
            v.__instance_id__ = 355
        elif _WMI_count_6 == 2:
            v = _wmi_object()
            v.__instance_id__ = 356
        elif _WMI_count_6 == 3:
            v = _wmi_object()
            v.__instance_id__ = 357
        elif _WMI_count_6 == 4:
            v = _wmi_object()
            v.__instance_id__ = 358
        elif _WMI_count_6 == 5:
            v = _wmi_object()
            v.__instance_id__ = 359
        _WMI_count_6 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_ConcreteJob.InstanceID="723BEA5D-9C0\
4-456C-89E0-99319978D542"':
        v = _wmi_object()
        v.__instance_id__ = 363
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_ConcreteJob.InstanceID="20EA8ADB-585\
5-40A9-AE19-5AC8CDB36EEA"':
        ret_value = None
        global _WMI_count_8
        if not '_WMI_count_8' in globals():
            _WMI_count_8 = 0
        if _WMI_count_8 == 0:
            v = _wmi_object()
            v.__instance_id__ = 385
        elif _WMI_count_8 == 1:
            v = _wmi_object()
            v.__instance_id__ = 386
        _WMI_count_8 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_ConcreteJob.InstanceID="68D376C0-66A\
7-4C85-86BC-A51A1EA7FDBB"':
        ret_value = None
        global _WMI_count_9
        if not '_WMI_count_9' in globals():
            _WMI_count_9 = 0
        if _WMI_count_9 == 0:
            v = _wmi_object()
            v.__instance_id__ = 407
        elif _WMI_count_9 == 1:
            v = _wmi_object()
            v.__instance_id__ = 408
        _WMI_count_9 += 1
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

    @Win32_OperatingSystem.setter
    def Win32_OperatingSystem(self, value):
        pass

    @property
    def Msvm_ResourceAllocationSettingData(self):
        if self.__id__ == 9:
            ret_value = None
            if not hasattr(self,
 '_Msvm_ResourceAllocationSettingData_count_0'):
                self._Msvm_ResourceAllocationSettingData_count_0 = 0
            if self._Msvm_ResourceAllocationSettingData_count_0 == 0:
                v = _wmi_class()
                v.__instance_id__ = 64
            elif self._Msvm_ResourceAllocationSettingData_count_0 == 1:
                v = _wmi_class()
                v.__instance_id__ = 158
            elif self._Msvm_ResourceAllocationSettingData_count_0 == 2:
                v = _wmi_class()
                v.__instance_id__ = 253
            self._Msvm_ResourceAllocationSettingData_count_0 += 1
            return v

    @Msvm_ResourceAllocationSettingData.setter
    def Msvm_ResourceAllocationSettingData(self, value):
        pass

    @property
    def Msvm_VirtualSystemManagementService(self):
        if self.__id__ == 9:
            ret_value = None
            if not hasattr(self,
 '_Msvm_VirtualSystemManagementService_count_0'):
                self._Msvm_VirtualSystemManagementService_count_0 = 0
            if self._Msvm_VirtualSystemManagementService_count_0 == 0:
                v = _wmi_class()
                v.__instance_id__ = 34
            elif self._Msvm_VirtualSystemManagementService_count_0 == 1:
                v = _wmi_class()
                v.__instance_id__ = 153
            elif self._Msvm_VirtualSystemManagementService_count_0 == 2:
                v = _wmi_class()
                v.__instance_id__ = 246
            elif self._Msvm_VirtualSystemManagementService_count_0 == 3:
                v = _wmi_class()
                v.__instance_id__ = 341
            elif self._Msvm_VirtualSystemManagementService_count_0 == 4:
                v = _wmi_class()
                v.__instance_id__ = 347
            self._Msvm_VirtualSystemManagementService_count_0 += 1
            return v
        elif self.__id__ == 11:
            ret_value = None
            if not hasattr(self,
 '_Msvm_VirtualSystemManagementService_count_1'):
                self._Msvm_VirtualSystemManagementService_count_1 = 0
            if self._Msvm_VirtualSystemManagementService_count_1 == 0:
                v = _wmi_class()
                v.__instance_id__ = 369
            elif self._Msvm_VirtualSystemManagementService_count_1 == 1:
                v = _wmi_class()
                v.__instance_id__ = 380
            self._Msvm_VirtualSystemManagementService_count_1 += 1
            return v

    @Msvm_VirtualSystemManagementService.setter
    def Msvm_VirtualSystemManagementService(self, value):
        pass

    @property
    def Msvm_VirtualSystemGlobalSettingData(self):
        if self.__id__ == 9:
            v = _wmi_class()
            v.__instance_id__ = 36
            return v

    @Msvm_VirtualSystemGlobalSettingData.setter
    def Msvm_VirtualSystemGlobalSettingData(self, value):
        pass

    @property
    def Msvm_ComputerSystem(self):
        if self.__id__ == 9:
            ret_value = None
            if not hasattr(self, '_Msvm_ComputerSystem_count_0'):
                self._Msvm_ComputerSystem_count_0 = 0
            if self._Msvm_ComputerSystem_count_0 == 0:
                v = _wmi_class()
                v.__instance_id__ = 10
            elif self._Msvm_ComputerSystem_count_0 == 1:
                v = _wmi_class()
                v.__instance_id__ = 39
            elif self._Msvm_ComputerSystem_count_0 == 2:
                v = _wmi_class()
                v.__instance_id__ = 345
            elif self._Msvm_ComputerSystem_count_0 == 3:
                v = _wmi_class()
                v.__instance_id__ = 351
            elif self._Msvm_ComputerSystem_count_0 == 4:
                v = _wmi_class()
                v.__instance_id__ = 364
            self._Msvm_ComputerSystem_count_0 += 1
            return v
        elif self.__id__ == 11:
            ret_value = None
            if not hasattr(self, '_Msvm_ComputerSystem_count_1'):
                self._Msvm_ComputerSystem_count_1 = 0
            if self._Msvm_ComputerSystem_count_1 == 0:
                v = _wmi_class()
                v.__instance_id__ = 360
            elif self._Msvm_ComputerSystem_count_1 == 1:
                v = _wmi_class()
                v.__instance_id__ = 367
            elif self._Msvm_ComputerSystem_count_1 == 2:
                v = _wmi_class()
                v.__instance_id__ = 375
            elif self._Msvm_ComputerSystem_count_1 == 3:
                v = _wmi_class()
                v.__instance_id__ = 378
            elif self._Msvm_ComputerSystem_count_1 == 4:
                v = _wmi_class()
                v.__instance_id__ = 382
            elif self._Msvm_ComputerSystem_count_1 == 5:
                v = _wmi_class()
                v.__instance_id__ = 387
            self._Msvm_ComputerSystem_count_1 += 1
            return v

    @Msvm_ComputerSystem.setter
    def Msvm_ComputerSystem(self, value):
        pass

    @property
    def MSVM_ComputerSystem(self):
        if self.__id__ == 9:
            ret_value = None
            if not hasattr(self, '_MSVM_ComputerSystem_count_0'):
                self._MSVM_ComputerSystem_count_0 = 0
            if self._MSVM_ComputerSystem_count_0 == 0:
                v = _wmi_class()
                v.__instance_id__ = 48
            elif self._MSVM_ComputerSystem_count_0 == 1:
                v = _wmi_class()
                v.__instance_id__ = 250
            self._MSVM_ComputerSystem_count_0 += 1
            return v

    @MSVM_ComputerSystem.setter
    def MSVM_ComputerSystem(self, value):
        pass

    def query(self, wql, instance_of=None, fields='[]'):
        if self.__id__ == 3 and wql == 'SELECT * FROM\
 MSiSCSIInitiator_SessionClass                     WHERE\
 TargetName=\'iqn.2010-10.org.openstack:volume-8957e088-dbee-4216-8056-978353a\
3e737\'':
            v = []
            return v
        elif self.__id__ == 377 and wql == u'Select * from CIM_DataFile where\
 Name =\
 \'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_adeb3f8f-5ca5-4ddf-89d\
2-7d22d8b0ab7d\\openstack_unit_test_vm_adeb3f8f-5ca5-4ddf-89d2-7d22d8b0ab7d.vh\
d\'':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 409
            v.append(v1)
            return v
        elif self.__id__ == 9 and wql == 'Select * from\
 Msvm_ImageManagementService':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 23
            v.append(v1)
            return v
        elif self.__id__ == 9 and wql == 'SELECT * FROM\
 Msvm_ResourceAllocationSettingData             WHERE ResourceSubType LIKE\
 \'Microsoft Synthetic Disk Drive\'            AND InstanceID LIKE\
 \'%Default%\'':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 63
            v.append(v1)
            return v
        elif self.__id__ == 9 and wql == 'SELECT * FROM\
 Msvm_ResourceAllocationSettingData                  WHERE ResourceSubType\
 LIKE \'Microsoft Virtual Hard Disk\' AND                  InstanceID LIKE\
 \'%Default%\' ':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 157
            v.append(v1)
            return v
        elif self.__id__ == 9 and wql == 'SELECT * FROM\
 Msvm_ResourceAllocationSettingData                 WHERE ResourceSubType =\
 \'Microsoft Synthetic SCSI Controller\'                AND InstanceID LIKE\
 \'%Default%\'':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 252
            v.append(v1)
            return v
        elif self.__id__ == 11 and wql == 'Select * from\
 Msvm_ImageManagementService':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 12
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
        elif self.__id__ == 48 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_adeb3f8f-5ca5-4ddf-89d2-7d22d8b0ab7d':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 49
            v.append(v1)
            return v
        elif self.__id__ == 250 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_adeb3f8f-5ca5-4ddf-89d2-7d22d8b0ab7d':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 251
            v.append(v1)
            return v
        elif self.__id__ == 10 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_adeb3f8f-5ca5-4ddf-89d2-7d22d8b0ab7d':
            v = []
            return v
        elif self.__id__ == 39 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_adeb3f8f-5ca5-4ddf-89d2-7d22d8b0ab7d':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 40
            v.append(v1)
            return v
        elif self.__id__ == 345 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_adeb3f8f-5ca5-4ddf-89d2-7d22d8b0ab7d':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 346
            v.append(v1)
            return v
        elif self.__id__ == 351 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_adeb3f8f-5ca5-4ddf-89d2-7d22d8b0ab7d':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 352
            v.append(v1)
            return v
        elif self.__id__ == 364 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_adeb3f8f-5ca5-4ddf-89d2-7d22d8b0ab7d':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 365
            v.append(v1)
            return v
        elif self.__id__ == 34:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 35
            v.append(v1)
            return v
        elif self.__id__ == 153:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 154
            v.append(v1)
            return v
        elif self.__id__ == 246:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 247
            v.append(v1)
            return v
        elif self.__id__ == 341:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 342
            v.append(v1)
            return v
        elif self.__id__ == 347:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 348
            v.append(v1)
            return v
        elif self.__id__ == 360 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_adeb3f8f-5ca5-4ddf-89d2-7d22d8b0ab7d':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 361
            v.append(v1)
            return v
        elif self.__id__ == 367 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_adeb3f8f-5ca5-4ddf-89d2-7d22d8b0ab7d':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 368
            v.append(v1)
            return v
        elif self.__id__ == 375 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_adeb3f8f-5ca5-4ddf-89d2-7d22d8b0ab7d':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 376
            v.append(v1)
            return v
        elif self.__id__ == 378 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_adeb3f8f-5ca5-4ddf-89d2-7d22d8b0ab7d':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 379
            v.append(v1)
            return v
        elif self.__id__ == 382 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_adeb3f8f-5ca5-4ddf-89d2-7d22d8b0ab7d':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 383
            v.append(v1)
            return v
        elif self.__id__ == 387 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_adeb3f8f-5ca5-4ddf-89d2-7d22d8b0ab7d':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 388
            v.append(v1)
            return v
        elif self.__id__ == 369:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 370
            v.append(v1)
            return v
        elif self.__id__ == 380:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 381
            v.append(v1)
            return v

    def new(self, **kwargs):
        if self.__id__ == 36:
            v = _wmi_object()
            v.__instance_id__ = 37
            return v
        elif self.__id__ == 64:
            v = _wmi_object()
            v.__instance_id__ = 65
            return v
        elif self.__id__ == 158:
            v = _wmi_object()
            v.__instance_id__ = 159
            return v
        elif self.__id__ == 253:
            v = _wmi_object()
            v.__instance_id__ = 254
            return v


class _wmi_object(object):

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__

    @property
    def CreateDifferencingVirtualHardDisk(self):
        if self.__id__ == 23:
            v = _wmi_method()
            v.__instance_id__ = 24
            return v

    @CreateDifferencingVirtualHardDisk.setter
    def CreateDifferencingVirtualHardDisk(self, value):
        pass

    @property
    def RequestStateChange(self):
        if self.__id__ == 352:
            v = _wmi_method()
            v.__instance_id__ = 353
            return v
        elif self.__id__ == 365:
            v = _wmi_method()
            v.__instance_id__ = 366
            return v
        elif self.__id__ == 361:
            v = _wmi_method()
            v.__instance_id__ = 362
            return v
        elif self.__id__ == 383:
            v = _wmi_method()
            v.__instance_id__ = 384
            return v

    @RequestStateChange.setter
    def RequestStateChange(self, value):
        pass

    @property
    def ModifyVirtualSystemResources(self):
        if self.__id__ == 35:
            ret_value = None
            if not hasattr(self, '_ModifyVirtualSystemResources_count_0'):
                self._ModifyVirtualSystemResources_count_0 = 0
            if self._ModifyVirtualSystemResources_count_0 == 0:
                v = _wmi_method()
                v.__instance_id__ = 43
            elif self._ModifyVirtualSystemResources_count_0 == 1:
                v = _wmi_method()
                v.__instance_id__ = 46
            self._ModifyVirtualSystemResources_count_0 += 1
            return v

    @ModifyVirtualSystemResources.setter
    def ModifyVirtualSystemResources(self, value):
        pass

    @property
    def Description(self):
        if self.__id__ == 33:
            return u'Creating Virtual Hard Disk'
        elif self.__id__ == 359:
            return u'Initializing and Starting Virtual Machine'

    @Description.setter
    def Description(self, value):
        pass

    @property
    def SettingType(self):
        if self.__id__ == 41:
            return 3

    @SettingType.setter
    def SettingType(self, value):
        pass

    @property
    def AddVirtualSystemResources(self):
        if self.__id__ == 154:
            v = _wmi_method()
            v.__instance_id__ = 155
            return v
        elif self.__id__ == 247:
            v = _wmi_method()
            v.__instance_id__ = 248
            return v
        elif self.__id__ == 342:
            v = _wmi_method()
            v.__instance_id__ = 343
            return v
        elif self.__id__ == 348:
            v = _wmi_method()
            v.__instance_id__ = 349
            return v

    @AddVirtualSystemResources.setter
    def AddVirtualSystemResources(self, value):
        pass

    @property
    def Address(self):
        if self.__id__ == 59:
            return u'0'
        elif self.__id__ == 60:
            return u'1'

    @Address.setter
    def Address(self, value):
        pass

    @property
    def ResourceSubType(self):
        if self.__id__ == 51:
            return u'Microsoft Virtual Keyboard'
        elif self.__id__ == 52:
            return u'Microsoft Virtual PS2 Mouse'
        elif self.__id__ == 53:
            return u'Microsoft S3 Display Controller'
        elif self.__id__ == 54:
            return u'Microsoft Synthetic Diskette Drive'
        elif self.__id__ == 55:
            return None
        elif self.__id__ == 56:
            return u'Microsoft Serial Controller'
        elif self.__id__ == 57:
            return u'Microsoft Serial Port'
        elif self.__id__ == 58:
            return u'Microsoft Serial Port'
        elif self.__id__ == 59:
            return u'Microsoft Emulated IDE Controller'
        elif self.__id__ == 60:
            return u'Microsoft Emulated IDE Controller'
        elif self.__id__ == 61:
            return u'Microsoft Synthetic Mouse'
        elif self.__id__ == 62:
            return u'Microsoft Synthetic Display Controller'
        elif self.__id__ == 390:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_12'):
                self._ResourceSubType_count_12 = 0
            if self._ResourceSubType_count_12 == 0:
                v = u'Microsoft Virtual Keyboard'
            elif self._ResourceSubType_count_12 == 1:
                v = u'Microsoft Virtual Keyboard'
            elif self._ResourceSubType_count_12 == 2:
                v = u'Microsoft Virtual Keyboard'
            self._ResourceSubType_count_12 += 1
            return v
        elif self.__id__ == 391:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_13'):
                self._ResourceSubType_count_13 = 0
            if self._ResourceSubType_count_13 == 0:
                v = u'Microsoft Virtual PS2 Mouse'
            elif self._ResourceSubType_count_13 == 1:
                v = u'Microsoft Virtual PS2 Mouse'
            elif self._ResourceSubType_count_13 == 2:
                v = u'Microsoft Virtual PS2 Mouse'
            self._ResourceSubType_count_13 += 1
            return v
        elif self.__id__ == 392:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_14'):
                self._ResourceSubType_count_14 = 0
            if self._ResourceSubType_count_14 == 0:
                v = u'Microsoft S3 Display Controller'
            elif self._ResourceSubType_count_14 == 1:
                v = u'Microsoft S3 Display Controller'
            elif self._ResourceSubType_count_14 == 2:
                v = u'Microsoft S3 Display Controller'
            self._ResourceSubType_count_14 += 1
            return v
        elif self.__id__ == 393:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_15'):
                self._ResourceSubType_count_15 = 0
            if self._ResourceSubType_count_15 == 0:
                v = u'Microsoft Synthetic Diskette Drive'
            elif self._ResourceSubType_count_15 == 1:
                v = u'Microsoft Synthetic Diskette Drive'
            elif self._ResourceSubType_count_15 == 2:
                v = u'Microsoft Synthetic Diskette Drive'
            self._ResourceSubType_count_15 += 1
            return v
        elif self.__id__ == 394:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_16'):
                self._ResourceSubType_count_16 = 0
            if self._ResourceSubType_count_16 == 0:
                v = None
            elif self._ResourceSubType_count_16 == 1:
                v = None
            elif self._ResourceSubType_count_16 == 2:
                v = None
            self._ResourceSubType_count_16 += 1
            return v
        elif self.__id__ == 395:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_17'):
                self._ResourceSubType_count_17 = 0
            if self._ResourceSubType_count_17 == 0:
                v = u'Microsoft Serial Controller'
            elif self._ResourceSubType_count_17 == 1:
                v = u'Microsoft Serial Controller'
            elif self._ResourceSubType_count_17 == 2:
                v = u'Microsoft Serial Controller'
            self._ResourceSubType_count_17 += 1
            return v
        elif self.__id__ == 396:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_18'):
                self._ResourceSubType_count_18 = 0
            if self._ResourceSubType_count_18 == 0:
                v = u'Microsoft Serial Port'
            elif self._ResourceSubType_count_18 == 1:
                v = u'Microsoft Serial Port'
            elif self._ResourceSubType_count_18 == 2:
                v = u'Microsoft Serial Port'
            self._ResourceSubType_count_18 += 1
            return v
        elif self.__id__ == 397:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_19'):
                self._ResourceSubType_count_19 = 0
            if self._ResourceSubType_count_19 == 0:
                v = u'Microsoft Serial Port'
            elif self._ResourceSubType_count_19 == 1:
                v = u'Microsoft Serial Port'
            elif self._ResourceSubType_count_19 == 2:
                v = u'Microsoft Serial Port'
            self._ResourceSubType_count_19 += 1
            return v
        elif self.__id__ == 398:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_20'):
                self._ResourceSubType_count_20 = 0
            if self._ResourceSubType_count_20 == 0:
                v = u'Microsoft Synthetic Disk Drive'
            elif self._ResourceSubType_count_20 == 1:
                v = u'Microsoft Synthetic Disk Drive'
            elif self._ResourceSubType_count_20 == 2:
                v = u'Microsoft Synthetic Disk Drive'
            self._ResourceSubType_count_20 += 1
            return v
        elif self.__id__ == 399:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_21'):
                self._ResourceSubType_count_21 = 0
            if self._ResourceSubType_count_21 == 0:
                v = u'Microsoft Virtual Hard Disk'
            elif self._ResourceSubType_count_21 == 1:
                v = u'Microsoft Virtual Hard Disk'
            elif self._ResourceSubType_count_21 == 2:
                v = u'Microsoft Virtual Hard Disk'
            self._ResourceSubType_count_21 += 1
            return v
        elif self.__id__ == 400:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_22'):
                self._ResourceSubType_count_22 = 0
            if self._ResourceSubType_count_22 == 0:
                v = u'Microsoft Emulated IDE Controller'
            elif self._ResourceSubType_count_22 == 1:
                v = u'Microsoft Emulated IDE Controller'
            elif self._ResourceSubType_count_22 == 2:
                v = u'Microsoft Emulated IDE Controller'
            self._ResourceSubType_count_22 += 1
            return v
        elif self.__id__ == 401:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_23'):
                self._ResourceSubType_count_23 = 0
            if self._ResourceSubType_count_23 == 0:
                v = u'Microsoft Emulated IDE Controller'
            elif self._ResourceSubType_count_23 == 1:
                v = u'Microsoft Emulated IDE Controller'
            elif self._ResourceSubType_count_23 == 2:
                v = u'Microsoft Emulated IDE Controller'
            self._ResourceSubType_count_23 += 1
            return v
        elif self.__id__ == 402:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_24'):
                self._ResourceSubType_count_24 = 0
            if self._ResourceSubType_count_24 == 0:
                v = u'Microsoft Synthetic Mouse'
            elif self._ResourceSubType_count_24 == 1:
                v = u'Microsoft Synthetic Mouse'
            elif self._ResourceSubType_count_24 == 2:
                v = u'Microsoft Synthetic Mouse'
            self._ResourceSubType_count_24 += 1
            return v
        elif self.__id__ == 403:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_25'):
                self._ResourceSubType_count_25 = 0
            if self._ResourceSubType_count_25 == 0:
                v = u'Microsoft Synthetic Display Controller'
            elif self._ResourceSubType_count_25 == 1:
                v = u'Microsoft Synthetic Display Controller'
            elif self._ResourceSubType_count_25 == 2:
                v = u'Microsoft Synthetic Display Controller'
            self._ResourceSubType_count_25 += 1
            return v
        elif self.__id__ == 404:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_26'):
                self._ResourceSubType_count_26 = 0
            if self._ResourceSubType_count_26 == 0:
                v = u'Microsoft Synthetic SCSI Controller'
            elif self._ResourceSubType_count_26 == 1:
                v = u'Microsoft Synthetic SCSI Controller'
            elif self._ResourceSubType_count_26 == 2:
                v = u'Microsoft Synthetic SCSI Controller'
            self._ResourceSubType_count_26 += 1
            return v

    @ResourceSubType.setter
    def ResourceSubType(self, value):
        pass

    @property
    def path_(self):
        if self.__id__ == 59:
            v = CDispatch()
            v.__instance_id__ = 152
            return v
        elif self.__id__ == 49:
            ret_value = None
            if not hasattr(self, '_path__count_1'):
                self._path__count_1 = 0
            if self._path__count_1 == 0:
                v = CDispatch()
                v.__instance_id__ = 156
            elif self._path__count_1 == 1:
                v = CDispatch()
                v.__instance_id__ = 249
            self._path__count_1 += 1
            return v
        elif self.__id__ == 251:
            v = CDispatch()
            v.__instance_id__ = 344
            return v
        elif self.__id__ == 40:
            ret_value = None
            if not hasattr(self, '_path__count_3'):
                self._path__count_3 = 0
            if self._path__count_3 == 0:
                v = CDispatch()
                v.__instance_id__ = 44
            elif self._path__count_3 == 1:
                v = CDispatch()
                v.__instance_id__ = 47
            self._path__count_3 += 1
            return v
        elif self.__id__ == 346:
            v = CDispatch()
            v.__instance_id__ = 350
            return v
        elif self.__id__ == 371:
            v = CDispatch()
            v.__instance_id__ = 372
            return v
        elif self.__id__ == 379:
            v = CDispatch()
            v.__instance_id__ = 406
            return v

    @path_.setter
    def path_(self, value):
        pass

    @property
    def ElapsedTime(self):
        if self.__id__ == 33:
            return u'00000000000001.017088:000'
        elif self.__id__ == 359:
            return u'00000000000000.772859:000'

    @ElapsedTime.setter
    def ElapsedTime(self, value):
        pass

    @property
    def Properties_(self):
        if self.__id__ == 63:
            ret_value = None
            if not hasattr(self, '_Properties__count_0'):
                self._Properties__count_0 = 0
            if self._Properties__count_0 == 0:
                v = CDispatch()
                v.__instance_id__ = 66
            elif self._Properties__count_0 == 1:
                v = CDispatch()
                v.__instance_id__ = 70
            elif self._Properties__count_0 == 2:
                v = CDispatch()
                v.__instance_id__ = 74
            elif self._Properties__count_0 == 3:
                v = CDispatch()
                v.__instance_id__ = 78
            elif self._Properties__count_0 == 4:
                v = CDispatch()
                v.__instance_id__ = 82
            elif self._Properties__count_0 == 5:
                v = CDispatch()
                v.__instance_id__ = 86
            elif self._Properties__count_0 == 6:
                v = CDispatch()
                v.__instance_id__ = 90
            elif self._Properties__count_0 == 7:
                v = CDispatch()
                v.__instance_id__ = 94
            elif self._Properties__count_0 == 8:
                v = CDispatch()
                v.__instance_id__ = 98
            elif self._Properties__count_0 == 9:
                v = CDispatch()
                v.__instance_id__ = 102
            elif self._Properties__count_0 == 10:
                v = CDispatch()
                v.__instance_id__ = 106
            elif self._Properties__count_0 == 11:
                v = CDispatch()
                v.__instance_id__ = 110
            elif self._Properties__count_0 == 12:
                v = CDispatch()
                v.__instance_id__ = 114
            elif self._Properties__count_0 == 13:
                v = CDispatch()
                v.__instance_id__ = 118
            elif self._Properties__count_0 == 14:
                v = CDispatch()
                v.__instance_id__ = 122
            elif self._Properties__count_0 == 15:
                v = CDispatch()
                v.__instance_id__ = 126
            elif self._Properties__count_0 == 16:
                v = CDispatch()
                v.__instance_id__ = 130
            elif self._Properties__count_0 == 17:
                v = CDispatch()
                v.__instance_id__ = 134
            elif self._Properties__count_0 == 18:
                v = CDispatch()
                v.__instance_id__ = 138
            elif self._Properties__count_0 == 19:
                v = CDispatch()
                v.__instance_id__ = 142
            elif self._Properties__count_0 == 20:
                v = CDispatch()
                v.__instance_id__ = 148
            self._Properties__count_0 += 1
            return v
        elif self.__id__ == 157:
            ret_value = None
            if not hasattr(self, '_Properties__count_1'):
                self._Properties__count_1 = 0
            if self._Properties__count_1 == 0:
                v = CDispatch()
                v.__instance_id__ = 160
            elif self._Properties__count_1 == 1:
                v = CDispatch()
                v.__instance_id__ = 164
            elif self._Properties__count_1 == 2:
                v = CDispatch()
                v.__instance_id__ = 168
            elif self._Properties__count_1 == 3:
                v = CDispatch()
                v.__instance_id__ = 172
            elif self._Properties__count_1 == 4:
                v = CDispatch()
                v.__instance_id__ = 176
            elif self._Properties__count_1 == 5:
                v = CDispatch()
                v.__instance_id__ = 180
            elif self._Properties__count_1 == 6:
                v = CDispatch()
                v.__instance_id__ = 184
            elif self._Properties__count_1 == 7:
                v = CDispatch()
                v.__instance_id__ = 188
            elif self._Properties__count_1 == 8:
                v = CDispatch()
                v.__instance_id__ = 192
            elif self._Properties__count_1 == 9:
                v = CDispatch()
                v.__instance_id__ = 196
            elif self._Properties__count_1 == 10:
                v = CDispatch()
                v.__instance_id__ = 200
            elif self._Properties__count_1 == 11:
                v = CDispatch()
                v.__instance_id__ = 204
            elif self._Properties__count_1 == 12:
                v = CDispatch()
                v.__instance_id__ = 208
            elif self._Properties__count_1 == 13:
                v = CDispatch()
                v.__instance_id__ = 212
            elif self._Properties__count_1 == 14:
                v = CDispatch()
                v.__instance_id__ = 216
            elif self._Properties__count_1 == 15:
                v = CDispatch()
                v.__instance_id__ = 220
            elif self._Properties__count_1 == 16:
                v = CDispatch()
                v.__instance_id__ = 224
            elif self._Properties__count_1 == 17:
                v = CDispatch()
                v.__instance_id__ = 228
            elif self._Properties__count_1 == 18:
                v = CDispatch()
                v.__instance_id__ = 232
            elif self._Properties__count_1 == 19:
                v = CDispatch()
                v.__instance_id__ = 236
            elif self._Properties__count_1 == 20:
                v = CDispatch()
                v.__instance_id__ = 242
            self._Properties__count_1 += 1
            return v
        elif self.__id__ == 252:
            ret_value = None
            if not hasattr(self, '_Properties__count_2'):
                self._Properties__count_2 = 0
            if self._Properties__count_2 == 0:
                v = CDispatch()
                v.__instance_id__ = 255
            elif self._Properties__count_2 == 1:
                v = CDispatch()
                v.__instance_id__ = 259
            elif self._Properties__count_2 == 2:
                v = CDispatch()
                v.__instance_id__ = 263
            elif self._Properties__count_2 == 3:
                v = CDispatch()
                v.__instance_id__ = 267
            elif self._Properties__count_2 == 4:
                v = CDispatch()
                v.__instance_id__ = 271
            elif self._Properties__count_2 == 5:
                v = CDispatch()
                v.__instance_id__ = 275
            elif self._Properties__count_2 == 6:
                v = CDispatch()
                v.__instance_id__ = 279
            elif self._Properties__count_2 == 7:
                v = CDispatch()
                v.__instance_id__ = 283
            elif self._Properties__count_2 == 8:
                v = CDispatch()
                v.__instance_id__ = 287
            elif self._Properties__count_2 == 9:
                v = CDispatch()
                v.__instance_id__ = 291
            elif self._Properties__count_2 == 10:
                v = CDispatch()
                v.__instance_id__ = 295
            elif self._Properties__count_2 == 11:
                v = CDispatch()
                v.__instance_id__ = 299
            elif self._Properties__count_2 == 12:
                v = CDispatch()
                v.__instance_id__ = 303
            elif self._Properties__count_2 == 13:
                v = CDispatch()
                v.__instance_id__ = 307
            elif self._Properties__count_2 == 14:
                v = CDispatch()
                v.__instance_id__ = 311
            elif self._Properties__count_2 == 15:
                v = CDispatch()
                v.__instance_id__ = 315
            elif self._Properties__count_2 == 16:
                v = CDispatch()
                v.__instance_id__ = 319
            elif self._Properties__count_2 == 17:
                v = CDispatch()
                v.__instance_id__ = 323
            elif self._Properties__count_2 == 18:
                v = CDispatch()
                v.__instance_id__ = 327
            elif self._Properties__count_2 == 19:
                v = CDispatch()
                v.__instance_id__ = 331
            elif self._Properties__count_2 == 20:
                v = CDispatch()
                v.__instance_id__ = 337
            self._Properties__count_2 += 1
            return v
        elif self.__id__ == 65:
            ret_value = None
            if not hasattr(self, '_Properties__count_3'):
                self._Properties__count_3 = 0
            if self._Properties__count_3 == 0:
                v = CDispatch()
                v.__instance_id__ = 68
            elif self._Properties__count_3 == 1:
                v = CDispatch()
                v.__instance_id__ = 72
            elif self._Properties__count_3 == 2:
                v = CDispatch()
                v.__instance_id__ = 76
            elif self._Properties__count_3 == 3:
                v = CDispatch()
                v.__instance_id__ = 80
            elif self._Properties__count_3 == 4:
                v = CDispatch()
                v.__instance_id__ = 84
            elif self._Properties__count_3 == 5:
                v = CDispatch()
                v.__instance_id__ = 88
            elif self._Properties__count_3 == 6:
                v = CDispatch()
                v.__instance_id__ = 92
            elif self._Properties__count_3 == 7:
                v = CDispatch()
                v.__instance_id__ = 96
            elif self._Properties__count_3 == 8:
                v = CDispatch()
                v.__instance_id__ = 100
            elif self._Properties__count_3 == 9:
                v = CDispatch()
                v.__instance_id__ = 104
            elif self._Properties__count_3 == 10:
                v = CDispatch()
                v.__instance_id__ = 108
            elif self._Properties__count_3 == 11:
                v = CDispatch()
                v.__instance_id__ = 112
            elif self._Properties__count_3 == 12:
                v = CDispatch()
                v.__instance_id__ = 116
            elif self._Properties__count_3 == 13:
                v = CDispatch()
                v.__instance_id__ = 120
            elif self._Properties__count_3 == 14:
                v = CDispatch()
                v.__instance_id__ = 124
            elif self._Properties__count_3 == 15:
                v = CDispatch()
                v.__instance_id__ = 128
            elif self._Properties__count_3 == 16:
                v = CDispatch()
                v.__instance_id__ = 132
            elif self._Properties__count_3 == 17:
                v = CDispatch()
                v.__instance_id__ = 136
            elif self._Properties__count_3 == 18:
                v = CDispatch()
                v.__instance_id__ = 140
            elif self._Properties__count_3 == 19:
                v = CDispatch()
                v.__instance_id__ = 144
            elif self._Properties__count_3 == 20:
                v = CDispatch()
                v.__instance_id__ = 146
            elif self._Properties__count_3 == 21:
                v = CDispatch()
                v.__instance_id__ = 150
            self._Properties__count_3 += 1
            return v
        elif self.__id__ == 159:
            ret_value = None
            if not hasattr(self, '_Properties__count_4'):
                self._Properties__count_4 = 0
            if self._Properties__count_4 == 0:
                v = CDispatch()
                v.__instance_id__ = 162
            elif self._Properties__count_4 == 1:
                v = CDispatch()
                v.__instance_id__ = 166
            elif self._Properties__count_4 == 2:
                v = CDispatch()
                v.__instance_id__ = 170
            elif self._Properties__count_4 == 3:
                v = CDispatch()
                v.__instance_id__ = 174
            elif self._Properties__count_4 == 4:
                v = CDispatch()
                v.__instance_id__ = 178
            elif self._Properties__count_4 == 5:
                v = CDispatch()
                v.__instance_id__ = 182
            elif self._Properties__count_4 == 6:
                v = CDispatch()
                v.__instance_id__ = 186
            elif self._Properties__count_4 == 7:
                v = CDispatch()
                v.__instance_id__ = 190
            elif self._Properties__count_4 == 8:
                v = CDispatch()
                v.__instance_id__ = 194
            elif self._Properties__count_4 == 9:
                v = CDispatch()
                v.__instance_id__ = 198
            elif self._Properties__count_4 == 10:
                v = CDispatch()
                v.__instance_id__ = 202
            elif self._Properties__count_4 == 11:
                v = CDispatch()
                v.__instance_id__ = 206
            elif self._Properties__count_4 == 12:
                v = CDispatch()
                v.__instance_id__ = 210
            elif self._Properties__count_4 == 13:
                v = CDispatch()
                v.__instance_id__ = 214
            elif self._Properties__count_4 == 14:
                v = CDispatch()
                v.__instance_id__ = 218
            elif self._Properties__count_4 == 15:
                v = CDispatch()
                v.__instance_id__ = 222
            elif self._Properties__count_4 == 16:
                v = CDispatch()
                v.__instance_id__ = 226
            elif self._Properties__count_4 == 17:
                v = CDispatch()
                v.__instance_id__ = 230
            elif self._Properties__count_4 == 18:
                v = CDispatch()
                v.__instance_id__ = 234
            elif self._Properties__count_4 == 19:
                v = CDispatch()
                v.__instance_id__ = 238
            elif self._Properties__count_4 == 20:
                v = CDispatch()
                v.__instance_id__ = 240
            elif self._Properties__count_4 == 21:
                v = CDispatch()
                v.__instance_id__ = 244
            self._Properties__count_4 += 1
            return v
        elif self.__id__ == 254:
            ret_value = None
            if not hasattr(self, '_Properties__count_5'):
                self._Properties__count_5 = 0
            if self._Properties__count_5 == 0:
                v = CDispatch()
                v.__instance_id__ = 257
            elif self._Properties__count_5 == 1:
                v = CDispatch()
                v.__instance_id__ = 261
            elif self._Properties__count_5 == 2:
                v = CDispatch()
                v.__instance_id__ = 265
            elif self._Properties__count_5 == 3:
                v = CDispatch()
                v.__instance_id__ = 269
            elif self._Properties__count_5 == 4:
                v = CDispatch()
                v.__instance_id__ = 273
            elif self._Properties__count_5 == 5:
                v = CDispatch()
                v.__instance_id__ = 277
            elif self._Properties__count_5 == 6:
                v = CDispatch()
                v.__instance_id__ = 281
            elif self._Properties__count_5 == 7:
                v = CDispatch()
                v.__instance_id__ = 285
            elif self._Properties__count_5 == 8:
                v = CDispatch()
                v.__instance_id__ = 289
            elif self._Properties__count_5 == 9:
                v = CDispatch()
                v.__instance_id__ = 293
            elif self._Properties__count_5 == 10:
                v = CDispatch()
                v.__instance_id__ = 297
            elif self._Properties__count_5 == 11:
                v = CDispatch()
                v.__instance_id__ = 301
            elif self._Properties__count_5 == 12:
                v = CDispatch()
                v.__instance_id__ = 305
            elif self._Properties__count_5 == 13:
                v = CDispatch()
                v.__instance_id__ = 309
            elif self._Properties__count_5 == 14:
                v = CDispatch()
                v.__instance_id__ = 313
            elif self._Properties__count_5 == 15:
                v = CDispatch()
                v.__instance_id__ = 317
            elif self._Properties__count_5 == 16:
                v = CDispatch()
                v.__instance_id__ = 321
            elif self._Properties__count_5 == 17:
                v = CDispatch()
                v.__instance_id__ = 325
            elif self._Properties__count_5 == 18:
                v = CDispatch()
                v.__instance_id__ = 329
            elif self._Properties__count_5 == 19:
                v = CDispatch()
                v.__instance_id__ = 333
            elif self._Properties__count_5 == 20:
                v = CDispatch()
                v.__instance_id__ = 335
            elif self._Properties__count_5 == 21:
                v = CDispatch()
                v.__instance_id__ = 339
            self._Properties__count_5 += 1
            return v

    @Properties_.setter
    def Properties_(self, value):
        pass

    @property
    def Connection(self):
        if self.__id__ == 399:
            v = ()
            v1 =\
 u'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_adeb3f8f-5ca5-4ddf-89d\
2-7d22d8b0ab7d\\openstack_unit_test_vm_adeb3f8f-5ca5-4ddf-89d2-7d22d8b0ab7d.vh\
d'
            v += (v1,)
            return v

    @Connection.setter
    def Connection(self, value):
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
        if self.__id__ == 12:
            v = _wmi_method()
            v.__instance_id__ = 13
            return v

    @CreateDynamicVirtualHardDisk.setter
    def CreateDynamicVirtualHardDisk(self, value):
        pass

    @property
    def JobState(self):
        if self.__id__ == 14:
            return 4
        elif self.__id__ == 15:
            return 4
        elif self.__id__ == 16:
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
            ret_value = None
            if not hasattr(self, '_JobState_count_8'):
                self._JobState_count_8 = 0
            if self._JobState_count_8 == 0:
                v = 7
            elif self._JobState_count_8 == 1:
                v = 7
            self._JobState_count_8 += 1
            return v
        elif self.__id__ == 25:
            return 4
        elif self.__id__ == 26:
            return 4
        elif self.__id__ == 27:
            return 4
        elif self.__id__ == 28:
            return 4
        elif self.__id__ == 29:
            return 4
        elif self.__id__ == 30:
            return 4
        elif self.__id__ == 31:
            return 4
        elif self.__id__ == 32:
            return 4
        elif self.__id__ == 33:
            ret_value = None
            if not hasattr(self, '_JobState_count_17'):
                self._JobState_count_17 = 0
            if self._JobState_count_17 == 0:
                v = 7
            elif self._JobState_count_17 == 1:
                v = 7
            self._JobState_count_17 += 1
            return v
        elif self.__id__ == 354:
            return 4
        elif self.__id__ == 355:
            return 4
        elif self.__id__ == 356:
            return 4
        elif self.__id__ == 357:
            return 4
        elif self.__id__ == 358:
            return 4
        elif self.__id__ == 359:
            ret_value = None
            if not hasattr(self, '_JobState_count_23'):
                self._JobState_count_23 = 0
            if self._JobState_count_23 == 0:
                v = 7
            elif self._JobState_count_23 == 1:
                v = 7
            self._JobState_count_23 += 1
            return v
        elif self.__id__ == 363:
            ret_value = None
            if not hasattr(self, '_JobState_count_24'):
                self._JobState_count_24 = 0
            if self._JobState_count_24 == 0:
                v = 7
            elif self._JobState_count_24 == 1:
                v = 7
            self._JobState_count_24 += 1
            return v
        elif self.__id__ == 385:
            return 4
        elif self.__id__ == 386:
            ret_value = None
            if not hasattr(self, '_JobState_count_26'):
                self._JobState_count_26 = 0
            if self._JobState_count_26 == 0:
                v = 7
            elif self._JobState_count_26 == 1:
                v = 7
            self._JobState_count_26 += 1
            return v
        elif self.__id__ == 407:
            return 4
        elif self.__id__ == 408:
            ret_value = None
            if not hasattr(self, '_JobState_count_28'):
                self._JobState_count_28 = 0
            if self._JobState_count_28 == 0:
                v = 7
            elif self._JobState_count_28 == 1:
                v = 7
            self._JobState_count_28 += 1
            return v

    @JobState.setter
    def JobState(self, value):
        pass

    @property
    def DefineVirtualSystem(self):
        if self.__id__ == 35:
            v = _wmi_method()
            v.__instance_id__ = 38
            return v

    @DefineVirtualSystem.setter
    def DefineVirtualSystem(self, value):
        pass

    @property
    def _properties(self):
        if self.__id__ == 63:
            v = []
            v1 = u'InstanceID'
            v.append(v1)
            v1 = u'ResourceSubType'
            v.append(v1)
            v1 = u'HostResource'
            v.append(v1)
            v1 = u'ElementName'
            v.append(v1)
            v1 = u'Description'
            v.append(v1)
            v1 = u'Parent'
            v.append(v1)
            v1 = u'VirtualQuantity'
            v.append(v1)
            v1 = u'AutomaticDeallocation'
            v.append(v1)
            v1 = u'AutomaticAllocation'
            v.append(v1)
            v1 = u'PoolID'
            v.append(v1)
            v1 = u'Reservation'
            v.append(v1)
            v1 = u'AllocationUnits'
            v.append(v1)
            v1 = u'MappingBehavior'
            v.append(v1)
            v1 = u'Address'
            v.append(v1)
            v1 = u'OtherResourceType'
            v.append(v1)
            v1 = u'Caption'
            v.append(v1)
            v1 = u'ConsumerVisibility'
            v.append(v1)
            v1 = u'Limit'
            v.append(v1)
            v1 = u'ResourceType'
            v.append(v1)
            v1 = u'Weight'
            v.append(v1)
            v1 = u'VirtualSystemIdentifiers'
            v.append(v1)
            v1 = u'Connection'
            v.append(v1)
            return v
        elif self.__id__ == 157:
            v = []
            v1 = u'InstanceID'
            v.append(v1)
            v1 = u'ResourceSubType'
            v.append(v1)
            v1 = u'HostResource'
            v.append(v1)
            v1 = u'ElementName'
            v.append(v1)
            v1 = u'Description'
            v.append(v1)
            v1 = u'Parent'
            v.append(v1)
            v1 = u'VirtualQuantity'
            v.append(v1)
            v1 = u'AutomaticDeallocation'
            v.append(v1)
            v1 = u'AutomaticAllocation'
            v.append(v1)
            v1 = u'PoolID'
            v.append(v1)
            v1 = u'Reservation'
            v.append(v1)
            v1 = u'AllocationUnits'
            v.append(v1)
            v1 = u'MappingBehavior'
            v.append(v1)
            v1 = u'Address'
            v.append(v1)
            v1 = u'OtherResourceType'
            v.append(v1)
            v1 = u'Caption'
            v.append(v1)
            v1 = u'ConsumerVisibility'
            v.append(v1)
            v1 = u'Limit'
            v.append(v1)
            v1 = u'ResourceType'
            v.append(v1)
            v1 = u'Weight'
            v.append(v1)
            v1 = u'VirtualSystemIdentifiers'
            v.append(v1)
            v1 = u'Connection'
            v.append(v1)
            return v
        elif self.__id__ == 252:
            v = []
            v1 = u'InstanceID'
            v.append(v1)
            v1 = u'ResourceSubType'
            v.append(v1)
            v1 = u'HostResource'
            v.append(v1)
            v1 = u'ElementName'
            v.append(v1)
            v1 = u'Description'
            v.append(v1)
            v1 = u'Parent'
            v.append(v1)
            v1 = u'VirtualQuantity'
            v.append(v1)
            v1 = u'AutomaticDeallocation'
            v.append(v1)
            v1 = u'AutomaticAllocation'
            v.append(v1)
            v1 = u'PoolID'
            v.append(v1)
            v1 = u'Reservation'
            v.append(v1)
            v1 = u'AllocationUnits'
            v.append(v1)
            v1 = u'MappingBehavior'
            v.append(v1)
            v1 = u'Address'
            v.append(v1)
            v1 = u'OtherResourceType'
            v.append(v1)
            v1 = u'Caption'
            v.append(v1)
            v1 = u'ConsumerVisibility'
            v.append(v1)
            v1 = u'Limit'
            v.append(v1)
            v1 = u'ResourceType'
            v.append(v1)
            v1 = u'Weight'
            v.append(v1)
            v1 = u'VirtualSystemIdentifiers'
            v.append(v1)
            v1 = u'Connection'
            v.append(v1)
            return v

    @_properties.setter
    def _properties(self, value):
        pass

    @property
    def DestroyVirtualSystem(self):
        if self.__id__ == 381:
            v = _wmi_method()
            v.__instance_id__ = 405
            return v

    @DestroyVirtualSystem.setter
    def DestroyVirtualSystem(self, value):
        pass

    @property
    def GetSummaryInformation(self):
        if self.__id__ == 370:
            v = _wmi_method()
            v.__instance_id__ = 373
            return v

    @GetSummaryInformation.setter
    def GetSummaryInformation(self, value):
        pass

    @property
    def Delete(self):
        if self.__id__ == 409:
            v = _wmi_method()
            v.__instance_id__ = 410
            return v

    @Delete.setter
    def Delete(self, value):
        pass

    def associators(self, wmi_association_class='', wmi_result_class=''):
        if self.__id__ == 50 and wmi_result_class ==\
 'MSVM_ResourceAllocationSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 51
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 52
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 53
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 54
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 55
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 56
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 57
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 58
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 59
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 60
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 61
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 62
            v.append(v1)
            return v
        elif self.__id__ == 49 and wmi_result_class ==\
 'Msvm_VirtualSystemSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 50
            v.append(v1)
            return v
        elif self.__id__ == 41 and wmi_result_class ==\
 'Msvm_MemorySettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 42
            v.append(v1)
            return v
        elif self.__id__ == 41 and wmi_result_class ==\
 'Msvm_ProcessorSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 45
            v.append(v1)
            return v
        elif self.__id__ == 40 and wmi_result_class ==\
 'Msvm_VirtualSystemSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 41
            v.append(v1)
            return v
        elif self.__id__ == 368 and wmi_association_class ==\
 'Msvm_SettingsDefineState' and wmi_result_class ==\
 'Msvm_VirtualSystemSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 371
            v.append(v1)
            return v
        elif self.__id__ == 389 and wmi_result_class ==\
 'MSVM_ResourceAllocationSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 390
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 391
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 392
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 393
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 394
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 395
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 396
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 397
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 398
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 399
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 400
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 401
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 402
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 403
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 404
            v.append(v1)
            return v
        elif self.__id__ == 388 and wmi_result_class ==\
 'Msvm_VirtualSystemSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 389
            v.append(v1)
            return v

    def GetText_(self, iObjectTextFormat='<PyOleMissing object at\
 0x04091890>', iFlags=0, objWbemNamedValueSet=None):
        if self.__id__ == 42 and iObjectTextFormat == 1:
            return u'<INSTANCE CLASSNAME="Msvm_MemorySettingData"><PROPERTY\
 NAME="__PATH" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>\\\\HV12OSDEMO1\\root\\virtualization:Msvm_MemorySetting\
Data.InstanceID="Microsoft:8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509\\\\4764334d-e0\
01-4176-82ee-5594ec9b530e"</VALUE></PROPERTY><PROPERTY NAME="__NAMESPACE"\
 CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>root\\virtualization</VALUE></PROPERTY><PROPERTY\
 NAME="__SERVER" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>HV12OSDEMO1</VALUE></PROPERTY><PROPERTY.ARRAY\
 NAME="__DERIVATION" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE.ARRAY><VALUE>CIM_ResourceAllocationSettingData</VALUE><V\
ALUE>CIM_SettingData</VALUE><VALUE>CIM_ManagedElement</VALUE></VALUE.ARRAY></P\
ROPERTY.ARRAY><PROPERTY NAME="__PROPERTY_COUNT" CLASSORIGIN="___SYSTEM"\
 TYPE="sint32"><VALUE>26</VALUE></PROPERTY><PROPERTY NAME="__RELPATH"\
 CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>Msvm_MemorySettingData.InstanceID="Microsoft:8FB6FE34-0C\
9B-472F-B0D8-9B7ADA69C509\\\\4764334d-e001-4176-82ee-5594ec9b530e"</VALUE></PR\
OPERTY><PROPERTY NAME="__DYNASTY" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>CIM_ManagedElement</VALUE></PROPERTY><PROPERTY\
 NAME="__SUPERCLASS" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>CIM_ResourceAllocationSettingData</VALUE></PROPERTY><PRO\
PERTY NAME="__CLASS" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>Msvm_MemorySettingData</VALUE></PROPERTY><PROPERTY\
 NAME="__GENUS" CLASSORIGIN="___SYSTEM"\
 TYPE="sint32"><VALUE>2</VALUE></PROPERTY><PROPERTY NAME="Address"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="AllocationUnits"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>MB</VALUE></PROPERTY><PROPERTY\
 NAME="AutomaticAllocation" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY\
 NAME="AutomaticDeallocation" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY NAME="Caption"\
 CLASSORIGIN="CIM_ManagedElement"\
 TYPE="string"><VALUE>Memory</VALUE></PROPERTY><PROPERTY.ARRAY\
 NAME="Connection" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY.ARRAY><PROPERTY NAME="ConsumerVisibility"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"><VALUE>3</VALUE></PROPERTY><PROPERTY NAME="Description"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>Settings for Microsoft\
 Virtual Machine Memory.</VALUE></PROPERTY><PROPERTY NAME="DeviceID"\
 CLASSORIGIN="Msvm_MemorySettingData" TYPE="string"></PROPERTY><PROPERTY\
 NAME="DeviceIDFormat" CLASSORIGIN="Msvm_MemorySettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="DynamicMemoryEnabled"\
 CLASSORIGIN="Msvm_MemorySettingData"\
 TYPE="boolean"><VALUE>FALSE</VALUE></PROPERTY><PROPERTY NAME="ElementName"\
 CLASSORIGIN="CIM_ManagedElement"\
 TYPE="string"><VALUE>Memory</VALUE></PROPERTY><PROPERTY.ARRAY\
 NAME="HostResource" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY.ARRAY><PROPERTY NAME="InstanceID"\
 CLASSORIGIN="CIM_SettingData"\
 TYPE="string"><VALUE>Microsoft:8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509\\4764334d\
-e001-4176-82ee-5594ec9b530e</VALUE></PROPERTY><PROPERTY NAME="IsVirtualized"\
 CLASSORIGIN="Msvm_MemorySettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY NAME="Limit"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>512</VALUE></PROPERTY><PROPERTY NAME="MappingBehavior"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="OtherResourceType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="Parent"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="PoolID"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>15129609-B465-4916-AA13-0CF4B109ADB0</VALUE></PROPERTY><\
PROPERTY NAME="Reservation" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>512</VALUE></PROPERTY><PROPERTY NAME="ResourceSubType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Microsoft Virtual Machine\
 Memory</VALUE></PROPERTY><PROPERTY NAME="ResourceType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"><VALUE>4</VALUE></PROPERTY><PROPERTY NAME="TargetMemoryBuffer"\
 CLASSORIGIN="Msvm_MemorySettingData"\
 TYPE="uint32"><VALUE>20</VALUE></PROPERTY><PROPERTY NAME="VirtualQuantity"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>512</VALUE></PROPERTY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>5000</VALUE></PROPERTY></INSTANCE>'
        elif self.__id__ == 45 and iObjectTextFormat == 1:
            return u'<INSTANCE CLASSNAME="Msvm_ProcessorSettingData"><PROPERTY\
 NAME="__PATH" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ProcessorSett\
ingData.InstanceID="Microsoft:8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509\\\\b637f346\
-6a0e-4dec-af52-bd70cb80a21d\\\\0"</VALUE></PROPERTY><PROPERTY\
 NAME="__NAMESPACE" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>root\\virtualization</VALUE></PROPERTY><PROPERTY\
 NAME="__SERVER" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>HV12OSDEMO1</VALUE></PROPERTY><PROPERTY.ARRAY\
 NAME="__DERIVATION" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE.ARRAY><VALUE>CIM_ResourceAllocationSettingData</VALUE><V\
ALUE>CIM_SettingData</VALUE><VALUE>CIM_ManagedElement</VALUE></VALUE.ARRAY></P\
ROPERTY.ARRAY><PROPERTY NAME="__PROPERTY_COUNT" CLASSORIGIN="___SYSTEM"\
 TYPE="sint32"><VALUE>29</VALUE></PROPERTY><PROPERTY NAME="__RELPATH"\
 CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>Msvm_ProcessorSettingData.InstanceID="Microsoft:8FB6FE34\
-0C9B-472F-B0D8-9B7ADA69C509\\\\b637f346-6a0e-4dec-af52-bd70cb80a21d\\\\0"</VA\
LUE></PROPERTY><PROPERTY NAME="__DYNASTY" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>CIM_ManagedElement</VALUE></PROPERTY><PROPERTY\
 NAME="__SUPERCLASS" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>CIM_ResourceAllocationSettingData</VALUE></PROPERTY><PRO\
PERTY NAME="__CLASS" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>Msvm_ProcessorSettingData</VALUE></PROPERTY><PROPERTY\
 NAME="__GENUS" CLASSORIGIN="___SYSTEM"\
 TYPE="sint32"><VALUE>2</VALUE></PROPERTY><PROPERTY NAME="Address"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="AllocationUnits"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Processor Cores</VALUE></PROPERTY><PROPERTY\
 NAME="AutomaticAllocation" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY\
 NAME="AutomaticDeallocation" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY NAME="Caption"\
 CLASSORIGIN="CIM_ManagedElement"\
 TYPE="string"><VALUE>Processor</VALUE></PROPERTY><PROPERTY.ARRAY\
 NAME="Connection" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY.ARRAY><PROPERTY NAME="ConsumerVisibility"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"><VALUE>3</VALUE></PROPERTY><PROPERTY NAME="Description"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>Settings for Microsoft\
 Virtual Processor.</VALUE></PROPERTY><PROPERTY NAME="DeviceID"\
 CLASSORIGIN="Msvm_ProcessorSettingData" TYPE="string"></PROPERTY><PROPERTY\
 NAME="DeviceIDFormat" CLASSORIGIN="Msvm_ProcessorSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="ElementName"\
 CLASSORIGIN="CIM_ManagedElement"\
 TYPE="string"><VALUE>Processor</VALUE></PROPERTY><PROPERTY.ARRAY\
 NAME="HostResource" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY.ARRAY><PROPERTY NAME="InstanceID"\
 CLASSORIGIN="CIM_SettingData"\
 TYPE="string"><VALUE>Microsoft:8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509\\b637f346\
-6a0e-4dec-af52-bd70cb80a21d\\0</VALUE></PROPERTY><PROPERTY\
 NAME="IsVirtualized" CLASSORIGIN="Msvm_ProcessorSettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY NAME="Limit"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>100000</VALUE></PROPERTY><PROPERTY NAME="LimitCPUID"\
 CLASSORIGIN="Msvm_ProcessorSettingData"\
 TYPE="boolean"><VALUE>FALSE</VALUE></PROPERTY><PROPERTY\
 NAME="LimitProcessorFeatures" CLASSORIGIN="Msvm_ProcessorSettingData"\
 TYPE="boolean"><VALUE>FALSE</VALUE></PROPERTY><PROPERTY\
 NAME="MappingBehavior" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="OtherResourceType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="Parent"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="PoolID"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>A4F3C4E4-5E15-4018-A713-96C2CFB4C9B8</VALUE></PROPERTY><\
PROPERTY NAME="ProcessorsPerSocket" CLASSORIGIN="Msvm_ProcessorSettingData"\
 TYPE="uint16"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="Reservation"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="ResourceSubType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Microsoft Processor</VALUE></PROPERTY><PROPERTY\
 NAME="ResourceType" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"><VALUE>3</VALUE></PROPERTY><PROPERTY NAME="SocketCount"\
 CLASSORIGIN="Msvm_ProcessorSettingData"\
 TYPE="uint16"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="ThreadsEnabled"\
 CLASSORIGIN="Msvm_ProcessorSettingData" TYPE="boolean"></PROPERTY><PROPERTY\
 NAME="VirtualQuantity" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>100</VALUE></PROPERTY></INSTANCE>'
        elif self.__id__ == 37 and iObjectTextFormat == 1:
            return u'<INSTANCE\
 CLASSNAME="Msvm_VirtualSystemGlobalSettingData"><PROPERTY NAME="__PATH"\
 CLASSORIGIN="___SYSTEM" TYPE="string"></PROPERTY><PROPERTY NAME="__NAMESPACE"\
 CLASSORIGIN="___SYSTEM" TYPE="string"></PROPERTY><PROPERTY NAME="__SERVER"\
 CLASSORIGIN="___SYSTEM" TYPE="string"></PROPERTY><PROPERTY.ARRAY\
 NAME="__DERIVATION" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE.ARRAY><VALUE>CIM_VirtualSystemSettingData</VALUE><VALUE>\
CIM_SettingData</VALUE><VALUE>CIM_ManagedElement</VALUE></VALUE.ARRAY></PROPER\
TY.ARRAY><PROPERTY NAME="__PROPERTY_COUNT" CLASSORIGIN="___SYSTEM"\
 TYPE="sint32"><VALUE>23</VALUE></PROPERTY><PROPERTY NAME="__RELPATH"\
 CLASSORIGIN="___SYSTEM" TYPE="string"></PROPERTY><PROPERTY NAME="__DYNASTY"\
 CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>CIM_ManagedElement</VALUE></PROPERTY><PROPERTY\
 NAME="__SUPERCLASS" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>CIM_VirtualSystemSettingData</VALUE></PROPERTY><PROPERTY\
 NAME="__CLASS" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>Msvm_VirtualSystemGlobalSettingData</VALUE></PROPERTY><P\
ROPERTY NAME="__GENUS" CLASSORIGIN="___SYSTEM"\
 TYPE="sint32"><VALUE>2</VALUE></PROPERTY><PROPERTY\
 NAME="AdditionalRecoveryInformation"\
 CLASSORIGIN="Msvm_VirtualSystemGlobalSettingData" PROPAGATED="true"\
 TYPE="string"></PROPERTY><PROPERTY NAME="AllowFullSCSICommandSet"\
 CLASSORIGIN="Msvm_VirtualSystemGlobalSettingData" PROPAGATED="true"\
 TYPE="boolean"></PROPERTY><PROPERTY NAME="AutoActivate"\
 CLASSORIGIN="CIM_VirtualSystemSettingData" PROPAGATED="true"\
 TYPE="boolean"></PROPERTY><PROPERTY NAME="AutomaticRecoveryAction"\
 CLASSORIGIN="Msvm_VirtualSystemGlobalSettingData" PROPAGATED="true"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="AutomaticShutdownAction"\
 CLASSORIGIN="Msvm_VirtualSystemGlobalSettingData" PROPAGATED="true"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="AutomaticStartupAction"\
 CLASSORIGIN="Msvm_VirtualSystemGlobalSettingData" PROPAGATED="true"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="AutomaticStartupActionDelay"\
 CLASSORIGIN="Msvm_VirtualSystemGlobalSettingData" PROPAGATED="true"\
 TYPE="datetime"><VALUE>00000000000000.000000:000</VALUE></PROPERTY><PROPERTY\
 NAME="Caption" CLASSORIGIN="CIM_ManagedElement" PROPAGATED="true"\
 TYPE="string"></PROPERTY><PROPERTY NAME="CreationTime"\
 CLASSORIGIN="CIM_VirtualSystemSettingData" PROPAGATED="true"\
 TYPE="datetime"></PROPERTY><PROPERTY NAME="DebugChannelId"\
 CLASSORIGIN="Msvm_VirtualSystemGlobalSettingData" PROPAGATED="true"\
 TYPE="uint32"></PROPERTY><PROPERTY NAME="DebugPort"\
 CLASSORIGIN="Msvm_VirtualSystemGlobalSettingData" PROPAGATED="true"\
 TYPE="uint32"></PROPERTY><PROPERTY NAME="DebugPortEnabled"\
 CLASSORIGIN="Msvm_VirtualSystemGlobalSettingData" PROPAGATED="true"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="Description"\
 CLASSORIGIN="CIM_ManagedElement" PROPAGATED="true"\
 TYPE="string"></PROPERTY><PROPERTY NAME="ElementName"\
 CLASSORIGIN="CIM_ManagedElement"\
 TYPE="string"><VALUE>openstack_unit_test_vm_adeb3f8f-5ca5-4ddf-89d2-7d22d8b0a\
b7d</VALUE></PROPERTY><PROPERTY NAME="ExternalDataRoot"\
 CLASSORIGIN="Msvm_VirtualSystemGlobalSettingData" PROPAGATED="true"\
 TYPE="string"></PROPERTY><PROPERTY NAME="InstanceID"\
 CLASSORIGIN="CIM_SettingData" PROPAGATED="true"\
 TYPE="string"></PROPERTY><PROPERTY NAME="OtherVirtualSystemType"\
 CLASSORIGIN="CIM_VirtualSystemSettingData" PROPAGATED="true"\
 TYPE="string"></PROPERTY><PROPERTY NAME="ScopeOfResidence"\
 CLASSORIGIN="Msvm_VirtualSystemGlobalSettingData" PROPAGATED="true"\
 TYPE="string"></PROPERTY><PROPERTY NAME="SettingType"\
 CLASSORIGIN="CIM_VirtualSystemSettingData" PROPAGATED="true"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="SnapshotDataRoot"\
 CLASSORIGIN="Msvm_VirtualSystemGlobalSettingData" PROPAGATED="true"\
 TYPE="string"></PROPERTY><PROPERTY NAME="SystemName"\
 CLASSORIGIN="CIM_VirtualSystemSettingData" PROPAGATED="true"\
 TYPE="string"></PROPERTY><PROPERTY NAME="Version"\
 CLASSORIGIN="Msvm_VirtualSystemGlobalSettingData" PROPAGATED="true"\
 TYPE="string"></PROPERTY><PROPERTY NAME="VirtualSystemType"\
 CLASSORIGIN="CIM_VirtualSystemSettingData" PROPAGATED="true"\
 TYPE="uint16"></PROPERTY></INSTANCE>'
        elif self.__id__ == 65 and iObjectTextFormat == 1:
            return u'<INSTANCE\
 CLASSNAME="Msvm_ResourceAllocationSettingData"><PROPERTY NAME="__PATH"\
 CLASSORIGIN="___SYSTEM" TYPE="string"></PROPERTY><PROPERTY NAME="__NAMESPACE"\
 CLASSORIGIN="___SYSTEM" TYPE="string"></PROPERTY><PROPERTY NAME="__SERVER"\
 CLASSORIGIN="___SYSTEM" TYPE="string"></PROPERTY><PROPERTY.ARRAY\
 NAME="__DERIVATION" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE.ARRAY><VALUE>CIM_ResourceAllocationSettingData</VALUE><V\
ALUE>CIM_SettingData</VALUE><VALUE>CIM_ManagedElement</VALUE></VALUE.ARRAY></P\
ROPERTY.ARRAY><PROPERTY NAME="__PROPERTY_COUNT" CLASSORIGIN="___SYSTEM"\
 TYPE="sint32"><VALUE>22</VALUE></PROPERTY><PROPERTY NAME="__RELPATH"\
 CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>Msvm_ResourceAllocationSettingData.InstanceID="Microsoft\
:Definition\\\\118C3BE5-0D31-4804-85F0-5C6074ABEA8F\\\\Default"</VALUE></PROPE\
RTY><PROPERTY NAME="__DYNASTY" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>CIM_ManagedElement</VALUE></PROPERTY><PROPERTY\
 NAME="__SUPERCLASS" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>CIM_ResourceAllocationSettingData</VALUE></PROPERTY><PRO\
PERTY NAME="__CLASS" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>Msvm_ResourceAllocationSettingData</VALUE></PROPERTY><PR\
OPERTY NAME="__GENUS" CLASSORIGIN="___SYSTEM"\
 TYPE="sint32"><VALUE>2</VALUE></PROPERTY><PROPERTY NAME="Address"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>0</VALUE></PROPERTY><PROPERTY NAME="AllocationUnits"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData" TYPE="string"><VALUE>Hard\
 Drives</VALUE></PROPERTY><PROPERTY NAME="AutomaticAllocation"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY\
 NAME="AutomaticDeallocation" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY NAME="Caption"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>Hard\
 Drive</VALUE></PROPERTY><PROPERTY.ARRAY NAME="Connection"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY.ARRAY><PROPERTY NAME="ConsumerVisibility"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="Description"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>Settings for the\
 Microsoft Virtual Hard Drive.</VALUE></PROPERTY><PROPERTY NAME="ElementName"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>Hard\
 Drive</VALUE></PROPERTY><PROPERTY.ARRAY NAME="HostResource"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY.ARRAY><PROPERTY NAME="InstanceID"\
 CLASSORIGIN="CIM_SettingData"\
 TYPE="string"><VALUE>Microsoft:Definition\\118C3BE5-0D31-4804-85F0-5C6074ABEA\
8F\\Default</VALUE></PROPERTY><PROPERTY NAME="Limit"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="MappingBehavior"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="OtherResourceType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="Parent"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAlloc\
ationSettingData.InstanceID="Microsoft:8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509\
\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\0"</VALUE></PROPERTY><PROPERTY\
 NAME="PoolID" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Microsoft:118C3BE5-0D31-4804-85F0-5C6074ABEA8F\\Root</VA\
LUE></PROPERTY><PROPERTY NAME="Reservation"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="ResourceSubType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Microsoft Synthetic Disk\
 Drive</VALUE></PROPERTY><PROPERTY NAME="ResourceType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"><VALUE>22</VALUE></PROPERTY><PROPERTY NAME="VirtualQuantity"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY.ARRAY\
 NAME="VirtualSystemIdentifiers"\
 CLASSORIGIN="Msvm_ResourceAllocationSettingData"\
 TYPE="string"><VALUE.ARRAY><VALUE>ce14bdf2-3267-4640-9b49-1c52496f49bd</VALUE\
></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>'
        elif self.__id__ == 159 and iObjectTextFormat == 1:
            return u'<INSTANCE\
 CLASSNAME="Msvm_ResourceAllocationSettingData"><PROPERTY NAME="__PATH"\
 CLASSORIGIN="___SYSTEM" TYPE="string"></PROPERTY><PROPERTY NAME="__NAMESPACE"\
 CLASSORIGIN="___SYSTEM" TYPE="string"></PROPERTY><PROPERTY NAME="__SERVER"\
 CLASSORIGIN="___SYSTEM" TYPE="string"></PROPERTY><PROPERTY.ARRAY\
 NAME="__DERIVATION" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE.ARRAY><VALUE>CIM_ResourceAllocationSettingData</VALUE><V\
ALUE>CIM_SettingData</VALUE><VALUE>CIM_ManagedElement</VALUE></VALUE.ARRAY></P\
ROPERTY.ARRAY><PROPERTY NAME="__PROPERTY_COUNT" CLASSORIGIN="___SYSTEM"\
 TYPE="sint32"><VALUE>22</VALUE></PROPERTY><PROPERTY NAME="__RELPATH"\
 CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>Msvm_ResourceAllocationSettingData.InstanceID="Microsoft\
:Definition\\\\70BB60D2-A9D3-46AA-B654-3DE53004B4F8\\\\Default"</VALUE></PROPE\
RTY><PROPERTY NAME="__DYNASTY" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>CIM_ManagedElement</VALUE></PROPERTY><PROPERTY\
 NAME="__SUPERCLASS" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>CIM_ResourceAllocationSettingData</VALUE></PROPERTY><PRO\
PERTY NAME="__CLASS" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>Msvm_ResourceAllocationSettingData</VALUE></PROPERTY><PR\
OPERTY NAME="__GENUS" CLASSORIGIN="___SYSTEM"\
 TYPE="sint32"><VALUE>2</VALUE></PROPERTY><PROPERTY NAME="Address"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="AllocationUnits"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Disks</VALUE></PROPERTY><PROPERTY\
 NAME="AutomaticAllocation" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY\
 NAME="AutomaticDeallocation" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY NAME="Caption"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>Hard Disk\
 Image</VALUE></PROPERTY><PROPERTY.ARRAY NAME="Connection"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE.ARRAY><VALUE>C:\\Hyper-V\\test\\instances\\openstack_uni\
t_test_vm_adeb3f8f-5ca5-4ddf-89d2-7d22d8b0ab7d\\openstack_unit_test_vm_adeb3f8\
f-5ca5-4ddf-89d2-7d22d8b0ab7d.vhd</VALUE></VALUE.ARRAY></PROPERTY.ARRAY><PROPE\
RTY NAME="ConsumerVisibility" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="Description"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>Settings for the\
 Microsoft Hard Disk Image.</VALUE></PROPERTY><PROPERTY NAME="ElementName"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>Hard Disk\
 Image</VALUE></PROPERTY><PROPERTY.ARRAY NAME="HostResource"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY.ARRAY><PROPERTY NAME="InstanceID"\
 CLASSORIGIN="CIM_SettingData"\
 TYPE="string"><VALUE>Microsoft:Definition\\70BB60D2-A9D3-46AA-B654-3DE53004B4\
F8\\Default</VALUE></PROPERTY><PROPERTY NAME="Limit"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="MappingBehavior"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="OtherResourceType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="Parent"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAlloc\
ationSettingData.InstanceID="Microsoft:8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509\
\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\0\\\\0\\\\D"</VALUE></PROPERTY><PR\
OPERTY NAME="PoolID" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Microsoft:70BB60D2-A9D3-46aa-B654-3DE53004B4F8\\Root</VA\
LUE></PROPERTY><PROPERTY NAME="Reservation"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="ResourceSubType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Microsoft Virtual Hard Disk</VALUE></PROPERTY><PROPERTY\
 NAME="ResourceType" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"><VALUE>21</VALUE></PROPERTY><PROPERTY NAME="VirtualQuantity"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY.ARRAY\
 NAME="VirtualSystemIdentifiers"\
 CLASSORIGIN="Msvm_ResourceAllocationSettingData"\
 TYPE="string"><VALUE.ARRAY><VALUE>72097355-50eb-477b-9223-9338802240f7</VALUE\
></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>'
        elif self.__id__ == 254 and iObjectTextFormat == 1:
            return u'<INSTANCE\
 CLASSNAME="Msvm_ResourceAllocationSettingData"><PROPERTY NAME="__PATH"\
 CLASSORIGIN="___SYSTEM" TYPE="string"></PROPERTY><PROPERTY NAME="__NAMESPACE"\
 CLASSORIGIN="___SYSTEM" TYPE="string"></PROPERTY><PROPERTY NAME="__SERVER"\
 CLASSORIGIN="___SYSTEM" TYPE="string"></PROPERTY><PROPERTY.ARRAY\
 NAME="__DERIVATION" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE.ARRAY><VALUE>CIM_ResourceAllocationSettingData</VALUE><V\
ALUE>CIM_SettingData</VALUE><VALUE>CIM_ManagedElement</VALUE></VALUE.ARRAY></P\
ROPERTY.ARRAY><PROPERTY NAME="__PROPERTY_COUNT" CLASSORIGIN="___SYSTEM"\
 TYPE="sint32"><VALUE>22</VALUE></PROPERTY><PROPERTY NAME="__RELPATH"\
 CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>Msvm_ResourceAllocationSettingData.InstanceID="Microsoft\
:Definition\\\\BDE5D4D6-E450-46D2-B925-976CA3E989B4\\\\Default"</VALUE></PROPE\
RTY><PROPERTY NAME="__DYNASTY" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>CIM_ManagedElement</VALUE></PROPERTY><PROPERTY\
 NAME="__SUPERCLASS" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>CIM_ResourceAllocationSettingData</VALUE></PROPERTY><PRO\
PERTY NAME="__CLASS" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>Msvm_ResourceAllocationSettingData</VALUE></PROPERTY><PR\
OPERTY NAME="__GENUS" CLASSORIGIN="___SYSTEM"\
 TYPE="sint32"><VALUE>2</VALUE></PROPERTY><PROPERTY NAME="Address"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="AllocationUnits"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Controllers</VALUE></PROPERTY><PROPERTY\
 NAME="AutomaticAllocation" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY\
 NAME="AutomaticDeallocation" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY NAME="Caption"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>SCSI\
 Controller</VALUE></PROPERTY><PROPERTY.ARRAY NAME="Connection"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY.ARRAY><PROPERTY NAME="ConsumerVisibility"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="Description"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>Settings for the\
 Microsoft Synthetic SCSI Controller.</VALUE></PROPERTY><PROPERTY\
 NAME="ElementName" CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>SCSI\
 Controller</VALUE></PROPERTY><PROPERTY.ARRAY NAME="HostResource"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY.ARRAY><PROPERTY NAME="InstanceID"\
 CLASSORIGIN="CIM_SettingData"\
 TYPE="string"><VALUE>Microsoft:Definition\\BDE5D4D6-E450-46D2-B925-976CA3E989\
B4\\Default</VALUE></PROPERTY><PROPERTY NAME="Limit"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="MappingBehavior"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="OtherResourceType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="Parent"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="PoolID"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Microsoft:bde5d4d6-e450-46d2-b925-976ca3e989b4\\Root</VA\
LUE></PROPERTY><PROPERTY NAME="Reservation"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="ResourceSubType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Microsoft Synthetic SCSI\
 Controller</VALUE></PROPERTY><PROPERTY NAME="ResourceType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"><VALUE>6</VALUE></PROPERTY><PROPERTY NAME="VirtualQuantity"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY.ARRAY\
 NAME="VirtualSystemIdentifiers"\
 CLASSORIGIN="Msvm_ResourceAllocationSettingData"\
 TYPE="string"><VALUE.ARRAY><VALUE>{ffb1c156-7262-4a52-afd4-0dd474eef4a1}</VAL\
UE></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>'


class _wmi_method(object):

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__

    def __call__(self, *args, **kwargs):
        if len(args) == 0 and self.__id__ == 410:
            v = ()
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 0 and self.__id__ == 24 and kwargs.get('Path') ==\
 'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_adeb3f8f-5ca5-4ddf-89d2\
-7d22d8b0ab7d\\openstack_unit_test_vm_adeb3f8f-5ca5-4ddf-89d2-7d22d8b0ab7d.vhd\
' and kwargs.get('ParentPath') == 'C:\\Hyper-V\\test\\instances\\_base\\1.vhd':
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_StorageJob.InstanceID="1DDDE39C-\
EF4D-4685-969C-816C3041DBD8"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v
        elif len(args) == 1 and self.__id__ == 353 and args[0] == 2:
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ConcreteJob.InstanceID="C9854C10\
-5CAF-4FC4-A092-16E0E8E4AED2"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v
        elif len(args) == 1 and self.__id__ == 366 and args[0] == 32768:
            v = ()
            v1 = None
            v += (v1,)
            v1 = 32775
            v += (v1,)
            return v
        elif len(args) == 3 and self.__id__ == 38 and str(args[0]) == '[]' and\
 args[1] is None and args[2] == u'<INSTANCE\
 CLASSNAME="Msvm_VirtualSystemGlobalSettingData"><PROPERTY NAME="__PATH"\
 CLASSORIGIN="___SYSTEM" TYPE="string"></PROPERTY><PROPERTY NAME="__NAMESPACE"\
 CLASSORIGIN="___SYSTEM" TYPE="string"></PROPERTY><PROPERTY NAME="__SERVER"\
 CLASSORIGIN="___SYSTEM" TYPE="string"></PROPERTY><PROPERTY.ARRAY\
 NAME="__DERIVATION" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE.ARRAY><VALUE>CIM_VirtualSystemSettingData</VALUE><VALUE>\
CIM_SettingData</VALUE><VALUE>CIM_ManagedElement</VALUE></VALUE.ARRAY></PROPER\
TY.ARRAY><PROPERTY NAME="__PROPERTY_COUNT" CLASSORIGIN="___SYSTEM"\
 TYPE="sint32"><VALUE>23</VALUE></PROPERTY><PROPERTY NAME="__RELPATH"\
 CLASSORIGIN="___SYSTEM" TYPE="string"></PROPERTY><PROPERTY NAME="__DYNASTY"\
 CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>CIM_ManagedElement</VALUE></PROPERTY><PROPERTY\
 NAME="__SUPERCLASS" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>CIM_VirtualSystemSettingData</VALUE></PROPERTY><PROPERTY\
 NAME="__CLASS" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>Msvm_VirtualSystemGlobalSettingData</VALUE></PROPERTY><P\
ROPERTY NAME="__GENUS" CLASSORIGIN="___SYSTEM"\
 TYPE="sint32"><VALUE>2</VALUE></PROPERTY><PROPERTY\
 NAME="AdditionalRecoveryInformation"\
 CLASSORIGIN="Msvm_VirtualSystemGlobalSettingData" PROPAGATED="true"\
 TYPE="string"></PROPERTY><PROPERTY NAME="AllowFullSCSICommandSet"\
 CLASSORIGIN="Msvm_VirtualSystemGlobalSettingData" PROPAGATED="true"\
 TYPE="boolean"></PROPERTY><PROPERTY NAME="AutoActivate"\
 CLASSORIGIN="CIM_VirtualSystemSettingData" PROPAGATED="true"\
 TYPE="boolean"></PROPERTY><PROPERTY NAME="AutomaticRecoveryAction"\
 CLASSORIGIN="Msvm_VirtualSystemGlobalSettingData" PROPAGATED="true"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="AutomaticShutdownAction"\
 CLASSORIGIN="Msvm_VirtualSystemGlobalSettingData" PROPAGATED="true"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="AutomaticStartupAction"\
 CLASSORIGIN="Msvm_VirtualSystemGlobalSettingData" PROPAGATED="true"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="AutomaticStartupActionDelay"\
 CLASSORIGIN="Msvm_VirtualSystemGlobalSettingData" PROPAGATED="true"\
 TYPE="datetime"><VALUE>00000000000000.000000:000</VALUE></PROPERTY><PROPERTY\
 NAME="Caption" CLASSORIGIN="CIM_ManagedElement" PROPAGATED="true"\
 TYPE="string"></PROPERTY><PROPERTY NAME="CreationTime"\
 CLASSORIGIN="CIM_VirtualSystemSettingData" PROPAGATED="true"\
 TYPE="datetime"></PROPERTY><PROPERTY NAME="DebugChannelId"\
 CLASSORIGIN="Msvm_VirtualSystemGlobalSettingData" PROPAGATED="true"\
 TYPE="uint32"></PROPERTY><PROPERTY NAME="DebugPort"\
 CLASSORIGIN="Msvm_VirtualSystemGlobalSettingData" PROPAGATED="true"\
 TYPE="uint32"></PROPERTY><PROPERTY NAME="DebugPortEnabled"\
 CLASSORIGIN="Msvm_VirtualSystemGlobalSettingData" PROPAGATED="true"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="Description"\
 CLASSORIGIN="CIM_ManagedElement" PROPAGATED="true"\
 TYPE="string"></PROPERTY><PROPERTY NAME="ElementName"\
 CLASSORIGIN="CIM_ManagedElement"\
 TYPE="string"><VALUE>openstack_unit_test_vm_adeb3f8f-5ca5-4ddf-89d2-7d22d8b0a\
b7d</VALUE></PROPERTY><PROPERTY NAME="ExternalDataRoot"\
 CLASSORIGIN="Msvm_VirtualSystemGlobalSettingData" PROPAGATED="true"\
 TYPE="string"></PROPERTY><PROPERTY NAME="InstanceID"\
 CLASSORIGIN="CIM_SettingData" PROPAGATED="true"\
 TYPE="string"></PROPERTY><PROPERTY NAME="OtherVirtualSystemType"\
 CLASSORIGIN="CIM_VirtualSystemSettingData" PROPAGATED="true"\
 TYPE="string"></PROPERTY><PROPERTY NAME="ScopeOfResidence"\
 CLASSORIGIN="Msvm_VirtualSystemGlobalSettingData" PROPAGATED="true"\
 TYPE="string"></PROPERTY><PROPERTY NAME="SettingType"\
 CLASSORIGIN="CIM_VirtualSystemSettingData" PROPAGATED="true"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="SnapshotDataRoot"\
 CLASSORIGIN="Msvm_VirtualSystemGlobalSettingData" PROPAGATED="true"\
 TYPE="string"></PROPERTY><PROPERTY NAME="SystemName"\
 CLASSORIGIN="CIM_VirtualSystemSettingData" PROPAGATED="true"\
 TYPE="string"></PROPERTY><PROPERTY NAME="Version"\
 CLASSORIGIN="Msvm_VirtualSystemGlobalSettingData" PROPAGATED="true"\
 TYPE="string"></PROPERTY><PROPERTY NAME="VirtualSystemType"\
 CLASSORIGIN="CIM_VirtualSystemSettingData" PROPAGATED="true"\
 TYPE="uint16"></PROPERTY></INSTANCE>':
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509"'
            v += (v1,)
            v1 = None
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 2 and self.__id__ == 43 and args[0] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509"' and\
 str(args[1]) == '[u\'<INSTANCE CLASSNAME="Msvm_MemorySettingData"><PROPERTY\
 NAME="__PATH" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>\\\\\\\\HV12OSDEMO1\\\\root\\\\virtualization:Msvm_Memor\
ySettingData.InstanceID="Microsoft:8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509\
\\\\\\\\4764334d-e001-4176-82ee-5594ec9b530e"</VALUE></PROPERTY><PROPERTY\
 NAME="__NAMESPACE" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>root\\\\virtualization</VALUE></PROPERTY><PROPERTY\
 NAME="__SERVER" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>HV12OSDEMO1</VALUE></PROPERTY><PROPERTY.ARRAY\
 NAME="__DERIVATION" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE.ARRAY><VALUE>CIM_ResourceAllocationSettingData</VALUE><V\
ALUE>CIM_SettingData</VALUE><VALUE>CIM_ManagedElement</VALUE></VALUE.ARRAY></P\
ROPERTY.ARRAY><PROPERTY NAME="__PROPERTY_COUNT" CLASSORIGIN="___SYSTEM"\
 TYPE="sint32"><VALUE>26</VALUE></PROPERTY><PROPERTY NAME="__RELPATH"\
 CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>Msvm_MemorySettingData.InstanceID="Microsoft:8FB6FE34-0C\
9B-472F-B0D8-9B7ADA69C509\\\\\\\\4764334d-e001-4176-82ee-5594ec9b530e"</VALUE>\
</PROPERTY><PROPERTY NAME="__DYNASTY" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>CIM_ManagedElement</VALUE></PROPERTY><PROPERTY\
 NAME="__SUPERCLASS" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>CIM_ResourceAllocationSettingData</VALUE></PROPERTY><PRO\
PERTY NAME="__CLASS" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>Msvm_MemorySettingData</VALUE></PROPERTY><PROPERTY\
 NAME="__GENUS" CLASSORIGIN="___SYSTEM"\
 TYPE="sint32"><VALUE>2</VALUE></PROPERTY><PROPERTY NAME="Address"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="AllocationUnits"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>MB</VALUE></PROPERTY><PROPERTY\
 NAME="AutomaticAllocation" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY\
 NAME="AutomaticDeallocation" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY NAME="Caption"\
 CLASSORIGIN="CIM_ManagedElement"\
 TYPE="string"><VALUE>Memory</VALUE></PROPERTY><PROPERTY.ARRAY\
 NAME="Connection" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY.ARRAY><PROPERTY NAME="ConsumerVisibility"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"><VALUE>3</VALUE></PROPERTY><PROPERTY NAME="Description"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>Settings for Microsoft\
 Virtual Machine Memory.</VALUE></PROPERTY><PROPERTY NAME="DeviceID"\
 CLASSORIGIN="Msvm_MemorySettingData" TYPE="string"></PROPERTY><PROPERTY\
 NAME="DeviceIDFormat" CLASSORIGIN="Msvm_MemorySettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="DynamicMemoryEnabled"\
 CLASSORIGIN="Msvm_MemorySettingData"\
 TYPE="boolean"><VALUE>FALSE</VALUE></PROPERTY><PROPERTY NAME="ElementName"\
 CLASSORIGIN="CIM_ManagedElement"\
 TYPE="string"><VALUE>Memory</VALUE></PROPERTY><PROPERTY.ARRAY\
 NAME="HostResource" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY.ARRAY><PROPERTY NAME="InstanceID"\
 CLASSORIGIN="CIM_SettingData"\
 TYPE="string"><VALUE>Microsoft:8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509\\\\476433\
4d-e001-4176-82ee-5594ec9b530e</VALUE></PROPERTY><PROPERTY\
 NAME="IsVirtualized" CLASSORIGIN="Msvm_MemorySettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY NAME="Limit"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>512</VALUE></PROPERTY><PROPERTY NAME="MappingBehavior"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="OtherResourceType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="Parent"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="PoolID"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>15129609-B465-4916-AA13-0CF4B109ADB0</VALUE></PROPERTY><\
PROPERTY NAME="Reservation" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>512</VALUE></PROPERTY><PROPERTY NAME="ResourceSubType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Microsoft Virtual Machine\
 Memory</VALUE></PROPERTY><PROPERTY NAME="ResourceType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"><VALUE>4</VALUE></PROPERTY><PROPERTY NAME="TargetMemoryBuffer"\
 CLASSORIGIN="Msvm_MemorySettingData"\
 TYPE="uint32"><VALUE>20</VALUE></PROPERTY><PROPERTY NAME="VirtualQuantity"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>512</VALUE></PROPERTY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>5000</VALUE></PROPERTY></INSTANCE>\']':
            v = ()
            v1 = None
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 2 and self.__id__ == 46 and args[0] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509"' and\
 str(args[1]) == '[u\'<INSTANCE\
 CLASSNAME="Msvm_ProcessorSettingData"><PROPERTY NAME="__PATH"\
 CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>\\\\\\\\HV12OSDEMO1\\\\root\\\\virtualization:Msvm_Proce\
ssorSettingData.InstanceID="Microsoft:8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509\
\\\\\\\\b637f346-6a0e-4dec-af52-bd70cb80a21d\\\\\\\\0"</VALUE></PROPERTY><PROP\
ERTY NAME="__NAMESPACE" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>root\\\\virtualization</VALUE></PROPERTY><PROPERTY\
 NAME="__SERVER" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>HV12OSDEMO1</VALUE></PROPERTY><PROPERTY.ARRAY\
 NAME="__DERIVATION" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE.ARRAY><VALUE>CIM_ResourceAllocationSettingData</VALUE><V\
ALUE>CIM_SettingData</VALUE><VALUE>CIM_ManagedElement</VALUE></VALUE.ARRAY></P\
ROPERTY.ARRAY><PROPERTY NAME="__PROPERTY_COUNT" CLASSORIGIN="___SYSTEM"\
 TYPE="sint32"><VALUE>29</VALUE></PROPERTY><PROPERTY NAME="__RELPATH"\
 CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>Msvm_ProcessorSettingData.InstanceID="Microsoft:8FB6FE34\
-0C9B-472F-B0D8-9B7ADA69C509\\\\\\\\b637f346-6a0e-4dec-af52-bd70cb80a21d\
\\\\\\\\0"</VALUE></PROPERTY><PROPERTY NAME="__DYNASTY"\
 CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>CIM_ManagedElement</VALUE></PROPERTY><PROPERTY\
 NAME="__SUPERCLASS" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>CIM_ResourceAllocationSettingData</VALUE></PROPERTY><PRO\
PERTY NAME="__CLASS" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>Msvm_ProcessorSettingData</VALUE></PROPERTY><PROPERTY\
 NAME="__GENUS" CLASSORIGIN="___SYSTEM"\
 TYPE="sint32"><VALUE>2</VALUE></PROPERTY><PROPERTY NAME="Address"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="AllocationUnits"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Processor Cores</VALUE></PROPERTY><PROPERTY\
 NAME="AutomaticAllocation" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY\
 NAME="AutomaticDeallocation" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY NAME="Caption"\
 CLASSORIGIN="CIM_ManagedElement"\
 TYPE="string"><VALUE>Processor</VALUE></PROPERTY><PROPERTY.ARRAY\
 NAME="Connection" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY.ARRAY><PROPERTY NAME="ConsumerVisibility"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"><VALUE>3</VALUE></PROPERTY><PROPERTY NAME="Description"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>Settings for Microsoft\
 Virtual Processor.</VALUE></PROPERTY><PROPERTY NAME="DeviceID"\
 CLASSORIGIN="Msvm_ProcessorSettingData" TYPE="string"></PROPERTY><PROPERTY\
 NAME="DeviceIDFormat" CLASSORIGIN="Msvm_ProcessorSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="ElementName"\
 CLASSORIGIN="CIM_ManagedElement"\
 TYPE="string"><VALUE>Processor</VALUE></PROPERTY><PROPERTY.ARRAY\
 NAME="HostResource" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY.ARRAY><PROPERTY NAME="InstanceID"\
 CLASSORIGIN="CIM_SettingData"\
 TYPE="string"><VALUE>Microsoft:8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509\\\\b637f3\
46-6a0e-4dec-af52-bd70cb80a21d\\\\0</VALUE></PROPERTY><PROPERTY\
 NAME="IsVirtualized" CLASSORIGIN="Msvm_ProcessorSettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY NAME="Limit"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>100000</VALUE></PROPERTY><PROPERTY NAME="LimitCPUID"\
 CLASSORIGIN="Msvm_ProcessorSettingData"\
 TYPE="boolean"><VALUE>FALSE</VALUE></PROPERTY><PROPERTY\
 NAME="LimitProcessorFeatures" CLASSORIGIN="Msvm_ProcessorSettingData"\
 TYPE="boolean"><VALUE>FALSE</VALUE></PROPERTY><PROPERTY\
 NAME="MappingBehavior" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="OtherResourceType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="Parent"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="PoolID"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>A4F3C4E4-5E15-4018-A713-96C2CFB4C9B8</VALUE></PROPERTY><\
PROPERTY NAME="ProcessorsPerSocket" CLASSORIGIN="Msvm_ProcessorSettingData"\
 TYPE="uint16"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="Reservation"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="ResourceSubType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Microsoft Processor</VALUE></PROPERTY><PROPERTY\
 NAME="ResourceType" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"><VALUE>3</VALUE></PROPERTY><PROPERTY NAME="SocketCount"\
 CLASSORIGIN="Msvm_ProcessorSettingData"\
 TYPE="uint16"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="ThreadsEnabled"\
 CLASSORIGIN="Msvm_ProcessorSettingData" TYPE="boolean"></PROPERTY><PROPERTY\
 NAME="VirtualQuantity" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>100</VALUE></PROPERTY></INSTANCE>\']':
            v = ()
            v1 = None
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 2 and self.__id__ == 155 and str(args[0]) ==\
 '[u\'<INSTANCE CLASSNAME="Msvm_ResourceAllocationSettingData"><PROPERTY\
 NAME="__PATH" CLASSORIGIN="___SYSTEM" TYPE="string"></PROPERTY><PROPERTY\
 NAME="__NAMESPACE" CLASSORIGIN="___SYSTEM" TYPE="string"></PROPERTY><PROPERTY\
 NAME="__SERVER" CLASSORIGIN="___SYSTEM"\
 TYPE="string"></PROPERTY><PROPERTY.ARRAY NAME="__DERIVATION"\
 CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE.ARRAY><VALUE>CIM_ResourceAllocationSettingData</VALUE><V\
ALUE>CIM_SettingData</VALUE><VALUE>CIM_ManagedElement</VALUE></VALUE.ARRAY></P\
ROPERTY.ARRAY><PROPERTY NAME="__PROPERTY_COUNT" CLASSORIGIN="___SYSTEM"\
 TYPE="sint32"><VALUE>22</VALUE></PROPERTY><PROPERTY NAME="__RELPATH"\
 CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>Msvm_ResourceAllocationSettingData.InstanceID="Microsoft\
:Definition\\\\\\\\118C3BE5-0D31-4804-85F0-5C6074ABEA8F\\\\\\\\Default"</VALUE\
></PROPERTY><PROPERTY NAME="__DYNASTY" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>CIM_ManagedElement</VALUE></PROPERTY><PROPERTY\
 NAME="__SUPERCLASS" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>CIM_ResourceAllocationSettingData</VALUE></PROPERTY><PRO\
PERTY NAME="__CLASS" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>Msvm_ResourceAllocationSettingData</VALUE></PROPERTY><PR\
OPERTY NAME="__GENUS" CLASSORIGIN="___SYSTEM"\
 TYPE="sint32"><VALUE>2</VALUE></PROPERTY><PROPERTY NAME="Address"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>0</VALUE></PROPERTY><PROPERTY NAME="AllocationUnits"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData" TYPE="string"><VALUE>Hard\
 Drives</VALUE></PROPERTY><PROPERTY NAME="AutomaticAllocation"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY\
 NAME="AutomaticDeallocation" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY NAME="Caption"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>Hard\
 Drive</VALUE></PROPERTY><PROPERTY.ARRAY NAME="Connection"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY.ARRAY><PROPERTY NAME="ConsumerVisibility"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="Description"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>Settings for the\
 Microsoft Virtual Hard Drive.</VALUE></PROPERTY><PROPERTY NAME="ElementName"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>Hard\
 Drive</VALUE></PROPERTY><PROPERTY.ARRAY NAME="HostResource"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY.ARRAY><PROPERTY NAME="InstanceID"\
 CLASSORIGIN="CIM_SettingData"\
 TYPE="string"><VALUE>Microsoft:Definition\\\\118C3BE5-0D31-4804-85F0-5C6074AB\
EA8F\\\\Default</VALUE></PROPERTY><PROPERTY NAME="Limit"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="MappingBehavior"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="OtherResourceType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="Parent"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>\\\\\\\\HV12OSDEMO1\\\\root\\\\virtualization:Msvm_Resou\
rceAllocationSettingData.InstanceID="Microsoft:8FB6FE34-0C9B-472F-B0D8-9B7ADA6\
9C509\\\\\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\\\\\0"</VALUE></PROPERTY>\
<PROPERTY NAME="PoolID" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Microsoft:118C3BE5-0D31-4804-85F0-5C6074ABEA8F\\\\Root</\
VALUE></PROPERTY><PROPERTY NAME="Reservation"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="ResourceSubType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Microsoft Synthetic Disk\
 Drive</VALUE></PROPERTY><PROPERTY NAME="ResourceType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"><VALUE>22</VALUE></PROPERTY><PROPERTY NAME="VirtualQuantity"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY.ARRAY\
 NAME="VirtualSystemIdentifiers"\
 CLASSORIGIN="Msvm_ResourceAllocationSettingData"\
 TYPE="string"><VALUE.ARRAY><VALUE>ce14bdf2-3267-4640-9b49-1c52496f49bd</VALUE\
></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509\\\\83F8638B-8DCA-4152\
-9EDA-2CA8B33039B4\\\\0\\\\0\\\\D"'
            v1.append(v2)
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 2 and self.__id__ == 248 and str(args[0]) ==\
 '[u\'<INSTANCE CLASSNAME="Msvm_ResourceAllocationSettingData"><PROPERTY\
 NAME="__PATH" CLASSORIGIN="___SYSTEM" TYPE="string"></PROPERTY><PROPERTY\
 NAME="__NAMESPACE" CLASSORIGIN="___SYSTEM" TYPE="string"></PROPERTY><PROPERTY\
 NAME="__SERVER" CLASSORIGIN="___SYSTEM"\
 TYPE="string"></PROPERTY><PROPERTY.ARRAY NAME="__DERIVATION"\
 CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE.ARRAY><VALUE>CIM_ResourceAllocationSettingData</VALUE><V\
ALUE>CIM_SettingData</VALUE><VALUE>CIM_ManagedElement</VALUE></VALUE.ARRAY></P\
ROPERTY.ARRAY><PROPERTY NAME="__PROPERTY_COUNT" CLASSORIGIN="___SYSTEM"\
 TYPE="sint32"><VALUE>22</VALUE></PROPERTY><PROPERTY NAME="__RELPATH"\
 CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>Msvm_ResourceAllocationSettingData.InstanceID="Microsoft\
:Definition\\\\\\\\70BB60D2-A9D3-46AA-B654-3DE53004B4F8\\\\\\\\Default"</VALUE\
></PROPERTY><PROPERTY NAME="__DYNASTY" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>CIM_ManagedElement</VALUE></PROPERTY><PROPERTY\
 NAME="__SUPERCLASS" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>CIM_ResourceAllocationSettingData</VALUE></PROPERTY><PRO\
PERTY NAME="__CLASS" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>Msvm_ResourceAllocationSettingData</VALUE></PROPERTY><PR\
OPERTY NAME="__GENUS" CLASSORIGIN="___SYSTEM"\
 TYPE="sint32"><VALUE>2</VALUE></PROPERTY><PROPERTY NAME="Address"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="AllocationUnits"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Disks</VALUE></PROPERTY><PROPERTY\
 NAME="AutomaticAllocation" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY\
 NAME="AutomaticDeallocation" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY NAME="Caption"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>Hard Disk\
 Image</VALUE></PROPERTY><PROPERTY.ARRAY NAME="Connection"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE.ARRAY><VALUE>C:\\\\Hyper-V\\\\test\\\\instances\\\\opens\
tack_unit_test_vm_adeb3f8f-5ca5-4ddf-89d2-7d22d8b0ab7d\\\\openstack_unit_test_\
vm_adeb3f8f-5ca5-4ddf-89d2-7d22d8b0ab7d.vhd</VALUE></VALUE.ARRAY></PROPERTY.AR\
RAY><PROPERTY NAME="ConsumerVisibility"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="Description"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>Settings for the\
 Microsoft Hard Disk Image.</VALUE></PROPERTY><PROPERTY NAME="ElementName"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>Hard Disk\
 Image</VALUE></PROPERTY><PROPERTY.ARRAY NAME="HostResource"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY.ARRAY><PROPERTY NAME="InstanceID"\
 CLASSORIGIN="CIM_SettingData"\
 TYPE="string"><VALUE>Microsoft:Definition\\\\70BB60D2-A9D3-46AA-B654-3DE53004\
B4F8\\\\Default</VALUE></PROPERTY><PROPERTY NAME="Limit"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="MappingBehavior"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="OtherResourceType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="Parent"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>\\\\\\\\HV12OSDEMO1\\\\root\\\\virtualization:Msvm_Resou\
rceAllocationSettingData.InstanceID="Microsoft:8FB6FE34-0C9B-472F-B0D8-9B7ADA6\
9C509\\\\\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\\\\\0\\\\\\\\0\\\\\\\\D"<\
/VALUE></PROPERTY><PROPERTY NAME="PoolID"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Microsoft:70BB60D2-A9D3-46aa-B654-3DE53004B4F8\\\\Root</\
VALUE></PROPERTY><PROPERTY NAME="Reservation"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="ResourceSubType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Microsoft Virtual Hard Disk</VALUE></PROPERTY><PROPERTY\
 NAME="ResourceType" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"><VALUE>21</VALUE></PROPERTY><PROPERTY NAME="VirtualQuantity"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY.ARRAY\
 NAME="VirtualSystemIdentifiers"\
 CLASSORIGIN="Msvm_ResourceAllocationSettingData"\
 TYPE="string"><VALUE.ARRAY><VALUE>72097355-50eb-477b-9223-9338802240f7</VALUE\
></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509\\\\83F8638B-8DCA-4152\
-9EDA-2CA8B33039B4\\\\0\\\\0\\\\L"'
            v1.append(v2)
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 2 and self.__id__ == 343 and str(args[0]) ==\
 '[u\'<INSTANCE CLASSNAME="Msvm_ResourceAllocationSettingData"><PROPERTY\
 NAME="__PATH" CLASSORIGIN="___SYSTEM" TYPE="string"></PROPERTY><PROPERTY\
 NAME="__NAMESPACE" CLASSORIGIN="___SYSTEM" TYPE="string"></PROPERTY><PROPERTY\
 NAME="__SERVER" CLASSORIGIN="___SYSTEM"\
 TYPE="string"></PROPERTY><PROPERTY.ARRAY NAME="__DERIVATION"\
 CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE.ARRAY><VALUE>CIM_ResourceAllocationSettingData</VALUE><V\
ALUE>CIM_SettingData</VALUE><VALUE>CIM_ManagedElement</VALUE></VALUE.ARRAY></P\
ROPERTY.ARRAY><PROPERTY NAME="__PROPERTY_COUNT" CLASSORIGIN="___SYSTEM"\
 TYPE="sint32"><VALUE>22</VALUE></PROPERTY><PROPERTY NAME="__RELPATH"\
 CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>Msvm_ResourceAllocationSettingData.InstanceID="Microsoft\
:Definition\\\\\\\\BDE5D4D6-E450-46D2-B925-976CA3E989B4\\\\\\\\Default"</VALUE\
></PROPERTY><PROPERTY NAME="__DYNASTY" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>CIM_ManagedElement</VALUE></PROPERTY><PROPERTY\
 NAME="__SUPERCLASS" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>CIM_ResourceAllocationSettingData</VALUE></PROPERTY><PRO\
PERTY NAME="__CLASS" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>Msvm_ResourceAllocationSettingData</VALUE></PROPERTY><PR\
OPERTY NAME="__GENUS" CLASSORIGIN="___SYSTEM"\
 TYPE="sint32"><VALUE>2</VALUE></PROPERTY><PROPERTY NAME="Address"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="AllocationUnits"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Controllers</VALUE></PROPERTY><PROPERTY\
 NAME="AutomaticAllocation" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY\
 NAME="AutomaticDeallocation" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY NAME="Caption"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>SCSI\
 Controller</VALUE></PROPERTY><PROPERTY.ARRAY NAME="Connection"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY.ARRAY><PROPERTY NAME="ConsumerVisibility"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="Description"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>Settings for the\
 Microsoft Synthetic SCSI Controller.</VALUE></PROPERTY><PROPERTY\
 NAME="ElementName" CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>SCSI\
 Controller</VALUE></PROPERTY><PROPERTY.ARRAY NAME="HostResource"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY.ARRAY><PROPERTY NAME="InstanceID"\
 CLASSORIGIN="CIM_SettingData"\
 TYPE="string"><VALUE>Microsoft:Definition\\\\BDE5D4D6-E450-46D2-B925-976CA3E9\
89B4\\\\Default</VALUE></PROPERTY><PROPERTY NAME="Limit"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="MappingBehavior"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="OtherResourceType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="Parent"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="PoolID"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Microsoft:bde5d4d6-e450-46d2-b925-976ca3e989b4\\\\Root</\
VALUE></PROPERTY><PROPERTY NAME="Reservation"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="ResourceSubType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Microsoft Synthetic SCSI\
 Controller</VALUE></PROPERTY><PROPERTY NAME="ResourceType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"><VALUE>6</VALUE></PROPERTY><PROPERTY NAME="VirtualQuantity"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY.ARRAY\
 NAME="VirtualSystemIdentifiers"\
 CLASSORIGIN="Msvm_ResourceAllocationSettingData"\
 TYPE="string"><VALUE.ARRAY><VALUE>{ffb1c156-7262-4a52-afd4-0dd474eef4a1}</VAL\
UE></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509\\\\EE75A390-5D20-4F5F\
-9584-8D275F2D8998\\\\0"'
            v1.append(v2)
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 2 and self.__id__ == 349 and str(args[0]) ==\
 '[u\'<INSTANCE CLASSNAME="Msvm_SyntheticEthernetPortSettingData"><PROPERTY\
 NAME="__PATH" CLASSORIGIN="___SYSTEM" TYPE="string"></PROPERTY><PROPERTY\
 NAME="__NAMESPACE" CLASSORIGIN="___SYSTEM" TYPE="string"></PROPERTY><PROPERTY\
 NAME="__SERVER" CLASSORIGIN="___SYSTEM"\
 TYPE="string"></PROPERTY><PROPERTY.ARRAY NAME="__DERIVATION"\
 CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE.ARRAY><VALUE>CIM_ResourceAllocationSettingData</VALUE><V\
ALUE>CIM_SettingData</VALUE><VALUE>CIM_ManagedElement</VALUE></VALUE.ARRAY></P\
ROPERTY.ARRAY><PROPERTY NAME="__PROPERTY_COUNT" CLASSORIGIN="___SYSTEM"\
 TYPE="sint32"><VALUE>23</VALUE></PROPERTY><PROPERTY NAME="__RELPATH"\
 CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>Msvm_SyntheticEthernetPortSettingData.InstanceID="Micros\
oft:Definition\\\\\\\\6A45335D-4C3A-44B7-B61F-C9808BBDF8ED\\\\\\\\Default"</VA\
LUE></PROPERTY><PROPERTY NAME="__DYNASTY" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>CIM_ManagedElement</VALUE></PROPERTY><PROPERTY\
 NAME="__SUPERCLASS" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>CIM_ResourceAllocationSettingData</VALUE></PROPERTY><PRO\
PERTY NAME="__CLASS" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>Msvm_SyntheticEthernetPortSettingData</VALUE></PROPERTY>\
<PROPERTY NAME="__GENUS" CLASSORIGIN="___SYSTEM"\
 TYPE="sint32"><VALUE>2</VALUE></PROPERTY><PROPERTY NAME="Address"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>DEADBEEF0001</VALUE></PROPERTY><PROPERTY\
 NAME="AllocationUnits" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Ports</VALUE></PROPERTY><PROPERTY\
 NAME="AutomaticAllocation" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY\
 NAME="AutomaticDeallocation" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY NAME="Caption"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>Ethernet\
 Port</VALUE></PROPERTY><PROPERTY.ARRAY NAME="Connection"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY.ARRAY><PROPERTY NAME="ConsumerVisibility"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="Description"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>Settings for the\
 Microsoft Synthetic Ethernet Port.</VALUE></PROPERTY><PROPERTY\
 NAME="ElementName" CLASSORIGIN="CIM_ManagedElement"\
 TYPE="string"><VALUE>00000000-0000-0000-0000-0000000000000001</VALUE></PROPER\
TY><PROPERTY.ARRAY NAME="HostResource"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY.ARRAY><PROPERTY NAME="InstanceID"\
 CLASSORIGIN="CIM_SettingData"\
 TYPE="string"><VALUE>Microsoft:Definition\\\\6A45335D-4C3A-44B7-B61F-C9808BBD\
F8ED\\\\Default</VALUE></PROPERTY><PROPERTY NAME="Limit"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="MappingBehavior"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="OtherResourceType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="Parent"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="PoolID"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Microsoft:6A45335D-4C3A-44b7-B61F-C9808BBDF8ED\\\\Root</\
VALUE></PROPERTY><PROPERTY NAME="Reservation"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="ResourceSubType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Microsoft Synthetic Ethernet\
 Port</VALUE></PROPERTY><PROPERTY NAME="ResourceType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"><VALUE>10</VALUE></PROPERTY><PROPERTY NAME="StaticMacAddress"\
 CLASSORIGIN="Msvm_SyntheticEthernetPortSettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY NAME="VirtualQuantity"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY.ARRAY\
 NAME="VirtualSystemIdentifiers"\
 CLASSORIGIN="Msvm_SyntheticEthernetPortSettingData"\
 TYPE="string"><VALUE.ARRAY><VALUE>{d9f81bf8-a6d3-46de-8061-eac59e9813c8}</VAL\
UE></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_SyntheticEthernetPortSettingData\
.InstanceID="Microsoft:8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509\\\\40DDBB1A-FF21-4\
09C-9B49-B913CB575BE3"'
            v1.append(v2)
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 0 and self.__id__ == 13 and\
 kwargs.get('MaxInternalSize') == 3145728 and kwargs.get('Path') ==\
 'C:\\Hyper-V\\test\\instances\\_base\\1.vhd':
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_StorageJob.InstanceID="BF07D796-\
9509-44B9-A313-A2475E14FB7B"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v
        elif len(args) == 1 and self.__id__ == 362 and args[0] == 32768:
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ConcreteJob.InstanceID="723BEA5D\
-9C04-456C-89E0-99319978D542"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v
        elif len(args) == 1 and self.__id__ == 384 and args[0] == 3:
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ConcreteJob.InstanceID="20EA8ADB\
-5855-40A9-AE19-5AC8CDB36EEA"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v
        elif len(args) == 2 and self.__id__ == 373 and str(args[0]) == '[100,\
 105]' and str(args[1]) ==\
 '[u\'\\\\\\\\HV12OSDEMO1\\\\root\\\\virtualization:Msvm_VirtualSystemSettingD\
ata.InstanceID="Microsoft:8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509"\']':
            v = ()
            v1 = 0
            v += (v1,)
            v1 = []
            v2 = CDispatch()
            v2.__instance_id__ = 374
            v1.append(v2)
            v += (v1,)
            return v
        elif len(args) == 1 and self.__id__ == 405 and args[0] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509"':
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ConcreteJob.InstanceID="68D376C0\
-66A7-4C85-86BC-A51A1EA7FDBB"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v


class CDispatch(object):

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__

    @property
    def EnabledState(self):
        if self.__id__ == 374:
            return 32768

    @EnabledState.setter
    def EnabledState(self, value):
        pass

    @property
    def Value(self):
        if self.__id__ == 67:
            return\
 u'Microsoft:Definition\\118C3BE5-0D31-4804-85F0-5C6074ABEA8F\\Default'
        elif self.__id__ == 71:
            return u'Microsoft Synthetic Disk Drive'
        elif self.__id__ == 75:
            return None
        elif self.__id__ == 79:
            return u'Hard Drive'
        elif self.__id__ == 83:
            return u'Settings for the Microsoft Virtual Hard Drive.'
        elif self.__id__ == 87:
            return None
        elif self.__id__ == 91:
            return u'1'
        elif self.__id__ == 95:
            return True
        elif self.__id__ == 99:
            return True
        elif self.__id__ == 103:
            return u'Microsoft:118C3BE5-0D31-4804-85F0-5C6074ABEA8F\\Root'
        elif self.__id__ == 107:
            return u'1'
        elif self.__id__ == 111:
            return u'Hard Drives'
        elif self.__id__ == 115:
            return None
        elif self.__id__ == 119:
            return None
        elif self.__id__ == 123:
            return None
        elif self.__id__ == 127:
            return u'Hard Drive'
        elif self.__id__ == 131:
            return None
        elif self.__id__ == 135:
            return u'1'
        elif self.__id__ == 139:
            return 22
        elif self.__id__ == 143:
            return 0
        elif self.__id__ == 149:
            return None
        elif self.__id__ == 161:
            return\
 u'Microsoft:Definition\\70BB60D2-A9D3-46AA-B654-3DE53004B4F8\\Default'
        elif self.__id__ == 165:
            return u'Microsoft Virtual Hard Disk'
        elif self.__id__ == 169:
            return None
        elif self.__id__ == 173:
            return u'Hard Disk Image'
        elif self.__id__ == 177:
            return u'Settings for the Microsoft Hard Disk Image.'
        elif self.__id__ == 181:
            return None
        elif self.__id__ == 185:
            return u'1'
        elif self.__id__ == 189:
            return True
        elif self.__id__ == 193:
            return True
        elif self.__id__ == 197:
            return u'Microsoft:70BB60D2-A9D3-46aa-B654-3DE53004B4F8\\Root'
        elif self.__id__ == 201:
            return u'1'
        elif self.__id__ == 205:
            return u'Disks'
        elif self.__id__ == 209:
            return None
        elif self.__id__ == 213:
            return None
        elif self.__id__ == 217:
            return None
        elif self.__id__ == 221:
            return u'Hard Disk Image'
        elif self.__id__ == 225:
            return None
        elif self.__id__ == 229:
            return u'1'
        elif self.__id__ == 233:
            return 21
        elif self.__id__ == 237:
            return 0
        elif self.__id__ == 243:
            return None
        elif self.__id__ == 256:
            return\
 u'Microsoft:Definition\\BDE5D4D6-E450-46D2-B925-976CA3E989B4\\Default'
        elif self.__id__ == 260:
            return u'Microsoft Synthetic SCSI Controller'
        elif self.__id__ == 264:
            return None
        elif self.__id__ == 268:
            return u'SCSI Controller'
        elif self.__id__ == 272:
            return u'Settings for the Microsoft Synthetic SCSI Controller.'
        elif self.__id__ == 276:
            return None
        elif self.__id__ == 280:
            return u'1'
        elif self.__id__ == 284:
            return True
        elif self.__id__ == 288:
            return True
        elif self.__id__ == 292:
            return u'Microsoft:bde5d4d6-e450-46d2-b925-976ca3e989b4\\Root'
        elif self.__id__ == 296:
            return u'1'
        elif self.__id__ == 300:
            return u'Controllers'
        elif self.__id__ == 304:
            return None
        elif self.__id__ == 308:
            return None
        elif self.__id__ == 312:
            return None
        elif self.__id__ == 316:
            return u'SCSI Controller'
        elif self.__id__ == 320:
            return None
        elif self.__id__ == 324:
            return u'1'
        elif self.__id__ == 328:
            return 6
        elif self.__id__ == 332:
            return 0
        elif self.__id__ == 338:
            return None

    @Value.setter
    def Value(self, value):
        pass

    def __call__(self, *args):
        if len(args) == 0 and self.__id__ == 152:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509\\\\83F8638B-8DCA-4152\
-9EDA-2CA8B33039B4\\\\0"'
        elif len(args) == 0 and self.__id__ == 156:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509"'
        elif len(args) == 0 and self.__id__ == 249:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509"'
        elif len(args) == 0 and self.__id__ == 344:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509"'
        elif len(args) == 0 and self.__id__ == 44:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509"'
        elif len(args) == 0 and self.__id__ == 47:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509"'
        elif len(args) == 0 and self.__id__ == 350:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509"'
        elif len(args) == 0 and self.__id__ == 372:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_VirtualSystemSettingData.Instanc\
eID="Microsoft:8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509"'
        elif len(args) == 0 and self.__id__ == 406:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="8FB6FE34-0C9B-472F-B0D8-9B7ADA69C509"'

    def Item(self, strName='<PyOleMissing object at 0x04091890>', iFlags=0):
        if self.__id__ == 66 and strName == u'InstanceID':
            v = CDispatch()
            v.__instance_id__ = 67
            return v
        elif self.__id__ == 70 and strName == u'ResourceSubType':
            v = CDispatch()
            v.__instance_id__ = 71
            return v
        elif self.__id__ == 74 and strName == u'HostResource':
            v = CDispatch()
            v.__instance_id__ = 75
            return v
        elif self.__id__ == 78 and strName == u'ElementName':
            v = CDispatch()
            v.__instance_id__ = 79
            return v
        elif self.__id__ == 82 and strName == u'Description':
            v = CDispatch()
            v.__instance_id__ = 83
            return v
        elif self.__id__ == 86 and strName == u'Parent':
            v = CDispatch()
            v.__instance_id__ = 87
            return v
        elif self.__id__ == 90 and strName == u'VirtualQuantity':
            v = CDispatch()
            v.__instance_id__ = 91
            return v
        elif self.__id__ == 94 and strName == u'AutomaticDeallocation':
            v = CDispatch()
            v.__instance_id__ = 95
            return v
        elif self.__id__ == 98 and strName == u'AutomaticAllocation':
            v = CDispatch()
            v.__instance_id__ = 99
            return v
        elif self.__id__ == 102 and strName == u'PoolID':
            v = CDispatch()
            v.__instance_id__ = 103
            return v
        elif self.__id__ == 106 and strName == u'Reservation':
            v = CDispatch()
            v.__instance_id__ = 107
            return v
        elif self.__id__ == 110 and strName == u'AllocationUnits':
            v = CDispatch()
            v.__instance_id__ = 111
            return v
        elif self.__id__ == 114 and strName == u'MappingBehavior':
            v = CDispatch()
            v.__instance_id__ = 115
            return v
        elif self.__id__ == 118 and strName == u'Address':
            v = CDispatch()
            v.__instance_id__ = 119
            return v
        elif self.__id__ == 122 and strName == u'OtherResourceType':
            v = CDispatch()
            v.__instance_id__ = 123
            return v
        elif self.__id__ == 126 and strName == u'Caption':
            v = CDispatch()
            v.__instance_id__ = 127
            return v
        elif self.__id__ == 130 and strName == u'ConsumerVisibility':
            v = CDispatch()
            v.__instance_id__ = 131
            return v
        elif self.__id__ == 134 and strName == u'Limit':
            v = CDispatch()
            v.__instance_id__ = 135
            return v
        elif self.__id__ == 138 and strName == u'ResourceType':
            v = CDispatch()
            v.__instance_id__ = 139
            return v
        elif self.__id__ == 142 and strName == u'Weight':
            v = CDispatch()
            v.__instance_id__ = 143
            return v
        elif self.__id__ == 148 and strName == u'Connection':
            v = CDispatch()
            v.__instance_id__ = 149
            return v
        elif self.__id__ == 160 and strName == u'InstanceID':
            v = CDispatch()
            v.__instance_id__ = 161
            return v
        elif self.__id__ == 164 and strName == u'ResourceSubType':
            v = CDispatch()
            v.__instance_id__ = 165
            return v
        elif self.__id__ == 168 and strName == u'HostResource':
            v = CDispatch()
            v.__instance_id__ = 169
            return v
        elif self.__id__ == 172 and strName == u'ElementName':
            v = CDispatch()
            v.__instance_id__ = 173
            return v
        elif self.__id__ == 176 and strName == u'Description':
            v = CDispatch()
            v.__instance_id__ = 177
            return v
        elif self.__id__ == 180 and strName == u'Parent':
            v = CDispatch()
            v.__instance_id__ = 181
            return v
        elif self.__id__ == 184 and strName == u'VirtualQuantity':
            v = CDispatch()
            v.__instance_id__ = 185
            return v
        elif self.__id__ == 188 and strName == u'AutomaticDeallocation':
            v = CDispatch()
            v.__instance_id__ = 189
            return v
        elif self.__id__ == 192 and strName == u'AutomaticAllocation':
            v = CDispatch()
            v.__instance_id__ = 193
            return v
        elif self.__id__ == 196 and strName == u'PoolID':
            v = CDispatch()
            v.__instance_id__ = 197
            return v
        elif self.__id__ == 200 and strName == u'Reservation':
            v = CDispatch()
            v.__instance_id__ = 201
            return v
        elif self.__id__ == 204 and strName == u'AllocationUnits':
            v = CDispatch()
            v.__instance_id__ = 205
            return v
        elif self.__id__ == 208 and strName == u'MappingBehavior':
            v = CDispatch()
            v.__instance_id__ = 209
            return v
        elif self.__id__ == 212 and strName == u'Address':
            v = CDispatch()
            v.__instance_id__ = 213
            return v
        elif self.__id__ == 216 and strName == u'OtherResourceType':
            v = CDispatch()
            v.__instance_id__ = 217
            return v
        elif self.__id__ == 220 and strName == u'Caption':
            v = CDispatch()
            v.__instance_id__ = 221
            return v
        elif self.__id__ == 224 and strName == u'ConsumerVisibility':
            v = CDispatch()
            v.__instance_id__ = 225
            return v
        elif self.__id__ == 228 and strName == u'Limit':
            v = CDispatch()
            v.__instance_id__ = 229
            return v
        elif self.__id__ == 232 and strName == u'ResourceType':
            v = CDispatch()
            v.__instance_id__ = 233
            return v
        elif self.__id__ == 236 and strName == u'Weight':
            v = CDispatch()
            v.__instance_id__ = 237
            return v
        elif self.__id__ == 242 and strName == u'Connection':
            v = CDispatch()
            v.__instance_id__ = 243
            return v
        elif self.__id__ == 255 and strName == u'InstanceID':
            v = CDispatch()
            v.__instance_id__ = 256
            return v
        elif self.__id__ == 259 and strName == u'ResourceSubType':
            v = CDispatch()
            v.__instance_id__ = 260
            return v
        elif self.__id__ == 263 and strName == u'HostResource':
            v = CDispatch()
            v.__instance_id__ = 264
            return v
        elif self.__id__ == 267 and strName == u'ElementName':
            v = CDispatch()
            v.__instance_id__ = 268
            return v
        elif self.__id__ == 271 and strName == u'Description':
            v = CDispatch()
            v.__instance_id__ = 272
            return v
        elif self.__id__ == 275 and strName == u'Parent':
            v = CDispatch()
            v.__instance_id__ = 276
            return v
        elif self.__id__ == 279 and strName == u'VirtualQuantity':
            v = CDispatch()
            v.__instance_id__ = 280
            return v
        elif self.__id__ == 283 and strName == u'AutomaticDeallocation':
            v = CDispatch()
            v.__instance_id__ = 284
            return v
        elif self.__id__ == 287 and strName == u'AutomaticAllocation':
            v = CDispatch()
            v.__instance_id__ = 288
            return v
        elif self.__id__ == 291 and strName == u'PoolID':
            v = CDispatch()
            v.__instance_id__ = 292
            return v
        elif self.__id__ == 295 and strName == u'Reservation':
            v = CDispatch()
            v.__instance_id__ = 296
            return v
        elif self.__id__ == 299 and strName == u'AllocationUnits':
            v = CDispatch()
            v.__instance_id__ = 300
            return v
        elif self.__id__ == 303 and strName == u'MappingBehavior':
            v = CDispatch()
            v.__instance_id__ = 304
            return v
        elif self.__id__ == 307 and strName == u'Address':
            v = CDispatch()
            v.__instance_id__ = 308
            return v
        elif self.__id__ == 311 and strName == u'OtherResourceType':
            v = CDispatch()
            v.__instance_id__ = 312
            return v
        elif self.__id__ == 315 and strName == u'Caption':
            v = CDispatch()
            v.__instance_id__ = 316
            return v
        elif self.__id__ == 319 and strName == u'ConsumerVisibility':
            v = CDispatch()
            v.__instance_id__ = 320
            return v
        elif self.__id__ == 323 and strName == u'Limit':
            v = CDispatch()
            v.__instance_id__ = 324
            return v
        elif self.__id__ == 327 and strName == u'ResourceType':
            v = CDispatch()
            v.__instance_id__ = 328
            return v
        elif self.__id__ == 331 and strName == u'Weight':
            v = CDispatch()
            v.__instance_id__ = 332
            return v
        elif self.__id__ == 337 and strName == u'Connection':
            v = CDispatch()
            v.__instance_id__ = 338
            return v
        elif self.__id__ == 68 and strName == u'InstanceID':
            v = CDispatch()
            v.__instance_id__ = 69
            return v
        elif self.__id__ == 72 and strName == u'ResourceSubType':
            v = CDispatch()
            v.__instance_id__ = 73
            return v
        elif self.__id__ == 76 and strName == u'HostResource':
            v = CDispatch()
            v.__instance_id__ = 77
            return v
        elif self.__id__ == 80 and strName == u'ElementName':
            v = CDispatch()
            v.__instance_id__ = 81
            return v
        elif self.__id__ == 84 and strName == u'Description':
            v = CDispatch()
            v.__instance_id__ = 85
            return v
        elif self.__id__ == 88 and strName == u'Parent':
            v = CDispatch()
            v.__instance_id__ = 89
            return v
        elif self.__id__ == 92 and strName == u'VirtualQuantity':
            v = CDispatch()
            v.__instance_id__ = 93
            return v
        elif self.__id__ == 96 and strName == u'AutomaticDeallocation':
            v = CDispatch()
            v.__instance_id__ = 97
            return v
        elif self.__id__ == 100 and strName == u'AutomaticAllocation':
            v = CDispatch()
            v.__instance_id__ = 101
            return v
        elif self.__id__ == 104 and strName == u'PoolID':
            v = CDispatch()
            v.__instance_id__ = 105
            return v
        elif self.__id__ == 108 and strName == u'Reservation':
            v = CDispatch()
            v.__instance_id__ = 109
            return v
        elif self.__id__ == 112 and strName == u'AllocationUnits':
            v = CDispatch()
            v.__instance_id__ = 113
            return v
        elif self.__id__ == 116 and strName == u'MappingBehavior':
            v = CDispatch()
            v.__instance_id__ = 117
            return v
        elif self.__id__ == 120 and strName == u'Address':
            v = CDispatch()
            v.__instance_id__ = 121
            return v
        elif self.__id__ == 124 and strName == u'OtherResourceType':
            v = CDispatch()
            v.__instance_id__ = 125
            return v
        elif self.__id__ == 128 and strName == u'Caption':
            v = CDispatch()
            v.__instance_id__ = 129
            return v
        elif self.__id__ == 132 and strName == u'ConsumerVisibility':
            v = CDispatch()
            v.__instance_id__ = 133
            return v
        elif self.__id__ == 136 and strName == u'Limit':
            v = CDispatch()
            v.__instance_id__ = 137
            return v
        elif self.__id__ == 140 and strName == u'ResourceType':
            v = CDispatch()
            v.__instance_id__ = 141
            return v
        elif self.__id__ == 144 and strName == u'Weight':
            v = CDispatch()
            v.__instance_id__ = 145
            return v
        elif self.__id__ == 146 and strName == u'VirtualSystemIdentifiers':
            v = CDispatch()
            v.__instance_id__ = 147
            return v
        elif self.__id__ == 150 and strName == u'Connection':
            v = CDispatch()
            v.__instance_id__ = 151
            return v
        elif self.__id__ == 162 and strName == u'InstanceID':
            v = CDispatch()
            v.__instance_id__ = 163
            return v
        elif self.__id__ == 166 and strName == u'ResourceSubType':
            v = CDispatch()
            v.__instance_id__ = 167
            return v
        elif self.__id__ == 170 and strName == u'HostResource':
            v = CDispatch()
            v.__instance_id__ = 171
            return v
        elif self.__id__ == 174 and strName == u'ElementName':
            v = CDispatch()
            v.__instance_id__ = 175
            return v
        elif self.__id__ == 178 and strName == u'Description':
            v = CDispatch()
            v.__instance_id__ = 179
            return v
        elif self.__id__ == 182 and strName == u'Parent':
            v = CDispatch()
            v.__instance_id__ = 183
            return v
        elif self.__id__ == 186 and strName == u'VirtualQuantity':
            v = CDispatch()
            v.__instance_id__ = 187
            return v
        elif self.__id__ == 190 and strName == u'AutomaticDeallocation':
            v = CDispatch()
            v.__instance_id__ = 191
            return v
        elif self.__id__ == 194 and strName == u'AutomaticAllocation':
            v = CDispatch()
            v.__instance_id__ = 195
            return v
        elif self.__id__ == 198 and strName == u'PoolID':
            v = CDispatch()
            v.__instance_id__ = 199
            return v
        elif self.__id__ == 202 and strName == u'Reservation':
            v = CDispatch()
            v.__instance_id__ = 203
            return v
        elif self.__id__ == 206 and strName == u'AllocationUnits':
            v = CDispatch()
            v.__instance_id__ = 207
            return v
        elif self.__id__ == 210 and strName == u'MappingBehavior':
            v = CDispatch()
            v.__instance_id__ = 211
            return v
        elif self.__id__ == 214 and strName == u'Address':
            v = CDispatch()
            v.__instance_id__ = 215
            return v
        elif self.__id__ == 218 and strName == u'OtherResourceType':
            v = CDispatch()
            v.__instance_id__ = 219
            return v
        elif self.__id__ == 222 and strName == u'Caption':
            v = CDispatch()
            v.__instance_id__ = 223
            return v
        elif self.__id__ == 226 and strName == u'ConsumerVisibility':
            v = CDispatch()
            v.__instance_id__ = 227
            return v
        elif self.__id__ == 230 and strName == u'Limit':
            v = CDispatch()
            v.__instance_id__ = 231
            return v
        elif self.__id__ == 234 and strName == u'ResourceType':
            v = CDispatch()
            v.__instance_id__ = 235
            return v
        elif self.__id__ == 238 and strName == u'Weight':
            v = CDispatch()
            v.__instance_id__ = 239
            return v
        elif self.__id__ == 240 and strName == u'VirtualSystemIdentifiers':
            v = CDispatch()
            v.__instance_id__ = 241
            return v
        elif self.__id__ == 244 and strName == u'Connection':
            v = CDispatch()
            v.__instance_id__ = 245
            return v
        elif self.__id__ == 257 and strName == u'InstanceID':
            v = CDispatch()
            v.__instance_id__ = 258
            return v
        elif self.__id__ == 261 and strName == u'ResourceSubType':
            v = CDispatch()
            v.__instance_id__ = 262
            return v
        elif self.__id__ == 265 and strName == u'HostResource':
            v = CDispatch()
            v.__instance_id__ = 266
            return v
        elif self.__id__ == 269 and strName == u'ElementName':
            v = CDispatch()
            v.__instance_id__ = 270
            return v
        elif self.__id__ == 273 and strName == u'Description':
            v = CDispatch()
            v.__instance_id__ = 274
            return v
        elif self.__id__ == 277 and strName == u'Parent':
            v = CDispatch()
            v.__instance_id__ = 278
            return v
        elif self.__id__ == 281 and strName == u'VirtualQuantity':
            v = CDispatch()
            v.__instance_id__ = 282
            return v
        elif self.__id__ == 285 and strName == u'AutomaticDeallocation':
            v = CDispatch()
            v.__instance_id__ = 286
            return v
        elif self.__id__ == 289 and strName == u'AutomaticAllocation':
            v = CDispatch()
            v.__instance_id__ = 290
            return v
        elif self.__id__ == 293 and strName == u'PoolID':
            v = CDispatch()
            v.__instance_id__ = 294
            return v
        elif self.__id__ == 297 and strName == u'Reservation':
            v = CDispatch()
            v.__instance_id__ = 298
            return v
        elif self.__id__ == 301 and strName == u'AllocationUnits':
            v = CDispatch()
            v.__instance_id__ = 302
            return v
        elif self.__id__ == 305 and strName == u'MappingBehavior':
            v = CDispatch()
            v.__instance_id__ = 306
            return v
        elif self.__id__ == 309 and strName == u'Address':
            v = CDispatch()
            v.__instance_id__ = 310
            return v
        elif self.__id__ == 313 and strName == u'OtherResourceType':
            v = CDispatch()
            v.__instance_id__ = 314
            return v
        elif self.__id__ == 317 and strName == u'Caption':
            v = CDispatch()
            v.__instance_id__ = 318
            return v
        elif self.__id__ == 321 and strName == u'ConsumerVisibility':
            v = CDispatch()
            v.__instance_id__ = 322
            return v
        elif self.__id__ == 325 and strName == u'Limit':
            v = CDispatch()
            v.__instance_id__ = 326
            return v
        elif self.__id__ == 329 and strName == u'ResourceType':
            v = CDispatch()
            v.__instance_id__ = 330
            return v
        elif self.__id__ == 333 and strName == u'Weight':
            v = CDispatch()
            v.__instance_id__ = 334
            return v
        elif self.__id__ == 335 and strName == u'VirtualSystemIdentifiers':
            v = CDispatch()
            v.__instance_id__ = 336
            return v
        elif self.__id__ == 339 and strName == u'Connection':
            v = CDispatch()
            v.__instance_id__ = 340
            return v
