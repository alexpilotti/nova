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
            v.__instance_id__ = 410
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
 u'//HV12OSDEMO1/root/virtualization:Msvm_StorageJob.InstanceID="B3684A6A-1997\
-48F3-9343-990F42F6AB1A"':
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
        elif _WMI_count_4 == 9:
            v = _wmi_object()
            v.__instance_id__ = 23
        _WMI_count_4 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_StorageJob.InstanceID="20B4D538-1D7C\
-4492-B5AD-F5528ABFB259"':
        ret_value = None
        global _WMI_count_5
        if not '_WMI_count_5' in globals():
            _WMI_count_5 = 0
        if _WMI_count_5 == 0:
            v = _wmi_object()
            v.__instance_id__ = 26
        elif _WMI_count_5 == 1:
            v = _wmi_object()
            v.__instance_id__ = 27
        elif _WMI_count_5 == 2:
            v = _wmi_object()
            v.__instance_id__ = 28
        elif _WMI_count_5 == 3:
            v = _wmi_object()
            v.__instance_id__ = 29
        elif _WMI_count_5 == 4:
            v = _wmi_object()
            v.__instance_id__ = 30
        elif _WMI_count_5 == 5:
            v = _wmi_object()
            v.__instance_id__ = 31
        elif _WMI_count_5 == 6:
            v = _wmi_object()
            v.__instance_id__ = 32
        elif _WMI_count_5 == 7:
            v = _wmi_object()
            v.__instance_id__ = 33
        elif _WMI_count_5 == 8:
            v = _wmi_object()
            v.__instance_id__ = 34
        _WMI_count_5 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_ConcreteJob.InstanceID="6D6997C2-CDE\
8-4B89-B3B3-03AA449B4A44"':
        ret_value = None
        global _WMI_count_6
        if not '_WMI_count_6' in globals():
            _WMI_count_6 = 0
        if _WMI_count_6 == 0:
            v = _wmi_object()
            v.__instance_id__ = 355
        elif _WMI_count_6 == 1:
            v = _wmi_object()
            v.__instance_id__ = 356
        elif _WMI_count_6 == 2:
            v = _wmi_object()
            v.__instance_id__ = 357
        elif _WMI_count_6 == 3:
            v = _wmi_object()
            v.__instance_id__ = 358
        elif _WMI_count_6 == 4:
            v = _wmi_object()
            v.__instance_id__ = 359
        elif _WMI_count_6 == 5:
            v = _wmi_object()
            v.__instance_id__ = 360
        _WMI_count_6 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_ConcreteJob.InstanceID="7031691B-392\
0-484A-BE6F-7CFEFBA81D55"':
        ret_value = None
        global _WMI_count_7
        if not '_WMI_count_7' in globals():
            _WMI_count_7 = 0
        if _WMI_count_7 == 0:
            v = _wmi_object()
            v.__instance_id__ = 388
        elif _WMI_count_7 == 1:
            v = _wmi_object()
            v.__instance_id__ = 389
        _WMI_count_7 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_ConcreteJob.InstanceID="3D372AC2-FB9\
7-43BF-B478-3D63C651D412"':
        ret_value = None
        global _WMI_count_8
        if not '_WMI_count_8' in globals():
            _WMI_count_8 = 0
        if _WMI_count_8 == 0:
            v = _wmi_object()
            v.__instance_id__ = 408
        elif _WMI_count_8 == 1:
            v = _wmi_object()
            v.__instance_id__ = 409
        _WMI_count_8 += 1
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
                v.__instance_id__ = 65
            elif self._Msvm_ResourceAllocationSettingData_count_0 == 1:
                v = _wmi_class()
                v.__instance_id__ = 159
            elif self._Msvm_ResourceAllocationSettingData_count_0 == 2:
                v = _wmi_class()
                v.__instance_id__ = 254
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
                v.__instance_id__ = 35
            elif self._Msvm_VirtualSystemManagementService_count_0 == 1:
                v = _wmi_class()
                v.__instance_id__ = 154
            elif self._Msvm_VirtualSystemManagementService_count_0 == 2:
                v = _wmi_class()
                v.__instance_id__ = 247
            elif self._Msvm_VirtualSystemManagementService_count_0 == 3:
                v = _wmi_class()
                v.__instance_id__ = 342
            elif self._Msvm_VirtualSystemManagementService_count_0 == 4:
                v = _wmi_class()
                v.__instance_id__ = 348
            elif self._Msvm_VirtualSystemManagementService_count_0 == 5:
                v = _wmi_class()
                v.__instance_id__ = 383
            self._Msvm_VirtualSystemManagementService_count_0 += 1
            return v

    @Msvm_VirtualSystemManagementService.setter
    def Msvm_VirtualSystemManagementService(self, value):
        pass

    @property
    def Msvm_VirtualSystemGlobalSettingData(self):
        if self.__id__ == 9:
            v = _wmi_class()
            v.__instance_id__ = 37
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
                v.__instance_id__ = 40
            elif self._Msvm_ComputerSystem_count_0 == 2:
                v = _wmi_class()
                v.__instance_id__ = 346
            elif self._Msvm_ComputerSystem_count_0 == 3:
                v = _wmi_class()
                v.__instance_id__ = 352
            elif self._Msvm_ComputerSystem_count_0 == 4:
                v = _wmi_class()
                v.__instance_id__ = 379
            elif self._Msvm_ComputerSystem_count_0 == 5:
                v = _wmi_class()
                v.__instance_id__ = 381
            elif self._Msvm_ComputerSystem_count_0 == 6:
                v = _wmi_class()
                v.__instance_id__ = 385
            self._Msvm_ComputerSystem_count_0 += 1
            return v
        elif self.__id__ == 11:
            ret_value = None
            if not hasattr(self, '_Msvm_ComputerSystem_count_1'):
                self._Msvm_ComputerSystem_count_1 = 0
            if self._Msvm_ComputerSystem_count_1 == 0:
                v = _wmi_class()
                v.__instance_id__ = 361
            elif self._Msvm_ComputerSystem_count_1 == 1:
                v = _wmi_class()
                v.__instance_id__ = 413
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
                v.__instance_id__ = 49
            elif self._MSVM_ComputerSystem_count_0 == 1:
                v = _wmi_class()
                v.__instance_id__ = 251
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
        elif self.__id__ == 410 and wql == u'Select * from CIM_DataFile where\
 Name =\
 \'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_6fb85d6a-58a1-4db1-ac2\
9-4969bcc6db91\\openstack_unit_test_vm_6fb85d6a-58a1-4db1-ac29-4969bcc6db91.vh\
d\'':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 411
            v.append(v1)
            return v
        elif self.__id__ == 9 and wql == 'Select * from\
 Msvm_ImageManagementService':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 24
            v.append(v1)
            return v
        elif self.__id__ == 9 and wql == 'SELECT * FROM\
 Msvm_ResourceAllocationSettingData             WHERE ResourceSubType LIKE\
 \'Microsoft Synthetic Disk Drive\'            AND InstanceID LIKE\
 \'%Default%\'':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 64
            v.append(v1)
            return v
        elif self.__id__ == 9 and wql == 'SELECT * FROM\
 Msvm_ResourceAllocationSettingData                  WHERE ResourceSubType\
 LIKE \'Microsoft Virtual Hard Disk\' AND                  InstanceID LIKE\
 \'%Default%\' ':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 158
            v.append(v1)
            return v
        elif self.__id__ == 9 and wql == 'SELECT * FROM\
 Msvm_ResourceAllocationSettingData                 WHERE ResourceSubType =\
 \'Microsoft Synthetic SCSI Controller\'                AND InstanceID LIKE\
 \'%Default%\'':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 253
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
        elif self.__id__ == 49 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_6fb85d6a-58a1-4db1-ac29-4969bcc6db91':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 50
            v.append(v1)
            return v
        elif self.__id__ == 251 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_6fb85d6a-58a1-4db1-ac29-4969bcc6db91':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 252
            v.append(v1)
            return v
        elif self.__id__ == 10 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_6fb85d6a-58a1-4db1-ac29-4969bcc6db91':
            v = []
            return v
        elif self.__id__ == 40 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_6fb85d6a-58a1-4db1-ac29-4969bcc6db91':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 41
            v.append(v1)
            return v
        elif self.__id__ == 346 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_6fb85d6a-58a1-4db1-ac29-4969bcc6db91':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 347
            v.append(v1)
            return v
        elif self.__id__ == 352 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_6fb85d6a-58a1-4db1-ac29-4969bcc6db91':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 353
            v.append(v1)
            return v
        elif self.__id__ == 379 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_6fb85d6a-58a1-4db1-ac29-4969bcc6db91':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 380
            v.append(v1)
            return v
        elif self.__id__ == 381 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_6fb85d6a-58a1-4db1-ac29-4969bcc6db91':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 382
            v.append(v1)
            return v
        elif self.__id__ == 385 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_6fb85d6a-58a1-4db1-ac29-4969bcc6db91':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 386
            v.append(v1)
            return v
        elif self.__id__ == 35:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 36
            v.append(v1)
            return v
        elif self.__id__ == 154:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 155
            v.append(v1)
            return v
        elif self.__id__ == 247:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 248
            v.append(v1)
            return v
        elif self.__id__ == 342:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 343
            v.append(v1)
            return v
        elif self.__id__ == 348:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 349
            v.append(v1)
            return v
        elif self.__id__ == 383:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 384
            v.append(v1)
            return v
        elif self.__id__ == 361 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_6fb85d6a-58a1-4db1-ac29-4969bcc6db91':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 362
            v.append(v1)
            return v
        elif self.__id__ == 413 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_6fb85d6a-58a1-4db1-ac29-4969bcc6db91':
            v = []
            return v

    def new(self, **kwargs):
        if self.__id__ == 37:
            v = _wmi_object()
            v.__instance_id__ = 38
            return v
        elif self.__id__ == 65:
            v = _wmi_object()
            v.__instance_id__ = 66
            return v
        elif self.__id__ == 159:
            v = _wmi_object()
            v.__instance_id__ = 160
            return v
        elif self.__id__ == 254:
            v = _wmi_object()
            v.__instance_id__ = 255
            return v


