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
            v.__instance_id__ = 403
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
        elif _WMI_count_3 == 2:
            v = _wmi_namespace()
            v.__instance_id__ = 363
        _WMI_count_3 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_StorageJob.InstanceID="30097D77-C5D9\
-48E9-BC16-55394F9D2161"':
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
 u'//HV12OSDEMO1/root/virtualization:Msvm_StorageJob.InstanceID="A1277F04-98ED\
-4B6C-8C3D-4342528C3819"':
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
        elif _WMI_count_5 == 9:
            v = _wmi_object()
            v.__instance_id__ = 35
        _WMI_count_5 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_ConcreteJob.InstanceID="B621668B-589\
B-4AED-A6C1-BACBEEEF52BB"':
        ret_value = None
        global _WMI_count_6
        if not '_WMI_count_6' in globals():
            _WMI_count_6 = 0
        if _WMI_count_6 == 0:
            v = _wmi_object()
            v.__instance_id__ = 356
        elif _WMI_count_6 == 1:
            v = _wmi_object()
            v.__instance_id__ = 357
        elif _WMI_count_6 == 2:
            v = _wmi_object()
            v.__instance_id__ = 358
        elif _WMI_count_6 == 3:
            v = _wmi_object()
            v.__instance_id__ = 359
        elif _WMI_count_6 == 4:
            v = _wmi_object()
            v.__instance_id__ = 360
        elif _WMI_count_6 == 5:
            v = _wmi_object()
            v.__instance_id__ = 361
        elif _WMI_count_6 == 6:
            v = _wmi_object()
            v.__instance_id__ = 362
        _WMI_count_6 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_ConcreteJob.InstanceID="ECA661CC-62C\
1-4B1D-A178-E9BBD8561901"':
        ret_value = None
        global _WMI_count_7
        if not '_WMI_count_7' in globals():
            _WMI_count_7 = 0
        if _WMI_count_7 == 0:
            v = _wmi_object()
            v.__instance_id__ = 372
        elif _WMI_count_7 == 1:
            v = _wmi_object()
            v.__instance_id__ = 373
        elif _WMI_count_7 == 2:
            v = _wmi_object()
            v.__instance_id__ = 374
        elif _WMI_count_7 == 3:
            v = _wmi_object()
            v.__instance_id__ = 375
        elif _WMI_count_7 == 4:
            v = _wmi_object()
            v.__instance_id__ = 376
        elif _WMI_count_7 == 5:
            v = _wmi_object()
            v.__instance_id__ = 377
        elif _WMI_count_7 == 6:
            v = _wmi_object()
            v.__instance_id__ = 378
        elif _WMI_count_7 == 7:
            v = _wmi_object()
            v.__instance_id__ = 379
        elif _WMI_count_7 == 8:
            v = _wmi_object()
            v.__instance_id__ = 380
        elif _WMI_count_7 == 9:
            v = _wmi_object()
            v.__instance_id__ = 381
        _WMI_count_7 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_StorageJob.InstanceID="EC2DD2C5-35F3\
-4F24-818E-3B204AA2552A"':
        ret_value = None
        global _WMI_count_8
        if not '_WMI_count_8' in globals():
            _WMI_count_8 = 0
        if _WMI_count_8 == 0:
            v = _wmi_object()
            v.__instance_id__ = 388
        elif _WMI_count_8 == 1:
            v = _wmi_object()
            v.__instance_id__ = 389
        elif _WMI_count_8 == 2:
            v = _wmi_object()
            v.__instance_id__ = 390
        elif _WMI_count_8 == 3:
            v = _wmi_object()
            v.__instance_id__ = 391
        elif _WMI_count_8 == 4:
            v = _wmi_object()
            v.__instance_id__ = 392
        elif _WMI_count_8 == 5:
            v = _wmi_object()
            v.__instance_id__ = 393
        elif _WMI_count_8 == 6:
            v = _wmi_object()
            v.__instance_id__ = 394
        elif _WMI_count_8 == 7:
            v = _wmi_object()
            v.__instance_id__ = 395
        elif _WMI_count_8 == 8:
            v = _wmi_object()
            v.__instance_id__ = 396
        _WMI_count_8 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_ConcreteJob.InstanceID="DD4B46C0-65F\
B-44F4-A9E0-85FD8B0AE141"':
        ret_value = None
        global _WMI_count_9
        if not '_WMI_count_9' in globals():
            _WMI_count_9 = 0
        if _WMI_count_9 == 0:
            v = _wmi_object()
            v.__instance_id__ = 399
        elif _WMI_count_9 == 1:
            v = _wmi_object()
            v.__instance_id__ = 400
        _WMI_count_9 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_ConcreteJob.InstanceID="57DC9C96-FBB\
8-4ED3-A03B-A535E4D87228"':
        ret_value = None
        global _WMI_count_10
        if not '_WMI_count_10' in globals():
            _WMI_count_10 = 0
        if _WMI_count_10 == 0:
            v = _wmi_object()
            v.__instance_id__ = 411
        elif _WMI_count_10 == 1:
            v = _wmi_object()
            v.__instance_id__ = 412
        _WMI_count_10 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_ConcreteJob.InstanceID="72C2A83D-6A2\
5-465B-A17E-416B99409C36"':
        ret_value = None
        global _WMI_count_11
        if not '_WMI_count_11' in globals():
            _WMI_count_11 = 0
        if _WMI_count_11 == 0:
            v = _wmi_object()
            v.__instance_id__ = 433
        elif _WMI_count_11 == 1:
            v = _wmi_object()
            v.__instance_id__ = 434
        _WMI_count_11 += 1
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
                v.__instance_id__ = 66
            elif self._Msvm_ResourceAllocationSettingData_count_0 == 1:
                v = _wmi_class()
                v.__instance_id__ = 160
            elif self._Msvm_ResourceAllocationSettingData_count_0 == 2:
                v = _wmi_class()
                v.__instance_id__ = 255
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
                v.__instance_id__ = 36
            elif self._Msvm_VirtualSystemManagementService_count_0 == 1:
                v = _wmi_class()
                v.__instance_id__ = 155
            elif self._Msvm_VirtualSystemManagementService_count_0 == 2:
                v = _wmi_class()
                v.__instance_id__ = 248
            elif self._Msvm_VirtualSystemManagementService_count_0 == 3:
                v = _wmi_class()
                v.__instance_id__ = 343
            elif self._Msvm_VirtualSystemManagementService_count_0 == 4:
                v = _wmi_class()
                v.__instance_id__ = 349
            self._Msvm_VirtualSystemManagementService_count_0 += 1
            return v
        elif self.__id__ == 11:
            v = _wmi_class()
            v.__instance_id__ = 406
            return v
        elif self.__id__ == 363:
            v = _wmi_class()
            v.__instance_id__ = 368
            return v

    @Msvm_VirtualSystemManagementService.setter
    def Msvm_VirtualSystemManagementService(self, value):
        pass

    @property
    def Msvm_VirtualSystemGlobalSettingData(self):
        if self.__id__ == 9:
            v = _wmi_class()
            v.__instance_id__ = 38
            return v

    @Msvm_VirtualSystemGlobalSettingData.setter
    def Msvm_VirtualSystemGlobalSettingData(self, value):
        pass

    @property
    def Msvm_ImageManagementService(self):
        if self.__id__ == 363:
            v = _wmi_class()
            v.__instance_id__ = 383
            return v

    @Msvm_ImageManagementService.setter
    def Msvm_ImageManagementService(self, value):
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
                v.__instance_id__ = 41
            elif self._Msvm_ComputerSystem_count_0 == 2:
                v = _wmi_class()
                v.__instance_id__ = 347
            elif self._Msvm_ComputerSystem_count_0 == 3:
                v = _wmi_class()
                v.__instance_id__ = 353
            self._Msvm_ComputerSystem_count_0 += 1
            return v
        elif self.__id__ == 11:
            ret_value = None
            if not hasattr(self, '_Msvm_ComputerSystem_count_1'):
                self._Msvm_ComputerSystem_count_1 = 0
            if self._Msvm_ComputerSystem_count_1 == 0:
                v = _wmi_class()
                v.__instance_id__ = 401
            elif self._Msvm_ComputerSystem_count_1 == 1:
                v = _wmi_class()
                v.__instance_id__ = 404
            elif self._Msvm_ComputerSystem_count_1 == 2:
                v = _wmi_class()
                v.__instance_id__ = 408
            elif self._Msvm_ComputerSystem_count_1 == 3:
                v = _wmi_class()
                v.__instance_id__ = 413
            self._Msvm_ComputerSystem_count_1 += 1
            return v
        elif self.__id__ == 363:
            ret_value = None
            if not hasattr(self, '_Msvm_ComputerSystem_count_2'):
                self._Msvm_ComputerSystem_count_2 = 0
            if self._Msvm_ComputerSystem_count_2 == 0:
                v = _wmi_class()
                v.__instance_id__ = 364
            elif self._Msvm_ComputerSystem_count_2 == 1:
                v = _wmi_class()
                v.__instance_id__ = 366
            self._Msvm_ComputerSystem_count_2 += 1
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
                v.__instance_id__ = 50
            elif self._MSVM_ComputerSystem_count_0 == 1:
                v = _wmi_class()
                v.__instance_id__ = 252
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
        elif self.__id__ == 403 and wql == u'Select * from CIM_DataFile where\
 Name =\
 \'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_d66dbe32-9e1c-4994-888\
4-70c064f3b8de\\openstack_unit_test_vm_d66dbe32-9e1c-4994-8884-70c064f3b8de.vh\
d\'':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 435
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
            v1.__instance_id__ = 65
            v.append(v1)
            return v
        elif self.__id__ == 9 and wql == 'SELECT * FROM\
 Msvm_ResourceAllocationSettingData                  WHERE ResourceSubType\
 LIKE \'Microsoft Virtual Hard Disk\' AND                  InstanceID LIKE\
 \'%Default%\' ':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 159
            v.append(v1)
            return v
        elif self.__id__ == 9 and wql == 'SELECT * FROM\
 Msvm_ResourceAllocationSettingData                 WHERE ResourceSubType =\
 \'Microsoft Synthetic SCSI Controller\'                AND InstanceID LIKE\
 \'%Default%\'':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 254
            v.append(v1)
            return v
        elif self.__id__ == 11 and wql == 'Select * from\
 Msvm_ImageManagementService':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 12
            v.append(v1)
            return v
        elif self.__id__ == 11 and wql == 'Select * from\
 Msvm_VirtualSystemSettingData where                 SettingType = 5 and\
 SystemName = \'openstack_unit_test_vm_d66dbe32-9e1c-4994-8884-70c064f3b8de\'':
            v = []
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
        elif self.__id__ == 50 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_d66dbe32-9e1c-4994-8884-70c064f3b8de':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 51
            v.append(v1)
            return v
        elif self.__id__ == 252 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_d66dbe32-9e1c-4994-8884-70c064f3b8de':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 253
            v.append(v1)
            return v
        elif self.__id__ == 10 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_d66dbe32-9e1c-4994-8884-70c064f3b8de':
            v = []
            return v
        elif self.__id__ == 41 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_d66dbe32-9e1c-4994-8884-70c064f3b8de':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 42
            v.append(v1)
            return v
        elif self.__id__ == 347 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_d66dbe32-9e1c-4994-8884-70c064f3b8de':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 348
            v.append(v1)
            return v
        elif self.__id__ == 353 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_d66dbe32-9e1c-4994-8884-70c064f3b8de':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 354
            v.append(v1)
            return v
        elif self.__id__ == 36:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 37
            v.append(v1)
            return v
        elif self.__id__ == 155:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 156
            v.append(v1)
            return v
        elif self.__id__ == 248:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 249
            v.append(v1)
            return v
        elif self.__id__ == 343:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 344
            v.append(v1)
            return v
        elif self.__id__ == 349:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 350
            v.append(v1)
            return v
        elif self.__id__ == 401 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_d66dbe32-9e1c-4994-8884-70c064f3b8de':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 402
            v.append(v1)
            return v
        elif self.__id__ == 404 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_d66dbe32-9e1c-4994-8884-70c064f3b8de':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 405
            v.append(v1)
            return v
        elif self.__id__ == 408 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_d66dbe32-9e1c-4994-8884-70c064f3b8de':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 409
            v.append(v1)
            return v
        elif self.__id__ == 413 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_d66dbe32-9e1c-4994-8884-70c064f3b8de':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 414
            v.append(v1)
            return v
        elif self.__id__ == 406:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 407
            v.append(v1)
            return v
        elif self.__id__ == 364 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_d66dbe32-9e1c-4994-8884-70c064f3b8de':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 365
            v.append(v1)
            return v
        elif self.__id__ == 366 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_d66dbe32-9e1c-4994-8884-70c064f3b8de':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 367
            v.append(v1)
            return v
        elif self.__id__ == 383:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 384
            v.append(v1)
            return v
        elif self.__id__ == 368:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 369
            v.append(v1)
            return v

    def new(self, **kwargs):
        if self.__id__ == 38:
            v = _wmi_object()
            v.__instance_id__ = 39
            return v
        elif self.__id__ == 66:
            v = _wmi_object()
            v.__instance_id__ = 67
            return v
        elif self.__id__ == 160:
            v = _wmi_object()
            v.__instance_id__ = 161
            return v
        elif self.__id__ == 255:
            v = _wmi_object()
            v.__instance_id__ = 256
            return v


