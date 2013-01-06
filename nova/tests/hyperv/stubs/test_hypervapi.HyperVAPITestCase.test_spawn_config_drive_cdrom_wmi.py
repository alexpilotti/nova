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
            v.__instance_id__ = 588
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
 u'//HV12OSDEMO1/root/virtualization:Msvm_StorageJob.InstanceID="57B4A236-4D15\
-4D1A-A24B-864F81BB5DED"':
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
 u'//HV12OSDEMO1/root/virtualization:Msvm_StorageJob.InstanceID="384E20B3-96F4\
-41EA-A9CF-0E7E5BCB7ABD"':
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
 u'//HV12OSDEMO1/root/virtualization:Msvm_ConcreteJob.InstanceID="79284D50-CC2\
2-45DE-B1DF-2CE1219DE5D7"':
        ret_value = None
        global _WMI_count_6
        if not '_WMI_count_6' in globals():
            _WMI_count_6 = 0
        if _WMI_count_6 == 0:
            v = _wmi_object()
            v.__instance_id__ = 560
        elif _WMI_count_6 == 1:
            v = _wmi_object()
            v.__instance_id__ = 561
        elif _WMI_count_6 == 2:
            v = _wmi_object()
            v.__instance_id__ = 562
        elif _WMI_count_6 == 3:
            v = _wmi_object()
            v.__instance_id__ = 563
        elif _WMI_count_6 == 4:
            v = _wmi_object()
            v.__instance_id__ = 564
        elif _WMI_count_6 == 5:
            v = _wmi_object()
            v.__instance_id__ = 565
        _WMI_count_6 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_ConcreteJob.InstanceID="7FA1144F-12C\
7-419E-BBDB-00A538C2ABBF"':
        ret_value = None
        global _WMI_count_7
        if not '_WMI_count_7' in globals():
            _WMI_count_7 = 0
        if _WMI_count_7 == 0:
            v = _wmi_object()
            v.__instance_id__ = 596
        elif _WMI_count_7 == 1:
            v = _wmi_object()
            v.__instance_id__ = 597
        _WMI_count_7 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_ConcreteJob.InstanceID="52BFBDFB-687\
C-45F7-98C9-A31134304AC1"':
        ret_value = None
        global _WMI_count_8
        if not '_WMI_count_8' in globals():
            _WMI_count_8 = 0
        if _WMI_count_8 == 0:
            v = _wmi_object()
            v.__instance_id__ = 620
        elif _WMI_count_8 == 1:
            v = _wmi_object()
            v.__instance_id__ = 621
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
            elif self._Msvm_ResourceAllocationSettingData_count_0 == 3:
                v = _wmi_class()
                v.__instance_id__ = 371
            elif self._Msvm_ResourceAllocationSettingData_count_0 == 4:
                v = _wmi_class()
                v.__instance_id__ = 465
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
                v.__instance_id__ = 460
            elif self._Msvm_VirtualSystemManagementService_count_0 == 6:
                v = _wmi_class()
                v.__instance_id__ = 553
            self._Msvm_VirtualSystemManagementService_count_0 += 1
            return v
        elif self.__id__ == 11:
            v = _wmi_class()
            v.__instance_id__ = 591
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
                v.__instance_id__ = 557
            self._Msvm_ComputerSystem_count_0 += 1
            return v
        elif self.__id__ == 11:
            ret_value = None
            if not hasattr(self, '_Msvm_ComputerSystem_count_1'):
                self._Msvm_ComputerSystem_count_1 = 0
            if self._Msvm_ComputerSystem_count_1 == 0:
                v = _wmi_class()
                v.__instance_id__ = 566
            elif self._Msvm_ComputerSystem_count_1 == 1:
                v = _wmi_class()
                v.__instance_id__ = 586
            elif self._Msvm_ComputerSystem_count_1 == 2:
                v = _wmi_class()
                v.__instance_id__ = 589
            elif self._Msvm_ComputerSystem_count_1 == 3:
                v = _wmi_class()
                v.__instance_id__ = 593
            elif self._Msvm_ComputerSystem_count_1 == 4:
                v = _wmi_class()
                v.__instance_id__ = 598
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
            elif self._MSVM_ComputerSystem_count_0 == 2:
                v = _wmi_class()
                v.__instance_id__ = 352
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
        elif self.__id__ == 588 and wql == u'Select * from CIM_DataFile where\
 Name =\
 \'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_419ac48a-c4e3-4772-a9c\
1-af7b187f21a1\\openstack_unit_test_vm_419ac48a-c4e3-4772-a9c1-af7b187f21a1.vh\
d\'':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 622
            v.append(v1)
            return v
        elif self.__id__ == 588 and wql == u'Select * from CIM_DataFile where\
 Name =\
 \'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_419ac48a-c4e3-4772-a9c\
1-af7b187f21a1\\configdrive.iso\'':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 624
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
        elif self.__id__ == 9 and wql == 'SELECT * FROM\
 Msvm_ResourceAllocationSettingData             WHERE ResourceSubType LIKE\
 \'Microsoft Synthetic DVD Drive\'            AND InstanceID LIKE\
 \'%Default%\'':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 370
            v.append(v1)
            return v
        elif self.__id__ == 9 and wql == 'SELECT * FROM\
 Msvm_ResourceAllocationSettingData                  WHERE ResourceSubType\
 LIKE \'Microsoft Virtual CD/DVD Disk\' AND                  InstanceID LIKE\
 \'%Default%\' ':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 464
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
 'openstack_unit_test_vm_419ac48a-c4e3-4772-a9c1-af7b187f21a1':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 50
            v.append(v1)
            return v
        elif self.__id__ == 251 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_419ac48a-c4e3-4772-a9c1-af7b187f21a1':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 252
            v.append(v1)
            return v
        elif self.__id__ == 352 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_419ac48a-c4e3-4772-a9c1-af7b187f21a1':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 353
            v.append(v1)
            return v
        elif self.__id__ == 10 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_419ac48a-c4e3-4772-a9c1-af7b187f21a1':
            v = []
            return v
        elif self.__id__ == 40 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_419ac48a-c4e3-4772-a9c1-af7b187f21a1':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 41
            v.append(v1)
            return v
        elif self.__id__ == 346 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_419ac48a-c4e3-4772-a9c1-af7b187f21a1':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 347
            v.append(v1)
            return v
        elif self.__id__ == 557 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_419ac48a-c4e3-4772-a9c1-af7b187f21a1':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 558
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
        elif self.__id__ == 460:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 461
            v.append(v1)
            return v
        elif self.__id__ == 553:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 554
            v.append(v1)
            return v
        elif self.__id__ == 566 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_419ac48a-c4e3-4772-a9c1-af7b187f21a1':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 567
            v.append(v1)
            return v
        elif self.__id__ == 586 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_419ac48a-c4e3-4772-a9c1-af7b187f21a1':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 587
            v.append(v1)
            return v
        elif self.__id__ == 589 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_419ac48a-c4e3-4772-a9c1-af7b187f21a1':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 590
            v.append(v1)
            return v
        elif self.__id__ == 593 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_419ac48a-c4e3-4772-a9c1-af7b187f21a1':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 594
            v.append(v1)
            return v
        elif self.__id__ == 598 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_419ac48a-c4e3-4772-a9c1-af7b187f21a1':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 599
            v.append(v1)
            return v
        elif self.__id__ == 591:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 592
            v.append(v1)
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
        elif self.__id__ == 371:
            v = _wmi_object()
            v.__instance_id__ = 372
            return v
        elif self.__id__ == 465:
            v = _wmi_object()
            v.__instance_id__ = 466
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
        if self.__id__ == 558:
            v = _wmi_method()
            v.__instance_id__ = 559
            return v
        elif self.__id__ == 594:
            v = _wmi_method()
            v.__instance_id__ = 595
            return v

    @RequestStateChange.setter
    def RequestStateChange(self, value):
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
        elif self.__id__ == 565:
            return u'Initializing and Starting Virtual Machine'

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
        elif self.__id__ == 461:
            v = _wmi_method()
            v.__instance_id__ = 462
            return v
        elif self.__id__ == 554:
            v = _wmi_method()
            v.__instance_id__ = 555
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
        elif self.__id__ == 365:
            return u'0'
        elif self.__id__ == 366:
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
        elif self.__id__ == 355:
            return u'Microsoft Virtual Keyboard'
        elif self.__id__ == 356:
            return u'Microsoft Virtual PS2 Mouse'
        elif self.__id__ == 357:
            return u'Microsoft S3 Display Controller'
        elif self.__id__ == 358:
            return u'Microsoft Synthetic Diskette Drive'
        elif self.__id__ == 359:
            return None
        elif self.__id__ == 360:
            return u'Microsoft Serial Controller'
        elif self.__id__ == 361:
            return u'Microsoft Serial Port'
        elif self.__id__ == 362:
            return u'Microsoft Serial Port'
        elif self.__id__ == 363:
            return u'Microsoft Synthetic Disk Drive'
        elif self.__id__ == 364:
            return u'Microsoft Virtual Hard Disk'
        elif self.__id__ == 365:
            return u'Microsoft Emulated IDE Controller'
        elif self.__id__ == 366:
            return u'Microsoft Emulated IDE Controller'
        elif self.__id__ == 367:
            return u'Microsoft Synthetic Mouse'
        elif self.__id__ == 368:
            return u'Microsoft Synthetic Display Controller'
        elif self.__id__ == 369:
            return u'Microsoft Synthetic SCSI Controller'
        elif self.__id__ == 569:
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
        elif self.__id__ == 570:
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
        elif self.__id__ == 571:
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
        elif self.__id__ == 572:
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
        elif self.__id__ == 573:
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
        elif self.__id__ == 574:
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
        elif self.__id__ == 575:
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
        elif self.__id__ == 576:
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
        elif self.__id__ == 577:
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
        elif self.__id__ == 578:
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
        elif self.__id__ == 579:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_37'):
                self._ResourceSubType_count_37 = 0
            if self._ResourceSubType_count_37 == 0:
                v = u'Microsoft Synthetic DVD Drive'
            elif self._ResourceSubType_count_37 == 1:
                v = u'Microsoft Synthetic DVD Drive'
            elif self._ResourceSubType_count_37 == 2:
                v = u'Microsoft Synthetic DVD Drive'
            self._ResourceSubType_count_37 += 1
            return v
        elif self.__id__ == 580:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_38'):
                self._ResourceSubType_count_38 = 0
            if self._ResourceSubType_count_38 == 0:
                v = u'Microsoft Virtual CD/DVD Disk'
            elif self._ResourceSubType_count_38 == 1:
                v = u'Microsoft Virtual CD/DVD Disk'
            elif self._ResourceSubType_count_38 == 2:
                v = u'Microsoft Virtual CD/DVD Disk'
            self._ResourceSubType_count_38 += 1
            return v
        elif self.__id__ == 581:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_39'):
                self._ResourceSubType_count_39 = 0
            if self._ResourceSubType_count_39 == 0:
                v = u'Microsoft Emulated IDE Controller'
            elif self._ResourceSubType_count_39 == 1:
                v = u'Microsoft Emulated IDE Controller'
            elif self._ResourceSubType_count_39 == 2:
                v = u'Microsoft Emulated IDE Controller'
            self._ResourceSubType_count_39 += 1
            return v
        elif self.__id__ == 582:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_40'):
                self._ResourceSubType_count_40 = 0
            if self._ResourceSubType_count_40 == 0:
                v = u'Microsoft Emulated IDE Controller'
            elif self._ResourceSubType_count_40 == 1:
                v = u'Microsoft Emulated IDE Controller'
            elif self._ResourceSubType_count_40 == 2:
                v = u'Microsoft Emulated IDE Controller'
            self._ResourceSubType_count_40 += 1
            return v
        elif self.__id__ == 583:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_41'):
                self._ResourceSubType_count_41 = 0
            if self._ResourceSubType_count_41 == 0:
                v = u'Microsoft Synthetic Mouse'
            elif self._ResourceSubType_count_41 == 1:
                v = u'Microsoft Synthetic Mouse'
            elif self._ResourceSubType_count_41 == 2:
                v = u'Microsoft Synthetic Mouse'
            self._ResourceSubType_count_41 += 1
            return v
        elif self.__id__ == 584:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_42'):
                self._ResourceSubType_count_42 = 0
            if self._ResourceSubType_count_42 == 0:
                v = u'Microsoft Synthetic Display Controller'
            elif self._ResourceSubType_count_42 == 1:
                v = u'Microsoft Synthetic Display Controller'
            elif self._ResourceSubType_count_42 == 2:
                v = u'Microsoft Synthetic Display Controller'
            self._ResourceSubType_count_42 += 1
            return v
        elif self.__id__ == 585:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_43'):
                self._ResourceSubType_count_43 = 0
            if self._ResourceSubType_count_43 == 0:
                v = u'Microsoft Synthetic SCSI Controller'
            elif self._ResourceSubType_count_43 == 1:
                v = u'Microsoft Synthetic SCSI Controller'
            elif self._ResourceSubType_count_43 == 2:
                v = u'Microsoft Synthetic SCSI Controller'
            self._ResourceSubType_count_43 += 1
            return v
        elif self.__id__ == 601:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_44'):
                self._ResourceSubType_count_44 = 0
            if self._ResourceSubType_count_44 == 0:
                v = u'Microsoft Virtual Keyboard'
            elif self._ResourceSubType_count_44 == 1:
                v = u'Microsoft Virtual Keyboard'
            elif self._ResourceSubType_count_44 == 2:
                v = u'Microsoft Virtual Keyboard'
            self._ResourceSubType_count_44 += 1
            return v
        elif self.__id__ == 602:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_45'):
                self._ResourceSubType_count_45 = 0
            if self._ResourceSubType_count_45 == 0:
                v = u'Microsoft Virtual PS2 Mouse'
            elif self._ResourceSubType_count_45 == 1:
                v = u'Microsoft Virtual PS2 Mouse'
            elif self._ResourceSubType_count_45 == 2:
                v = u'Microsoft Virtual PS2 Mouse'
            self._ResourceSubType_count_45 += 1
            return v
        elif self.__id__ == 603:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_46'):
                self._ResourceSubType_count_46 = 0
            if self._ResourceSubType_count_46 == 0:
                v = u'Microsoft S3 Display Controller'
            elif self._ResourceSubType_count_46 == 1:
                v = u'Microsoft S3 Display Controller'
            elif self._ResourceSubType_count_46 == 2:
                v = u'Microsoft S3 Display Controller'
            self._ResourceSubType_count_46 += 1
            return v
        elif self.__id__ == 604:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_47'):
                self._ResourceSubType_count_47 = 0
            if self._ResourceSubType_count_47 == 0:
                v = u'Microsoft Synthetic Diskette Drive'
            elif self._ResourceSubType_count_47 == 1:
                v = u'Microsoft Synthetic Diskette Drive'
            elif self._ResourceSubType_count_47 == 2:
                v = u'Microsoft Synthetic Diskette Drive'
            self._ResourceSubType_count_47 += 1
            return v
        elif self.__id__ == 605:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_48'):
                self._ResourceSubType_count_48 = 0
            if self._ResourceSubType_count_48 == 0:
                v = None
            elif self._ResourceSubType_count_48 == 1:
                v = None
            elif self._ResourceSubType_count_48 == 2:
                v = None
            self._ResourceSubType_count_48 += 1
            return v
        elif self.__id__ == 606:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_49'):
                self._ResourceSubType_count_49 = 0
            if self._ResourceSubType_count_49 == 0:
                v = u'Microsoft Serial Controller'
            elif self._ResourceSubType_count_49 == 1:
                v = u'Microsoft Serial Controller'
            elif self._ResourceSubType_count_49 == 2:
                v = u'Microsoft Serial Controller'
            self._ResourceSubType_count_49 += 1
            return v
        elif self.__id__ == 607:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_50'):
                self._ResourceSubType_count_50 = 0
            if self._ResourceSubType_count_50 == 0:
                v = u'Microsoft Serial Port'
            elif self._ResourceSubType_count_50 == 1:
                v = u'Microsoft Serial Port'
            elif self._ResourceSubType_count_50 == 2:
                v = u'Microsoft Serial Port'
            self._ResourceSubType_count_50 += 1
            return v
        elif self.__id__ == 608:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_51'):
                self._ResourceSubType_count_51 = 0
            if self._ResourceSubType_count_51 == 0:
                v = u'Microsoft Serial Port'
            elif self._ResourceSubType_count_51 == 1:
                v = u'Microsoft Serial Port'
            elif self._ResourceSubType_count_51 == 2:
                v = u'Microsoft Serial Port'
            self._ResourceSubType_count_51 += 1
            return v
        elif self.__id__ == 609:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_52'):
                self._ResourceSubType_count_52 = 0
            if self._ResourceSubType_count_52 == 0:
                v = u'Microsoft Synthetic Disk Drive'
            elif self._ResourceSubType_count_52 == 1:
                v = u'Microsoft Synthetic Disk Drive'
            elif self._ResourceSubType_count_52 == 2:
                v = u'Microsoft Synthetic Disk Drive'
            self._ResourceSubType_count_52 += 1
            return v
        elif self.__id__ == 610:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_53'):
                self._ResourceSubType_count_53 = 0
            if self._ResourceSubType_count_53 == 0:
                v = u'Microsoft Virtual Hard Disk'
            elif self._ResourceSubType_count_53 == 1:
                v = u'Microsoft Virtual Hard Disk'
            elif self._ResourceSubType_count_53 == 2:
                v = u'Microsoft Virtual Hard Disk'
            self._ResourceSubType_count_53 += 1
            return v
        elif self.__id__ == 611:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_54'):
                self._ResourceSubType_count_54 = 0
            if self._ResourceSubType_count_54 == 0:
                v = u'Microsoft Synthetic DVD Drive'
            elif self._ResourceSubType_count_54 == 1:
                v = u'Microsoft Synthetic DVD Drive'
            elif self._ResourceSubType_count_54 == 2:
                v = u'Microsoft Synthetic DVD Drive'
            self._ResourceSubType_count_54 += 1
            return v
        elif self.__id__ == 612:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_55'):
                self._ResourceSubType_count_55 = 0
            if self._ResourceSubType_count_55 == 0:
                v = u'Microsoft Virtual CD/DVD Disk'
            elif self._ResourceSubType_count_55 == 1:
                v = u'Microsoft Virtual CD/DVD Disk'
            elif self._ResourceSubType_count_55 == 2:
                v = u'Microsoft Virtual CD/DVD Disk'
            self._ResourceSubType_count_55 += 1
            return v
        elif self.__id__ == 613:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_56'):
                self._ResourceSubType_count_56 = 0
            if self._ResourceSubType_count_56 == 0:
                v = u'Microsoft Emulated IDE Controller'
            elif self._ResourceSubType_count_56 == 1:
                v = u'Microsoft Emulated IDE Controller'
            elif self._ResourceSubType_count_56 == 2:
                v = u'Microsoft Emulated IDE Controller'
            self._ResourceSubType_count_56 += 1
            return v
        elif self.__id__ == 614:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_57'):
                self._ResourceSubType_count_57 = 0
            if self._ResourceSubType_count_57 == 0:
                v = u'Microsoft Emulated IDE Controller'
            elif self._ResourceSubType_count_57 == 1:
                v = u'Microsoft Emulated IDE Controller'
            elif self._ResourceSubType_count_57 == 2:
                v = u'Microsoft Emulated IDE Controller'
            self._ResourceSubType_count_57 += 1
            return v
        elif self.__id__ == 615:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_58'):
                self._ResourceSubType_count_58 = 0
            if self._ResourceSubType_count_58 == 0:
                v = u'Microsoft Synthetic Mouse'
            elif self._ResourceSubType_count_58 == 1:
                v = u'Microsoft Synthetic Mouse'
            elif self._ResourceSubType_count_58 == 2:
                v = u'Microsoft Synthetic Mouse'
            self._ResourceSubType_count_58 += 1
            return v
        elif self.__id__ == 616:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_59'):
                self._ResourceSubType_count_59 = 0
            if self._ResourceSubType_count_59 == 0:
                v = u'Microsoft Synthetic Display Controller'
            elif self._ResourceSubType_count_59 == 1:
                v = u'Microsoft Synthetic Display Controller'
            elif self._ResourceSubType_count_59 == 2:
                v = u'Microsoft Synthetic Display Controller'
            self._ResourceSubType_count_59 += 1
            return v
        elif self.__id__ == 617:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_60'):
                self._ResourceSubType_count_60 = 0
            if self._ResourceSubType_count_60 == 0:
                v = u'Microsoft Synthetic SCSI Controller'
            elif self._ResourceSubType_count_60 == 1:
                v = u'Microsoft Synthetic SCSI Controller'
            elif self._ResourceSubType_count_60 == 2:
                v = u'Microsoft Synthetic SCSI Controller'
            self._ResourceSubType_count_60 += 1
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
        elif self.__id__ == 366:
            v = CDispatch()
            v.__instance_id__ = 459
            return v
        elif self.__id__ == 353:
            ret_value = None
            if not hasattr(self, '_path__count_4'):
                self._path__count_4 = 0
            if self._path__count_4 == 0:
                v = CDispatch()
                v.__instance_id__ = 463
            elif self._path__count_4 == 1:
                v = CDispatch()
                v.__instance_id__ = 556
            self._path__count_4 += 1
            return v
        elif self.__id__ == 41:
            ret_value = None
            if not hasattr(self, '_path__count_5'):
                self._path__count_5 = 0
            if self._path__count_5 == 0:
                v = CDispatch()
                v.__instance_id__ = 45
            elif self._path__count_5 == 1:
                v = CDispatch()
                v.__instance_id__ = 48
            self._path__count_5 += 1
            return v
        elif self.__id__ == 347:
            v = CDispatch()
            v.__instance_id__ = 351
            return v
        elif self.__id__ == 590:
            v = CDispatch()
            v.__instance_id__ = 619
            return v

    @path_.setter
    def path_(self, value):
        pass

    @property
    def ElapsedTime(self):
        if self.__id__ == 34:
            return u'00000000000001.017059:000'
        elif self.__id__ == 565:
            return u'00000000000000.736380:000'

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
        elif self.__id__ == 370:
            ret_value = None
            if not hasattr(self, '_Properties__count_3'):
                self._Properties__count_3 = 0
            if self._Properties__count_3 == 0:
                v = CDispatch()
                v.__instance_id__ = 373
            elif self._Properties__count_3 == 1:
                v = CDispatch()
                v.__instance_id__ = 377
            elif self._Properties__count_3 == 2:
                v = CDispatch()
                v.__instance_id__ = 381
            elif self._Properties__count_3 == 3:
                v = CDispatch()
                v.__instance_id__ = 385
            elif self._Properties__count_3 == 4:
                v = CDispatch()
                v.__instance_id__ = 389
            elif self._Properties__count_3 == 5:
                v = CDispatch()
                v.__instance_id__ = 393
            elif self._Properties__count_3 == 6:
                v = CDispatch()
                v.__instance_id__ = 397
            elif self._Properties__count_3 == 7:
                v = CDispatch()
                v.__instance_id__ = 401
            elif self._Properties__count_3 == 8:
                v = CDispatch()
                v.__instance_id__ = 405
            elif self._Properties__count_3 == 9:
                v = CDispatch()
                v.__instance_id__ = 409
            elif self._Properties__count_3 == 10:
                v = CDispatch()
                v.__instance_id__ = 413
            elif self._Properties__count_3 == 11:
                v = CDispatch()
                v.__instance_id__ = 417
            elif self._Properties__count_3 == 12:
                v = CDispatch()
                v.__instance_id__ = 421
            elif self._Properties__count_3 == 13:
                v = CDispatch()
                v.__instance_id__ = 425
            elif self._Properties__count_3 == 14:
                v = CDispatch()
                v.__instance_id__ = 429
            elif self._Properties__count_3 == 15:
                v = CDispatch()
                v.__instance_id__ = 433
            elif self._Properties__count_3 == 16:
                v = CDispatch()
                v.__instance_id__ = 437
            elif self._Properties__count_3 == 17:
                v = CDispatch()
                v.__instance_id__ = 441
            elif self._Properties__count_3 == 18:
                v = CDispatch()
                v.__instance_id__ = 445
            elif self._Properties__count_3 == 19:
                v = CDispatch()
                v.__instance_id__ = 449
            elif self._Properties__count_3 == 20:
                v = CDispatch()
                v.__instance_id__ = 455
            self._Properties__count_3 += 1
            return v
        elif self.__id__ == 464:
            ret_value = None
            if not hasattr(self, '_Properties__count_4'):
                self._Properties__count_4 = 0
            if self._Properties__count_4 == 0:
                v = CDispatch()
                v.__instance_id__ = 467
            elif self._Properties__count_4 == 1:
                v = CDispatch()
                v.__instance_id__ = 471
            elif self._Properties__count_4 == 2:
                v = CDispatch()
                v.__instance_id__ = 475
            elif self._Properties__count_4 == 3:
                v = CDispatch()
                v.__instance_id__ = 479
            elif self._Properties__count_4 == 4:
                v = CDispatch()
                v.__instance_id__ = 483
            elif self._Properties__count_4 == 5:
                v = CDispatch()
                v.__instance_id__ = 487
            elif self._Properties__count_4 == 6:
                v = CDispatch()
                v.__instance_id__ = 491
            elif self._Properties__count_4 == 7:
                v = CDispatch()
                v.__instance_id__ = 495
            elif self._Properties__count_4 == 8:
                v = CDispatch()
                v.__instance_id__ = 499
            elif self._Properties__count_4 == 9:
                v = CDispatch()
                v.__instance_id__ = 503
            elif self._Properties__count_4 == 10:
                v = CDispatch()
                v.__instance_id__ = 507
            elif self._Properties__count_4 == 11:
                v = CDispatch()
                v.__instance_id__ = 511
            elif self._Properties__count_4 == 12:
                v = CDispatch()
                v.__instance_id__ = 515
            elif self._Properties__count_4 == 13:
                v = CDispatch()
                v.__instance_id__ = 519
            elif self._Properties__count_4 == 14:
                v = CDispatch()
                v.__instance_id__ = 523
            elif self._Properties__count_4 == 15:
                v = CDispatch()
                v.__instance_id__ = 527
            elif self._Properties__count_4 == 16:
                v = CDispatch()
                v.__instance_id__ = 531
            elif self._Properties__count_4 == 17:
                v = CDispatch()
                v.__instance_id__ = 535
            elif self._Properties__count_4 == 18:
                v = CDispatch()
                v.__instance_id__ = 539
            elif self._Properties__count_4 == 19:
                v = CDispatch()
                v.__instance_id__ = 543
            elif self._Properties__count_4 == 20:
                v = CDispatch()
                v.__instance_id__ = 549
            self._Properties__count_4 += 1
            return v
        elif self.__id__ == 66:
            ret_value = None
            if not hasattr(self, '_Properties__count_5'):
                self._Properties__count_5 = 0
            if self._Properties__count_5 == 0:
                v = CDispatch()
                v.__instance_id__ = 69
            elif self._Properties__count_5 == 1:
                v = CDispatch()
                v.__instance_id__ = 73
            elif self._Properties__count_5 == 2:
                v = CDispatch()
                v.__instance_id__ = 77
            elif self._Properties__count_5 == 3:
                v = CDispatch()
                v.__instance_id__ = 81
            elif self._Properties__count_5 == 4:
                v = CDispatch()
                v.__instance_id__ = 85
            elif self._Properties__count_5 == 5:
                v = CDispatch()
                v.__instance_id__ = 89
            elif self._Properties__count_5 == 6:
                v = CDispatch()
                v.__instance_id__ = 93
            elif self._Properties__count_5 == 7:
                v = CDispatch()
                v.__instance_id__ = 97
            elif self._Properties__count_5 == 8:
                v = CDispatch()
                v.__instance_id__ = 101
            elif self._Properties__count_5 == 9:
                v = CDispatch()
                v.__instance_id__ = 105
            elif self._Properties__count_5 == 10:
                v = CDispatch()
                v.__instance_id__ = 109
            elif self._Properties__count_5 == 11:
                v = CDispatch()
                v.__instance_id__ = 113
            elif self._Properties__count_5 == 12:
                v = CDispatch()
                v.__instance_id__ = 117
            elif self._Properties__count_5 == 13:
                v = CDispatch()
                v.__instance_id__ = 121
            elif self._Properties__count_5 == 14:
                v = CDispatch()
                v.__instance_id__ = 125
            elif self._Properties__count_5 == 15:
                v = CDispatch()
                v.__instance_id__ = 129
            elif self._Properties__count_5 == 16:
                v = CDispatch()
                v.__instance_id__ = 133
            elif self._Properties__count_5 == 17:
                v = CDispatch()
                v.__instance_id__ = 137
            elif self._Properties__count_5 == 18:
                v = CDispatch()
                v.__instance_id__ = 141
            elif self._Properties__count_5 == 19:
                v = CDispatch()
                v.__instance_id__ = 145
            elif self._Properties__count_5 == 20:
                v = CDispatch()
                v.__instance_id__ = 147
            elif self._Properties__count_5 == 21:
                v = CDispatch()
                v.__instance_id__ = 151
            self._Properties__count_5 += 1
            return v
        elif self.__id__ == 160:
            ret_value = None
            if not hasattr(self, '_Properties__count_6'):
                self._Properties__count_6 = 0
            if self._Properties__count_6 == 0:
                v = CDispatch()
                v.__instance_id__ = 163
            elif self._Properties__count_6 == 1:
                v = CDispatch()
                v.__instance_id__ = 167
            elif self._Properties__count_6 == 2:
                v = CDispatch()
                v.__instance_id__ = 171
            elif self._Properties__count_6 == 3:
                v = CDispatch()
                v.__instance_id__ = 175
            elif self._Properties__count_6 == 4:
                v = CDispatch()
                v.__instance_id__ = 179
            elif self._Properties__count_6 == 5:
                v = CDispatch()
                v.__instance_id__ = 183
            elif self._Properties__count_6 == 6:
                v = CDispatch()
                v.__instance_id__ = 187
            elif self._Properties__count_6 == 7:
                v = CDispatch()
                v.__instance_id__ = 191
            elif self._Properties__count_6 == 8:
                v = CDispatch()
                v.__instance_id__ = 195
            elif self._Properties__count_6 == 9:
                v = CDispatch()
                v.__instance_id__ = 199
            elif self._Properties__count_6 == 10:
                v = CDispatch()
                v.__instance_id__ = 203
            elif self._Properties__count_6 == 11:
                v = CDispatch()
                v.__instance_id__ = 207
            elif self._Properties__count_6 == 12:
                v = CDispatch()
                v.__instance_id__ = 211
            elif self._Properties__count_6 == 13:
                v = CDispatch()
                v.__instance_id__ = 215
            elif self._Properties__count_6 == 14:
                v = CDispatch()
                v.__instance_id__ = 219
            elif self._Properties__count_6 == 15:
                v = CDispatch()
                v.__instance_id__ = 223
            elif self._Properties__count_6 == 16:
                v = CDispatch()
                v.__instance_id__ = 227
            elif self._Properties__count_6 == 17:
                v = CDispatch()
                v.__instance_id__ = 231
            elif self._Properties__count_6 == 18:
                v = CDispatch()
                v.__instance_id__ = 235
            elif self._Properties__count_6 == 19:
                v = CDispatch()
                v.__instance_id__ = 239
            elif self._Properties__count_6 == 20:
                v = CDispatch()
                v.__instance_id__ = 241
            elif self._Properties__count_6 == 21:
                v = CDispatch()
                v.__instance_id__ = 245
            self._Properties__count_6 += 1
            return v
        elif self.__id__ == 255:
            ret_value = None
            if not hasattr(self, '_Properties__count_7'):
                self._Properties__count_7 = 0
            if self._Properties__count_7 == 0:
                v = CDispatch()
                v.__instance_id__ = 258
            elif self._Properties__count_7 == 1:
                v = CDispatch()
                v.__instance_id__ = 262
            elif self._Properties__count_7 == 2:
                v = CDispatch()
                v.__instance_id__ = 266
            elif self._Properties__count_7 == 3:
                v = CDispatch()
                v.__instance_id__ = 270
            elif self._Properties__count_7 == 4:
                v = CDispatch()
                v.__instance_id__ = 274
            elif self._Properties__count_7 == 5:
                v = CDispatch()
                v.__instance_id__ = 278
            elif self._Properties__count_7 == 6:
                v = CDispatch()
                v.__instance_id__ = 282
            elif self._Properties__count_7 == 7:
                v = CDispatch()
                v.__instance_id__ = 286
            elif self._Properties__count_7 == 8:
                v = CDispatch()
                v.__instance_id__ = 290
            elif self._Properties__count_7 == 9:
                v = CDispatch()
                v.__instance_id__ = 294
            elif self._Properties__count_7 == 10:
                v = CDispatch()
                v.__instance_id__ = 298
            elif self._Properties__count_7 == 11:
                v = CDispatch()
                v.__instance_id__ = 302
            elif self._Properties__count_7 == 12:
                v = CDispatch()
                v.__instance_id__ = 306
            elif self._Properties__count_7 == 13:
                v = CDispatch()
                v.__instance_id__ = 310
            elif self._Properties__count_7 == 14:
                v = CDispatch()
                v.__instance_id__ = 314
            elif self._Properties__count_7 == 15:
                v = CDispatch()
                v.__instance_id__ = 318
            elif self._Properties__count_7 == 16:
                v = CDispatch()
                v.__instance_id__ = 322
            elif self._Properties__count_7 == 17:
                v = CDispatch()
                v.__instance_id__ = 326
            elif self._Properties__count_7 == 18:
                v = CDispatch()
                v.__instance_id__ = 330
            elif self._Properties__count_7 == 19:
                v = CDispatch()
                v.__instance_id__ = 334
            elif self._Properties__count_7 == 20:
                v = CDispatch()
                v.__instance_id__ = 336
            elif self._Properties__count_7 == 21:
                v = CDispatch()
                v.__instance_id__ = 340
            self._Properties__count_7 += 1
            return v
        elif self.__id__ == 372:
            ret_value = None
            if not hasattr(self, '_Properties__count_8'):
                self._Properties__count_8 = 0
            if self._Properties__count_8 == 0:
                v = CDispatch()
                v.__instance_id__ = 375
            elif self._Properties__count_8 == 1:
                v = CDispatch()
                v.__instance_id__ = 379
            elif self._Properties__count_8 == 2:
                v = CDispatch()
                v.__instance_id__ = 383
            elif self._Properties__count_8 == 3:
                v = CDispatch()
                v.__instance_id__ = 387
            elif self._Properties__count_8 == 4:
                v = CDispatch()
                v.__instance_id__ = 391
            elif self._Properties__count_8 == 5:
                v = CDispatch()
                v.__instance_id__ = 395
            elif self._Properties__count_8 == 6:
                v = CDispatch()
                v.__instance_id__ = 399
            elif self._Properties__count_8 == 7:
                v = CDispatch()
                v.__instance_id__ = 403
            elif self._Properties__count_8 == 8:
                v = CDispatch()
                v.__instance_id__ = 407
            elif self._Properties__count_8 == 9:
                v = CDispatch()
                v.__instance_id__ = 411
            elif self._Properties__count_8 == 10:
                v = CDispatch()
                v.__instance_id__ = 415
            elif self._Properties__count_8 == 11:
                v = CDispatch()
                v.__instance_id__ = 419
            elif self._Properties__count_8 == 12:
                v = CDispatch()
                v.__instance_id__ = 423
            elif self._Properties__count_8 == 13:
                v = CDispatch()
                v.__instance_id__ = 427
            elif self._Properties__count_8 == 14:
                v = CDispatch()
                v.__instance_id__ = 431
            elif self._Properties__count_8 == 15:
                v = CDispatch()
                v.__instance_id__ = 435
            elif self._Properties__count_8 == 16:
                v = CDispatch()
                v.__instance_id__ = 439
            elif self._Properties__count_8 == 17:
                v = CDispatch()
                v.__instance_id__ = 443
            elif self._Properties__count_8 == 18:
                v = CDispatch()
                v.__instance_id__ = 447
            elif self._Properties__count_8 == 19:
                v = CDispatch()
                v.__instance_id__ = 451
            elif self._Properties__count_8 == 20:
                v = CDispatch()
                v.__instance_id__ = 453
            elif self._Properties__count_8 == 21:
                v = CDispatch()
                v.__instance_id__ = 457
            self._Properties__count_8 += 1
            return v
        elif self.__id__ == 466:
            ret_value = None
            if not hasattr(self, '_Properties__count_9'):
                self._Properties__count_9 = 0
            if self._Properties__count_9 == 0:
                v = CDispatch()
                v.__instance_id__ = 469
            elif self._Properties__count_9 == 1:
                v = CDispatch()
                v.__instance_id__ = 473
            elif self._Properties__count_9 == 2:
                v = CDispatch()
                v.__instance_id__ = 477
            elif self._Properties__count_9 == 3:
                v = CDispatch()
                v.__instance_id__ = 481
            elif self._Properties__count_9 == 4:
                v = CDispatch()
                v.__instance_id__ = 485
            elif self._Properties__count_9 == 5:
                v = CDispatch()
                v.__instance_id__ = 489
            elif self._Properties__count_9 == 6:
                v = CDispatch()
                v.__instance_id__ = 493
            elif self._Properties__count_9 == 7:
                v = CDispatch()
                v.__instance_id__ = 497
            elif self._Properties__count_9 == 8:
                v = CDispatch()
                v.__instance_id__ = 501
            elif self._Properties__count_9 == 9:
                v = CDispatch()
                v.__instance_id__ = 505
            elif self._Properties__count_9 == 10:
                v = CDispatch()
                v.__instance_id__ = 509
            elif self._Properties__count_9 == 11:
                v = CDispatch()
                v.__instance_id__ = 513
            elif self._Properties__count_9 == 12:
                v = CDispatch()
                v.__instance_id__ = 517
            elif self._Properties__count_9 == 13:
                v = CDispatch()
                v.__instance_id__ = 521
            elif self._Properties__count_9 == 14:
                v = CDispatch()
                v.__instance_id__ = 525
            elif self._Properties__count_9 == 15:
                v = CDispatch()
                v.__instance_id__ = 529
            elif self._Properties__count_9 == 16:
                v = CDispatch()
                v.__instance_id__ = 533
            elif self._Properties__count_9 == 17:
                v = CDispatch()
                v.__instance_id__ = 537
            elif self._Properties__count_9 == 18:
                v = CDispatch()
                v.__instance_id__ = 541
            elif self._Properties__count_9 == 19:
                v = CDispatch()
                v.__instance_id__ = 545
            elif self._Properties__count_9 == 20:
                v = CDispatch()
                v.__instance_id__ = 547
            elif self._Properties__count_9 == 21:
                v = CDispatch()
                v.__instance_id__ = 551
            self._Properties__count_9 += 1
            return v

    @Properties_.setter
    def Properties_(self, value):
        pass

    @property
    def Connection(self):
        if self.__id__ == 578:
            v = ()
            v1 =\
 u'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_419ac48a-c4e3-4772-a9c\
1-af7b187f21a1\\openstack_unit_test_vm_419ac48a-c4e3-4772-a9c1-af7b187f21a1.vh\
d'
            v += (v1,)
            return v
        elif self.__id__ == 580:
            v = ()
            v1 =\
 u'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_419ac48a-c4e3-4772-a9c\
1-af7b187f21a1\\configdrive.iso'
            v += (v1,)
            return v
        elif self.__id__ == 610:
            v = ()
            v1 =\
 u'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_419ac48a-c4e3-4772-a9c\
1-af7b187f21a1\\openstack_unit_test_vm_419ac48a-c4e3-4772-a9c1-af7b187f21a1.vh\
d'
            v += (v1,)
            return v
        elif self.__id__ == 612:
            v = ()
            v1 =\
 u'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_419ac48a-c4e3-4772-a9c\
1-af7b187f21a1\\configdrive.iso'
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
        elif self.__id__ == 560:
            return 4
        elif self.__id__ == 561:
            return 4
        elif self.__id__ == 562:
            return 4
        elif self.__id__ == 563:
            return 4
        elif self.__id__ == 564:
            return 4
        elif self.__id__ == 565:
            ret_value = None
            if not hasattr(self, '_JobState_count_24'):
                self._JobState_count_24 = 0
            if self._JobState_count_24 == 0:
                v = 7
            elif self._JobState_count_24 == 1:
                v = 7
            self._JobState_count_24 += 1
            return v
        elif self.__id__ == 596:
            return 4
        elif self.__id__ == 597:
            ret_value = None
            if not hasattr(self, '_JobState_count_26'):
                self._JobState_count_26 = 0
            if self._JobState_count_26 == 0:
                v = 7
            elif self._JobState_count_26 == 1:
                v = 7
            self._JobState_count_26 += 1
            return v
        elif self.__id__ == 620:
            return 4
        elif self.__id__ == 621:
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
        elif self.__id__ == 370:
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
        elif self.__id__ == 464:
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
        if self.__id__ == 592:
            v = _wmi_method()
            v.__instance_id__ = 618
            return v

    @DestroyVirtualSystem.setter
    def DestroyVirtualSystem(self, value):
        pass

    @property
    def Delete(self):
        if self.__id__ == 622:
            v = _wmi_method()
            v.__instance_id__ = 623
            return v
        elif self.__id__ == 624:
            v = _wmi_method()
            v.__instance_id__ = 625
            return v

    @Delete.setter
    def Delete(self, value):
        pass

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
        elif self.__id__ == 354 and wmi_result_class ==\
 'MSVM_ResourceAllocationSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 355
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 356
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 357
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 358
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 359
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 360
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 361
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 362
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 363
            v.append(v1)
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
            return v
        elif self.__id__ == 353 and wmi_result_class ==\
 'Msvm_VirtualSystemSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 354
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
        elif self.__id__ == 568 and wmi_result_class ==\
 'MSVM_ResourceAllocationSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 569
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 570
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 571
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 572
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 573
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 574
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 575
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 576
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 577
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 578
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 579
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 580
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 581
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 582
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 583
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 584
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 585
            v.append(v1)
            return v
        elif self.__id__ == 567 and wmi_result_class ==\
 'Msvm_VirtualSystemSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 568
            v.append(v1)
            return v
        elif self.__id__ == 600 and wmi_result_class ==\
 'MSVM_ResourceAllocationSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 601
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 602
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 603
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 604
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 605
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 606
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 607
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 608
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 609
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 610
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 611
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 612
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 613
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 614
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 615
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 616
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 617
            v.append(v1)
            return v
        elif self.__id__ == 599 and wmi_result_class ==\
 'Msvm_VirtualSystemSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 600
            v.append(v1)
            return v

    def GetText_(self, iObjectTextFormat='<PyOleMissing object at\
 0x04091890>', iFlags=0, objWbemNamedValueSet=None):
        if self.__id__ == 43 and iObjectTextFormat == 1:
            return u'<INSTANCE CLASSNAME="Msvm_MemorySettingData"><PROPERTY\
 NAME="__PATH" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>\\\\HV12OSDEMO1\\root\\virtualization:Msvm_MemorySetting\
Data.InstanceID="Microsoft:DCBC4151-F6C0-4E6C-928E-66ECF7253C1E\\\\4764334d-e0\
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
 TYPE="string"><VALUE>Msvm_MemorySettingData.InstanceID="Microsoft:DCBC4151-F6\
C0-4E6C-928E-66ECF7253C1E\\\\4764334d-e001-4176-82ee-5594ec9b530e"</VALUE></PR\
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
 TYPE="string"><VALUE>Microsoft:DCBC4151-F6C0-4E6C-928E-66ECF7253C1E\\4764334d\
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
ingData.InstanceID="Microsoft:DCBC4151-F6C0-4E6C-928E-66ECF7253C1E\\\\b637f346\
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
 TYPE="string"><VALUE>Msvm_ProcessorSettingData.InstanceID="Microsoft:DCBC4151\
-F6C0-4E6C-928E-66ECF7253C1E\\\\b637f346-6a0e-4dec-af52-bd70cb80a21d\\\\0"</VA\
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
 TYPE="string"><VALUE>Microsoft:DCBC4151-F6C0-4E6C-928E-66ECF7253C1E\\b637f346\
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
 TYPE="string"><VALUE>openstack_unit_test_vm_419ac48a-c4e3-4772-a9c1-af7b187f2\