class _wmi_object(object):

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__

    @property
    def CreateDifferencingVirtualHardDisk(self):
        if self.__id__ == 24:
            v = _wmi_method()
            v.__instance_id__ = 25
            return v

    @CreateDifferencingVirtualHardDisk.setter
    def CreateDifferencingVirtualHardDisk(self, value):
        pass

    @property
    def RequestStateChange(self):
        if self.__id__ == 353:
            v = _wmi_method()
            v.__instance_id__ = 354
            return v
        elif self.__id__ == 386:
            v = _wmi_method()
            v.__instance_id__ = 387
            return v

    @RequestStateChange.setter
    def RequestStateChange(self, value):
        pass

    @property
    def ElementName(self):
        if self.__id__ == 380:
            return\
 u'openstack_unit_test_vm_6fb85d6a-58a1-4db1-ac29-4969bcc6db91'

    @ElementName.setter
    def ElementName(self, value):
        pass

    @property
    def ModifyVirtualSystemResources(self):
        if self.__id__ == 36:
            ret_value = None
            if not hasattr(self, '_ModifyVirtualSystemResources_count_0'):
                self._ModifyVirtualSystemResources_count_0 = 0
            if self._ModifyVirtualSystemResources_count_0 == 0:
                v = _wmi_method()
                v.__instance_id__ = 44
            elif self._ModifyVirtualSystemResources_count_0 == 1:
                v = _wmi_method()
                v.__instance_id__ = 47
            self._ModifyVirtualSystemResources_count_0 += 1
            return v

    @ModifyVirtualSystemResources.setter
    def ModifyVirtualSystemResources(self, value):
        pass

    @property
    def Description(self):
        if self.__id__ == 34:
            return u'Creating Virtual Hard Disk'
        elif self.__id__ == 360:
            return u'Initializing and Starting Virtual Machine'
        elif self.__id__ == 389:
            return u'Turning Off Virtual Machine'
        elif self.__id__ == 409:
            return u'Destroying Virtual Machine'

    @Description.setter
    def Description(self, value):
        pass

    @property
    def SettingType(self):
        if self.__id__ == 42:
            return 3

    @SettingType.setter
    def SettingType(self, value):
        pass

    @property
    def AddVirtualSystemResources(self):
        if self.__id__ == 155:
            v = _wmi_method()
            v.__instance_id__ = 156
            return v
        elif self.__id__ == 248:
            v = _wmi_method()
            v.__instance_id__ = 249
            return v
        elif self.__id__ == 343:
            v = _wmi_method()
            v.__instance_id__ = 344
            return v
        elif self.__id__ == 349:
            v = _wmi_method()
            v.__instance_id__ = 350
            return v

    @AddVirtualSystemResources.setter
    def AddVirtualSystemResources(self, value):
        pass

    @property
    def Address(self):
        if self.__id__ == 60:
            return u'0'
        elif self.__id__ == 61:
            return u'1'

    @Address.setter
    def Address(self, value):
        pass

    @property
    def ResourceSubType(self):
        if self.__id__ == 52:
            return u'Microsoft Virtual Keyboard'
        elif self.__id__ == 53:
            return u'Microsoft Virtual PS2 Mouse'
        elif self.__id__ == 54:
            return u'Microsoft S3 Display Controller'
        elif self.__id__ == 55:
            return u'Microsoft Synthetic Diskette Drive'
        elif self.__id__ == 56:
            return None
        elif self.__id__ == 57:
            return u'Microsoft Serial Controller'
        elif self.__id__ == 58:
            return u'Microsoft Serial Port'
        elif self.__id__ == 59:
            return u'Microsoft Serial Port'
        elif self.__id__ == 60:
            return u'Microsoft Emulated IDE Controller'
        elif self.__id__ == 61:
            return u'Microsoft Emulated IDE Controller'
        elif self.__id__ == 62:
            return u'Microsoft Synthetic Mouse'
        elif self.__id__ == 63:
            return u'Microsoft Synthetic Display Controller'
        elif self.__id__ == 391:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_12'):
                self._ResourceSubType_count_12 = 0
            if self._ResourceSubType_count_12 == 0:
                v = u'Microsoft Virtual Keyboard'
            elif self._ResourceSubType_count_12 == 1:
                v = u'Microsoft Virtual Keyboard'
            self._ResourceSubType_count_12 += 1
            return v
        elif self.__id__ == 392:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_13'):
                self._ResourceSubType_count_13 = 0
            if self._ResourceSubType_count_13 == 0:
                v = u'Microsoft Virtual PS2 Mouse'
            elif self._ResourceSubType_count_13 == 1:
                v = u'Microsoft Virtual PS2 Mouse'
            self._ResourceSubType_count_13 += 1
            return v
        elif self.__id__ == 393:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_14'):
                self._ResourceSubType_count_14 = 0
            if self._ResourceSubType_count_14 == 0:
                v = u'Microsoft S3 Display Controller'
            elif self._ResourceSubType_count_14 == 1:
                v = u'Microsoft S3 Display Controller'
            self._ResourceSubType_count_14 += 1
            return v
        elif self.__id__ == 394:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_15'):
                self._ResourceSubType_count_15 = 0
            if self._ResourceSubType_count_15 == 0:
                v = u'Microsoft Synthetic Diskette Drive'
            elif self._ResourceSubType_count_15 == 1:
                v = u'Microsoft Synthetic Diskette Drive'
            self._ResourceSubType_count_15 += 1
            return v
        elif self.__id__ == 395:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_16'):
                self._ResourceSubType_count_16 = 0
            if self._ResourceSubType_count_16 == 0:
                v = None
            elif self._ResourceSubType_count_16 == 1:
                v = None
            self._ResourceSubType_count_16 += 1
            return v
        elif self.__id__ == 396:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_17'):
                self._ResourceSubType_count_17 = 0
            if self._ResourceSubType_count_17 == 0:
                v = u'Microsoft Serial Controller'
            elif self._ResourceSubType_count_17 == 1:
                v = u'Microsoft Serial Controller'
            self._ResourceSubType_count_17 += 1
            return v
        elif self.__id__ == 397:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_18'):
                self._ResourceSubType_count_18 = 0
            if self._ResourceSubType_count_18 == 0:
                v = u'Microsoft Serial Port'
            elif self._ResourceSubType_count_18 == 1:
                v = u'Microsoft Serial Port'
            self._ResourceSubType_count_18 += 1
            return v
        elif self.__id__ == 398:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_19'):
                self._ResourceSubType_count_19 = 0
            if self._ResourceSubType_count_19 == 0:
                v = u'Microsoft Serial Port'
            elif self._ResourceSubType_count_19 == 1:
                v = u'Microsoft Serial Port'
            self._ResourceSubType_count_19 += 1
            return v
        elif self.__id__ == 399:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_20'):
                self._ResourceSubType_count_20 = 0
            if self._ResourceSubType_count_20 == 0:
                v = u'Microsoft Synthetic Disk Drive'
            elif self._ResourceSubType_count_20 == 1:
                v = u'Microsoft Synthetic Disk Drive'
            self._ResourceSubType_count_20 += 1
            return v
        elif self.__id__ == 400:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_21'):
                self._ResourceSubType_count_21 = 0
            if self._ResourceSubType_count_21 == 0:
                v = u'Microsoft Virtual Hard Disk'
            elif self._ResourceSubType_count_21 == 1:
                v = u'Microsoft Virtual Hard Disk'
            self._ResourceSubType_count_21 += 1
            return v
        elif self.__id__ == 401:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_22'):
                self._ResourceSubType_count_22 = 0
            if self._ResourceSubType_count_22 == 0:
                v = u'Microsoft Emulated IDE Controller'
            elif self._ResourceSubType_count_22 == 1:
                v = u'Microsoft Emulated IDE Controller'
            self._ResourceSubType_count_22 += 1
            return v
        elif self.__id__ == 402:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_23'):
                self._ResourceSubType_count_23 = 0
            if self._ResourceSubType_count_23 == 0:
                v = u'Microsoft Emulated IDE Controller'
            elif self._ResourceSubType_count_23 == 1:
                v = u'Microsoft Emulated IDE Controller'
            self._ResourceSubType_count_23 += 1
            return v
        elif self.__id__ == 403:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_24'):
                self._ResourceSubType_count_24 = 0
            if self._ResourceSubType_count_24 == 0:
                v = u'Microsoft Synthetic Mouse'
            elif self._ResourceSubType_count_24 == 1:
                v = u'Microsoft Synthetic Mouse'
            self._ResourceSubType_count_24 += 1
            return v
        elif self.__id__ == 404:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_25'):
                self._ResourceSubType_count_25 = 0
            if self._ResourceSubType_count_25 == 0:
                v = u'Microsoft Synthetic Display Controller'
            elif self._ResourceSubType_count_25 == 1:
                v = u'Microsoft Synthetic Display Controller'
            self._ResourceSubType_count_25 += 1
            return v
        elif self.__id__ == 405:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_26'):
                self._ResourceSubType_count_26 = 0
            if self._ResourceSubType_count_26 == 0:
                v = u'Microsoft Synthetic SCSI Controller'
            elif self._ResourceSubType_count_26 == 1:
                v = u'Microsoft Synthetic SCSI Controller'
            self._ResourceSubType_count_26 += 1
            return v
        elif self.__id__ == 364:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_27'):
                self._ResourceSubType_count_27 = 0
            if self._ResourceSubType_count_27 == 0:
                v = u'Microsoft Virtual Keyboard'
            elif self._ResourceSubType_count_27 == 1:
                v = u'Microsoft Virtual Keyboard'
            elif self._ResourceSubType_count_27 == 2:
                v = u'Microsoft Virtual Keyboard'
            self._ResourceSubType_count_27 += 1
            return v
        elif self.__id__ == 365:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_28'):
                self._ResourceSubType_count_28 = 0
            if self._ResourceSubType_count_28 == 0:
                v = u'Microsoft Virtual PS2 Mouse'
            elif self._ResourceSubType_count_28 == 1:
                v = u'Microsoft Virtual PS2 Mouse'
            elif self._ResourceSubType_count_28 == 2:
                v = u'Microsoft Virtual PS2 Mouse'
            self._ResourceSubType_count_28 += 1
            return v
        elif self.__id__ == 366:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_29'):
                self._ResourceSubType_count_29 = 0
            if self._ResourceSubType_count_29 == 0:
                v = u'Microsoft S3 Display Controller'
            elif self._ResourceSubType_count_29 == 1:
                v = u'Microsoft S3 Display Controller'
            elif self._ResourceSubType_count_29 == 2:
                v = u'Microsoft S3 Display Controller'
            self._ResourceSubType_count_29 += 1
            return v
        elif self.__id__ == 367:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_30'):
                self._ResourceSubType_count_30 = 0
            if self._ResourceSubType_count_30 == 0:
                v = u'Microsoft Synthetic Diskette Drive'
            elif self._ResourceSubType_count_30 == 1:
                v = u'Microsoft Synthetic Diskette Drive'
            elif self._ResourceSubType_count_30 == 2:
                v = u'Microsoft Synthetic Diskette Drive'
            self._ResourceSubType_count_30 += 1
            return v
        elif self.__id__ == 368:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_31'):
                self._ResourceSubType_count_31 = 0
            if self._ResourceSubType_count_31 == 0:
                v = None
            elif self._ResourceSubType_count_31 == 1:
                v = None
            elif self._ResourceSubType_count_31 == 2:
                v = None
            self._ResourceSubType_count_31 += 1
            return v
        elif self.__id__ == 369:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_32'):
                self._ResourceSubType_count_32 = 0
            if self._ResourceSubType_count_32 == 0:
                v = u'Microsoft Serial Controller'
            elif self._ResourceSubType_count_32 == 1:
                v = u'Microsoft Serial Controller'
            elif self._ResourceSubType_count_32 == 2:
                v = u'Microsoft Serial Controller'
            self._ResourceSubType_count_32 += 1
            return v
        elif self.__id__ == 370:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_33'):
                self._ResourceSubType_count_33 = 0
            if self._ResourceSubType_count_33 == 0:
                v = u'Microsoft Serial Port'
            elif self._ResourceSubType_count_33 == 1:
                v = u'Microsoft Serial Port'
            elif self._ResourceSubType_count_33 == 2:
                v = u'Microsoft Serial Port'
            self._ResourceSubType_count_33 += 1
            return v
        elif self.__id__ == 371:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_34'):
                self._ResourceSubType_count_34 = 0
            if self._ResourceSubType_count_34 == 0:
                v = u'Microsoft Serial Port'
            elif self._ResourceSubType_count_34 == 1:
                v = u'Microsoft Serial Port'
            elif self._ResourceSubType_count_34 == 2:
                v = u'Microsoft Serial Port'
            self._ResourceSubType_count_34 += 1
            return v
        elif self.__id__ == 372:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_35'):
                self._ResourceSubType_count_35 = 0
            if self._ResourceSubType_count_35 == 0:
                v = u'Microsoft Synthetic Disk Drive'
            elif self._ResourceSubType_count_35 == 1:
                v = u'Microsoft Synthetic Disk Drive'
            elif self._ResourceSubType_count_35 == 2:
                v = u'Microsoft Synthetic Disk Drive'
            self._ResourceSubType_count_35 += 1
            return v
        elif self.__id__ == 373:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_36'):
                self._ResourceSubType_count_36 = 0
            if self._ResourceSubType_count_36 == 0:
                v = u'Microsoft Virtual Hard Disk'
            elif self._ResourceSubType_count_36 == 1:
                v = u'Microsoft Virtual Hard Disk'
            elif self._ResourceSubType_count_36 == 2:
                v = u'Microsoft Virtual Hard Disk'
            self._ResourceSubType_count_36 += 1
            return v
        elif self.__id__ == 374:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_37'):
                self._ResourceSubType_count_37 = 0
            if self._ResourceSubType_count_37 == 0:
                v = u'Microsoft Emulated IDE Controller'
            elif self._ResourceSubType_count_37 == 1:
                v = u'Microsoft Emulated IDE Controller'
            elif self._ResourceSubType_count_37 == 2:
                v = u'Microsoft Emulated IDE Controller'
            self._ResourceSubType_count_37 += 1
            return v
        elif self.__id__ == 375:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_38'):
                self._ResourceSubType_count_38 = 0
            if self._ResourceSubType_count_38 == 0:
                v = u'Microsoft Emulated IDE Controller'
            elif self._ResourceSubType_count_38 == 1:
                v = u'Microsoft Emulated IDE Controller'
            elif self._ResourceSubType_count_38 == 2:
                v = u'Microsoft Emulated IDE Controller'
            self._ResourceSubType_count_38 += 1
            return v
        elif self.__id__ == 376:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_39'):
                self._ResourceSubType_count_39 = 0
            if self._ResourceSubType_count_39 == 0:
                v = u'Microsoft Synthetic Mouse'
            elif self._ResourceSubType_count_39 == 1:
                v = u'Microsoft Synthetic Mouse'
            elif self._ResourceSubType_count_39 == 2:
                v = u'Microsoft Synthetic Mouse'
            self._ResourceSubType_count_39 += 1
            return v
        elif self.__id__ == 377:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_40'):
                self._ResourceSubType_count_40 = 0
            if self._ResourceSubType_count_40 == 0:
                v = u'Microsoft Synthetic Display Controller'
            elif self._ResourceSubType_count_40 == 1:
                v = u'Microsoft Synthetic Display Controller'
            elif self._ResourceSubType_count_40 == 2:
                v = u'Microsoft Synthetic Display Controller'
            self._ResourceSubType_count_40 += 1
            return v
        elif self.__id__ == 378:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_41'):
                self._ResourceSubType_count_41 = 0
            if self._ResourceSubType_count_41 == 0:
                v = u'Microsoft Synthetic SCSI Controller'
            elif self._ResourceSubType_count_41 == 1:
                v = u'Microsoft Synthetic SCSI Controller'
            elif self._ResourceSubType_count_41 == 2:
                v = u'Microsoft Synthetic SCSI Controller'
            self._ResourceSubType_count_41 += 1
            return v

    @ResourceSubType.setter
    def ResourceSubType(self, value):
        pass

    @property
    def path_(self):
        if self.__id__ == 60:
            v = CDispatch()
            v.__instance_id__ = 153
            return v
        elif self.__id__ == 50:
            ret_value = None
            if not hasattr(self, '_path__count_1'):
                self._path__count_1 = 0
            if self._path__count_1 == 0:
                v = CDispatch()
                v.__instance_id__ = 157
            elif self._path__count_1 == 1:
                v = CDispatch()
                v.__instance_id__ = 250
            self._path__count_1 += 1
            return v
        elif self.__id__ == 252:
            v = CDispatch()
            v.__instance_id__ = 345
            return v
        elif self.__id__ == 41:
            ret_value = None
            if not hasattr(self, '_path__count_3'):
                self._path__count_3 = 0
            if self._path__count_3 == 0:
                v = CDispatch()
                v.__instance_id__ = 45
            elif self._path__count_3 == 1:
                v = CDispatch()
                v.__instance_id__ = 48
            self._path__count_3 += 1
            return v
        elif self.__id__ == 347:
            v = CDispatch()
            v.__instance_id__ = 351
            return v
        elif self.__id__ == 382:
            v = CDispatch()
            v.__instance_id__ = 407
            return v

    @path_.setter
    def path_(self, value):
        pass

    @property
    def ElapsedTime(self):
        if self.__id__ == 34:
            return u'00000000000001.013966:000'
        elif self.__id__ == 360:
            return u'00000000000000.715472:000'
        elif self.__id__ == 389:
            return u'00000000000000.147677:000'
        elif self.__id__ == 409:
            return u'00000000000000.067970:000'

    @ElapsedTime.setter
    def ElapsedTime(self, value):
        pass

    @property
    def Properties_(self):
        if self.__id__ == 64:
            ret_value = None
            if not hasattr(self, '_Properties__count_0'):
                self._Properties__count_0 = 0
            if self._Properties__count_0 == 0:
                v = CDispatch()
                v.__instance_id__ = 67
            elif self._Properties__count_0 == 1:
                v = CDispatch()
                v.__instance_id__ = 71
            elif self._Properties__count_0 == 2:
                v = CDispatch()
                v.__instance_id__ = 75
            elif self._Properties__count_0 == 3:
                v = CDispatch()
                v.__instance_id__ = 79
            elif self._Properties__count_0 == 4:
                v = CDispatch()
                v.__instance_id__ = 83
            elif self._Properties__count_0 == 5:
                v = CDispatch()
                v.__instance_id__ = 87
            elif self._Properties__count_0 == 6:
                v = CDispatch()
                v.__instance_id__ = 91
            elif self._Properties__count_0 == 7:
                v = CDispatch()
                v.__instance_id__ = 95
            elif self._Properties__count_0 == 8:
                v = CDispatch()
                v.__instance_id__ = 99
            elif self._Properties__count_0 == 9:
                v = CDispatch()
                v.__instance_id__ = 103
            elif self._Properties__count_0 == 10:
                v = CDispatch()
                v.__instance_id__ = 107
            elif self._Properties__count_0 == 11:
                v = CDispatch()
                v.__instance_id__ = 111
            elif self._Properties__count_0 == 12:
                v = CDispatch()
                v.__instance_id__ = 115
            elif self._Properties__count_0 == 13:
                v = CDispatch()
                v.__instance_id__ = 119
            elif self._Properties__count_0 == 14:
                v = CDispatch()
                v.__instance_id__ = 123
            elif self._Properties__count_0 == 15:
                v = CDispatch()
                v.__instance_id__ = 127
            elif self._Properties__count_0 == 16:
                v = CDispatch()
                v.__instance_id__ = 131
            elif self._Properties__count_0 == 17:
                v = CDispatch()
                v.__instance_id__ = 135
            elif self._Properties__count_0 == 18:
                v = CDispatch()
                v.__instance_id__ = 139
            elif self._Properties__count_0 == 19:
                v = CDispatch()
                v.__instance_id__ = 143
            elif self._Properties__count_0 == 20:
                v = CDispatch()
                v.__instance_id__ = 149
            self._Properties__count_0 += 1
            return v
        elif self.__id__ == 158:
            ret_value = None
            if not hasattr(self, '_Properties__count_1'):
                self._Properties__count_1 = 0
            if self._Properties__count_1 == 0:
                v = CDispatch()
                v.__instance_id__ = 161
            elif self._Properties__count_1 == 1:
                v = CDispatch()
                v.__instance_id__ = 165
            elif self._Properties__count_1 == 2:
                v = CDispatch()
                v.__instance_id__ = 169
            elif self._Properties__count_1 == 3:
                v = CDispatch()
                v.__instance_id__ = 173
            elif self._Properties__count_1 == 4:
                v = CDispatch()
                v.__instance_id__ = 177
            elif self._Properties__count_1 == 5:
                v = CDispatch()
                v.__instance_id__ = 181
            elif self._Properties__count_1 == 6:
                v = CDispatch()
                v.__instance_id__ = 185
            elif self._Properties__count_1 == 7:
                v = CDispatch()
                v.__instance_id__ = 189
            elif self._Properties__count_1 == 8:
                v = CDispatch()
                v.__instance_id__ = 193
            elif self._Properties__count_1 == 9:
                v = CDispatch()
                v.__instance_id__ = 197
            elif self._Properties__count_1 == 10:
                v = CDispatch()
                v.__instance_id__ = 201
            elif self._Properties__count_1 == 11:
                v = CDispatch()
                v.__instance_id__ = 205
            elif self._Properties__count_1 == 12:
                v = CDispatch()
                v.__instance_id__ = 209
            elif self._Properties__count_1 == 13:
                v = CDispatch()
                v.__instance_id__ = 213
            elif self._Properties__count_1 == 14:
                v = CDispatch()
                v.__instance_id__ = 217
            elif self._Properties__count_1 == 15:
                v = CDispatch()
                v.__instance_id__ = 221
            elif self._Properties__count_1 == 16:
                v = CDispatch()
                v.__instance_id__ = 225
            elif self._Properties__count_1 == 17:
                v = CDispatch()
                v.__instance_id__ = 229
            elif self._Properties__count_1 == 18:
                v = CDispatch()
                v.__instance_id__ = 233
            elif self._Properties__count_1 == 19:
                v = CDispatch()
                v.__instance_id__ = 237
            elif self._Properties__count_1 == 20:
                v = CDispatch()
                v.__instance_id__ = 243
            self._Properties__count_1 += 1
            return v
        elif self.__id__ == 253:
            ret_value = None
            if not hasattr(self, '_Properties__count_2'):
                self._Properties__count_2 = 0
            if self._Properties__count_2 == 0:
                v = CDispatch()
                v.__instance_id__ = 256
            elif self._Properties__count_2 == 1:
                v = CDispatch()
                v.__instance_id__ = 260
            elif self._Properties__count_2 == 2:
                v = CDispatch()
                v.__instance_id__ = 264
            elif self._Properties__count_2 == 3:
                v = CDispatch()
                v.__instance_id__ = 268
            elif self._Properties__count_2 == 4:
                v = CDispatch()
                v.__instance_id__ = 272
            elif self._Properties__count_2 == 5:
                v = CDispatch()
                v.__instance_id__ = 276
            elif self._Properties__count_2 == 6:
                v = CDispatch()
                v.__instance_id__ = 280
            elif self._Properties__count_2 == 7:
                v = CDispatch()
                v.__instance_id__ = 284
            elif self._Properties__count_2 == 8:
                v = CDispatch()
                v.__instance_id__ = 288
            elif self._Properties__count_2 == 9:
                v = CDispatch()
                v.__instance_id__ = 292
            elif self._Properties__count_2 == 10:
                v = CDispatch()
                v.__instance_id__ = 296
            elif self._Properties__count_2 == 11:
                v = CDispatch()
                v.__instance_id__ = 300
            elif self._Properties__count_2 == 12:
                v = CDispatch()
                v.__instance_id__ = 304
            elif self._Properties__count_2 == 13:
                v = CDispatch()
                v.__instance_id__ = 308
            elif self._Properties__count_2 == 14:
                v = CDispatch()
                v.__instance_id__ = 312
            elif self._Properties__count_2 == 15:
                v = CDispatch()
                v.__instance_id__ = 316
            elif self._Properties__count_2 == 16:
                v = CDispatch()
                v.__instance_id__ = 320
            elif self._Properties__count_2 == 17:
                v = CDispatch()
                v.__instance_id__ = 324
            elif self._Properties__count_2 == 18:
                v = CDispatch()
                v.__instance_id__ = 328
            elif self._Properties__count_2 == 19:
                v = CDispatch()
                v.__instance_id__ = 332
            elif self._Properties__count_2 == 20:
                v = CDispatch()
                v.__instance_id__ = 338
            self._Properties__count_2 += 1
            return v
        elif self.__id__ == 66:
            ret_value = None
            if not hasattr(self, '_Properties__count_3'):
                self._Properties__count_3 = 0
            if self._Properties__count_3 == 0:
                v = CDispatch()
                v.__instance_id__ = 69
            elif self._Properties__count_3 == 1:
                v = CDispatch()
                v.__instance_id__ = 73
            elif self._Properties__count_3 == 2:
                v = CDispatch()
                v.__instance_id__ = 77
            elif self._Properties__count_3 == 3:
                v = CDispatch()
                v.__instance_id__ = 81
            elif self._Properties__count_3 == 4:
                v = CDispatch()
                v.__instance_id__ = 85
            elif self._Properties__count_3 == 5:
                v = CDispatch()
                v.__instance_id__ = 89
            elif self._Properties__count_3 == 6:
                v = CDispatch()
                v.__instance_id__ = 93
            elif self._Properties__count_3 == 7:
                v = CDispatch()
                v.__instance_id__ = 97
            elif self._Properties__count_3 == 8:
                v = CDispatch()
                v.__instance_id__ = 101
            elif self._Properties__count_3 == 9:
                v = CDispatch()
                v.__instance_id__ = 105
            elif self._Properties__count_3 == 10:
                v = CDispatch()
                v.__instance_id__ = 109
            elif self._Properties__count_3 == 11:
                v = CDispatch()
                v.__instance_id__ = 113
            elif self._Properties__count_3 == 12:
                v = CDispatch()
                v.__instance_id__ = 117
            elif self._Properties__count_3 == 13:
                v = CDispatch()
                v.__instance_id__ = 121
            elif self._Properties__count_3 == 14:
                v = CDispatch()
                v.__instance_id__ = 125
            elif self._Properties__count_3 == 15:
                v = CDispatch()
                v.__instance_id__ = 129
            elif self._Properties__count_3 == 16:
                v = CDispatch()
                v.__instance_id__ = 133
            elif self._Properties__count_3 == 17:
                v = CDispatch()
                v.__instance_id__ = 137
            elif self._Properties__count_3 == 18:
                v = CDispatch()
                v.__instance_id__ = 141
            elif self._Properties__count_3 == 19:
                v = CDispatch()
                v.__instance_id__ = 145
            elif self._Properties__count_3 == 20:
                v = CDispatch()
                v.__instance_id__ = 147
            elif self._Properties__count_3 == 21:
                v = CDispatch()
                v.__instance_id__ = 151
            self._Properties__count_3 += 1
            return v
        elif self.__id__ == 160:
            ret_value = None
            if not hasattr(self, '_Properties__count_4'):
                self._Properties__count_4 = 0
            if self._Properties__count_4 == 0:
                v = CDispatch()
                v.__instance_id__ = 163
            elif self._Properties__count_4 == 1:
                v = CDispatch()
                v.__instance_id__ = 167
            elif self._Properties__count_4 == 2:
                v = CDispatch()
                v.__instance_id__ = 171
            elif self._Properties__count_4 == 3:
                v = CDispatch()
                v.__instance_id__ = 175
            elif self._Properties__count_4 == 4:
                v = CDispatch()
                v.__instance_id__ = 179
            elif self._Properties__count_4 == 5:
                v = CDispatch()
                v.__instance_id__ = 183
            elif self._Properties__count_4 == 6:
                v = CDispatch()
                v.__instance_id__ = 187
            elif self._Properties__count_4 == 7:
                v = CDispatch()
                v.__instance_id__ = 191
            elif self._Properties__count_4 == 8:
                v = CDispatch()
                v.__instance_id__ = 195
            elif self._Properties__count_4 == 9:
                v = CDispatch()
                v.__instance_id__ = 199
            elif self._Properties__count_4 == 10:
                v = CDispatch()
                v.__instance_id__ = 203
            elif self._Properties__count_4 == 11:
                v = CDispatch()
                v.__instance_id__ = 207
            elif self._Properties__count_4 == 12:
                v = CDispatch()
                v.__instance_id__ = 211
            elif self._Properties__count_4 == 13:
                v = CDispatch()
                v.__instance_id__ = 215
            elif self._Properties__count_4 == 14:
                v = CDispatch()
                v.__instance_id__ = 219
            elif self._Properties__count_4 == 15:
                v = CDispatch()
                v.__instance_id__ = 223
            elif self._Properties__count_4 == 16:
                v = CDispatch()
                v.__instance_id__ = 227
            elif self._Properties__count_4 == 17:
                v = CDispatch()
                v.__instance_id__ = 231
            elif self._Properties__count_4 == 18:
                v = CDispatch()
                v.__instance_id__ = 235
            elif self._Properties__count_4 == 19:
                v = CDispatch()
                v.__instance_id__ = 239
            elif self._Properties__count_4 == 20:
                v = CDispatch()
                v.__instance_id__ = 241
            elif self._Properties__count_4 == 21:
                v = CDispatch()
                v.__instance_id__ = 245
            self._Properties__count_4 += 1
            return v
        elif self.__id__ == 255:
            ret_value = None
            if not hasattr(self, '_Properties__count_5'):
                self._Properties__count_5 = 0
            if self._Properties__count_5 == 0:
                v = CDispatch()
                v.__instance_id__ = 258
            elif self._Properties__count_5 == 1:
                v = CDispatch()
                v.__instance_id__ = 262
            elif self._Properties__count_5 == 2:
                v = CDispatch()
                v.__instance_id__ = 266
            elif self._Properties__count_5 == 3:
                v = CDispatch()
                v.__instance_id__ = 270
            elif self._Properties__count_5 == 4:
                v = CDispatch()
                v.__instance_id__ = 274
            elif self._Properties__count_5 == 5:
                v = CDispatch()
                v.__instance_id__ = 278
            elif self._Properties__count_5 == 6:
                v = CDispatch()
                v.__instance_id__ = 282
            elif self._Properties__count_5 == 7:
                v = CDispatch()
                v.__instance_id__ = 286
            elif self._Properties__count_5 == 8:
                v = CDispatch()
                v.__instance_id__ = 290
            elif self._Properties__count_5 == 9:
                v = CDispatch()
                v.__instance_id__ = 294
            elif self._Properties__count_5 == 10:
                v = CDispatch()
                v.__instance_id__ = 298
            elif self._Properties__count_5 == 11:
                v = CDispatch()
                v.__instance_id__ = 302
            elif self._Properties__count_5 == 12:
                v = CDispatch()
                v.__instance_id__ = 306
            elif self._Properties__count_5 == 13:
                v = CDispatch()
                v.__instance_id__ = 310
            elif self._Properties__count_5 == 14:
                v = CDispatch()
                v.__instance_id__ = 314
            elif self._Properties__count_5 == 15:
                v = CDispatch()
                v.__instance_id__ = 318
            elif self._Properties__count_5 == 16:
                v = CDispatch()
                v.__instance_id__ = 322
            elif self._Properties__count_5 == 17:
                v = CDispatch()
                v.__instance_id__ = 326
            elif self._Properties__count_5 == 18:
                v = CDispatch()
                v.__instance_id__ = 330
            elif self._Properties__count_5 == 19:
                v = CDispatch()
                v.__instance_id__ = 334
            elif self._Properties__count_5 == 20:
                v = CDispatch()
                v.__instance_id__ = 336
            elif self._Properties__count_5 == 21:
                v = CDispatch()
                v.__instance_id__ = 340
            self._Properties__count_5 += 1
            return v

    @Properties_.setter
    def Properties_(self, value):
        pass

    @property
    def Connection(self):
        if self.__id__ == 400:
            v = ()
            v1 =\
 u'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_6fb85d6a-58a1-4db1-ac2\
9-4969bcc6db91\\openstack_unit_test_vm_6fb85d6a-58a1-4db1-ac29-4969bcc6db91.vh\
d'
            v += (v1,)
            return v
        elif self.__id__ == 373:
            v = ()
            v1 =\
 u'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_6fb85d6a-58a1-4db1-ac2\
9-4969bcc6db91\\openstack_unit_test_vm_6fb85d6a-58a1-4db1-ac29-4969bcc6db91.vh\
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
            return 4
        elif self.__id__ == 23:
            ret_value = None
            if not hasattr(self, '_JobState_count_9'):
                self._JobState_count_9 = 0
            if self._JobState_count_9 == 0:
                v = 7
            elif self._JobState_count_9 == 1:
                v = 7
            self._JobState_count_9 += 1
            return v
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
            return 4
        elif self.__id__ == 34:
            ret_value = None
            if not hasattr(self, '_JobState_count_18'):
                self._JobState_count_18 = 0
            if self._JobState_count_18 == 0:
                v = 7
            elif self._JobState_count_18 == 1:
                v = 7
            self._JobState_count_18 += 1
            return v
        elif self.__id__ == 355:
            return 4
        elif self.__id__ == 356:
            return 4
        elif self.__id__ == 357:
            return 4
        elif self.__id__ == 358:
            return 4
        elif self.__id__ == 359:
            return 4
        elif self.__id__ == 360:
            ret_value = None
            if not hasattr(self, '_JobState_count_24'):
                self._JobState_count_24 = 0
            if self._JobState_count_24 == 0:
                v = 7
            elif self._JobState_count_24 == 1:
                v = 7
            self._JobState_count_24 += 1
            return v
        elif self.__id__ == 388:
            return 4
        elif self.__id__ == 389:
            ret_value = None
            if not hasattr(self, '_JobState_count_26'):
                self._JobState_count_26 = 0
            if self._JobState_count_26 == 0:
                v = 7
            elif self._JobState_count_26 == 1:
                v = 7
            self._JobState_count_26 += 1
            return v
        elif self.__id__ == 408:
            return 4
        elif self.__id__ == 409:
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
        if self.__id__ == 36:
            v = _wmi_method()
            v.__instance_id__ = 39
            return v

    @DefineVirtualSystem.setter
    def DefineVirtualSystem(self, value):
        pass

    @property
    def _properties(self):
        if self.__id__ == 64:
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
        elif self.__id__ == 158:
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
        elif self.__id__ == 253:
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
        if self.__id__ == 384:
            v = _wmi_method()
            v.__instance_id__ = 406
            return v

    @DestroyVirtualSystem.setter
    def DestroyVirtualSystem(self, value):
        pass

    @property
    def Delete(self):
        if self.__id__ == 411:
            v = _wmi_method()
            v.__instance_id__ = 412
            return v

    @Delete.setter
    def Delete(self, value):
        pass

    def __str__(self):
        if self.__id__ == 411:
            return '\ninstance of CIM_DataFile\n{\n	AccessMask =\
 18809343;\n	Archive = TRUE;\n	Caption =\
 "c:\\\\hyper-v\\\\test\\\\instances\\\\openstack_unit_test_vm_6fb85d6a-58a1-4\
db1-ac29-4969bcc6db91\\\\openstack_unit_test_vm_6fb85d6a-58a1-4db1-ac29-4969bc\
c6db91.vhd";\n	Compressed = FALSE;\n	CreationClassName =\
 "CIM_LogicalFile";\n	CreationDate =\
 "20130103221144.616112+120";\n	CSCreationClassName =\
 "Win32_ComputerSystem";\n	CSName = "HV12OSDEMO1";\n	Description =\
 "c:\\\\hyper-v\\\\test\\\\instances\\\\openstack_unit_test_vm_6fb85d6a-58a1-4\
db1-ac29-4969bcc6db91\\\\openstack_unit_test_vm_6fb85d6a-58a1-4db1-ac29-4969bc\
c6db91.vhd";\n	Drive = "c:";\n	EightDotThreeFileName =\
 "c:\\\\hyper-v\\\\test\\\\instances\\\\openstack_unit_test_vm_6fb85d6a-58a1-4\
db1-ac29-4969bcc6db91\\\\openst~1.vhd";\n	Encrypted = FALSE;\n	Extension =\
 "vhd";\n	FileName =\
 "openstack_unit_test_vm_6fb85d6a-58a1-4db1-ac29-4969bcc6db91";\n	FileSize =\
 "81920";\n	FileType = "Disc Image File";\n	FSCreationClassName =\
 "Win32_FileSystem";\n	FSName = "NTFS";\n	Hidden = FALSE;\n	InstallDate =\
 "20130103221144.616112+120";\n	LastAccessed =\
 "20130103221144.616112+120";\n	LastModified =\
 "20130103221149.349813+120";\n	Name =\
 "c:\\\\hyper-v\\\\test\\\\instances\\\\openstack_unit_test_vm_6fb85d6a-58a1-4\
db1-ac29-4969bcc6db91\\\\openstack_unit_test_vm_6fb85d6a-58a1-4db1-ac29-4969bc\
c6db91.vhd";\n	Path =\
 "\\\\hyper-v\\\\test\\\\instances\\\\openstack_unit_test_vm_6fb85d6a-58a1-4db\
1-ac29-4969bcc6db91\\\\";\n	Readable = TRUE;\n	Status = "OK";\n	System =\
 FALSE;\n	Writeable = TRUE;\n};\n'

    def GetText_(self, iObjectTextFormat='<PyOleMissing object at\
 0x04091890>', iFlags=0, objWbemNamedValueSet=None):
        if self.__id__ == 43 and iObjectTextFormat == 1:
            return u'<INSTANCE CLASSNAME="Msvm_MemorySettingData"><PROPERTY\
 NAME="__PATH" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>\\\\HV12OSDEMO1\\root\\virtualization:Msvm_MemorySetting\
Data.InstanceID="Microsoft:394ADE39-C8E8-4950-A414-90742C58334B\\\\4764334d-e0\
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
 TYPE="string"><VALUE>Msvm_MemorySettingData.InstanceID="Microsoft:394ADE39-C8\
E8-4950-A414-90742C58334B\\\\4764334d-e001-4176-82ee-5594ec9b530e"</VALUE></PR\
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
 TYPE="string"><VALUE>Microsoft:394ADE39-C8E8-4950-A414-90742C58334B\\4764334d\
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
        elif self.__id__ == 46 and iObjectTextFormat == 1:
            return u'<INSTANCE CLASSNAME="Msvm_ProcessorSettingData"><PROPERTY\
 NAME="__PATH" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ProcessorSett\
ingData.InstanceID="Microsoft:394ADE39-C8E8-4950-A414-90742C58334B\\\\b637f346\
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
 TYPE="string"><VALUE>Msvm_ProcessorSettingData.InstanceID="Microsoft:394ADE39\
-C8E8-4950-A414-90742C58334B\\\\b637f346-6a0e-4dec-af52-bd70cb80a21d\\\\0"</VA\
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
 TYPE="string"><VALUE>Microsoft:394ADE39-C8E8-4950-A414-90742C58334B\\b637f346\
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
        elif self.__id__ == 38 and iObjectTextFormat == 1:
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
 TYPE="string"><VALUE>openstack_unit_test_vm_6fb85d6a-58a1-4db1-ac29-4969bcc6d\