class _wmi_object(object):

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__

    @property
    def path_(self):
        if self.__id__ == 61:
            v = CDispatch()
            v.__instance_id__ = 154
            return v
        elif self.__id__ == 51:
            ret_value = None
            if not hasattr(self, '_path__count_1'):
                self._path__count_1 = 0
            if self._path__count_1 == 0:
                v = CDispatch()
                v.__instance_id__ = 158
            elif self._path__count_1 == 1:
                v = CDispatch()
                v.__instance_id__ = 251
            self._path__count_1 += 1
            return v
        elif self.__id__ == 253:
            v = CDispatch()
            v.__instance_id__ = 346
            return v
        elif self.__id__ == 42:
            ret_value = None
            if not hasattr(self, '_path__count_3'):
                self._path__count_3 = 0
            if self._path__count_3 == 0:
                v = CDispatch()
                v.__instance_id__ = 46
            elif self._path__count_3 == 1:
                v = CDispatch()
                v.__instance_id__ = 49
            self._path__count_3 += 1
            return v
        elif self.__id__ == 348:
            v = CDispatch()
            v.__instance_id__ = 352
            return v
        elif self.__id__ == 405:
            v = CDispatch()
            v.__instance_id__ = 432
            return v
        elif self.__id__ == 367:
            v = CDispatch()
            v.__instance_id__ = 371
            return v
        elif self.__id__ == 382:
            v = CDispatch()
            v.__instance_id__ = 398
            return v

    @path_.setter
    def path_(self, value):
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
    def ModifyVirtualSystemResources(self):
        if self.__id__ == 37:
            ret_value = None
            if not hasattr(self, '_ModifyVirtualSystemResources_count_0'):
                self._ModifyVirtualSystemResources_count_0 = 0
            if self._ModifyVirtualSystemResources_count_0 == 0:
                v = _wmi_method()
                v.__instance_id__ = 45
            elif self._ModifyVirtualSystemResources_count_0 == 1:
                v = _wmi_method()
                v.__instance_id__ = 48
            self._ModifyVirtualSystemResources_count_0 += 1
            return v

    @ModifyVirtualSystemResources.setter
    def ModifyVirtualSystemResources(self, value):
        pass

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
    def MergeVirtualHardDisk(self):
        if self.__id__ == 384:
            v = _wmi_method()
            v.__instance_id__ = 387
            return v

    @MergeVirtualHardDisk.setter
    def MergeVirtualHardDisk(self, value):
        pass

    @property
    def ElementName(self):
        if self.__id__ == 365:
            return\
 u'openstack_unit_test_vm_d66dbe32-9e1c-4994-8884-70c064f3b8de'

    @ElementName.setter
    def ElementName(self, value):
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
            return 4
        elif self.__id__ == 35:
            ret_value = None
            if not hasattr(self, '_JobState_count_19'):
                self._JobState_count_19 = 0
            if self._JobState_count_19 == 0:
                v = 7
            elif self._JobState_count_19 == 1:
                v = 7
            self._JobState_count_19 += 1
            return v
        elif self.__id__ == 356:
            return 4
        elif self.__id__ == 357:
            return 4
        elif self.__id__ == 358:
            return 4
        elif self.__id__ == 359:
            return 4
        elif self.__id__ == 360:
            return 4
        elif self.__id__ == 361:
            return 4
        elif self.__id__ == 362:
            ret_value = None
            if not hasattr(self, '_JobState_count_26'):
                self._JobState_count_26 = 0
            if self._JobState_count_26 == 0:
                v = 7
            elif self._JobState_count_26 == 1:
                v = 7
            self._JobState_count_26 += 1
            return v
        elif self.__id__ == 372:
            return 4
        elif self.__id__ == 373:
            return 4
        elif self.__id__ == 374:
            return 4
        elif self.__id__ == 375:
            return 4
        elif self.__id__ == 376:
            return 4
        elif self.__id__ == 377:
            return 4
        elif self.__id__ == 378:
            return 4
        elif self.__id__ == 379:
            return 4
        elif self.__id__ == 380:
            ret_value = None
            if not hasattr(self, '_JobState_count_35'):
                self._JobState_count_35 = 0
            if self._JobState_count_35 == 0:
                v = 7
            elif self._JobState_count_35 == 1:
                v = 7
            self._JobState_count_35 += 1
            return v
        elif self.__id__ == 388:
            return 4
        elif self.__id__ == 389:
            return 4
        elif self.__id__ == 390:
            return 4
        elif self.__id__ == 391:
            return 4
        elif self.__id__ == 392:
            return 4
        elif self.__id__ == 393:
            return 4
        elif self.__id__ == 394:
            return 4
        elif self.__id__ == 395:
            return 4
        elif self.__id__ == 396:
            ret_value = None
            if not hasattr(self, '_JobState_count_44'):
                self._JobState_count_44 = 0
            if self._JobState_count_44 == 0:
                v = 7
            elif self._JobState_count_44 == 1:
                v = 7
            self._JobState_count_44 += 1
            return v
        elif self.__id__ == 399:
            return 4
        elif self.__id__ == 400:
            ret_value = None
            if not hasattr(self, '_JobState_count_46'):
                self._JobState_count_46 = 0
            if self._JobState_count_46 == 0:
                v = 7
            elif self._JobState_count_46 == 1:
                v = 7
            self._JobState_count_46 += 1
            return v
        elif self.__id__ == 411:
            return 4
        elif self.__id__ == 412:
            ret_value = None
            if not hasattr(self, '_JobState_count_48'):
                self._JobState_count_48 = 0
            if self._JobState_count_48 == 0:
                v = 7
            elif self._JobState_count_48 == 1:
                v = 7
            self._JobState_count_48 += 1
            return v
        elif self.__id__ == 433:
            return 4
        elif self.__id__ == 434:
            ret_value = None
            if not hasattr(self, '_JobState_count_50'):
                self._JobState_count_50 = 0
            if self._JobState_count_50 == 0:
                v = 7
            elif self._JobState_count_50 == 1:
                v = 7
            self._JobState_count_50 += 1
            return v

    @JobState.setter
    def JobState(self, value):
        pass

    @property
    def Description(self):
        if self.__id__ == 35:
            return u'Creating Virtual Hard Disk'
        elif self.__id__ == 362:
            return u'Initializing and Starting Virtual Machine'
        elif self.__id__ == 380:
            return u'Taking Virtual Machine Snapshot'
        elif self.__id__ == 396:
            return u'Merging Virtual Disk'
        elif self.__id__ == 400:
            return u'Deleting Snapshot'

    @Description.setter
    def Description(self, value):
        pass

    @property
    def AddVirtualSystemResources(self):
        if self.__id__ == 156:
            v = _wmi_method()
            v.__instance_id__ = 157
            return v
        elif self.__id__ == 249:
            v = _wmi_method()
            v.__instance_id__ = 250
            return v
        elif self.__id__ == 344:
            v = _wmi_method()
            v.__instance_id__ = 345
            return v
        elif self.__id__ == 350:
            v = _wmi_method()
            v.__instance_id__ = 351
            return v

    @AddVirtualSystemResources.setter
    def AddVirtualSystemResources(self, value):
        pass

    @property
    def GetVirtualHardDiskInfo(self):
        if self.__id__ == 384:
            v = _wmi_method()
            v.__instance_id__ = 385
            return v

    @GetVirtualHardDiskInfo.setter
    def GetVirtualHardDiskInfo(self, value):
        pass

    @property
    def Properties_(self):
        if self.__id__ == 65:
            ret_value = None
            if not hasattr(self, '_Properties__count_0'):
                self._Properties__count_0 = 0
            if self._Properties__count_0 == 0:
                v = CDispatch()
                v.__instance_id__ = 68
            elif self._Properties__count_0 == 1:
                v = CDispatch()
                v.__instance_id__ = 72
            elif self._Properties__count_0 == 2:
                v = CDispatch()
                v.__instance_id__ = 76
            elif self._Properties__count_0 == 3:
                v = CDispatch()
                v.__instance_id__ = 80
            elif self._Properties__count_0 == 4:
                v = CDispatch()
                v.__instance_id__ = 84
            elif self._Properties__count_0 == 5:
                v = CDispatch()
                v.__instance_id__ = 88
            elif self._Properties__count_0 == 6:
                v = CDispatch()
                v.__instance_id__ = 92
            elif self._Properties__count_0 == 7:
                v = CDispatch()
                v.__instance_id__ = 96
            elif self._Properties__count_0 == 8:
                v = CDispatch()
                v.__instance_id__ = 100
            elif self._Properties__count_0 == 9:
                v = CDispatch()
                v.__instance_id__ = 104
            elif self._Properties__count_0 == 10:
                v = CDispatch()
                v.__instance_id__ = 108
            elif self._Properties__count_0 == 11:
                v = CDispatch()
                v.__instance_id__ = 112
            elif self._Properties__count_0 == 12:
                v = CDispatch()
                v.__instance_id__ = 116
            elif self._Properties__count_0 == 13:
                v = CDispatch()
                v.__instance_id__ = 120
            elif self._Properties__count_0 == 14:
                v = CDispatch()
                v.__instance_id__ = 124
            elif self._Properties__count_0 == 15:
                v = CDispatch()
                v.__instance_id__ = 128
            elif self._Properties__count_0 == 16:
                v = CDispatch()
                v.__instance_id__ = 132
            elif self._Properties__count_0 == 17:
                v = CDispatch()
                v.__instance_id__ = 136
            elif self._Properties__count_0 == 18:
                v = CDispatch()
                v.__instance_id__ = 140
            elif self._Properties__count_0 == 19:
                v = CDispatch()
                v.__instance_id__ = 144
            elif self._Properties__count_0 == 20:
                v = CDispatch()
                v.__instance_id__ = 150
            self._Properties__count_0 += 1
            return v
        elif self.__id__ == 159:
            ret_value = None
            if not hasattr(self, '_Properties__count_1'):
                self._Properties__count_1 = 0
            if self._Properties__count_1 == 0:
                v = CDispatch()
                v.__instance_id__ = 162
            elif self._Properties__count_1 == 1:
                v = CDispatch()
                v.__instance_id__ = 166
            elif self._Properties__count_1 == 2:
                v = CDispatch()
                v.__instance_id__ = 170
            elif self._Properties__count_1 == 3:
                v = CDispatch()
                v.__instance_id__ = 174
            elif self._Properties__count_1 == 4:
                v = CDispatch()
                v.__instance_id__ = 178
            elif self._Properties__count_1 == 5:
                v = CDispatch()
                v.__instance_id__ = 182
            elif self._Properties__count_1 == 6:
                v = CDispatch()
                v.__instance_id__ = 186
            elif self._Properties__count_1 == 7:
                v = CDispatch()
                v.__instance_id__ = 190
            elif self._Properties__count_1 == 8:
                v = CDispatch()
                v.__instance_id__ = 194
            elif self._Properties__count_1 == 9:
                v = CDispatch()
                v.__instance_id__ = 198
            elif self._Properties__count_1 == 10:
                v = CDispatch()
                v.__instance_id__ = 202
            elif self._Properties__count_1 == 11:
                v = CDispatch()
                v.__instance_id__ = 206
            elif self._Properties__count_1 == 12:
                v = CDispatch()
                v.__instance_id__ = 210
            elif self._Properties__count_1 == 13:
                v = CDispatch()
                v.__instance_id__ = 214
            elif self._Properties__count_1 == 14:
                v = CDispatch()
                v.__instance_id__ = 218
            elif self._Properties__count_1 == 15:
                v = CDispatch()
                v.__instance_id__ = 222
            elif self._Properties__count_1 == 16:
                v = CDispatch()
                v.__instance_id__ = 226
            elif self._Properties__count_1 == 17:
                v = CDispatch()
                v.__instance_id__ = 230
            elif self._Properties__count_1 == 18:
                v = CDispatch()
                v.__instance_id__ = 234
            elif self._Properties__count_1 == 19:
                v = CDispatch()
                v.__instance_id__ = 238
            elif self._Properties__count_1 == 20:
                v = CDispatch()
                v.__instance_id__ = 244
            self._Properties__count_1 += 1
            return v
        elif self.__id__ == 254:
            ret_value = None
            if not hasattr(self, '_Properties__count_2'):
                self._Properties__count_2 = 0
            if self._Properties__count_2 == 0:
                v = CDispatch()
                v.__instance_id__ = 257
            elif self._Properties__count_2 == 1:
                v = CDispatch()
                v.__instance_id__ = 261
            elif self._Properties__count_2 == 2:
                v = CDispatch()
                v.__instance_id__ = 265
            elif self._Properties__count_2 == 3:
                v = CDispatch()
                v.__instance_id__ = 269
            elif self._Properties__count_2 == 4:
                v = CDispatch()
                v.__instance_id__ = 273
            elif self._Properties__count_2 == 5:
                v = CDispatch()
                v.__instance_id__ = 277
            elif self._Properties__count_2 == 6:
                v = CDispatch()
                v.__instance_id__ = 281
            elif self._Properties__count_2 == 7:
                v = CDispatch()
                v.__instance_id__ = 285
            elif self._Properties__count_2 == 8:
                v = CDispatch()
                v.__instance_id__ = 289
            elif self._Properties__count_2 == 9:
                v = CDispatch()
                v.__instance_id__ = 293
            elif self._Properties__count_2 == 10:
                v = CDispatch()
                v.__instance_id__ = 297
            elif self._Properties__count_2 == 11:
                v = CDispatch()
                v.__instance_id__ = 301
            elif self._Properties__count_2 == 12:
                v = CDispatch()
                v.__instance_id__ = 305
            elif self._Properties__count_2 == 13:
                v = CDispatch()
                v.__instance_id__ = 309
            elif self._Properties__count_2 == 14:
                v = CDispatch()
                v.__instance_id__ = 313
            elif self._Properties__count_2 == 15:
                v = CDispatch()
                v.__instance_id__ = 317
            elif self._Properties__count_2 == 16:
                v = CDispatch()
                v.__instance_id__ = 321
            elif self._Properties__count_2 == 17:
                v = CDispatch()
                v.__instance_id__ = 325
            elif self._Properties__count_2 == 18:
                v = CDispatch()
                v.__instance_id__ = 329
            elif self._Properties__count_2 == 19:
                v = CDispatch()
                v.__instance_id__ = 333
            elif self._Properties__count_2 == 20:
                v = CDispatch()
                v.__instance_id__ = 339
            self._Properties__count_2 += 1
            return v
        elif self.__id__ == 67:
            ret_value = None
            if not hasattr(self, '_Properties__count_3'):
                self._Properties__count_3 = 0
            if self._Properties__count_3 == 0:
                v = CDispatch()
                v.__instance_id__ = 70
            elif self._Properties__count_3 == 1:
                v = CDispatch()
                v.__instance_id__ = 74
            elif self._Properties__count_3 == 2:
                v = CDispatch()
                v.__instance_id__ = 78
            elif self._Properties__count_3 == 3:
                v = CDispatch()
                v.__instance_id__ = 82
            elif self._Properties__count_3 == 4:
                v = CDispatch()
                v.__instance_id__ = 86
            elif self._Properties__count_3 == 5:
                v = CDispatch()
                v.__instance_id__ = 90
            elif self._Properties__count_3 == 6:
                v = CDispatch()
                v.__instance_id__ = 94
            elif self._Properties__count_3 == 7:
                v = CDispatch()
                v.__instance_id__ = 98
            elif self._Properties__count_3 == 8:
                v = CDispatch()
                v.__instance_id__ = 102
            elif self._Properties__count_3 == 9:
                v = CDispatch()
                v.__instance_id__ = 106
            elif self._Properties__count_3 == 10:
                v = CDispatch()
                v.__instance_id__ = 110
            elif self._Properties__count_3 == 11:
                v = CDispatch()
                v.__instance_id__ = 114
            elif self._Properties__count_3 == 12:
                v = CDispatch()
                v.__instance_id__ = 118
            elif self._Properties__count_3 == 13:
                v = CDispatch()
                v.__instance_id__ = 122
            elif self._Properties__count_3 == 14:
                v = CDispatch()
                v.__instance_id__ = 126
            elif self._Properties__count_3 == 15:
                v = CDispatch()
                v.__instance_id__ = 130
            elif self._Properties__count_3 == 16:
                v = CDispatch()
                v.__instance_id__ = 134
            elif self._Properties__count_3 == 17:
                v = CDispatch()
                v.__instance_id__ = 138
            elif self._Properties__count_3 == 18:
                v = CDispatch()
                v.__instance_id__ = 142
            elif self._Properties__count_3 == 19:
                v = CDispatch()
                v.__instance_id__ = 146
            elif self._Properties__count_3 == 20:
                v = CDispatch()
                v.__instance_id__ = 148
            elif self._Properties__count_3 == 21:
                v = CDispatch()
                v.__instance_id__ = 152
            self._Properties__count_3 += 1
            return v
        elif self.__id__ == 161:
            ret_value = None
            if not hasattr(self, '_Properties__count_4'):
                self._Properties__count_4 = 0
            if self._Properties__count_4 == 0:
                v = CDispatch()
                v.__instance_id__ = 164
            elif self._Properties__count_4 == 1:
                v = CDispatch()
                v.__instance_id__ = 168
            elif self._Properties__count_4 == 2:
                v = CDispatch()
                v.__instance_id__ = 172
            elif self._Properties__count_4 == 3:
                v = CDispatch()
                v.__instance_id__ = 176
            elif self._Properties__count_4 == 4:
                v = CDispatch()
                v.__instance_id__ = 180
            elif self._Properties__count_4 == 5:
                v = CDispatch()
                v.__instance_id__ = 184
            elif self._Properties__count_4 == 6:
                v = CDispatch()
                v.__instance_id__ = 188
            elif self._Properties__count_4 == 7:
                v = CDispatch()
                v.__instance_id__ = 192
            elif self._Properties__count_4 == 8:
                v = CDispatch()
                v.__instance_id__ = 196
            elif self._Properties__count_4 == 9:
                v = CDispatch()
                v.__instance_id__ = 200
            elif self._Properties__count_4 == 10:
                v = CDispatch()
                v.__instance_id__ = 204
            elif self._Properties__count_4 == 11:
                v = CDispatch()
                v.__instance_id__ = 208
            elif self._Properties__count_4 == 12:
                v = CDispatch()
                v.__instance_id__ = 212
            elif self._Properties__count_4 == 13:
                v = CDispatch()
                v.__instance_id__ = 216
            elif self._Properties__count_4 == 14:
                v = CDispatch()
                v.__instance_id__ = 220
            elif self._Properties__count_4 == 15:
                v = CDispatch()
                v.__instance_id__ = 224
            elif self._Properties__count_4 == 16:
                v = CDispatch()
                v.__instance_id__ = 228
            elif self._Properties__count_4 == 17:
                v = CDispatch()
                v.__instance_id__ = 232
            elif self._Properties__count_4 == 18:
                v = CDispatch()
                v.__instance_id__ = 236
            elif self._Properties__count_4 == 19:
                v = CDispatch()
                v.__instance_id__ = 240
            elif self._Properties__count_4 == 20:
                v = CDispatch()
                v.__instance_id__ = 242
            elif self._Properties__count_4 == 21:
                v = CDispatch()
                v.__instance_id__ = 246
            self._Properties__count_4 += 1
            return v
        elif self.__id__ == 256:
            ret_value = None
            if not hasattr(self, '_Properties__count_5'):
                self._Properties__count_5 = 0
            if self._Properties__count_5 == 0:
                v = CDispatch()
                v.__instance_id__ = 259
            elif self._Properties__count_5 == 1:
                v = CDispatch()
                v.__instance_id__ = 263
            elif self._Properties__count_5 == 2:
                v = CDispatch()
                v.__instance_id__ = 267
            elif self._Properties__count_5 == 3:
                v = CDispatch()
                v.__instance_id__ = 271
            elif self._Properties__count_5 == 4:
                v = CDispatch()
                v.__instance_id__ = 275
            elif self._Properties__count_5 == 5:
                v = CDispatch()
                v.__instance_id__ = 279
            elif self._Properties__count_5 == 6:
                v = CDispatch()
                v.__instance_id__ = 283
            elif self._Properties__count_5 == 7:
                v = CDispatch()
                v.__instance_id__ = 287
            elif self._Properties__count_5 == 8:
                v = CDispatch()
                v.__instance_id__ = 291
            elif self._Properties__count_5 == 9:
                v = CDispatch()
                v.__instance_id__ = 295
            elif self._Properties__count_5 == 10:
                v = CDispatch()
                v.__instance_id__ = 299
            elif self._Properties__count_5 == 11:
                v = CDispatch()
                v.__instance_id__ = 303
            elif self._Properties__count_5 == 12:
                v = CDispatch()
                v.__instance_id__ = 307
            elif self._Properties__count_5 == 13:
                v = CDispatch()
                v.__instance_id__ = 311
            elif self._Properties__count_5 == 14:
                v = CDispatch()
                v.__instance_id__ = 315
            elif self._Properties__count_5 == 15:
                v = CDispatch()
                v.__instance_id__ = 319
            elif self._Properties__count_5 == 16:
                v = CDispatch()
                v.__instance_id__ = 323
            elif self._Properties__count_5 == 17:
                v = CDispatch()
                v.__instance_id__ = 327
            elif self._Properties__count_5 == 18:
                v = CDispatch()
                v.__instance_id__ = 331
            elif self._Properties__count_5 == 19:
                v = CDispatch()
                v.__instance_id__ = 335
            elif self._Properties__count_5 == 20:
                v = CDispatch()
                v.__instance_id__ = 337
            elif self._Properties__count_5 == 21:
                v = CDispatch()
                v.__instance_id__ = 341
            self._Properties__count_5 += 1
            return v

    @Properties_.setter
    def Properties_(self, value):
        pass

    @property
    def Address(self):
        if self.__id__ == 61:
            return u'0'
        elif self.__id__ == 62:
            return u'1'

    @Address.setter
    def Address(self, value):
        pass

    @property
    def RemoveVirtualSystemSnapshot(self):
        if self.__id__ == 369:
            v = _wmi_method()
            v.__instance_id__ = 397
            return v

    @RemoveVirtualSystemSnapshot.setter
    def RemoveVirtualSystemSnapshot(self, value):
        pass

    @property
    def RequestStateChange(self):
        if self.__id__ == 354:
            v = _wmi_method()
            v.__instance_id__ = 355
            return v
        elif self.__id__ == 409:
            v = _wmi_method()
            v.__instance_id__ = 410
            return v

    @RequestStateChange.setter
    def RequestStateChange(self, value):
        pass

    @property
    def DefineVirtualSystem(self):
        if self.__id__ == 37:
            v = _wmi_method()
            v.__instance_id__ = 40
            return v

    @DefineVirtualSystem.setter
    def DefineVirtualSystem(self, value):
        pass

    @property
    def _properties(self):
        if self.__id__ == 65:
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
        elif self.__id__ == 159:
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
        elif self.__id__ == 254:
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
    def ElapsedTime(self):
        if self.__id__ == 35:
            return u'00000000000001.009001:000'
        elif self.__id__ == 362:
            return u'00000000000000.825023:000'
        elif self.__id__ == 380:
            return u'00000000000001.500355:000'
        elif self.__id__ == 396:
            return u'00000000000001.022890:000'
        elif self.__id__ == 400:
            return u'00000000000000.190842:000'

    @ElapsedTime.setter
    def ElapsedTime(self, value):
        pass

    @property
    def Connection(self):
        if self.__id__ == 425:
            v = ()
            v1 =\
 u'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_d66dbe32-9e1c-4994-888\
4-70c064f3b8de\\openstack_unit_test_vm_d66dbe32-9e1c-4994-8884-70c064f3b8de.vh\
d'
            v += (v1,)
            return v

    @Connection.setter
    def Connection(self, value):
        pass

    @property
    def Delete(self):
        if self.__id__ == 435:
            v = _wmi_method()
            v.__instance_id__ = 436
            return v

    @Delete.setter
    def Delete(self, value):
        pass

    @property
    def DestroyVirtualSystem(self):
        if self.__id__ == 407:
            v = _wmi_method()
            v.__instance_id__ = 431
            return v

    @DestroyVirtualSystem.setter
    def DestroyVirtualSystem(self, value):
        pass

    @property
    def ResourceSubType(self):
        if self.__id__ == 53:
            return u'Microsoft Virtual Keyboard'
        elif self.__id__ == 54:
            return u'Microsoft Virtual PS2 Mouse'
        elif self.__id__ == 55:
            return u'Microsoft S3 Display Controller'
        elif self.__id__ == 56:
            return u'Microsoft Synthetic Diskette Drive'
        elif self.__id__ == 57:
            return None
        elif self.__id__ == 58:
            return u'Microsoft Serial Controller'
        elif self.__id__ == 59:
            return u'Microsoft Serial Port'
        elif self.__id__ == 60:
            return u'Microsoft Serial Port'
        elif self.__id__ == 61:
            return u'Microsoft Emulated IDE Controller'
        elif self.__id__ == 62:
            return u'Microsoft Emulated IDE Controller'
        elif self.__id__ == 63:
            return u'Microsoft Synthetic Mouse'
        elif self.__id__ == 64:
            return u'Microsoft Synthetic Display Controller'
        elif self.__id__ == 416:
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
        elif self.__id__ == 417:
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
        elif self.__id__ == 418:
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
        elif self.__id__ == 419:
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
        elif self.__id__ == 420:
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
        elif self.__id__ == 421:
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
        elif self.__id__ == 422:
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
        elif self.__id__ == 423:
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
        elif self.__id__ == 424:
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
        elif self.__id__ == 425:
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
        elif self.__id__ == 426:
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
        elif self.__id__ == 427:
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
        elif self.__id__ == 428:
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
        elif self.__id__ == 429:
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
        elif self.__id__ == 430:
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
    def CreateVirtualSystemSnapshot(self):
        if self.__id__ == 369:
            v = _wmi_method()
            v.__instance_id__ = 370
            return v

    @CreateVirtualSystemSnapshot.setter
    def CreateVirtualSystemSnapshot(self, value):
        pass

    @property
    def ReconnectParentVirtualHardDisk(self):
        if self.__id__ == 384:
            v = _wmi_method()
            v.__instance_id__ = 386
            return v

    @ReconnectParentVirtualHardDisk.setter
    def ReconnectParentVirtualHardDisk(self, value):
        pass

    @property
    def SettingType(self):
        if self.__id__ == 43:
            return 3

    @SettingType.setter
    def SettingType(self, value):
        pass

    def associators(self, wmi_association_class='', wmi_result_class=''):
        if self.__id__ == 52 and wmi_result_class ==\
 'MSVM_ResourceAllocationSettingData':
            v = []
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
            v1 = _wmi_object()
            v1.__instance_id__ = 64
            v.append(v1)
            return v
        elif self.__id__ == 51 and wmi_result_class ==\
 'Msvm_VirtualSystemSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 52
            v.append(v1)
            return v
        elif self.__id__ == 43 and wmi_result_class ==\
 'Msvm_MemorySettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 44
            v.append(v1)
            return v
        elif self.__id__ == 43 and wmi_result_class ==\
 'Msvm_ProcessorSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 47
            v.append(v1)
            return v
        elif self.__id__ == 42 and wmi_result_class ==\
 'Msvm_VirtualSystemSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 43
            v.append(v1)
            return v
        elif self.__id__ == 415 and wmi_result_class ==\
 'MSVM_ResourceAllocationSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 416
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 417
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 418
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 419
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 420
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 421
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 422
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 423
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 424
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 425
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 426
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 427
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 428
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 429
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 430
            v.append(v1)
            return v
        elif self.__id__ == 414 and wmi_result_class ==\
 'Msvm_VirtualSystemSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 415
            v.append(v1)
            return v
        elif self.__id__ == 381 and wmi_result_class ==\
 'Msvm_VirtualSystemSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 382
            v.append(v1)
            return v

    def GetText_(self, iObjectTextFormat='<PyOleMissing object at\
 0x04091890>', iFlags=0, objWbemNamedValueSet=None):
        if self.__id__ == 44 and iObjectTextFormat == 1:
            return u'<INSTANCE CLASSNAME="Msvm_MemorySettingData"><PROPERTY\
 NAME="__PATH" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>\\\\HV12OSDEMO1\\root\\virtualization:Msvm_MemorySetting\
Data.InstanceID="Microsoft:9F222654-941B-4DDF-AA8F-8002A3F3BF86\\\\4764334d-e0\
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
 TYPE="string"><VALUE>Msvm_MemorySettingData.InstanceID="Microsoft:9F222654-94\
1B-4DDF-AA8F-8002A3F3BF86\\\\4764334d-e001-4176-82ee-5594ec9b530e"</VALUE></PR\
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
 TYPE="string"><VALUE>Microsoft:9F222654-941B-4DDF-AA8F-8002A3F3BF86\\4764334d\
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
        elif self.__id__ == 47 and iObjectTextFormat == 1:
            return u'<INSTANCE CLASSNAME="Msvm_ProcessorSettingData"><PROPERTY\
 NAME="__PATH" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ProcessorSett\
ingData.InstanceID="Microsoft:9F222654-941B-4DDF-AA8F-8002A3F3BF86\\\\b637f346\
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
 TYPE="string"><VALUE>Msvm_ProcessorSettingData.InstanceID="Microsoft:9F222654\
-941B-4DDF-AA8F-8002A3F3BF86\\\\b637f346-6a0e-4dec-af52-bd70cb80a21d\\\\0"</VA\
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
 TYPE="string"><VALUE>Microsoft:9F222654-941B-4DDF-AA8F-8002A3F3BF86\\b637f346\
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
        elif self.__id__ == 39 and iObjectTextFormat == 1:
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
 TYPE="string"><VALUE>openstack_unit_test_vm_d66dbe32-9e1c-4994-8884-70c064f3b\