1a1</VALUE></PROPERTY><PROPERTY NAME="ExternalDataRoot"\
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
ationSettingData.InstanceID="Microsoft:DCBC4151-F6C0-4E6C-928E-66ECF7253C1E\
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
 TYPE="string"><VALUE.ARRAY><VALUE>124a4546-ca41-4f41-81ab-7ad054a3abc8</VALUE\
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
t_test_vm_419ac48a-c4e3-4772-a9c1-af7b187f21a1\\openstack_unit_test_vm_419ac48\
a-c4e3-4772-a9c1-af7b187f21a1.vhd</VALUE></VALUE.ARRAY></PROPERTY.ARRAY><PROPE\
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
ationSettingData.InstanceID="Microsoft:DCBC4151-F6C0-4E6C-928E-66ECF7253C1E\
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
 TYPE="string"><VALUE.ARRAY><VALUE>7678ac8e-88e5-4b0c-bc7e-7261660a29e7</VALUE\
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
 TYPE="string"><VALUE.ARRAY><VALUE>{073bc54e-d644-4e2c-9668-000738efb4a3}</VAL\
UE></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>'
        elif self.__id__ == 372 and iObjectTextFormat == 1:
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
:Definition\\\\7951A5ED-8DC5-42D7-AA8C-9F14C54CEB84\\\\Default"</VALUE></PROPE\
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
 CLASSORIGIN="CIM_ResourceAllocationSettingData" TYPE="string"><VALUE>DVD\
 Drives</VALUE></PROPERTY><PROPERTY NAME="AutomaticAllocation"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY\
 NAME="AutomaticDeallocation" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY NAME="Caption"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>DVD\
 Drive</VALUE></PROPERTY><PROPERTY.ARRAY NAME="Connection"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY.ARRAY><PROPERTY NAME="ConsumerVisibility"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="Description"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>Settings for the\
 Microsoft Virtual DVD Drive.</VALUE></PROPERTY><PROPERTY NAME="ElementName"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>DVD\
 Drive</VALUE></PROPERTY><PROPERTY.ARRAY NAME="HostResource"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY.ARRAY><PROPERTY NAME="InstanceID"\
 CLASSORIGIN="CIM_SettingData"\
 TYPE="string"><VALUE>Microsoft:Definition\\7951A5ED-8DC5-42D7-AA8C-9F14C54CEB\