b91</VALUE></PROPERTY><PROPERTY NAME="ExternalDataRoot"\
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
        elif self.__id__ == 66 and iObjectTextFormat == 1:
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
ationSettingData.InstanceID="Microsoft:394ADE39-C8E8-4950-A414-90742C58334B\
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
 TYPE="string"><VALUE.ARRAY><VALUE>f0fb575e-cd84-4f1c-934f-2b22aa4e69e2</VALUE\
></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>'
        elif self.__id__ == 160 and iObjectTextFormat == 1:
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
t_test_vm_6fb85d6a-58a1-4db1-ac29-4969bcc6db91\\openstack_unit_test_vm_6fb85d6\
a-58a1-4db1-ac29-4969bcc6db91.vhd</VALUE></VALUE.ARRAY></PROPERTY.ARRAY><PROPE\
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
ationSettingData.InstanceID="Microsoft:394ADE39-C8E8-4950-A414-90742C58334B\
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
 TYPE="string"><VALUE.ARRAY><VALUE>a0ad2779-b78b-4527-aac6-dee5604a22d6</VALUE\
></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>'
        elif self.__id__ == 255 and iObjectTextFormat == 1:
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
 TYPE="string"><VALUE.ARRAY><VALUE>{429c999c-392d-4587-9adc-51c355fdd336}</VAL\