8de</VALUE></PROPERTY><PROPERTY NAME="ExternalDataRoot"\
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
        elif self.__id__ == 67 and iObjectTextFormat == 1:
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
ationSettingData.InstanceID="Microsoft:9F222654-941B-4DDF-AA8F-8002A3F3BF86\
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
 TYPE="string"><VALUE.ARRAY><VALUE>26166620-076d-41b1-b5f0-9bbde4ff29e3</VALUE\
></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>'
        elif self.__id__ == 161 and iObjectTextFormat == 1:
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
t_test_vm_d66dbe32-9e1c-4994-8884-70c064f3b8de\\openstack_unit_test_vm_d66dbe3\
2-9e1c-4994-8884-70c064f3b8de.vhd</VALUE></VALUE.ARRAY></PROPERTY.ARRAY><PROPE\
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
ationSettingData.InstanceID="Microsoft:9F222654-941B-4DDF-AA8F-8002A3F3BF86\
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
 TYPE="string"><VALUE.ARRAY><VALUE>d7e792a2-ca61-4ebb-8502-dc1fa5fd3bae</VALUE\
></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>'
        elif self.__id__ == 256 and iObjectTextFormat == 1:
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
 TYPE="string"><VALUE.ARRAY><VALUE>{b79076bb-a6e3-4520-8e4a-3322b965305d}</VAL\
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
        if len(args) == 0 and self.__id__ == 436:
            v = ()
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 0 and self.__id__ == 25 and kwargs.get('Path') ==\
 'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_d66dbe32-9e1c-4994-8884\
-70c064f3b8de\\openstack_unit_test_vm_d66dbe32-9e1c-4994-8884-70c064f3b8de.vhd\
' and kwargs.get('ParentPath') == 'C:\\Hyper-V\\test\\instances\\_base\\1.vhd':
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_StorageJob.InstanceID="A1277F04-\
98ED-4B6C-8C3D-4342528C3819"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v
        elif len(args) == 1 and self.__id__ == 355 and args[0] == 2:
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ConcreteJob.InstanceID="B621668B\
-589B-4AED-A6C1-BACBEEEF52BB"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v
        elif len(args) == 3 and self.__id__ == 40 and str(args[0]) == '[]' and\
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
 TYPE="string"><VALUE>openstack_unit_test_vm_d66dbe32-9e1c-4994-8884-70c064f3b\