84\\Default</VALUE></PROPERTY><PROPERTY NAME="Limit"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="MappingBehavior"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="OtherResourceType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="Parent"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAlloc\
ationSettingData.InstanceID="Microsoft:DCBC4151-F6C0-4E6C-928E-66ECF7253C1E\
\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\1"</VALUE></PROPERTY><PROPERTY\
 NAME="PoolID" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Microsoft:7951A5ED-8DC5-42d7-AA8C-9F14C54CEB84\\Root</VA\
LUE></PROPERTY><PROPERTY NAME="Reservation"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="ResourceSubType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Microsoft Synthetic DVD\
 Drive</VALUE></PROPERTY><PROPERTY NAME="ResourceType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"><VALUE>16</VALUE></PROPERTY><PROPERTY NAME="VirtualQuantity"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY.ARRAY\
 NAME="VirtualSystemIdentifiers"\
 CLASSORIGIN="Msvm_ResourceAllocationSettingData"\
 TYPE="string"><VALUE.ARRAY><VALUE>15f22047-8a8b-4d81-aa4e-bf19be5a3733</VALUE\
></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>'
        elif self.__id__ == 466 and iObjectTextFormat == 1:
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
:Definition\\\\D92D268E-9AA8-49DD-8C7D-821CEFB5F597\\\\Default"</VALUE></PROPE\
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
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>ISO Disk\
 Image</VALUE></PROPERTY><PROPERTY.ARRAY NAME="Connection"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE.ARRAY><VALUE>C:\\Hyper-V\\test\\instances\\openstack_uni\