UE></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>'

    def associators(self, wmi_association_class='', wmi_result_class=''):
        if self.__id__ == 51 and wmi_result_class ==\
 'MSVM_ResourceAllocationSettingData':
            v = []
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
            v1 = _wmi_object()
            v1.__instance_id__ = 63
            v.append(v1)
            return v
        elif self.__id__ == 50 and wmi_result_class ==\
 'Msvm_VirtualSystemSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 51
            v.append(v1)
            return v
        elif self.__id__ == 42 and wmi_result_class ==\
 'Msvm_MemorySettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 43
            v.append(v1)
            return v
        elif self.__id__ == 42 and wmi_result_class ==\
 'Msvm_ProcessorSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 46
            v.append(v1)
            return v
        elif self.__id__ == 41 and wmi_result_class ==\
 'Msvm_VirtualSystemSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 42
            v.append(v1)
            return v
        elif self.__id__ == 390 and wmi_result_class ==\
 'MSVM_ResourceAllocationSettingData':
            v = []
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
            v1 = _wmi_object()
            v1.__instance_id__ = 405
            v.append(v1)
            return v
        elif self.__id__ == 382 and wmi_result_class ==\
 'Msvm_VirtualSystemSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 390
            v.append(v1)
            return v
        elif self.__id__ == 363 and wmi_result_class ==\
 'MSVM_ResourceAllocationSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 364
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 365
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 366
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 367
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 368
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 369
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 370
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 371
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 372
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 373
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 374
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 375
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 376
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 377
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 378
            v.append(v1)
            return v
        elif self.__id__ == 362 and wmi_result_class ==\
 'Msvm_VirtualSystemSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 363
            v.append(v1)
            return v