8de</VALUE></PROPERTY><PROPERTY NAME="ExternalDataRoot"\
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
="Msvm_ComputerSystem",Name="9F222654-941B-4DDF-AA8F-8002A3F3BF86"'
            v += (v1,)
            v1 = None
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 2 and self.__id__ == 45 and args[0] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="9F222654-941B-4DDF-AA8F-8002A3F3BF86"' and\
 str(args[1]) == '[u\'<INSTANCE CLASSNAME="Msvm_MemorySettingData"><PROPERTY\
 NAME="__PATH" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>\\\\\\\\HV12OSDEMO1\\\\root\\\\virtualization:Msvm_Memor\
ySettingData.InstanceID="Microsoft:9F222654-941B-4DDF-AA8F-8002A3F3BF86\
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
 TYPE="string"><VALUE>Msvm_MemorySettingData.InstanceID="Microsoft:9F222654-94\
1B-4DDF-AA8F-8002A3F3BF86\\\\\\\\4764334d-e001-4176-82ee-5594ec9b530e"</VALUE>\
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
 TYPE="string"><VALUE>Microsoft:9F222654-941B-4DDF-AA8F-8002A3F3BF86\\\\476433\
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
        elif len(args) == 2 and self.__id__ == 48 and args[0] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="9F222654-941B-4DDF-AA8F-8002A3F3BF86"' and\
 str(args[1]) == '[u\'<INSTANCE\
 CLASSNAME="Msvm_ProcessorSettingData"><PROPERTY NAME="__PATH"\
 CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>\\\\\\\\HV12OSDEMO1\\\\root\\\\virtualization:Msvm_Proce\
ssorSettingData.InstanceID="Microsoft:9F222654-941B-4DDF-AA8F-8002A3F3BF86\
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
 TYPE="string"><VALUE>Msvm_ProcessorSettingData.InstanceID="Microsoft:9F222654\
-941B-4DDF-AA8F-8002A3F3BF86\\\\\\\\b637f346-6a0e-4dec-af52-bd70cb80a21d\
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
 TYPE="string"><VALUE>Microsoft:9F222654-941B-4DDF-AA8F-8002A3F3BF86\\\\b637f3\
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
        elif len(args) == 2 and self.__id__ == 157 and str(args[0]) ==\
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
rceAllocationSettingData.InstanceID="Microsoft:9F222654-941B-4DDF-AA8F-8002A3F\
3BF86\\\\\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\\\\\0"</VALUE></PROPERTY>\
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
 TYPE="string"><VALUE.ARRAY><VALUE>26166620-076d-41b1-b5f0-9bbde4ff29e3</VALUE\
></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="9F222654-941B-4DDF-AA8F-8002A3F3BF86"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:9F222654-941B-4DDF-AA8F-8002A3F3BF86\\\\83F8638B-8DCA-4152\
-9EDA-2CA8B33039B4\\\\0\\\\0\\\\D"'
            v1.append(v2)
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 2 and self.__id__ == 250 and str(args[0]) ==\
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
tack_unit_test_vm_d66dbe32-9e1c-4994-8884-70c064f3b8de\\\\openstack_unit_test_\
vm_d66dbe32-9e1c-4994-8884-70c064f3b8de.vhd</VALUE></VALUE.ARRAY></PROPERTY.AR\
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
rceAllocationSettingData.InstanceID="Microsoft:9F222654-941B-4DDF-AA8F-8002A3F\
3BF86\\\\\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\\\\\0\\\\\\\\0\\\\\\\\D"<\
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
 TYPE="string"><VALUE.ARRAY><VALUE>d7e792a2-ca61-4ebb-8502-dc1fa5fd3bae</VALUE\
></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="9F222654-941B-4DDF-AA8F-8002A3F3BF86"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:9F222654-941B-4DDF-AA8F-8002A3F3BF86\\\\83F8638B-8DCA-4152\
-9EDA-2CA8B33039B4\\\\0\\\\0\\\\L"'
            v1.append(v2)
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 2 and self.__id__ == 345 and str(args[0]) ==\
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
 TYPE="string"><VALUE.ARRAY><VALUE>{b79076bb-a6e3-4520-8e4a-3322b965305d}</VAL\
UE></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="9F222654-941B-4DDF-AA8F-8002A3F3BF86"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:9F222654-941B-4DDF-AA8F-8002A3F3BF86\\\\5A7DC824-71BC-4E7B\
-B9DF-E99C20A62B3C\\\\0"'
            v1.append(v2)
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 2 and self.__id__ == 351 and str(args[0]) ==\
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
 TYPE="string"><VALUE.ARRAY><VALUE>{23c3d986-b1c7-4a42-86b7-bfdae4431d15}</VAL\
UE></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="9F222654-941B-4DDF-AA8F-8002A3F3BF86"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_SyntheticEthernetPortSettingData\
.InstanceID="Microsoft:9F222654-941B-4DDF-AA8F-8002A3F3BF86\\\\F638B072-65E1-4\
3C1-A0E0-670F23F59A5A"'
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
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_StorageJob.InstanceID="30097D77-\
C5D9-48E9-BC16-55394F9D2161"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v
        elif len(args) == 1 and self.__id__ == 410 and args[0] == 3:
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ConcreteJob.InstanceID="57DC9C96\
-FBB8-4ED3-A03B-A535E4D87228"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v
        elif len(args) == 1 and self.__id__ == 431 and args[0] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="9F222654-941B-4DDF-AA8F-8002A3F3BF86"':
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ConcreteJob.InstanceID="72C2A83D\
-6A25-465B-A17E-416B99409C36"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v
        elif len(args) == 0 and self.__id__ == 387 and\
 kwargs.get('SourcePath') ==\
 'C:\\Hyper-V\\test\\instances\\export\\openstack_unit_test_vm_d66dbe32-9e1c-4\
994-8884-70c064f3b8de\\openstack_unit_test_vm_d66dbe32-9e1c-4994-8884-70c064f3\
b8de.vhd' and kwargs.get('DestinationPath') ==\
 'C:\\Hyper-V\\test\\instances\\export\\openstack_unit_test_vm_d66dbe32-9e1c-4\
994-8884-70c064f3b8de\\1.vhd':
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_StorageJob.InstanceID="EC2DD2C5-\
35F3-4F24-818E-3B204AA2552A"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v
        elif len(args) == 0 and self.__id__ == 386 and kwargs.get('Force') is\
 True and kwargs.get('ChildPath') ==\
 'C:\\Hyper-V\\test\\instances\\export\\openstack_unit_test_vm_d66dbe32-9e1c-4\
994-8884-70c064f3b8de\\openstack_unit_test_vm_d66dbe32-9e1c-4994-8884-70c064f3\
b8de.vhd' and kwargs.get('ParentPath') ==\
 'C:\\Hyper-V\\test\\instances\\export\\openstack_unit_test_vm_d66dbe32-9e1c-4\
994-8884-70c064f3b8de\\1.vhd':
            v = ()
            v1 = None
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 1 and self.__id__ == 385 and args[0] ==\
 'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_d66dbe32-9e1c-4994-8884\
-70c064f3b8de\\openstack_unit_test_vm_d66dbe32-9e1c-4994-8884-70c064f3b8de.vhd\
':
            v = ()
            v1 = u'<INSTANCE CLASSNAME="Msvm_VirtualHardDiskInfo"><PROPERTY\
 NAME="FileSize" TYPE="uint64"><VALUE>81920</VALUE></PROPERTY><PROPERTY\
 NAME="InSavedState" TYPE="boolean"><VALUE>FALSE</VALUE></PROPERTY><PROPERTY\
 NAME="InUse" TYPE="boolean"><VALUE>FALSE</VALUE></PROPERTY><PROPERTY\
 NAME="MaxInternalSize"\
 TYPE="uint64"><VALUE>3145728</VALUE></PROPERTY><PROPERTY NAME="ParentPath"\
 TYPE="string"><VALUE>C:\\Hyper-V\\test\\instances\\_base\\1.vhd</VALUE></PROP\
ERTY><PROPERTY NAME="Type"\
 TYPE="uint16"><VALUE>4</VALUE></PROPERTY></INSTANCE>'
            v += (v1,)
            v1 = None
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 1 and self.__id__ == 397 and args[0] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_VirtualSystemSettingData.Instanc\
eID="Microsoft:D2DF9CDA-0803-4091-A786-49047965B299"':
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ConcreteJob.InstanceID="DD4B46C0\
-65FB-44F4-A9E0-85FD8B0AE141"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v
        elif len(args) == 1 and self.__id__ == 370 and args[0] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="9F222654-941B-4DDF-AA8F-8002A3F3BF86"':
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ConcreteJob.InstanceID="ECA661CC\
-62C1-4B1D-A178-E9BBD8561901"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            v1 = None
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
        if self.__id__ == 69:
            return\
 u'Microsoft:Definition\\118C3BE5-0D31-4804-85F0-5C6074ABEA8F\\Default'
        elif self.__id__ == 73:
            return u'Microsoft Synthetic Disk Drive'
        elif self.__id__ == 77:
            return None
        elif self.__id__ == 81:
            return u'Hard Drive'
        elif self.__id__ == 85:
            return u'Settings for the Microsoft Virtual Hard Drive.'
        elif self.__id__ == 89:
            return None
        elif self.__id__ == 93:
            return u'1'
        elif self.__id__ == 97:
            return True
        elif self.__id__ == 101:
            return True
        elif self.__id__ == 105:
            return u'Microsoft:118C3BE5-0D31-4804-85F0-5C6074ABEA8F\\Root'
        elif self.__id__ == 109:
            return u'1'
        elif self.__id__ == 113:
            return u'Hard Drives'
        elif self.__id__ == 117:
            return None
        elif self.__id__ == 121:
            return None
        elif self.__id__ == 125:
            return None
        elif self.__id__ == 129:
            return u'Hard Drive'
        elif self.__id__ == 133:
            return None
        elif self.__id__ == 137:
            return u'1'
        elif self.__id__ == 141:
            return 22
        elif self.__id__ == 145:
            return 0
        elif self.__id__ == 151:
            return None
        elif self.__id__ == 163:
            return\
 u'Microsoft:Definition\\70BB60D2-A9D3-46AA-B654-3DE53004B4F8\\Default'
        elif self.__id__ == 167:
            return u'Microsoft Virtual Hard Disk'
        elif self.__id__ == 171:
            return None
        elif self.__id__ == 175:
            return u'Hard Disk Image'
        elif self.__id__ == 179:
            return u'Settings for the Microsoft Hard Disk Image.'
        elif self.__id__ == 183:
            return None
        elif self.__id__ == 187:
            return u'1'
        elif self.__id__ == 191:
            return True
        elif self.__id__ == 195:
            return True
        elif self.__id__ == 199:
            return u'Microsoft:70BB60D2-A9D3-46aa-B654-3DE53004B4F8\\Root'
        elif self.__id__ == 203:
            return u'1'
        elif self.__id__ == 207:
            return u'Disks'
        elif self.__id__ == 211:
            return None
        elif self.__id__ == 215:
            return None
        elif self.__id__ == 219:
            return None
        elif self.__id__ == 223:
            return u'Hard Disk Image'
        elif self.__id__ == 227:
            return None
        elif self.__id__ == 231:
            return u'1'
        elif self.__id__ == 235:
            return 21
        elif self.__id__ == 239:
            return 0
        elif self.__id__ == 245:
            return None
        elif self.__id__ == 258:
            return\
 u'Microsoft:Definition\\BDE5D4D6-E450-46D2-B925-976CA3E989B4\\Default'
        elif self.__id__ == 262:
            return u'Microsoft Synthetic SCSI Controller'
        elif self.__id__ == 266:
            return None
        elif self.__id__ == 270:
            return u'SCSI Controller'
        elif self.__id__ == 274:
            return u'Settings for the Microsoft Synthetic SCSI Controller.'
        elif self.__id__ == 278:
            return None
        elif self.__id__ == 282:
            return u'1'
        elif self.__id__ == 286:
            return True
        elif self.__id__ == 290:
            return True
        elif self.__id__ == 294:
            return u'Microsoft:bde5d4d6-e450-46d2-b925-976ca3e989b4\\Root'
        elif self.__id__ == 298:
            return u'1'
        elif self.__id__ == 302:
            return u'Controllers'
        elif self.__id__ == 306:
            return None
        elif self.__id__ == 310:
            return None
        elif self.__id__ == 314:
            return None
        elif self.__id__ == 318:
            return u'SCSI Controller'
        elif self.__id__ == 322:
            return None
        elif self.__id__ == 326:
            return u'1'
        elif self.__id__ == 330:
            return 6
        elif self.__id__ == 334:
            return 0
        elif self.__id__ == 340:
            return None

    @Value.setter
    def Value(self, value):
        pass

    def __call__(self, *args):
        if len(args) == 0 and self.__id__ == 154:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:9F222654-941B-4DDF-AA8F-8002A3F3BF86\\\\83F8638B-8DCA-4152\
-9EDA-2CA8B33039B4\\\\0"'
        elif len(args) == 0 and self.__id__ == 158:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="9F222654-941B-4DDF-AA8F-8002A3F3BF86"'
        elif len(args) == 0 and self.__id__ == 251:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="9F222654-941B-4DDF-AA8F-8002A3F3BF86"'
        elif len(args) == 0 and self.__id__ == 346:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="9F222654-941B-4DDF-AA8F-8002A3F3BF86"'
        elif len(args) == 0 and self.__id__ == 46:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="9F222654-941B-4DDF-AA8F-8002A3F3BF86"'
        elif len(args) == 0 and self.__id__ == 49:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="9F222654-941B-4DDF-AA8F-8002A3F3BF86"'
        elif len(args) == 0 and self.__id__ == 352:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="9F222654-941B-4DDF-AA8F-8002A3F3BF86"'
        elif len(args) == 0 and self.__id__ == 432:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="9F222654-941B-4DDF-AA8F-8002A3F3BF86"'
        elif len(args) == 0 and self.__id__ == 371:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="9F222654-941B-4DDF-AA8F-8002A3F3BF86"'
        elif len(args) == 0 and self.__id__ == 398:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_VirtualSystemSettingData.Instanc\
eID="Microsoft:D2DF9CDA-0803-4091-A786-49047965B299"'

    def Item(self, strName='<PyOleMissing object at 0x04091890>', iFlags=0):
        if self.__id__ == 68 and strName == u'InstanceID':
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
        elif self.__id__ == 339 and strName == u'Connection':
            v = CDispatch()
            v.__instance_id__ = 340
            return v
        elif self.__id__ == 70 and strName == u'InstanceID':
            v = CDispatch()
            v.__instance_id__ = 71
            return v
        elif self.__id__ == 74 and strName == u'ResourceSubType':
            v = CDispatch()
            v.__instance_id__ = 75
            return v
        elif self.__id__ == 78 and strName == u'HostResource':
            v = CDispatch()
            v.__instance_id__ = 79
            return v
        elif self.__id__ == 82 and strName == u'ElementName':
            v = CDispatch()
            v.__instance_id__ = 83
            return v
        elif self.__id__ == 86 and strName == u'Description':
            v = CDispatch()
            v.__instance_id__ = 87
            return v
        elif self.__id__ == 90 and strName == u'Parent':
            v = CDispatch()
            v.__instance_id__ = 91
            return v
        elif self.__id__ == 94 and strName == u'VirtualQuantity':
            v = CDispatch()
            v.__instance_id__ = 95
            return v
        elif self.__id__ == 98 and strName == u'AutomaticDeallocation':
            v = CDispatch()
            v.__instance_id__ = 99
            return v
        elif self.__id__ == 102 and strName == u'AutomaticAllocation':
            v = CDispatch()
            v.__instance_id__ = 103
            return v
        elif self.__id__ == 106 and strName == u'PoolID':
            v = CDispatch()
            v.__instance_id__ = 107
            return v
        elif self.__id__ == 110 and strName == u'Reservation':
            v = CDispatch()
            v.__instance_id__ = 111
            return v
        elif self.__id__ == 114 and strName == u'AllocationUnits':
            v = CDispatch()
            v.__instance_id__ = 115
            return v
        elif self.__id__ == 118 and strName == u'MappingBehavior':
            v = CDispatch()
            v.__instance_id__ = 119
            return v
        elif self.__id__ == 122 and strName == u'Address':
            v = CDispatch()
            v.__instance_id__ = 123
            return v
        elif self.__id__ == 126 and strName == u'OtherResourceType':
            v = CDispatch()
            v.__instance_id__ = 127
            return v
        elif self.__id__ == 130 and strName == u'Caption':
            v = CDispatch()
            v.__instance_id__ = 131
            return v
        elif self.__id__ == 134 and strName == u'ConsumerVisibility':
            v = CDispatch()
            v.__instance_id__ = 135
            return v
        elif self.__id__ == 138 and strName == u'Limit':
            v = CDispatch()
            v.__instance_id__ = 139
            return v
        elif self.__id__ == 142 and strName == u'ResourceType':
            v = CDispatch()
            v.__instance_id__ = 143
            return v
        elif self.__id__ == 146 and strName == u'Weight':
            v = CDispatch()
            v.__instance_id__ = 147
            return v
        elif self.__id__ == 148 and strName == u'VirtualSystemIdentifiers':
            v = CDispatch()
            v.__instance_id__ = 149
            return v
        elif self.__id__ == 152 and strName == u'Connection':
            v = CDispatch()
            v.__instance_id__ = 153
            return v
        elif self.__id__ == 164 and strName == u'InstanceID':
            v = CDispatch()
            v.__instance_id__ = 165
            return v
        elif self.__id__ == 168 and strName == u'ResourceSubType':
            v = CDispatch()
            v.__instance_id__ = 169
            return v
        elif self.__id__ == 172 and strName == u'HostResource':
            v = CDispatch()
            v.__instance_id__ = 173
            return v
        elif self.__id__ == 176 and strName == u'ElementName':
            v = CDispatch()
            v.__instance_id__ = 177
            return v
        elif self.__id__ == 180 and strName == u'Description':
            v = CDispatch()
            v.__instance_id__ = 181
            return v
        elif self.__id__ == 184 and strName == u'Parent':
            v = CDispatch()
            v.__instance_id__ = 185
            return v
        elif self.__id__ == 188 and strName == u'VirtualQuantity':
            v = CDispatch()
            v.__instance_id__ = 189
            return v
        elif self.__id__ == 192 and strName == u'AutomaticDeallocation':
            v = CDispatch()
            v.__instance_id__ = 193
            return v
        elif self.__id__ == 196 and strName == u'AutomaticAllocation':
            v = CDispatch()
            v.__instance_id__ = 197
            return v
        elif self.__id__ == 200 and strName == u'PoolID':
            v = CDispatch()
            v.__instance_id__ = 201
            return v
        elif self.__id__ == 204 and strName == u'Reservation':
            v = CDispatch()
            v.__instance_id__ = 205
            return v
        elif self.__id__ == 208 and strName == u'AllocationUnits':
            v = CDispatch()
            v.__instance_id__ = 209
            return v
        elif self.__id__ == 212 and strName == u'MappingBehavior':
            v = CDispatch()
            v.__instance_id__ = 213
            return v
        elif self.__id__ == 216 and strName == u'Address':
            v = CDispatch()
            v.__instance_id__ = 217
            return v
        elif self.__id__ == 220 and strName == u'OtherResourceType':
            v = CDispatch()
            v.__instance_id__ = 221
            return v
        elif self.__id__ == 224 and strName == u'Caption':
            v = CDispatch()
            v.__instance_id__ = 225
            return v
        elif self.__id__ == 228 and strName == u'ConsumerVisibility':
            v = CDispatch()
            v.__instance_id__ = 229
            return v
        elif self.__id__ == 232 and strName == u'Limit':
            v = CDispatch()
            v.__instance_id__ = 233
            return v
        elif self.__id__ == 236 and strName == u'ResourceType':
            v = CDispatch()
            v.__instance_id__ = 237
            return v
        elif self.__id__ == 240 and strName == u'Weight':
            v = CDispatch()
            v.__instance_id__ = 241
            return v
        elif self.__id__ == 242 and strName == u'VirtualSystemIdentifiers':
            v = CDispatch()
            v.__instance_id__ = 243
            return v
        elif self.__id__ == 246 and strName == u'Connection':
            v = CDispatch()
            v.__instance_id__ = 247
            return v
        elif self.__id__ == 259 and strName == u'InstanceID':
            v = CDispatch()
            v.__instance_id__ = 260
            return v
        elif self.__id__ == 263 and strName == u'ResourceSubType':
            v = CDispatch()
            v.__instance_id__ = 264
            return v
        elif self.__id__ == 267 and strName == u'HostResource':
            v = CDispatch()
            v.__instance_id__ = 268
            return v
        elif self.__id__ == 271 and strName == u'ElementName':
            v = CDispatch()
            v.__instance_id__ = 272
            return v
        elif self.__id__ == 275 and strName == u'Description':
            v = CDispatch()
            v.__instance_id__ = 276
            return v
        elif self.__id__ == 279 and strName == u'Parent':
            v = CDispatch()
            v.__instance_id__ = 280
            return v
        elif self.__id__ == 283 and strName == u'VirtualQuantity':
            v = CDispatch()
            v.__instance_id__ = 284
            return v
        elif self.__id__ == 287 and strName == u'AutomaticDeallocation':
            v = CDispatch()
            v.__instance_id__ = 288
            return v
        elif self.__id__ == 291 and strName == u'AutomaticAllocation':
            v = CDispatch()
            v.__instance_id__ = 292
            return v
        elif self.__id__ == 295 and strName == u'PoolID':
            v = CDispatch()
            v.__instance_id__ = 296
            return v
        elif self.__id__ == 299 and strName == u'Reservation':
            v = CDispatch()
            v.__instance_id__ = 300
            return v
        elif self.__id__ == 303 and strName == u'AllocationUnits':
            v = CDispatch()
            v.__instance_id__ = 304
            return v
        elif self.__id__ == 307 and strName == u'MappingBehavior':
            v = CDispatch()
            v.__instance_id__ = 308
            return v
        elif self.__id__ == 311 and strName == u'Address':
            v = CDispatch()
            v.__instance_id__ = 312
            return v
        elif self.__id__ == 315 and strName == u'OtherResourceType':
            v = CDispatch()
            v.__instance_id__ = 316
            return v
        elif self.__id__ == 319 and strName == u'Caption':
            v = CDispatch()
            v.__instance_id__ = 320
            return v
        elif self.__id__ == 323 and strName == u'ConsumerVisibility':
            v = CDispatch()
            v.__instance_id__ = 324
            return v
        elif self.__id__ == 327 and strName == u'Limit':
            v = CDispatch()
            v.__instance_id__ = 328
            return v
        elif self.__id__ == 331 and strName == u'ResourceType':
            v = CDispatch()
            v.__instance_id__ = 332
            return v
        elif self.__id__ == 335 and strName == u'Weight':
            v = CDispatch()
            v.__instance_id__ = 336
            return v
        elif self.__id__ == 337 and strName == u'VirtualSystemIdentifiers':
            v = CDispatch()
            v.__instance_id__ = 338
            return v
        elif self.__id__ == 341 and strName == u'Connection':
            v = CDispatch()
            v.__instance_id__ = 342
            return v