t_test_vm_419ac48a-c4e3-4772-a9c1-af7b187f21a1\\configdrive.iso</VALUE></VALUE\
.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="ConsumerVisibility"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="Description"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>Settings for the\
 Microsoft ISO Disk Image.</VALUE></PROPERTY><PROPERTY NAME="ElementName"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>ISO Disk\
 Image</VALUE></PROPERTY><PROPERTY.ARRAY NAME="HostResource"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY.ARRAY><PROPERTY NAME="InstanceID"\
 CLASSORIGIN="CIM_SettingData"\
 TYPE="string"><VALUE>Microsoft:Definition\\D92D268E-9AA8-49DD-8C7D-821CEFB5F5\
97\\Default</VALUE></PROPERTY><PROPERTY NAME="Limit"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="MappingBehavior"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="OtherResourceType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="Parent"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAlloc\
ationSettingData.InstanceID="Microsoft:DCBC4151-F6C0-4E6C-928E-66ECF7253C1E\
\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\1\\\\0\\\\D"</VALUE></PROPERTY><PR\
OPERTY NAME="PoolID" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Microsoft:D92D268E-9AA8-49dd-8C7D-821CEFB5F597\\Root</VA\
LUE></PROPERTY><PROPERTY NAME="Reservation"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="ResourceSubType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Microsoft Virtual CD/DVD\
 Disk</VALUE></PROPERTY><PROPERTY NAME="ResourceType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"><VALUE>21</VALUE></PROPERTY><PROPERTY NAME="VirtualQuantity"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY.ARRAY\
 NAME="VirtualSystemIdentifiers"\
 CLASSORIGIN="Msvm_ResourceAllocationSettingData"\
 TYPE="string"><VALUE.ARRAY><VALUE>62857f83-7691-4371-a9ef-f1a4b46b711b</VALUE\