class _wmi_method(object):

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__

    def __call__(self, *args, **kwargs):
        if len(args) == 0 and self.__id__ == 412:
            v = ()
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 0 and self.__id__ == 25 and kwargs.get('Path') ==\
 'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_6fb85d6a-58a1-4db1-ac29\
-4969bcc6db91\\openstack_unit_test_vm_6fb85d6a-58a1-4db1-ac29-4969bcc6db91.vhd\
' and kwargs.get('ParentPath') == 'C:\\Hyper-V\\test\\instances\\_base\\1.vhd':
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_StorageJob.InstanceID="20B4D538-\
1D7C-4492-B5AD-F5528ABFB259"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v
        elif len(args) == 1 and self.__id__ == 354 and args[0] == 2:
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ConcreteJob.InstanceID="6D6997C2\
-CDE8-4B89-B3B3-03AA449B4A44"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v
        elif len(args) == 1 and self.__id__ == 387 and args[0] == 3:
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ConcreteJob.InstanceID="7031691B\
-3920-484A-BE6F-7CFEFBA81D55"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v
        elif len(args) == 3 and self.__id__ == 39 and str(args[0]) == '[]' and\
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
 TYPE="string"><VALUE>openstack_unit_test_vm_6fb85d6a-58a1-4db1-ac29-4969bcc6d\