></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>'


class _wmi_method(object):

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__

    def __call__(self, *args, **kwargs):
        if len(args) == 0 and self.__id__ == 623:
            v = ()
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 0 and self.__id__ == 625:
            v = ()
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 0 and self.__id__ == 25 and kwargs.get('Path') ==\
 'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_419ac48a-c4e3-4772-a9c1\
-af7b187f21a1\\openstack_unit_test_vm_419ac48a-c4e3-4772-a9c1-af7b187f21a1.vhd\
' and kwargs.get('ParentPath') == 'C:\\Hyper-V\\test\\instances\\_base\\1.vhd':
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_StorageJob.InstanceID="384E20B3-\
96F4-41EA-A9CF-0E7E5BCB7ABD"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v
        elif len(args) == 1 and self.__id__ == 559 and args[0] == 2:
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ConcreteJob.InstanceID="79284D50\
-CC22-45DE-B1DF-2CE1219DE5D7"'
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
 TYPE="string"><VALUE>openstack_unit_test_vm_419ac48a-c4e3-4772-a9c1-af7b187f2\
1a1</VALUE></PROPERTY><PROPERTY NAME="ExternalDataRoot"\
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
="Msvm_ComputerSystem",Name="DCBC4151-F6C0-4E6C-928E-66ECF7253C1E"'
            v += (v1,)
            v1 = None
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 2 and self.__id__ == 44 and args[0] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="DCBC4151-F6C0-4E6C-928E-66ECF7253C1E"' and\
 str(args[1]) == '[u\'<INSTANCE CLASSNAME="Msvm_MemorySettingData"><PROPERTY\
 NAME="__PATH" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>\\\\\\\\HV12OSDEMO1\\\\root\\\\virtualization:Msvm_Memor\
ySettingData.InstanceID="Microsoft:DCBC4151-F6C0-4E6C-928E-66ECF7253C1E\
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
 TYPE="string"><VALUE>Msvm_MemorySettingData.InstanceID="Microsoft:DCBC4151-F6\
C0-4E6C-928E-66ECF7253C1E\\\\\\\\4764334d-e001-4176-82ee-5594ec9b530e"</VALUE>\
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
 TYPE="string"><VALUE>Microsoft:DCBC4151-F6C0-4E6C-928E-66ECF7253C1E\\\\476433\
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
="Msvm_ComputerSystem",Name="DCBC4151-F6C0-4E6C-928E-66ECF7253C1E"' and\
 str(args[1]) == '[u\'<INSTANCE\
 CLASSNAME="Msvm_ProcessorSettingData"><PROPERTY NAME="__PATH"\
 CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>\\\\\\\\HV12OSDEMO1\\\\root\\\\virtualization:Msvm_Proce\
ssorSettingData.InstanceID="Microsoft:DCBC4151-F6C0-4E6C-928E-66ECF7253C1E\
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
 TYPE="string"><VALUE>Msvm_ProcessorSettingData.InstanceID="Microsoft:DCBC4151\
-F6C0-4E6C-928E-66ECF7253C1E\\\\\\\\b637f346-6a0e-4dec-af52-bd70cb80a21d\
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
 TYPE="string"><VALUE>Microsoft:DCBC4151-F6C0-4E6C-928E-66ECF7253C1E\\\\b637f3\
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
rceAllocationSettingData.InstanceID="Microsoft:DCBC4151-F6C0-4E6C-928E-66ECF72\
53C1E\\\\\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\\\\\0"</VALUE></PROPERTY>\
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
 TYPE="string"><VALUE.ARRAY><VALUE>124a4546-ca41-4f41-81ab-7ad054a3abc8</VALUE\
></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="DCBC4151-F6C0-4E6C-928E-66ECF7253C1E"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:DCBC4151-F6C0-4E6C-928E-66ECF7253C1E\\\\83F8638B-8DCA-4152\
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
tack_unit_test_vm_419ac48a-c4e3-4772-a9c1-af7b187f21a1\\\\openstack_unit_test_\
vm_419ac48a-c4e3-4772-a9c1-af7b187f21a1.vhd</VALUE></VALUE.ARRAY></PROPERTY.AR\
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
rceAllocationSettingData.InstanceID="Microsoft:DCBC4151-F6C0-4E6C-928E-66ECF72\
53C1E\\\\\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\\\\\0\\\\\\\\0\\\\\\\\D"<\
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
 TYPE="string"><VALUE.ARRAY><VALUE>7678ac8e-88e5-4b0c-bc7e-7261660a29e7</VALUE\
></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="DCBC4151-F6C0-4E6C-928E-66ECF7253C1E"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:DCBC4151-F6C0-4E6C-928E-66ECF7253C1E\\\\83F8638B-8DCA-4152\
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
 TYPE="string"><VALUE.ARRAY><VALUE>{073bc54e-d644-4e2c-9668-000738efb4a3}</VAL\
UE></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="DCBC4151-F6C0-4E6C-928E-66ECF7253C1E"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:DCBC4151-F6C0-4E6C-928E-66ECF7253C1E\\\\E2412D06-484A-4946\
-99D7-618E38A3A345\\\\0"'
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
 TYPE="string"><VALUE.ARRAY><VALUE>{607efe9d-d90e-486e-b812-a0d926324767}</VAL\
UE></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="DCBC4151-F6C0-4E6C-928E-66ECF7253C1E"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_SyntheticEthernetPortSettingData\
.InstanceID="Microsoft:DCBC4151-F6C0-4E6C-928E-66ECF7253C1E\\\\080A00DB-00D8-4\
7DA-AE90-CEE330A167A6"'
            v1.append(v2)
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 2 and self.__id__ == 462 and str(args[0]) ==\
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
:Definition\\\\\\\\7951A5ED-8DC5-42D7-AA8C-9F14C54CEB84\\\\\\\\Default"</VALUE\
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
 CLASSORIGIN="CIM_ResourceAllocationSettingData" TYPE="string"><VALUE>DVD\
 Drives</VALUE></PROPERTY><PROPERTY NAME="AutomaticAllocation"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY\
 NAME="AutomaticDeallocation" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="boolean"><VALUE>TRUE</VALUE></PROPERTY><PROPERTY NAME="Caption"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>DVD\
 Drive</VALUE></PROPERTY><PROPERTY.ARRAY NAME="Connection"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY.ARRAY><PROPERTY NAME="ConsumerVisibility"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="Description"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>Settings for the\
 Microsoft Virtual DVD Drive.</VALUE></PROPERTY><PROPERTY NAME="ElementName"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>DVD\
 Drive</VALUE></PROPERTY><PROPERTY.ARRAY NAME="HostResource"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY.ARRAY><PROPERTY NAME="InstanceID"\
 CLASSORIGIN="CIM_SettingData"\
 TYPE="string"><VALUE>Microsoft:Definition\\\\7951A5ED-8DC5-42D7-AA8C-9F14C54C\
EB84\\\\Default</VALUE></PROPERTY><PROPERTY NAME="Limit"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="MappingBehavior"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="OtherResourceType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="Parent"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>\\\\\\\\HV12OSDEMO1\\\\root\\\\virtualization:Msvm_Resou\
rceAllocationSettingData.InstanceID="Microsoft:DCBC4151-F6C0-4E6C-928E-66ECF72\
53C1E\\\\\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\\\\\1"</VALUE></PROPERTY>\
<PROPERTY NAME="PoolID" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Microsoft:7951A5ED-8DC5-42d7-AA8C-9F14C54CEB84\\\\Root</\
VALUE></PROPERTY><PROPERTY NAME="Reservation"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="ResourceSubType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Microsoft Synthetic DVD\
 Drive</VALUE></PROPERTY><PROPERTY NAME="ResourceType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"><VALUE>16</VALUE></PROPERTY><PROPERTY NAME="VirtualQuantity"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY.ARRAY\
 NAME="VirtualSystemIdentifiers"\
 CLASSORIGIN="Msvm_ResourceAllocationSettingData"\
 TYPE="string"><VALUE.ARRAY><VALUE>15f22047-8a8b-4d81-aa4e-bf19be5a3733</VALUE\
></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="DCBC4151-F6C0-4E6C-928E-66ECF7253C1E"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:DCBC4151-F6C0-4E6C-928E-66ECF7253C1E\\\\83F8638B-8DCA-4152\
-9EDA-2CA8B33039B4\\\\1\\\\0\\\\D"'
            v1.append(v2)
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 2 and self.__id__ == 555 and str(args[0]) ==\
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
:Definition\\\\\\\\D92D268E-9AA8-49DD-8C7D-821CEFB5F597\\\\\\\\Default"</VALUE\
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
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>ISO Disk\
 Image</VALUE></PROPERTY><PROPERTY.ARRAY NAME="Connection"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE.ARRAY><VALUE>C:\\\\Hyper-V\\\\test\\\\instances\\\\opens\
tack_unit_test_vm_419ac48a-c4e3-4772-a9c1-af7b187f21a1\\\\configdrive.iso</VAL\
UE></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="ConsumerVisibility"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="Description"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>Settings for the\
 Microsoft ISO Disk Image.</VALUE></PROPERTY><PROPERTY NAME="ElementName"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>ISO Disk\
 Image</VALUE></PROPERTY><PROPERTY.ARRAY NAME="HostResource"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY.ARRAY><PROPERTY NAME="InstanceID"\
 CLASSORIGIN="CIM_SettingData"\
 TYPE="string"><VALUE>Microsoft:Definition\\\\D92D268E-9AA8-49DD-8C7D-821CEFB5\
F597\\\\Default</VALUE></PROPERTY><PROPERTY NAME="Limit"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="MappingBehavior"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="OtherResourceType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="Parent"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>\\\\\\\\HV12OSDEMO1\\\\root\\\\virtualization:Msvm_Resou\
rceAllocationSettingData.InstanceID="Microsoft:DCBC4151-F6C0-4E6C-928E-66ECF72\
53C1E\\\\\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\\\\\1\\\\\\\\0\\\\\\\\D"<\
/VALUE></PROPERTY><PROPERTY NAME="PoolID"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Microsoft:D92D268E-9AA8-49dd-8C7D-821CEFB5F597\\\\Root</\
VALUE></PROPERTY><PROPERTY NAME="Reservation"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="ResourceSubType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Microsoft Virtual CD/DVD\
 Disk</VALUE></PROPERTY><PROPERTY NAME="ResourceType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"><VALUE>21</VALUE></PROPERTY><PROPERTY NAME="VirtualQuantity"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY.ARRAY\
 NAME="VirtualSystemIdentifiers"\
 CLASSORIGIN="Msvm_ResourceAllocationSettingData"\
 TYPE="string"><VALUE.ARRAY><VALUE>62857f83-7691-4371-a9ef-f1a4b46b711b</VALUE\
></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="DCBC4151-F6C0-4E6C-928E-66ECF7253C1E"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:DCBC4151-F6C0-4E6C-928E-66ECF7253C1E\\\\83F8638B-8DCA-4152\
-9EDA-2CA8B33039B4\\\\1\\\\0\\\\L"'
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
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_StorageJob.InstanceID="57B4A236-\
4D15-4D1A-A24B-864F81BB5DED"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v
        elif len(args) == 1 and self.__id__ == 595 and args[0] == 3:
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ConcreteJob.InstanceID="7FA1144F\
-12C7-419E-BBDB-00A538C2ABBF"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v
        elif len(args) == 1 and self.__id__ == 618 and args[0] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="DCBC4151-F6C0-4E6C-928E-66ECF7253C1E"':
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ConcreteJob.InstanceID="52BFBDFB\
-687C-45F7-98C9-A31134304AC1"'
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
        elif self.__id__ == 374:
            return\
 u'Microsoft:Definition\\7951A5ED-8DC5-42D7-AA8C-9F14C54CEB84\\Default'
        elif self.__id__ == 378:
            return u'Microsoft Synthetic DVD Drive'
        elif self.__id__ == 382:
            return None
        elif self.__id__ == 386:
            return u'DVD Drive'
        elif self.__id__ == 390:
            return u'Settings for the Microsoft Virtual DVD Drive.'
        elif self.__id__ == 394:
            return None
        elif self.__id__ == 398:
            return u'1'
        elif self.__id__ == 402:
            return True
        elif self.__id__ == 406:
            return True
        elif self.__id__ == 410:
            return u'Microsoft:7951A5ED-8DC5-42d7-AA8C-9F14C54CEB84\\Root'
        elif self.__id__ == 414:
            return u'1'
        elif self.__id__ == 418:
            return u'DVD Drives'
        elif self.__id__ == 422:
            return None
        elif self.__id__ == 426:
            return None
        elif self.__id__ == 430:
            return None
        elif self.__id__ == 434:
            return u'DVD Drive'
        elif self.__id__ == 438:
            return None
        elif self.__id__ == 442:
            return u'1'
        elif self.__id__ == 446:
            return 16
        elif self.__id__ == 450:
            return 0
        elif self.__id__ == 456:
            return None
        elif self.__id__ == 468:
            return\
 u'Microsoft:Definition\\D92D268E-9AA8-49DD-8C7D-821CEFB5F597\\Default'
        elif self.__id__ == 472:
            return u'Microsoft Virtual CD/DVD Disk'
        elif self.__id__ == 476:
            return None
        elif self.__id__ == 480:
            return u'ISO Disk Image'
        elif self.__id__ == 484:
            return u'Settings for the Microsoft ISO Disk Image.'
        elif self.__id__ == 488:
            return None
        elif self.__id__ == 492:
            return u'1'
        elif self.__id__ == 496:
            return True
        elif self.__id__ == 500:
            return True
        elif self.__id__ == 504:
            return u'Microsoft:D92D268E-9AA8-49dd-8C7D-821CEFB5F597\\Root'
        elif self.__id__ == 508:
            return u'1'
        elif self.__id__ == 512:
            return u'Disks'
        elif self.__id__ == 516:
            return None
        elif self.__id__ == 520:
            return None
        elif self.__id__ == 524:
            return None
        elif self.__id__ == 528:
            return u'ISO Disk Image'
        elif self.__id__ == 532:
            return None
        elif self.__id__ == 536:
            return u'1'
        elif self.__id__ == 540:
            return 21
        elif self.__id__ == 544:
            return 0
        elif self.__id__ == 550:
            return None

    @Value.setter
    def Value(self, value):
        pass

    def __call__(self, *args):
        if len(args) == 0 and self.__id__ == 153:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:DCBC4151-F6C0-4E6C-928E-66ECF7253C1E\\\\83F8638B-8DCA-4152\
-9EDA-2CA8B33039B4\\\\0"'
        elif len(args) == 0 and self.__id__ == 157:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="DCBC4151-F6C0-4E6C-928E-66ECF7253C1E"'
        elif len(args) == 0 and self.__id__ == 250:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="DCBC4151-F6C0-4E6C-928E-66ECF7253C1E"'
        elif len(args) == 0 and self.__id__ == 345:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="DCBC4151-F6C0-4E6C-928E-66ECF7253C1E"'
        elif len(args) == 0 and self.__id__ == 459:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:DCBC4151-F6C0-4E6C-928E-66ECF7253C1E\\\\83F8638B-8DCA-4152\
-9EDA-2CA8B33039B4\\\\1"'
        elif len(args) == 0 and self.__id__ == 463:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="DCBC4151-F6C0-4E6C-928E-66ECF7253C1E"'
        elif len(args) == 0 and self.__id__ == 556:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="DCBC4151-F6C0-4E6C-928E-66ECF7253C1E"'
        elif len(args) == 0 and self.__id__ == 45:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="DCBC4151-F6C0-4E6C-928E-66ECF7253C1E"'
        elif len(args) == 0 and self.__id__ == 48:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="DCBC4151-F6C0-4E6C-928E-66ECF7253C1E"'
        elif len(args) == 0 and self.__id__ == 351:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="DCBC4151-F6C0-4E6C-928E-66ECF7253C1E"'
        elif len(args) == 0 and self.__id__ == 619:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="DCBC4151-F6C0-4E6C-928E-66ECF7253C1E"'

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
        elif self.__id__ == 373 and strName == u'InstanceID':
            v = CDispatch()
            v.__instance_id__ = 374
            return v
        elif self.__id__ == 377 and strName == u'ResourceSubType':
            v = CDispatch()
            v.__instance_id__ = 378
            return v
        elif self.__id__ == 381 and strName == u'HostResource':
            v = CDispatch()
            v.__instance_id__ = 382
            return v
        elif self.__id__ == 385 and strName == u'ElementName':
            v = CDispatch()
            v.__instance_id__ = 386
            return v
        elif self.__id__ == 389 and strName == u'Description':
            v = CDispatch()
            v.__instance_id__ = 390
            return v
        elif self.__id__ == 393 and strName == u'Parent':
            v = CDispatch()
            v.__instance_id__ = 394
            return v
        elif self.__id__ == 397 and strName == u'VirtualQuantity':
            v = CDispatch()
            v.__instance_id__ = 398
            return v
        elif self.__id__ == 401 and strName == u'AutomaticDeallocation':
            v = CDispatch()
            v.__instance_id__ = 402
            return v
        elif self.__id__ == 405 and strName == u'AutomaticAllocation':
            v = CDispatch()
            v.__instance_id__ = 406
            return v
        elif self.__id__ == 409 and strName == u'PoolID':
            v = CDispatch()
            v.__instance_id__ = 410
            return v
        elif self.__id__ == 413 and strName == u'Reservation':
            v = CDispatch()
            v.__instance_id__ = 414
            return v
        elif self.__id__ == 417 and strName == u'AllocationUnits':
            v = CDispatch()
            v.__instance_id__ = 418
            return v
        elif self.__id__ == 421 and strName == u'MappingBehavior':
            v = CDispatch()
            v.__instance_id__ = 422
            return v
        elif self.__id__ == 425 and strName == u'Address':
            v = CDispatch()
            v.__instance_id__ = 426
            return v
        elif self.__id__ == 429 and strName == u'OtherResourceType':
            v = CDispatch()
            v.__instance_id__ = 430
            return v
        elif self.__id__ == 433 and strName == u'Caption':
            v = CDispatch()
            v.__instance_id__ = 434
            return v
        elif self.__id__ == 437 and strName == u'ConsumerVisibility':
            v = CDispatch()
            v.__instance_id__ = 438
            return v
        elif self.__id__ == 441 and strName == u'Limit':
            v = CDispatch()
            v.__instance_id__ = 442
            return v
        elif self.__id__ == 445 and strName == u'ResourceType':
            v = CDispatch()
            v.__instance_id__ = 446
            return v
        elif self.__id__ == 449 and strName == u'Weight':
            v = CDispatch()
            v.__instance_id__ = 450
            return v
        elif self.__id__ == 455 and strName == u'Connection':
            v = CDispatch()
            v.__instance_id__ = 456
            return v
        elif self.__id__ == 467 and strName == u'InstanceID':
            v = CDispatch()
            v.__instance_id__ = 468
            return v
        elif self.__id__ == 471 and strName == u'ResourceSubType':
            v = CDispatch()
            v.__instance_id__ = 472
            return v
        elif self.__id__ == 475 and strName == u'HostResource':
            v = CDispatch()
            v.__instance_id__ = 476
            return v
        elif self.__id__ == 479 and strName == u'ElementName':
            v = CDispatch()
            v.__instance_id__ = 480
            return v
        elif self.__id__ == 483 and strName == u'Description':
            v = CDispatch()
            v.__instance_id__ = 484
            return v
        elif self.__id__ == 487 and strName == u'Parent':
            v = CDispatch()
            v.__instance_id__ = 488
            return v
        elif self.__id__ == 491 and strName == u'VirtualQuantity':
            v = CDispatch()
            v.__instance_id__ = 492
            return v
        elif self.__id__ == 495 and strName == u'AutomaticDeallocation':
            v = CDispatch()
            v.__instance_id__ = 496
            return v
        elif self.__id__ == 499 and strName == u'AutomaticAllocation':
            v = CDispatch()
            v.__instance_id__ = 500
            return v
        elif self.__id__ == 503 and strName == u'PoolID':
            v = CDispatch()
            v.__instance_id__ = 504
            return v
        elif self.__id__ == 507 and strName == u'Reservation':
            v = CDispatch()
            v.__instance_id__ = 508
            return v
        elif self.__id__ == 511 and strName == u'AllocationUnits':
            v = CDispatch()
            v.__instance_id__ = 512
            return v
        elif self.__id__ == 515 and strName == u'MappingBehavior':
            v = CDispatch()
            v.__instance_id__ = 516
            return v
        elif self.__id__ == 519 and strName == u'Address':
            v = CDispatch()
            v.__instance_id__ = 520
            return v
        elif self.__id__ == 523 and strName == u'OtherResourceType':
            v = CDispatch()
            v.__instance_id__ = 524
            return v
        elif self.__id__ == 527 and strName == u'Caption':
            v = CDispatch()
            v.__instance_id__ = 528
            return v
        elif self.__id__ == 531 and strName == u'ConsumerVisibility':
            v = CDispatch()
            v.__instance_id__ = 532
            return v
        elif self.__id__ == 535 and strName == u'Limit':
            v = CDispatch()
            v.__instance_id__ = 536
            return v
        elif self.__id__ == 539 and strName == u'ResourceType':
            v = CDispatch()
            v.__instance_id__ = 540
            return v
        elif self.__id__ == 543 and strName == u'Weight':
            v = CDispatch()
            v.__instance_id__ = 544
            return v
        elif self.__id__ == 549 and strName == u'Connection':
            v = CDispatch()
            v.__instance_id__ = 550
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
        elif self.__id__ == 375 and strName == u'InstanceID':
            v = CDispatch()
            v.__instance_id__ = 376
            return v
        elif self.__id__ == 379 and strName == u'ResourceSubType':
            v = CDispatch()
            v.__instance_id__ = 380
            return v
        elif self.__id__ == 383 and strName == u'HostResource':
            v = CDispatch()
            v.__instance_id__ = 384
            return v
        elif self.__id__ == 387 and strName == u'ElementName':
            v = CDispatch()
            v.__instance_id__ = 388
            return v
        elif self.__id__ == 391 and strName == u'Description':
            v = CDispatch()
            v.__instance_id__ = 392
            return v
        elif self.__id__ == 395 and strName == u'Parent':
            v = CDispatch()
            v.__instance_id__ = 396
            return v
        elif self.__id__ == 399 and strName == u'VirtualQuantity':
            v = CDispatch()
            v.__instance_id__ = 400
            return v
        elif self.__id__ == 403 and strName == u'AutomaticDeallocation':
            v = CDispatch()
            v.__instance_id__ = 404
            return v
        elif self.__id__ == 407 and strName == u'AutomaticAllocation':
            v = CDispatch()
            v.__instance_id__ = 408
            return v
        elif self.__id__ == 411 and strName == u'PoolID':
            v = CDispatch()
            v.__instance_id__ = 412
            return v
        elif self.__id__ == 415 and strName == u'Reservation':
            v = CDispatch()
            v.__instance_id__ = 416
            return v
        elif self.__id__ == 419 and strName == u'AllocationUnits':
            v = CDispatch()
            v.__instance_id__ = 420
            return v
        elif self.__id__ == 423 and strName == u'MappingBehavior':
            v = CDispatch()
            v.__instance_id__ = 424
            return v
        elif self.__id__ == 427 and strName == u'Address':
            v = CDispatch()
            v.__instance_id__ = 428
            return v
        elif self.__id__ == 431 and strName == u'OtherResourceType':
            v = CDispatch()
            v.__instance_id__ = 432
            return v
        elif self.__id__ == 435 and strName == u'Caption':
            v = CDispatch()
            v.__instance_id__ = 436
            return v
        elif self.__id__ == 439 and strName == u'ConsumerVisibility':
            v = CDispatch()
            v.__instance_id__ = 440
            return v
        elif self.__id__ == 443 and strName == u'Limit':
            v = CDispatch()
            v.__instance_id__ = 444
            return v
        elif self.__id__ == 447 and strName == u'ResourceType':
            v = CDispatch()
            v.__instance_id__ = 448
            return v
        elif self.__id__ == 451 and strName == u'Weight':
            v = CDispatch()
            v.__instance_id__ = 452
            return v
        elif self.__id__ == 453 and strName == u'VirtualSystemIdentifiers':
            v = CDispatch()
            v.__instance_id__ = 454
            return v
        elif self.__id__ == 457 and strName == u'Connection':
            v = CDispatch()
            v.__instance_id__ = 458
            return v
        elif self.__id__ == 469 and strName == u'InstanceID':
            v = CDispatch()
            v.__instance_id__ = 470
            return v
        elif self.__id__ == 473 and strName == u'ResourceSubType':
            v = CDispatch()
            v.__instance_id__ = 474
            return v
        elif self.__id__ == 477 and strName == u'HostResource':
            v = CDispatch()
            v.__instance_id__ = 478
            return v
        elif self.__id__ == 481 and strName == u'ElementName':
            v = CDispatch()
            v.__instance_id__ = 482
            return v
        elif self.__id__ == 485 and strName == u'Description':
            v = CDispatch()
            v.__instance_id__ = 486
            return v
        elif self.__id__ == 489 and strName == u'Parent':
            v = CDispatch()
            v.__instance_id__ = 490
            return v
        elif self.__id__ == 493 and strName == u'VirtualQuantity':
            v = CDispatch()
            v.__instance_id__ = 494
            return v
        elif self.__id__ == 497 and strName == u'AutomaticDeallocation':
            v = CDispatch()
            v.__instance_id__ = 498
            return v
        elif self.__id__ == 501 and strName == u'AutomaticAllocation':
            v = CDispatch()
            v.__instance_id__ = 502
            return v
        elif self.__id__ == 505 and strName == u'PoolID':
            v = CDispatch()
            v.__instance_id__ = 506
            return v
        elif self.__id__ == 509 and strName == u'Reservation':
            v = CDispatch()
            v.__instance_id__ = 510
            return v
        elif self.__id__ == 513 and strName == u'AllocationUnits':
            v = CDispatch()
            v.__instance_id__ = 514
            return v
        elif self.__id__ == 517 and strName == u'MappingBehavior':
            v = CDispatch()
            v.__instance_id__ = 518
            return v
        elif self.__id__ == 521 and strName == u'Address':
            v = CDispatch()
            v.__instance_id__ = 522
            return v
        elif self.__id__ == 525 and strName == u'OtherResourceType':
            v = CDispatch()
            v.__instance_id__ = 526
            return v
        elif self.__id__ == 529 and strName == u'Caption':
            v = CDispatch()
            v.__instance_id__ = 530
            return v
        elif self.__id__ == 533 and strName == u'ConsumerVisibility':
            v = CDispatch()
            v.__instance_id__ = 534
            return v
        elif self.__id__ == 537 and strName == u'Limit':
            v = CDispatch()
            v.__instance_id__ = 538
            return v
        elif self.__id__ == 541 and strName == u'ResourceType':
            v = CDispatch()
            v.__instance_id__ = 542
            return v
        elif self.__id__ == 545 and strName == u'Weight':
            v = CDispatch()
            v.__instance_id__ = 546
            return v
        elif self.__id__ == 547 and strName == u'VirtualSystemIdentifiers':
            v = CDispatch()
            v.__instance_id__ = 548
            return v
        elif self.__id__ == 551 and strName == u'Connection':
            v = CDispatch()
            v.__instance_id__ = 552
            return v