b91</VALUE></PROPERTY><PROPERTY NAME="ExternalDataRoot"\
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
="Msvm_ComputerSystem",Name="394ADE39-C8E8-4950-A414-90742C58334B"'
            v += (v1,)
            v1 = None
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 2 and self.__id__ == 44 and args[0] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="394ADE39-C8E8-4950-A414-90742C58334B"' and\
 str(args[1]) == '[u\'<INSTANCE CLASSNAME="Msvm_MemorySettingData"><PROPERTY\
 NAME="__PATH" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>\\\\\\\\HV12OSDEMO1\\\\root\\\\virtualization:Msvm_Memor\
ySettingData.InstanceID="Microsoft:394ADE39-C8E8-4950-A414-90742C58334B\
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
 TYPE="string"><VALUE>Msvm_MemorySettingData.InstanceID="Microsoft:394ADE39-C8\
E8-4950-A414-90742C58334B\\\\\\\\4764334d-e001-4176-82ee-5594ec9b530e"</VALUE>\
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
 TYPE="string"><VALUE>Microsoft:394ADE39-C8E8-4950-A414-90742C58334B\\\\476433\
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
        elif len(args) == 2 and self.__id__ == 47 and args[0] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="394ADE39-C8E8-4950-A414-90742C58334B"' and\
 str(args[1]) == '[u\'<INSTANCE\
 CLASSNAME="Msvm_ProcessorSettingData"><PROPERTY NAME="__PATH"\
 CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>\\\\\\\\HV12OSDEMO1\\\\root\\\\virtualization:Msvm_Proce\
ssorSettingData.InstanceID="Microsoft:394ADE39-C8E8-4950-A414-90742C58334B\
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
 TYPE="string"><VALUE>Msvm_ProcessorSettingData.InstanceID="Microsoft:394ADE39\
-C8E8-4950-A414-90742C58334B\\\\\\\\b637f346-6a0e-4dec-af52-bd70cb80a21d\
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
 TYPE="string"><VALUE>Microsoft:394ADE39-C8E8-4950-A414-90742C58334B\\\\b637f3\
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
        elif len(args) == 2 and self.__id__ == 156 and str(args[0]) ==\
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
rceAllocationSettingData.InstanceID="Microsoft:394ADE39-C8E8-4950-A414-90742C5\
8334B\\\\\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\\\\\0"</VALUE></PROPERTY>\
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
 TYPE="string"><VALUE.ARRAY><VALUE>f0fb575e-cd84-4f1c-934f-2b22aa4e69e2</VALUE\
></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="394ADE39-C8E8-4950-A414-90742C58334B"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:394ADE39-C8E8-4950-A414-90742C58334B\\\\83F8638B-8DCA-4152\
-9EDA-2CA8B33039B4\\\\0\\\\0\\\\D"'
            v1.append(v2)
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 2 and self.__id__ == 249 and str(args[0]) ==\
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
tack_unit_test_vm_6fb85d6a-58a1-4db1-ac29-4969bcc6db91\\\\openstack_unit_test_\
vm_6fb85d6a-58a1-4db1-ac29-4969bcc6db91.vhd</VALUE></VALUE.ARRAY></PROPERTY.AR\
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
rceAllocationSettingData.InstanceID="Microsoft:394ADE39-C8E8-4950-A414-90742C5\
8334B\\\\\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\\\\\0\\\\\\\\0\\\\\\\\D"<\
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
 TYPE="string"><VALUE.ARRAY><VALUE>a0ad2779-b78b-4527-aac6-dee5604a22d6</VALUE\
></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="394ADE39-C8E8-4950-A414-90742C58334B"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:394ADE39-C8E8-4950-A414-90742C58334B\\\\83F8638B-8DCA-4152\
-9EDA-2CA8B33039B4\\\\0\\\\0\\\\L"'
            v1.append(v2)
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 2 and self.__id__ == 344 and str(args[0]) ==\
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
 TYPE="string"><VALUE.ARRAY><VALUE>{429c999c-392d-4587-9adc-51c355fdd336}</VAL\
UE></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="394ADE39-C8E8-4950-A414-90742C58334B"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:394ADE39-C8E8-4950-A414-90742C58334B\\\\C7073C55-6B7A-44DA\
-AB19-4786E3B42918\\\\0"'
            v1.append(v2)
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 2 and self.__id__ == 350 and str(args[0]) ==\
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
 TYPE="string"><VALUE.ARRAY><VALUE>{6a386ac7-fbc1-4a5a-838a-6fc2a7c7bb93}</VAL\
UE></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="394ADE39-C8E8-4950-A414-90742C58334B"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_SyntheticEthernetPortSettingData\
.InstanceID="Microsoft:394ADE39-C8E8-4950-A414-90742C58334B\\\\27CD8F1C-F44B-4\
0A5-B63E-E618797A8282"'
            v1.append(v2)
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 1 and self.__id__ == 406 and args[0] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="394ADE39-C8E8-4950-A414-90742C58334B"':
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ConcreteJob.InstanceID="3D372AC2\
-FB97-43BF-B478-3D63C651D412"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v
        elif len(args) == 0 and self.__id__ == 13 and\
 kwargs.get('MaxInternalSize') == 3145728 and kwargs.get('Path') ==\
 'C:\\Hyper-V\\test\\instances\\_base\\1.vhd':
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_StorageJob.InstanceID="B3684A6A-\
1997-48F3-9343-990F42F6AB1A"'
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
    def Value(self):
        if self.__id__ == 68:
            return\
 u'Microsoft:Definition\\118C3BE5-0D31-4804-85F0-5C6074ABEA8F\\Default'
        elif self.__id__ == 72:
            return u'Microsoft Synthetic Disk Drive'
        elif self.__id__ == 76:
            return None
        elif self.__id__ == 80:
            return u'Hard Drive'
        elif self.__id__ == 84:
            return u'Settings for the Microsoft Virtual Hard Drive.'
        elif self.__id__ == 88:
            return None
        elif self.__id__ == 92:
            return u'1'
        elif self.__id__ == 96:
            return True
        elif self.__id__ == 100:
            return True
        elif self.__id__ == 104:
            return u'Microsoft:118C3BE5-0D31-4804-85F0-5C6074ABEA8F\\Root'
        elif self.__id__ == 108:
            return u'1'
        elif self.__id__ == 112:
            return u'Hard Drives'
        elif self.__id__ == 116:
            return None
        elif self.__id__ == 120:
            return None
        elif self.__id__ == 124:
            return None
        elif self.__id__ == 128:
            return u'Hard Drive'
        elif self.__id__ == 132:
            return None
        elif self.__id__ == 136:
            return u'1'
        elif self.__id__ == 140:
            return 22
        elif self.__id__ == 144:
            return 0
        elif self.__id__ == 150:
            return None
        elif self.__id__ == 162:
            return\
 u'Microsoft:Definition\\70BB60D2-A9D3-46AA-B654-3DE53004B4F8\\Default'
        elif self.__id__ == 166:
            return u'Microsoft Virtual Hard Disk'
        elif self.__id__ == 170:
            return None
        elif self.__id__ == 174:
            return u'Hard Disk Image'
        elif self.__id__ == 178:
            return u'Settings for the Microsoft Hard Disk Image.'
        elif self.__id__ == 182:
            return None
        elif self.__id__ == 186:
            return u'1'
        elif self.__id__ == 190:
            return True
        elif self.__id__ == 194:
            return True
        elif self.__id__ == 198:
            return u'Microsoft:70BB60D2-A9D3-46aa-B654-3DE53004B4F8\\Root'
        elif self.__id__ == 202:
            return u'1'
        elif self.__id__ == 206:
            return u'Disks'
        elif self.__id__ == 210:
            return None
        elif self.__id__ == 214:
            return None
        elif self.__id__ == 218:
            return None
        elif self.__id__ == 222:
            return u'Hard Disk Image'
        elif self.__id__ == 226:
            return None
        elif self.__id__ == 230:
            return u'1'
        elif self.__id__ == 234:
            return 21
        elif self.__id__ == 238:
            return 0
        elif self.__id__ == 244:
            return None
        elif self.__id__ == 257:
            return\
 u'Microsoft:Definition\\BDE5D4D6-E450-46D2-B925-976CA3E989B4\\Default'
        elif self.__id__ == 261:
            return u'Microsoft Synthetic SCSI Controller'
        elif self.__id__ == 265:
            return None
        elif self.__id__ == 269:
            return u'SCSI Controller'
        elif self.__id__ == 273:
            return u'Settings for the Microsoft Synthetic SCSI Controller.'
        elif self.__id__ == 277:
            return None
        elif self.__id__ == 281:
            return u'1'
        elif self.__id__ == 285:
            return True
        elif self.__id__ == 289:
            return True
        elif self.__id__ == 293:
            return u'Microsoft:bde5d4d6-e450-46d2-b925-976ca3e989b4\\Root'
        elif self.__id__ == 297:
            return u'1'
        elif self.__id__ == 301:
            return u'Controllers'
        elif self.__id__ == 305:
            return None
        elif self.__id__ == 309:
            return None
        elif self.__id__ == 313:
            return None
        elif self.__id__ == 317:
            return u'SCSI Controller'
        elif self.__id__ == 321:
            return None
        elif self.__id__ == 325:
            return u'1'
        elif self.__id__ == 329:
            return 6
        elif self.__id__ == 333:
            return 0
        elif self.__id__ == 339:
            return None

    @Value.setter
    def Value(self, value):
        pass

    def __call__(self, *args):
        if len(args) == 0 and self.__id__ == 153:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:394ADE39-C8E8-4950-A414-90742C58334B\\\\83F8638B-8DCA-4152\
-9EDA-2CA8B33039B4\\\\0"'
        elif len(args) == 0 and self.__id__ == 157:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="394ADE39-C8E8-4950-A414-90742C58334B"'
        elif len(args) == 0 and self.__id__ == 250:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="394ADE39-C8E8-4950-A414-90742C58334B"'
        elif len(args) == 0 and self.__id__ == 345:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="394ADE39-C8E8-4950-A414-90742C58334B"'
        elif len(args) == 0 and self.__id__ == 45:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="394ADE39-C8E8-4950-A414-90742C58334B"'
        elif len(args) == 0 and self.__id__ == 48:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="394ADE39-C8E8-4950-A414-90742C58334B"'
        elif len(args) == 0 and self.__id__ == 351:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="394ADE39-C8E8-4950-A414-90742C58334B"'
        elif len(args) == 0 and self.__id__ == 407:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="394ADE39-C8E8-4950-A414-90742C58334B"'

    def Item(self, strName='<PyOleMissing object at 0x04091890>', iFlags=0):
        if self.__id__ == 67 and strName == u'InstanceID':
            v = CDispatch()
            v.__instance_id__ = 68
            return v
        elif self.__id__ == 71 and strName == u'ResourceSubType':
            v = CDispatch()
            v.__instance_id__ = 72
            return v
        elif self.__id__ == 75 and strName == u'HostResource':
            v = CDispatch()
            v.__instance_id__ = 76
            return v
        elif self.__id__ == 79 and strName == u'ElementName':
            v = CDispatch()
            v.__instance_id__ = 80
            return v
        elif self.__id__ == 83 and strName == u'Description':
            v = CDispatch()
            v.__instance_id__ = 84
            return v
        elif self.__id__ == 87 and strName == u'Parent':
            v = CDispatch()
            v.__instance_id__ = 88
            return v
        elif self.__id__ == 91 and strName == u'VirtualQuantity':
            v = CDispatch()
            v.__instance_id__ = 92
            return v
        elif self.__id__ == 95 and strName == u'AutomaticDeallocation':
            v = CDispatch()
            v.__instance_id__ = 96
            return v
        elif self.__id__ == 99 and strName == u'AutomaticAllocation':
            v = CDispatch()
            v.__instance_id__ = 100
            return v
        elif self.__id__ == 103 and strName == u'PoolID':
            v = CDispatch()
            v.__instance_id__ = 104
            return v
        elif self.__id__ == 107 and strName == u'Reservation':
            v = CDispatch()
            v.__instance_id__ = 108
            return v
        elif self.__id__ == 111 and strName == u'AllocationUnits':
            v = CDispatch()
            v.__instance_id__ = 112
            return v
        elif self.__id__ == 115 and strName == u'MappingBehavior':
            v = CDispatch()
            v.__instance_id__ = 116
            return v
        elif self.__id__ == 119 and strName == u'Address':
            v = CDispatch()
            v.__instance_id__ = 120
            return v
        elif self.__id__ == 123 and strName == u'OtherResourceType':
            v = CDispatch()
            v.__instance_id__ = 124
            return v
        elif self.__id__ == 127 and strName == u'Caption':
            v = CDispatch()
            v.__instance_id__ = 128
            return v
        elif self.__id__ == 131 and strName == u'ConsumerVisibility':
            v = CDispatch()
            v.__instance_id__ = 132
            return v
        elif self.__id__ == 135 and strName == u'Limit':
            v = CDispatch()
            v.__instance_id__ = 136
            return v
        elif self.__id__ == 139 and strName == u'ResourceType':
            v = CDispatch()
            v.__instance_id__ = 140
            return v
        elif self.__id__ == 143 and strName == u'Weight':
            v = CDispatch()
            v.__instance_id__ = 144
            return v
        elif self.__id__ == 149 and strName == u'Connection':
            v = CDispatch()
            v.__instance_id__ = 150
            return v
        elif self.__id__ == 161 and strName == u'InstanceID':
            v = CDispatch()
            v.__instance_id__ = 162
            return v
        elif self.__id__ == 165 and strName == u'ResourceSubType':
            v = CDispatch()
            v.__instance_id__ = 166
            return v
        elif self.__id__ == 169 and strName == u'HostResource':
            v = CDispatch()
            v.__instance_id__ = 170
            return v
        elif self.__id__ == 173 and strName == u'ElementName':
            v = CDispatch()
            v.__instance_id__ = 174
            return v
        elif self.__id__ == 177 and strName == u'Description':
            v = CDispatch()
            v.__instance_id__ = 178
            return v
        elif self.__id__ == 181 and strName == u'Parent':
            v = CDispatch()
            v.__instance_id__ = 182
            return v
        elif self.__id__ == 185 and strName == u'VirtualQuantity':
            v = CDispatch()
            v.__instance_id__ = 186
            return v
        elif self.__id__ == 189 and strName == u'AutomaticDeallocation':
            v = CDispatch()
            v.__instance_id__ = 190
            return v
        elif self.__id__ == 193 and strName == u'AutomaticAllocation':
            v = CDispatch()
            v.__instance_id__ = 194
            return v
        elif self.__id__ == 197 and strName == u'PoolID':
            v = CDispatch()
            v.__instance_id__ = 198
            return v
        elif self.__id__ == 201 and strName == u'Reservation':
            v = CDispatch()
            v.__instance_id__ = 202
            return v
        elif self.__id__ == 205 and strName == u'AllocationUnits':
            v = CDispatch()
            v.__instance_id__ = 206
            return v
        elif self.__id__ == 209 and strName == u'MappingBehavior':
            v = CDispatch()
            v.__instance_id__ = 210
            return v
        elif self.__id__ == 213 and strName == u'Address':
            v = CDispatch()
            v.__instance_id__ = 214
            return v
        elif self.__id__ == 217 and strName == u'OtherResourceType':
            v = CDispatch()
            v.__instance_id__ = 218
            return v
        elif self.__id__ == 221 and strName == u'Caption':
            v = CDispatch()
            v.__instance_id__ = 222
            return v
        elif self.__id__ == 225 and strName == u'ConsumerVisibility':
            v = CDispatch()
            v.__instance_id__ = 226
            return v
        elif self.__id__ == 229 and strName == u'Limit':
            v = CDispatch()
            v.__instance_id__ = 230
            return v
        elif self.__id__ == 233 and strName == u'ResourceType':
            v = CDispatch()
            v.__instance_id__ = 234
            return v
        elif self.__id__ == 237 and strName == u'Weight':
            v = CDispatch()
            v.__instance_id__ = 238
            return v
        elif self.__id__ == 243 and strName == u'Connection':
            v = CDispatch()
            v.__instance_id__ = 244
            return v
        elif self.__id__ == 256 and strName == u'InstanceID':
            v = CDispatch()
            v.__instance_id__ = 257
            return v
        elif self.__id__ == 260 and strName == u'ResourceSubType':
            v = CDispatch()
            v.__instance_id__ = 261
            return v
        elif self.__id__ == 264 and strName == u'HostResource':
            v = CDispatch()
            v.__instance_id__ = 265
            return v
        elif self.__id__ == 268 and strName == u'ElementName':
            v = CDispatch()
            v.__instance_id__ = 269
            return v
        elif self.__id__ == 272 and strName == u'Description':
            v = CDispatch()
            v.__instance_id__ = 273
            return v
        elif self.__id__ == 276 and strName == u'Parent':
            v = CDispatch()
            v.__instance_id__ = 277
            return v
        elif self.__id__ == 280 and strName == u'VirtualQuantity':
            v = CDispatch()
            v.__instance_id__ = 281
            return v
        elif self.__id__ == 284 and strName == u'AutomaticDeallocation':
            v = CDispatch()
            v.__instance_id__ = 285
            return v
        elif self.__id__ == 288 and strName == u'AutomaticAllocation':
            v = CDispatch()
            v.__instance_id__ = 289
            return v
        elif self.__id__ == 292 and strName == u'PoolID':
            v = CDispatch()
            v.__instance_id__ = 293
            return v
        elif self.__id__ == 296 and strName == u'Reservation':
            v = CDispatch()
            v.__instance_id__ = 297
            return v
        elif self.__id__ == 300 and strName == u'AllocationUnits':
            v = CDispatch()
            v.__instance_id__ = 301
            return v
        elif self.__id__ == 304 and strName == u'MappingBehavior':
            v = CDispatch()
            v.__instance_id__ = 305
            return v
        elif self.__id__ == 308 and strName == u'Address':
            v = CDispatch()
            v.__instance_id__ = 309
            return v
        elif self.__id__ == 312 and strName == u'OtherResourceType':
            v = CDispatch()
            v.__instance_id__ = 313
            return v
        elif self.__id__ == 316 and strName == u'Caption':
            v = CDispatch()
            v.__instance_id__ = 317
            return v
        elif self.__id__ == 320 and strName == u'ConsumerVisibility':
            v = CDispatch()
            v.__instance_id__ = 321
            return v
        elif self.__id__ == 324 and strName == u'Limit':
            v = CDispatch()
            v.__instance_id__ = 325
            return v
        elif self.__id__ == 328 and strName == u'ResourceType':
            v = CDispatch()
            v.__instance_id__ = 329
            return v
        elif self.__id__ == 332 and strName == u'Weight':
            v = CDispatch()
            v.__instance_id__ = 333
            return v
        elif self.__id__ == 338 and strName == u'Connection':
            v = CDispatch()
            v.__instance_id__ = 339
            return v
        elif self.__id__ == 69 and strName == u'InstanceID':
            v = CDispatch()
            v.__instance_id__ = 70
            return v
        elif self.__id__ == 73 and strName == u'ResourceSubType':
            v = CDispatch()
            v.__instance_id__ = 74
            return v
        elif self.__id__ == 77 and strName == u'HostResource':
            v = CDispatch()
            v.__instance_id__ = 78
            return v
        elif self.__id__ == 81 and strName == u'ElementName':
            v = CDispatch()
            v.__instance_id__ = 82
            return v
        elif self.__id__ == 85 and strName == u'Description':
            v = CDispatch()
            v.__instance_id__ = 86
            return v
        elif self.__id__ == 89 and strName == u'Parent':
            v = CDispatch()
            v.__instance_id__ = 90
            return v
        elif self.__id__ == 93 and strName == u'VirtualQuantity':
            v = CDispatch()
            v.__instance_id__ = 94
            return v
        elif self.__id__ == 97 and strName == u'AutomaticDeallocation':
            v = CDispatch()
            v.__instance_id__ = 98
            return v
        elif self.__id__ == 101 and strName == u'AutomaticAllocation':
            v = CDispatch()
            v.__instance_id__ = 102
            return v
        elif self.__id__ == 105 and strName == u'PoolID':
            v = CDispatch()
            v.__instance_id__ = 106
            return v
        elif self.__id__ == 109 and strName == u'Reservation':
            v = CDispatch()
            v.__instance_id__ = 110
            return v
        elif self.__id__ == 113 and strName == u'AllocationUnits':
            v = CDispatch()
            v.__instance_id__ = 114
            return v
        elif self.__id__ == 117 and strName == u'MappingBehavior':
            v = CDispatch()
            v.__instance_id__ = 118
            return v
        elif self.__id__ == 121 and strName == u'Address':
            v = CDispatch()
            v.__instance_id__ = 122
            return v
        elif self.__id__ == 125 and strName == u'OtherResourceType':
            v = CDispatch()
            v.__instance_id__ = 126
            return v
        elif self.__id__ == 129 and strName == u'Caption':
            v = CDispatch()
            v.__instance_id__ = 130
            return v
        elif self.__id__ == 133 and strName == u'ConsumerVisibility':
            v = CDispatch()
            v.__instance_id__ = 134
            return v
        elif self.__id__ == 137 and strName == u'Limit':
            v = CDispatch()
            v.__instance_id__ = 138
            return v
        elif self.__id__ == 141 and strName == u'ResourceType':
            v = CDispatch()
            v.__instance_id__ = 142
            return v
        elif self.__id__ == 145 and strName == u'Weight':
            v = CDispatch()
            v.__instance_id__ = 146
            return v
        elif self.__id__ == 147 and strName == u'VirtualSystemIdentifiers':
            v = CDispatch()
            v.__instance_id__ = 148
            return v
        elif self.__id__ == 151 and strName == u'Connection':
            v = CDispatch()
            v.__instance_id__ = 152
            return v
        elif self.__id__ == 163 and strName == u'InstanceID':
            v = CDispatch()
            v.__instance_id__ = 164
            return v
        elif self.__id__ == 167 and strName == u'ResourceSubType':
            v = CDispatch()
            v.__instance_id__ = 168
            return v
        elif self.__id__ == 171 and strName == u'HostResource':
            v = CDispatch()
            v.__instance_id__ = 172
            return v
        elif self.__id__ == 175 and strName == u'ElementName':
            v = CDispatch()
            v.__instance_id__ = 176
            return v
        elif self.__id__ == 179 and strName == u'Description':
            v = CDispatch()
            v.__instance_id__ = 180
            return v
        elif self.__id__ == 183 and strName == u'Parent':
            v = CDispatch()
            v.__instance_id__ = 184
            return v
        elif self.__id__ == 187 and strName == u'VirtualQuantity':
            v = CDispatch()
            v.__instance_id__ = 188
            return v
        elif self.__id__ == 191 and strName == u'AutomaticDeallocation':
            v = CDispatch()
            v.__instance_id__ = 192
            return v
        elif self.__id__ == 195 and strName == u'AutomaticAllocation':
            v = CDispatch()
            v.__instance_id__ = 196
            return v
        elif self.__id__ == 199 and strName == u'PoolID':
            v = CDispatch()
            v.__instance_id__ = 200
            return v
        elif self.__id__ == 203 and strName == u'Reservation':
            v = CDispatch()
            v.__instance_id__ = 204
            return v
        elif self.__id__ == 207 and strName == u'AllocationUnits':
            v = CDispatch()
            v.__instance_id__ = 208
            return v
        elif self.__id__ == 211 and strName == u'MappingBehavior':
            v = CDispatch()
            v.__instance_id__ = 212
            return v
        elif self.__id__ == 215 and strName == u'Address':
            v = CDispatch()
            v.__instance_id__ = 216
            return v
        elif self.__id__ == 219 and strName == u'OtherResourceType':
            v = CDispatch()
            v.__instance_id__ = 220
            return v
        elif self.__id__ == 223 and strName == u'Caption':
            v = CDispatch()
            v.__instance_id__ = 224
            return v
        elif self.__id__ == 227 and strName == u'ConsumerVisibility':
            v = CDispatch()
            v.__instance_id__ = 228
            return v
        elif self.__id__ == 231 and strName == u'Limit':
            v = CDispatch()
            v.__instance_id__ = 232
            return v
        elif self.__id__ == 235 and strName == u'ResourceType':
            v = CDispatch()
            v.__instance_id__ = 236
            return v
        elif self.__id__ == 239 and strName == u'Weight':
            v = CDispatch()
            v.__instance_id__ = 240
            return v
        elif self.__id__ == 241 and strName == u'VirtualSystemIdentifiers':
            v = CDispatch()
            v.__instance_id__ = 242
            return v
        elif self.__id__ == 245 and strName == u'Connection':
            v = CDispatch()
            v.__instance_id__ = 246
            return v
        elif self.__id__ == 258 and strName == u'InstanceID':
            v = CDispatch()
            v.__instance_id__ = 259
            return v
        elif self.__id__ == 262 and strName == u'ResourceSubType':
            v = CDispatch()
            v.__instance_id__ = 263
            return v
        elif self.__id__ == 266 and strName == u'HostResource':
            v = CDispatch()
            v.__instance_id__ = 267
            return v
        elif self.__id__ == 270 and strName == u'ElementName':
            v = CDispatch()
            v.__instance_id__ = 271
            return v
        elif self.__id__ == 274 and strName == u'Description':
            v = CDispatch()
            v.__instance_id__ = 275
            return v
        elif self.__id__ == 278 and strName == u'Parent':
            v = CDispatch()
            v.__instance_id__ = 279
            return v
        elif self.__id__ == 282 and strName == u'VirtualQuantity':
            v = CDispatch()
            v.__instance_id__ = 283
            return v
        elif self.__id__ == 286 and strName == u'AutomaticDeallocation':
            v = CDispatch()
            v.__instance_id__ = 287
            return v
        elif self.__id__ == 290 and strName == u'AutomaticAllocation':
            v = CDispatch()
            v.__instance_id__ = 291
            return v
        elif self.__id__ == 294 and strName == u'PoolID':
            v = CDispatch()
            v.__instance_id__ = 295
            return v
        elif self.__id__ == 298 and strName == u'Reservation':
            v = CDispatch()
            v.__instance_id__ = 299
            return v
        elif self.__id__ == 302 and strName == u'AllocationUnits':
            v = CDispatch()
            v.__instance_id__ = 303
            return v
        elif self.__id__ == 306 and strName == u'MappingBehavior':
            v = CDispatch()
            v.__instance_id__ = 307
            return v
        elif self.__id__ == 310 and strName == u'Address':
            v = CDispatch()
            v.__instance_id__ = 311
            return v
        elif self.__id__ == 314 and strName == u'OtherResourceType':
            v = CDispatch()
            v.__instance_id__ = 315
            return v
        elif self.__id__ == 318 and strName == u'Caption':
            v = CDispatch()
            v.__instance_id__ = 319
            return v
        elif self.__id__ == 322 and strName == u'ConsumerVisibility':
            v = CDispatch()
            v.__instance_id__ = 323
            return v
        elif self.__id__ == 326 and strName == u'Limit':
            v = CDispatch()
            v.__instance_id__ = 327
            return v
        elif self.__id__ == 330 and strName == u'ResourceType':
            v = CDispatch()
            v.__instance_id__ = 331
            return v
        elif self.__id__ == 334 and strName == u'Weight':
            v = CDispatch()
            v.__instance_id__ = 335
            return v
        elif self.__id__ == 336 and strName == u'VirtualSystemIdentifiers':
            v = CDispatch()
            v.__instance_id__ = 337
            return v
        elif self.__id__ == 340 and strName == u'Connection':
            v = CDispatch()
            v.__instance_id__ = 341
            return v
