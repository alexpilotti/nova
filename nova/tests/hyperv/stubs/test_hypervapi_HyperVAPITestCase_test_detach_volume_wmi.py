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
        ret_value = None
        global _WMI_count_2
        if not '_WMI_count_2' in globals():
            _WMI_count_2 = 0
        if _WMI_count_2 == 0:
            v = _wmi_namespace(4)
        elif _WMI_count_2 == 1:
            v = _wmi_namespace(532)
        _WMI_count_2 += 1
        return v
    elif moniker == '//./root/virtualization':
        ret_value = None
        global _WMI_count_3
        if not '_WMI_count_3' in globals():
            _WMI_count_3 = 0
        if _WMI_count_3 == 0:
            v = _wmi_namespace(9)
        elif _WMI_count_3 == 1:
            v = _wmi_namespace(11)
        elif _WMI_count_3 == 2:
            v = _wmi_namespace(371)
        _WMI_count_3 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_StorageJob.InstanceID="D2D9F35C-C5DF\
-4289-B392-DD62EB58B98B"':
        ret_value = None
        global _WMI_count_4
        if not '_WMI_count_4' in globals():
            _WMI_count_4 = 0
        if _WMI_count_4 == 0:
            v = _wmi_object(14)
        elif _WMI_count_4 == 1:
            v = _wmi_object(15)
        elif _WMI_count_4 == 2:
            v = _wmi_object(16)
        elif _WMI_count_4 == 3:
            v = _wmi_object(17)
        elif _WMI_count_4 == 4:
            v = _wmi_object(18)
        elif _WMI_count_4 == 5:
            v = _wmi_object(19)
        elif _WMI_count_4 == 6:
            v = _wmi_object(20)
        elif _WMI_count_4 == 7:
            v = _wmi_object(21)
        elif _WMI_count_4 == 8:
            v = _wmi_object(22)
        _WMI_count_4 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_StorageJob.InstanceID="86DCA9CA-88CB\
-4D38-8A87-4F1657077E40"':
        ret_value = None
        global _WMI_count_5
        if not '_WMI_count_5' in globals():
            _WMI_count_5 = 0
        if _WMI_count_5 == 0:
            v = _wmi_object(25)
        elif _WMI_count_5 == 1:
            v = _wmi_object(26)
        elif _WMI_count_5 == 2:
            v = _wmi_object(27)
        elif _WMI_count_5 == 3:
            v = _wmi_object(28)
        elif _WMI_count_5 == 4:
            v = _wmi_object(29)
        elif _WMI_count_5 == 5:
            v = _wmi_object(30)
        elif _WMI_count_5 == 6:
            v = _wmi_object(31)
        elif _WMI_count_5 == 7:
            v = _wmi_object(32)
        elif _WMI_count_5 == 8:
            v = _wmi_object(33)
        elif _WMI_count_5 == 9:
            v = _wmi_object(34)
        _WMI_count_5 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_ConcreteJob.InstanceID="B799C1C0-626\
8-40AD-8499-21064DDA27D1"':
        ret_value = None
        global _WMI_count_6
        if not '_WMI_count_6' in globals():
            _WMI_count_6 = 0
        if _WMI_count_6 == 0:
            v = _wmi_object(355)
        elif _WMI_count_6 == 1:
            v = _wmi_object(356)
        elif _WMI_count_6 == 2:
            v = _wmi_object(357)
        elif _WMI_count_6 == 3:
            v = _wmi_object(358)
        elif _WMI_count_6 == 4:
            v = _wmi_object(359)
        elif _WMI_count_6 == 5:
            v = _wmi_object(360)
        elif _WMI_count_6 == 6:
            v = _wmi_object(361)
        _WMI_count_6 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_ConcreteJob.InstanceID="947AAABB-C58\
2-4C88-8869-6B5B48E9FF86"':
        ret_value = None
        global _WMI_count_7
        if not '_WMI_count_7' in globals():
            _WMI_count_7 = 0
        if _WMI_count_7 == 0:
            v = _wmi_object(540)
        elif _WMI_count_7 == 1:
            v = _wmi_object(541)
        _WMI_count_7 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_ConcreteJob.InstanceID="28789C5D-CD3\
3-4A2C-BE31-85CF6328CA5E"':
        ret_value = None
        global _WMI_count_8
        if not '_WMI_count_8' in globals():
            _WMI_count_8 = 0
        if _WMI_count_8 == 0:
            v = _wmi_object(562)
        elif _WMI_count_8 == 1:
            v = _wmi_object(563)
        _WMI_count_8 += 1
        return v


class _wmi_namespace(object):

    def __init__(self, instance_id=1, *args, **kwargs):
        self.__instance_id__ = instance_id

    @property
    def __id__(self):
        return self.__instance_id__

    @property
    def Win32_OperatingSystem(self):
        if self.__id__ == 4:
            v = _wmi_class(5)
            return v

    @Win32_OperatingSystem.setter
    def Win32_OperatingSystem(self, value):
        pass

    @property
    def MSFT_iSCSITarget(self):
        if self.__id__ == 7:
            ret_value = None
            if not hasattr(self, '_MSFT_iSCSITarget_count_0'):
                self._MSFT_iSCSITarget_count_0 = 0
            if self._MSFT_iSCSITarget_count_0 == 0:
                v = _wmi_class(365)
            elif self._MSFT_iSCSITarget_count_0 == 1:
                v = _wmi_class(506)
            self._MSFT_iSCSITarget_count_0 += 1
            return v

    @MSFT_iSCSITarget.setter
    def MSFT_iSCSITarget(self, value):
        pass

    @property
    def Msvm_ResourceAllocationSettingData(self):
        if self.__id__ == 9:
            ret_value = None
            if not hasattr(self,
 '_Msvm_ResourceAllocationSettingData_count_0'):
                self._Msvm_ResourceAllocationSettingData_count_0 = 0
            if self._Msvm_ResourceAllocationSettingData_count_0 == 0:
                v = _wmi_class(65)
            elif self._Msvm_ResourceAllocationSettingData_count_0 == 1:
                v = _wmi_class(159)
            elif self._Msvm_ResourceAllocationSettingData_count_0 == 2:
                v = _wmi_class(254)
            self._Msvm_ResourceAllocationSettingData_count_0 += 1
            return v
        elif self.__id__ == 371:
            v = _wmi_class(394)
            return v

    @Msvm_ResourceAllocationSettingData.setter
    def Msvm_ResourceAllocationSettingData(self, value):
        pass

    @property
    def MSFT_iSCSITargetPortal(self):
        if self.__id__ == 7:
            v = _wmi_class(362)
            return v

    @MSFT_iSCSITargetPortal.setter
    def MSFT_iSCSITargetPortal(self, value):
        pass

    @property
    def Msvm_VirtualSystemManagementService(self):
        if self.__id__ == 9:
            ret_value = None
            if not hasattr(self,
 '_Msvm_VirtualSystemManagementService_count_0'):
                self._Msvm_VirtualSystemManagementService_count_0 = 0
            if self._Msvm_VirtualSystemManagementService_count_0 == 0:
                v = _wmi_class(35)
            elif self._Msvm_VirtualSystemManagementService_count_0 == 1:
                v = _wmi_class(154)
            elif self._Msvm_VirtualSystemManagementService_count_0 == 2:
                v = _wmi_class(247)
            elif self._Msvm_VirtualSystemManagementService_count_0 == 3:
                v = _wmi_class(342)
            elif self._Msvm_VirtualSystemManagementService_count_0 == 4:
                v = _wmi_class(348)
            self._Msvm_VirtualSystemManagementService_count_0 += 1
            return v
        elif self.__id__ == 11:
            v = _wmi_class(535)
            return v
        elif self.__id__ == 371:
            ret_value = None
            if not hasattr(self,
 '_Msvm_VirtualSystemManagementService_count_2'):
                self._Msvm_VirtualSystemManagementService_count_2 = 0
            if self._Msvm_VirtualSystemManagementService_count_2 == 0:
                v = _wmi_class(484)
            elif self._Msvm_VirtualSystemManagementService_count_2 == 1:
                v = _wmi_class(501)
            self._Msvm_VirtualSystemManagementService_count_2 += 1
            return v

    @Msvm_VirtualSystemManagementService.setter
    def Msvm_VirtualSystemManagementService(self, value):
        pass

    @property
    def Msvm_ComputerSystem(self):
        if self.__id__ == 9:
            ret_value = None
            if not hasattr(self, '_Msvm_ComputerSystem_count_0'):
                self._Msvm_ComputerSystem_count_0 = 0
            if self._Msvm_ComputerSystem_count_0 == 0:
                v = _wmi_class(10)
            elif self._Msvm_ComputerSystem_count_0 == 1:
                v = _wmi_class(40)
            elif self._Msvm_ComputerSystem_count_0 == 2:
                v = _wmi_class(346)
            elif self._Msvm_ComputerSystem_count_0 == 3:
                v = _wmi_class(352)
            self._Msvm_ComputerSystem_count_0 += 1
            return v
        elif self.__id__ == 11:
            ret_value = None
            if not hasattr(self, '_Msvm_ComputerSystem_count_1'):
                self._Msvm_ComputerSystem_count_1 = 0
            if self._Msvm_ComputerSystem_count_1 == 0:
                v = _wmi_class(512)
            elif self._Msvm_ComputerSystem_count_1 == 1:
                v = _wmi_class(530)
            elif self._Msvm_ComputerSystem_count_1 == 2:
                v = _wmi_class(533)
            elif self._Msvm_ComputerSystem_count_1 == 3:
                v = _wmi_class(537)
            elif self._Msvm_ComputerSystem_count_1 == 4:
                v = _wmi_class(542)
            self._Msvm_ComputerSystem_count_1 += 1
            return v

    @Msvm_ComputerSystem.setter
    def Msvm_ComputerSystem(self, value):
        pass

    @property
    def Msvm_VirtualSystemGlobalSettingData(self):
        if self.__id__ == 9:
            v = _wmi_class(37)
            return v

    @Msvm_VirtualSystemGlobalSettingData.setter
    def Msvm_VirtualSystemGlobalSettingData(self, value):
        pass

    @property
    def MSFT_iSCSISession(self):
        if self.__id__ == 7:
            v = _wmi_class(508)
            return v

    @MSFT_iSCSISession.setter
    def MSFT_iSCSISession(self, value):
        pass

    @property
    def MSVM_ComputerSystem(self):
        if self.__id__ == 9:
            ret_value = None
            if not hasattr(self, '_MSVM_ComputerSystem_count_0'):
                self._MSVM_ComputerSystem_count_0 = 0
            if self._MSVM_ComputerSystem_count_0 == 0:
                v = _wmi_class(49)
            elif self._MSVM_ComputerSystem_count_0 == 1:
                v = _wmi_class(251)
            self._MSVM_ComputerSystem_count_0 += 1
            return v
        elif self.__id__ == 371:
            ret_value = None
            if not hasattr(self, '_MSVM_ComputerSystem_count_1'):
                self._MSVM_ComputerSystem_count_1 = 0
            if self._MSVM_ComputerSystem_count_1 == 0:
                v = _wmi_class(374)
            elif self._MSVM_ComputerSystem_count_1 == 1:
                v = _wmi_class(499)
            self._MSVM_ComputerSystem_count_1 += 1
            return v

    @MSVM_ComputerSystem.setter
    def MSVM_ComputerSystem(self, value):
        pass

    def query(self, wql, instance_of=None, fields='[]'):
        if self.__id__ == 3 and wql == 'SELECT * FROM\
 MSiSCSIInitiator_SessionClass                     WHERE\
 TargetName=\'iqn.2010-10.org.openstack:volume-ccb39627-34fa-4f47-968b-6580d9d\
7ee2b\'':
            ret_value = None
            if not hasattr(self, '_query_count_0'):
                self._query_count_0 = 0
            if self._query_count_0 == 0:
                v = []
            elif self._query_count_0 == 1:
                v = []
            self._query_count_0 += 1
            return v
        elif self.__id__ == 8 and wql == 'SELECT * FROM\
 MSiSCSIInitiator_SessionClass                 WHERE\
 TargetName=\'iqn.2010-10.org.openstack:volume-ccb39627-34fa-4f47-968b-6580d9d\
7ee2b\'':
            ret_value = None
            if not hasattr(self, '_query_count_1'):
                self._query_count_1 = 0
            if self._query_count_1 == 0:
                v = []
                v1 = _wmi_object(368)
                v.append(v1)
            elif self._query_count_1 == 1:
                v = []
                v1 = _wmi_object(488)
                v.append(v1)
            self._query_count_1 += 1
            return v
        elif self.__id__ == 532 and wql == u'Select * from CIM_DataFile where\
 Name =\
 \'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_82c326ef-3696-41c4-ad5\
1-9fd855bd8fa7\\openstack_unit_test_vm_82c326ef-3696-41c4-ad51-9fd855bd8fa7.vh\
d\'':
            v = []
            v1 = _wmi_object(564)
            v.append(v1)
            return v
        elif self.__id__ == 9 and wql == 'Select * from\
 Msvm_ImageManagementService':
            v = []
            v1 = _wmi_object(23)
            v.append(v1)
            return v
        elif self.__id__ == 9 and wql == 'SELECT * FROM\
 Msvm_ResourceAllocationSettingData             WHERE ResourceSubType LIKE\
 \'Microsoft Synthetic Disk Drive\'            AND InstanceID LIKE\
 \'%Default%\'':
            v = []
            v1 = _wmi_object(64)
            v.append(v1)
            return v
        elif self.__id__ == 9 and wql == 'SELECT * FROM\
 Msvm_ResourceAllocationSettingData                  WHERE ResourceSubType\
 LIKE \'Microsoft Virtual Hard Disk\' AND                  InstanceID LIKE\
 \'%Default%\' ':
            v = []
            v1 = _wmi_object(158)
            v.append(v1)
            return v
        elif self.__id__ == 9 and wql == 'SELECT * FROM\
 Msvm_ResourceAllocationSettingData                 WHERE ResourceSubType =\
 \'Microsoft Synthetic SCSI Controller\'                AND InstanceID LIKE\
 \'%Default%\'':
            v = []
            v1 = _wmi_object(253)
            v.append(v1)
            return v
        elif self.__id__ == 11 and wql == 'Select * from\
 Msvm_ImageManagementService':
            v = []
            v1 = _wmi_object(12)
            v.append(v1)
            return v
        elif self.__id__ == 371 and wql == 'SELECT * FROM Msvm_DiskDrive WHERE\
 DriveNumber=1':
            ret_value = None
            if not hasattr(self, '_query_count_8'):
                self._query_count_8 = 0
            if self._query_count_8 == 0:
                v = []
                v1 = _wmi_object(372)
                v.append(v1)
            elif self._query_count_8 == 1:
                v = []
                v1 = _wmi_object(373)
                v.append(v1)
            elif self._query_count_8 == 2:
                v = []
                v1 = _wmi_object(491)
                v.append(v1)
            elif self._query_count_8 == 3:
                v = []
                v1 = _wmi_object(492)
                v.append(v1)
            self._query_count_8 += 1
            return v
        elif self.__id__ == 371 and wql == u'SELECT * FROM\
 Msvm_ResourceAllocationSettingData                 WHERE ResourceSubType LIKE\
 \'Microsoft Physical Disk Drive\'                AND Parent =\
 \'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:04FB9E92-46A2-4F69-9555-6E4323312DA2\\\\5F053DDB-3C35-4A44\
-8E4E-2056CC3A440A\\\\0"\'':
            v = []
            return v
        elif self.__id__ == 371 and wql == 'SELECT * FROM\
 Msvm_ResourceAllocationSettingData                 WHERE ResourceSubType LIKE\
 \'Microsoft Physical Disk Drive\'                AND InstanceID LIKE\
 \'%Default%\'':
            v = []
            v1 = _wmi_object(393)
            v.append(v1)
            return v
        elif self.__id__ == 371 and wql == 'SELECT * FROM\
 Msvm_ResourceAllocationSettingData                 WHERE ResourceSubType LIKE\
 \'Microsoft Physical Disk Drive\'':
            v = []
            v1 = _wmi_object(493)
            v.append(v1)
            v1 = _wmi_object(494)
            v.append(v1)
            v1 = _wmi_object(495)
            v.append(v1)
            v1 = _wmi_object(496)
            v.append(v1)
            v1 = _wmi_object(497)
            v.append(v1)
            return v


class _wmi_class(object):

    def __init__(self, instance_id=1, *args, **kwargs):
        self.__instance_id__ = instance_id

    @property
    def __id__(self):
        return self.__instance_id__

    @property
    def New(self):
        if self.__id__ == 362:
            v = _wmi_method(363)
            return v

    @New.setter
    def New(self, value):
        pass

    @property
    def Connect(self):
        if self.__id__ == 365:
            v = _wmi_method(366)
            return v

    @Connect.setter
    def Connect(self, value):
        pass

    def __call__(self, fields='[]', **where_clause):
        if self.__id__ == 508 and where_clause.get('TargetNodeAddress') ==\
 'iqn.2010-10.org.openstack:volume-ccb39627-34fa-4f47-968b-6580d9d7ee2b':
            v = []
            v1 = _wmi_object(509)
            v.append(v1)
            return v
        elif self.__id__ == 506 and where_clause.get('NodeAddress') ==\
 'iqn.2010-10.org.openstack:volume-ccb39627-34fa-4f47-968b-6580d9d7ee2b':
            v = []
            v1 = _wmi_object(507)
            v.append(v1)
            return v
        elif self.__id__ == 5:
            v = []
            v1 = _wmi_object(6)
            v.append(v1)
            return v
        elif self.__id__ == 49 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_82c326ef-3696-41c4-ad51-9fd855bd8fa7':
            v = []
            v1 = _wmi_object(50)
            v.append(v1)
            return v
        elif self.__id__ == 251 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_82c326ef-3696-41c4-ad51-9fd855bd8fa7':
            v = []
            v1 = _wmi_object(252)
            v.append(v1)
            return v
        elif self.__id__ == 10 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_82c326ef-3696-41c4-ad51-9fd855bd8fa7':
            v = []
            return v
        elif self.__id__ == 40 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_82c326ef-3696-41c4-ad51-9fd855bd8fa7':
            v = []
            v1 = _wmi_object(41)
            v.append(v1)
            return v
        elif self.__id__ == 346 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_82c326ef-3696-41c4-ad51-9fd855bd8fa7':
            v = []
            v1 = _wmi_object(347)
            v.append(v1)
            return v
        elif self.__id__ == 352 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_82c326ef-3696-41c4-ad51-9fd855bd8fa7':
            v = []
            v1 = _wmi_object(353)
            v.append(v1)
            return v
        elif self.__id__ == 35:
            v = []
            v1 = _wmi_object(36)
            v.append(v1)
            return v
        elif self.__id__ == 154:
            v = []
            v1 = _wmi_object(155)
            v.append(v1)
            return v
        elif self.__id__ == 247:
            v = []
            v1 = _wmi_object(248)
            v.append(v1)
            return v
        elif self.__id__ == 342:
            v = []
            v1 = _wmi_object(343)
            v.append(v1)
            return v
        elif self.__id__ == 348:
            v = []
            v1 = _wmi_object(349)
            v.append(v1)
            return v
        elif self.__id__ == 512 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_82c326ef-3696-41c4-ad51-9fd855bd8fa7':
            v = []
            v1 = _wmi_object(513)
            v.append(v1)
            return v
        elif self.__id__ == 530 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_82c326ef-3696-41c4-ad51-9fd855bd8fa7':
            v = []
            v1 = _wmi_object(531)
            v.append(v1)
            return v
        elif self.__id__ == 533 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_82c326ef-3696-41c4-ad51-9fd855bd8fa7':
            v = []
            v1 = _wmi_object(534)
            v.append(v1)
            return v
        elif self.__id__ == 537 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_82c326ef-3696-41c4-ad51-9fd855bd8fa7':
            v = []
            v1 = _wmi_object(538)
            v.append(v1)
            return v
        elif self.__id__ == 542 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_82c326ef-3696-41c4-ad51-9fd855bd8fa7':
            v = []
            v1 = _wmi_object(543)
            v.append(v1)
            return v
        elif self.__id__ == 535:
            v = []
            v1 = _wmi_object(536)
            v.append(v1)
            return v
        elif self.__id__ == 374 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_82c326ef-3696-41c4-ad51-9fd855bd8fa7':
            v = []
            v1 = _wmi_object(375)
            v.append(v1)
            return v
        elif self.__id__ == 499 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_82c326ef-3696-41c4-ad51-9fd855bd8fa7':
            v = []
            v1 = _wmi_object(500)
            v.append(v1)
            return v
        elif self.__id__ == 484:
            v = []
            v1 = _wmi_object(485)
            v.append(v1)
            return v
        elif self.__id__ == 501:
            v = []
            v1 = _wmi_object(502)
            v.append(v1)
            return v

    def new(self, **kwargs):
        if self.__id__ == 37:
            v = _wmi_object(38)
            return v
        elif self.__id__ == 65:
            v = _wmi_object(66)
            return v
        elif self.__id__ == 159:
            v = _wmi_object(160)
            return v
        elif self.__id__ == 254:
            v = _wmi_object(255)
            return v
        elif self.__id__ == 394:
            v = _wmi_object(395)
            return v


class _wmi_object(object):

    def __init__(self, instance_id=1, *args, **kwargs):
        self.__instance_id__ = instance_id

    @property
    def __id__(self):
        return self.__instance_id__

    @property
    def Disconnect(self):
        if self.__id__ == 507:
            v = _wmi_method(511)
            return v

    @Disconnect.setter
    def Disconnect(self, value):
        pass

    @property
    def path_(self):
        if self.__id__ == 60:
            v = CDispatch(153)
            return v
        elif self.__id__ == 50:
            ret_value = None
            if not hasattr(self, '_path__count_1'):
                self._path__count_1 = 0
            if self._path__count_1 == 0:
                v = CDispatch(157)
            elif self._path__count_1 == 1:
                v = CDispatch(250)
            self._path__count_1 += 1
            return v
        elif self.__id__ == 252:
            v = CDispatch(345)
            return v
        elif self.__id__ == 41:
            ret_value = None
            if not hasattr(self, '_path__count_3'):
                self._path__count_3 = 0
            if self._path__count_3 == 0:
                v = CDispatch(45)
            elif self._path__count_3 == 1:
                v = CDispatch(48)
            self._path__count_3 += 1
            return v
        elif self.__id__ == 347:
            v = CDispatch(351)
            return v
        elif self.__id__ == 534:
            v = CDispatch(561)
            return v
        elif self.__id__ == 373:
            v = CDispatch(483)
            return v
        elif self.__id__ == 492:
            v = CDispatch(498)
            return v
        elif self.__id__ == 497:
            v = CDispatch(504)
            return v
        elif self.__id__ == 391:
            ret_value = None
            if not hasattr(self, '_path__count_9'):
                self._path__count_9 = 0
            if self._path__count_9 == 0:
                v = CDispatch(392)
            elif self._path__count_9 == 1:
                v = CDispatch(482)
            self._path__count_9 += 1
            return v
        elif self.__id__ == 375:
            v = CDispatch(487)
            return v
        elif self.__id__ == 500:
            v = CDispatch(505)
            return v

    @path_.setter
    def path_(self, value):
        pass

    @property
    def HostResource(self):
        if self.__id__ == 493:
            return None
        elif self.__id__ == 494:
            return None
        elif self.__id__ == 495:
            return None
        elif self.__id__ == 496:
            return None
        elif self.__id__ == 497:
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_DiskDrive.CreationClassName="Msv\
m_DiskDrive",DeviceID="Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\\\\1",Sy\
stemCreationClassName="Msvm_ComputerSystem",SystemName="HV12OSDEMO1"'
            v += (v1,)
            return v

    @HostResource.setter
    def HostResource(self, value):
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
            v = _wmi_method(13)
            return v

    @CreateDynamicVirtualHardDisk.setter
    def CreateDynamicVirtualHardDisk(self, value):
        pass

    @property
    def ModifyVirtualSystemResources(self):
        if self.__id__ == 36:
            ret_value = None
            if not hasattr(self, '_ModifyVirtualSystemResources_count_0'):
                self._ModifyVirtualSystemResources_count_0 = 0
            if self._ModifyVirtualSystemResources_count_0 == 0:
                v = _wmi_method(44)
            elif self._ModifyVirtualSystemResources_count_0 == 1:
                v = _wmi_method(47)
            self._ModifyVirtualSystemResources_count_0 += 1
            return v

    @ModifyVirtualSystemResources.setter
    def ModifyVirtualSystemResources(self, value):
        pass

    @property
    def RemoveVirtualSystemResources(self):
        if self.__id__ == 502:
            v = _wmi_method(503)
            return v

    @RemoveVirtualSystemResources.setter
    def RemoveVirtualSystemResources(self, value):
        pass

    @property
    def CreateDifferencingVirtualHardDisk(self):
        if self.__id__ == 23:
            v = _wmi_method(24)
            return v

    @CreateDifferencingVirtualHardDisk.setter
    def CreateDifferencingVirtualHardDisk(self, value):
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
            return 4
        elif self.__id__ == 361:
            ret_value = None
            if not hasattr(self, '_JobState_count_25'):
                self._JobState_count_25 = 0
            if self._JobState_count_25 == 0:
                v = 7
            elif self._JobState_count_25 == 1:
                v = 7
            self._JobState_count_25 += 1
            return v
        elif self.__id__ == 540:
            return 4
        elif self.__id__ == 541:
            ret_value = None
            if not hasattr(self, '_JobState_count_27'):
                self._JobState_count_27 = 0
            if self._JobState_count_27 == 0:
                v = 7
            elif self._JobState_count_27 == 1:
                v = 7
            self._JobState_count_27 += 1
            return v
        elif self.__id__ == 562:
            return 4
        elif self.__id__ == 563:
            ret_value = None
            if not hasattr(self, '_JobState_count_29'):
                self._JobState_count_29 = 0
            if self._JobState_count_29 == 0:
                v = 7
            elif self._JobState_count_29 == 1:
                v = 7
            self._JobState_count_29 += 1
            return v

    @JobState.setter
    def JobState(self, value):
        pass

    @property
    def Description(self):
        if self.__id__ == 34:
            return u'Creating Virtual Hard Disk'
        elif self.__id__ == 361:
            return u'Initializing and Starting Virtual Machine'

    @Description.setter
    def Description(self, value):
        pass

    @property
    def AddVirtualSystemResources(self):
        if self.__id__ == 155:
            v = _wmi_method(156)
            return v
        elif self.__id__ == 248:
            v = _wmi_method(249)
            return v
        elif self.__id__ == 343:
            v = _wmi_method(344)
            return v
        elif self.__id__ == 349:
            v = _wmi_method(350)
            return v
        elif self.__id__ == 485:
            v = _wmi_method(486)
            return v

    @AddVirtualSystemResources.setter
    def AddVirtualSystemResources(self, value):
        pass

    @property
    def IsConnected(self):
        if self.__id__ == 507:
            return True

    @IsConnected.setter
    def IsConnected(self, value):
        pass

    @property
    def Properties_(self):
        if self.__id__ == 64:
            ret_value = None
            if not hasattr(self, '_Properties__count_0'):
                self._Properties__count_0 = 0
            if self._Properties__count_0 == 0:
                v = CDispatch(67)
            elif self._Properties__count_0 == 1:
                v = CDispatch(71)
            elif self._Properties__count_0 == 2:
                v = CDispatch(75)
            elif self._Properties__count_0 == 3:
                v = CDispatch(79)
            elif self._Properties__count_0 == 4:
                v = CDispatch(83)
            elif self._Properties__count_0 == 5:
                v = CDispatch(87)
            elif self._Properties__count_0 == 6:
                v = CDispatch(91)
            elif self._Properties__count_0 == 7:
                v = CDispatch(95)
            elif self._Properties__count_0 == 8:
                v = CDispatch(99)
            elif self._Properties__count_0 == 9:
                v = CDispatch(103)
            elif self._Properties__count_0 == 10:
                v = CDispatch(107)
            elif self._Properties__count_0 == 11:
                v = CDispatch(111)
            elif self._Properties__count_0 == 12:
                v = CDispatch(115)
            elif self._Properties__count_0 == 13:
                v = CDispatch(119)
            elif self._Properties__count_0 == 14:
                v = CDispatch(123)
            elif self._Properties__count_0 == 15:
                v = CDispatch(127)
            elif self._Properties__count_0 == 16:
                v = CDispatch(131)
            elif self._Properties__count_0 == 17:
                v = CDispatch(135)
            elif self._Properties__count_0 == 18:
                v = CDispatch(139)
            elif self._Properties__count_0 == 19:
                v = CDispatch(143)
            elif self._Properties__count_0 == 20:
                v = CDispatch(149)
            self._Properties__count_0 += 1
            return v
        elif self.__id__ == 158:
            ret_value = None
            if not hasattr(self, '_Properties__count_1'):
                self._Properties__count_1 = 0
            if self._Properties__count_1 == 0:
                v = CDispatch(161)
            elif self._Properties__count_1 == 1:
                v = CDispatch(165)
            elif self._Properties__count_1 == 2:
                v = CDispatch(169)
            elif self._Properties__count_1 == 3:
                v = CDispatch(173)
            elif self._Properties__count_1 == 4:
                v = CDispatch(177)
            elif self._Properties__count_1 == 5:
                v = CDispatch(181)
            elif self._Properties__count_1 == 6:
                v = CDispatch(185)
            elif self._Properties__count_1 == 7:
                v = CDispatch(189)
            elif self._Properties__count_1 == 8:
                v = CDispatch(193)
            elif self._Properties__count_1 == 9:
                v = CDispatch(197)
            elif self._Properties__count_1 == 10:
                v = CDispatch(201)
            elif self._Properties__count_1 == 11:
                v = CDispatch(205)
            elif self._Properties__count_1 == 12:
                v = CDispatch(209)
            elif self._Properties__count_1 == 13:
                v = CDispatch(213)
            elif self._Properties__count_1 == 14:
                v = CDispatch(217)
            elif self._Properties__count_1 == 15:
                v = CDispatch(221)
            elif self._Properties__count_1 == 16:
                v = CDispatch(225)
            elif self._Properties__count_1 == 17:
                v = CDispatch(229)
            elif self._Properties__count_1 == 18:
                v = CDispatch(233)
            elif self._Properties__count_1 == 19:
                v = CDispatch(237)
            elif self._Properties__count_1 == 20:
                v = CDispatch(243)
            self._Properties__count_1 += 1
            return v
        elif self.__id__ == 253:
            ret_value = None
            if not hasattr(self, '_Properties__count_2'):
                self._Properties__count_2 = 0
            if self._Properties__count_2 == 0:
                v = CDispatch(256)
            elif self._Properties__count_2 == 1:
                v = CDispatch(260)
            elif self._Properties__count_2 == 2:
                v = CDispatch(264)
            elif self._Properties__count_2 == 3:
                v = CDispatch(268)
            elif self._Properties__count_2 == 4:
                v = CDispatch(272)
            elif self._Properties__count_2 == 5:
                v = CDispatch(276)
            elif self._Properties__count_2 == 6:
                v = CDispatch(280)
            elif self._Properties__count_2 == 7:
                v = CDispatch(284)
            elif self._Properties__count_2 == 8:
                v = CDispatch(288)
            elif self._Properties__count_2 == 9:
                v = CDispatch(292)
            elif self._Properties__count_2 == 10:
                v = CDispatch(296)
            elif self._Properties__count_2 == 11:
                v = CDispatch(300)
            elif self._Properties__count_2 == 12:
                v = CDispatch(304)
            elif self._Properties__count_2 == 13:
                v = CDispatch(308)
            elif self._Properties__count_2 == 14:
                v = CDispatch(312)
            elif self._Properties__count_2 == 15:
                v = CDispatch(316)
            elif self._Properties__count_2 == 16:
                v = CDispatch(320)
            elif self._Properties__count_2 == 17:
                v = CDispatch(324)
            elif self._Properties__count_2 == 18:
                v = CDispatch(328)
            elif self._Properties__count_2 == 19:
                v = CDispatch(332)
            elif self._Properties__count_2 == 20:
                v = CDispatch(338)
            self._Properties__count_2 += 1
            return v
        elif self.__id__ == 66:
            ret_value = None
            if not hasattr(self, '_Properties__count_3'):
                self._Properties__count_3 = 0
            if self._Properties__count_3 == 0:
                v = CDispatch(69)
            elif self._Properties__count_3 == 1:
                v = CDispatch(73)
            elif self._Properties__count_3 == 2:
                v = CDispatch(77)
            elif self._Properties__count_3 == 3:
                v = CDispatch(81)
            elif self._Properties__count_3 == 4:
                v = CDispatch(85)
            elif self._Properties__count_3 == 5:
                v = CDispatch(89)
            elif self._Properties__count_3 == 6:
                v = CDispatch(93)
            elif self._Properties__count_3 == 7:
                v = CDispatch(97)
            elif self._Properties__count_3 == 8:
                v = CDispatch(101)
            elif self._Properties__count_3 == 9:
                v = CDispatch(105)
            elif self._Properties__count_3 == 10:
                v = CDispatch(109)
            elif self._Properties__count_3 == 11:
                v = CDispatch(113)
            elif self._Properties__count_3 == 12:
                v = CDispatch(117)
            elif self._Properties__count_3 == 13:
                v = CDispatch(121)
            elif self._Properties__count_3 == 14:
                v = CDispatch(125)
            elif self._Properties__count_3 == 15:
                v = CDispatch(129)
            elif self._Properties__count_3 == 16:
                v = CDispatch(133)
            elif self._Properties__count_3 == 17:
                v = CDispatch(137)
            elif self._Properties__count_3 == 18:
                v = CDispatch(141)
            elif self._Properties__count_3 == 19:
                v = CDispatch(145)
            elif self._Properties__count_3 == 20:
                v = CDispatch(147)
            elif self._Properties__count_3 == 21:
                v = CDispatch(151)
            self._Properties__count_3 += 1
            return v
        elif self.__id__ == 160:
            ret_value = None
            if not hasattr(self, '_Properties__count_4'):
                self._Properties__count_4 = 0
            if self._Properties__count_4 == 0:
                v = CDispatch(163)
            elif self._Properties__count_4 == 1:
                v = CDispatch(167)
            elif self._Properties__count_4 == 2:
                v = CDispatch(171)
            elif self._Properties__count_4 == 3:
                v = CDispatch(175)
            elif self._Properties__count_4 == 4:
                v = CDispatch(179)
            elif self._Properties__count_4 == 5:
                v = CDispatch(183)
            elif self._Properties__count_4 == 6:
                v = CDispatch(187)
            elif self._Properties__count_4 == 7:
                v = CDispatch(191)
            elif self._Properties__count_4 == 8:
                v = CDispatch(195)
            elif self._Properties__count_4 == 9:
                v = CDispatch(199)
            elif self._Properties__count_4 == 10:
                v = CDispatch(203)
            elif self._Properties__count_4 == 11:
                v = CDispatch(207)
            elif self._Properties__count_4 == 12:
                v = CDispatch(211)
            elif self._Properties__count_4 == 13:
                v = CDispatch(215)
            elif self._Properties__count_4 == 14:
                v = CDispatch(219)
            elif self._Properties__count_4 == 15:
                v = CDispatch(223)
            elif self._Properties__count_4 == 16:
                v = CDispatch(227)
            elif self._Properties__count_4 == 17:
                v = CDispatch(231)
            elif self._Properties__count_4 == 18:
                v = CDispatch(235)
            elif self._Properties__count_4 == 19:
                v = CDispatch(239)
            elif self._Properties__count_4 == 20:
                v = CDispatch(241)
            elif self._Properties__count_4 == 21:
                v = CDispatch(245)
            self._Properties__count_4 += 1
            return v
        elif self.__id__ == 255:
            ret_value = None
            if not hasattr(self, '_Properties__count_5'):
                self._Properties__count_5 = 0
            if self._Properties__count_5 == 0:
                v = CDispatch(258)
            elif self._Properties__count_5 == 1:
                v = CDispatch(262)
            elif self._Properties__count_5 == 2:
                v = CDispatch(266)
            elif self._Properties__count_5 == 3:
                v = CDispatch(270)
            elif self._Properties__count_5 == 4:
                v = CDispatch(274)
            elif self._Properties__count_5 == 5:
                v = CDispatch(278)
            elif self._Properties__count_5 == 6:
                v = CDispatch(282)
            elif self._Properties__count_5 == 7:
                v = CDispatch(286)
            elif self._Properties__count_5 == 8:
                v = CDispatch(290)
            elif self._Properties__count_5 == 9:
                v = CDispatch(294)
            elif self._Properties__count_5 == 10:
                v = CDispatch(298)
            elif self._Properties__count_5 == 11:
                v = CDispatch(302)
            elif self._Properties__count_5 == 12:
                v = CDispatch(306)
            elif self._Properties__count_5 == 13:
                v = CDispatch(310)
            elif self._Properties__count_5 == 14:
                v = CDispatch(314)
            elif self._Properties__count_5 == 15:
                v = CDispatch(318)
            elif self._Properties__count_5 == 16:
                v = CDispatch(322)
            elif self._Properties__count_5 == 17:
                v = CDispatch(326)
            elif self._Properties__count_5 == 18:
                v = CDispatch(330)
            elif self._Properties__count_5 == 19:
                v = CDispatch(334)
            elif self._Properties__count_5 == 20:
                v = CDispatch(336)
            elif self._Properties__count_5 == 21:
                v = CDispatch(340)
            self._Properties__count_5 += 1
            return v
        elif self.__id__ == 393:
            ret_value = None
            if not hasattr(self, '_Properties__count_6'):
                self._Properties__count_6 = 0
            if self._Properties__count_6 == 0:
                v = CDispatch(396)
            elif self._Properties__count_6 == 1:
                v = CDispatch(400)
            elif self._Properties__count_6 == 2:
                v = CDispatch(404)
            elif self._Properties__count_6 == 3:
                v = CDispatch(408)
            elif self._Properties__count_6 == 4:
                v = CDispatch(412)
            elif self._Properties__count_6 == 5:
                v = CDispatch(416)
            elif self._Properties__count_6 == 6:
                v = CDispatch(420)
            elif self._Properties__count_6 == 7:
                v = CDispatch(424)
            elif self._Properties__count_6 == 8:
                v = CDispatch(428)
            elif self._Properties__count_6 == 9:
                v = CDispatch(432)
            elif self._Properties__count_6 == 10:
                v = CDispatch(436)
            elif self._Properties__count_6 == 11:
                v = CDispatch(440)
            elif self._Properties__count_6 == 12:
                v = CDispatch(444)
            elif self._Properties__count_6 == 13:
                v = CDispatch(448)
            elif self._Properties__count_6 == 14:
                v = CDispatch(452)
            elif self._Properties__count_6 == 15:
                v = CDispatch(456)
            elif self._Properties__count_6 == 16:
                v = CDispatch(460)
            elif self._Properties__count_6 == 17:
                v = CDispatch(464)
            elif self._Properties__count_6 == 18:
                v = CDispatch(468)
            elif self._Properties__count_6 == 19:
                v = CDispatch(472)
            elif self._Properties__count_6 == 20:
                v = CDispatch(478)
            self._Properties__count_6 += 1
            return v
        elif self.__id__ == 395:
            ret_value = None
            if not hasattr(self, '_Properties__count_7'):
                self._Properties__count_7 = 0
            if self._Properties__count_7 == 0:
                v = CDispatch(398)
            elif self._Properties__count_7 == 1:
                v = CDispatch(402)
            elif self._Properties__count_7 == 2:
                v = CDispatch(406)
            elif self._Properties__count_7 == 3:
                v = CDispatch(410)
            elif self._Properties__count_7 == 4:
                v = CDispatch(414)
            elif self._Properties__count_7 == 5:
                v = CDispatch(418)
            elif self._Properties__count_7 == 6:
                v = CDispatch(422)
            elif self._Properties__count_7 == 7:
                v = CDispatch(426)
            elif self._Properties__count_7 == 8:
                v = CDispatch(430)
            elif self._Properties__count_7 == 9:
                v = CDispatch(434)
            elif self._Properties__count_7 == 10:
                v = CDispatch(438)
            elif self._Properties__count_7 == 11:
                v = CDispatch(442)
            elif self._Properties__count_7 == 12:
                v = CDispatch(446)
            elif self._Properties__count_7 == 13:
                v = CDispatch(450)
            elif self._Properties__count_7 == 14:
                v = CDispatch(454)
            elif self._Properties__count_7 == 15:
                v = CDispatch(458)
            elif self._Properties__count_7 == 16:
                v = CDispatch(462)
            elif self._Properties__count_7 == 17:
                v = CDispatch(466)
            elif self._Properties__count_7 == 18:
                v = CDispatch(470)
            elif self._Properties__count_7 == 19:
                v = CDispatch(474)
            elif self._Properties__count_7 == 20:
                v = CDispatch(476)
            elif self._Properties__count_7 == 21:
                v = CDispatch(480)
            self._Properties__count_7 += 1
            return v

    @Properties_.setter
    def Properties_(self, value):
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
    def RequestStateChange(self):
        if self.__id__ == 353:
            v = _wmi_method(354)
            return v
        elif self.__id__ == 538:
            v = _wmi_method(539)
            return v

    @RequestStateChange.setter
    def RequestStateChange(self, value):
        pass

    @property
    def Unregister(self):
        if self.__id__ == 509:
            v = _wmi_method(510)
            return v

    @Unregister.setter
    def Unregister(self, value):
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
        elif self.__id__ == 393:
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
    def Devices(self):
        if self.__id__ == 368:
            v = ()
            v1 = CDispatch(369)
            v += (v1,)
            v1 = CDispatch(370)
            v += (v1,)
            return v
        elif self.__id__ == 488:
            v = ()
            v1 = CDispatch(489)
            v += (v1,)
            v1 = CDispatch(490)
            v += (v1,)
            return v

    @Devices.setter
    def Devices(self, value):
        pass

    @property
    def ElapsedTime(self):
        if self.__id__ == 34:
            return u'00000000000001.008797:000'
        elif self.__id__ == 361:
            return u'00000000000000.803464:000'

    @ElapsedTime.setter
    def ElapsedTime(self, value):
        pass

    @property
    def Connection(self):
        if self.__id__ == 524:
            v = ()
            v1 =\
 u'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_82c326ef-3696-41c4-ad5\
1-9fd855bd8fa7\\openstack_unit_test_vm_82c326ef-3696-41c4-ad51-9fd855bd8fa7.vh\
d'
            v += (v1,)
            return v
        elif self.__id__ == 554:
            v = ()
            v1 =\
 u'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_82c326ef-3696-41c4-ad5\
1-9fd855bd8fa7\\openstack_unit_test_vm_82c326ef-3696-41c4-ad51-9fd855bd8fa7.vh\
d'
            v += (v1,)
            return v

    @Connection.setter
    def Connection(self, value):
        pass

    @property
    def Delete(self):
        if self.__id__ == 564:
            v = _wmi_method(565)
            return v

    @Delete.setter
    def Delete(self, value):
        pass

    @property
    def IsPersistent(self):
        if self.__id__ == 509:
            return True

    @IsPersistent.setter
    def IsPersistent(self, value):
        pass

    @property
    def DestroyVirtualSystem(self):
        if self.__id__ == 536:
            v = _wmi_method(560)
            return v

    @DestroyVirtualSystem.setter
    def DestroyVirtualSystem(self, value):
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
        elif self.__id__ == 515:
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
        elif self.__id__ == 516:
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
        elif self.__id__ == 517:
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
        elif self.__id__ == 518:
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
        elif self.__id__ == 519:
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
        elif self.__id__ == 520:
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
        elif self.__id__ == 521:
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
        elif self.__id__ == 522:
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
        elif self.__id__ == 523:
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
        elif self.__id__ == 524:
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
        elif self.__id__ == 525:
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
        elif self.__id__ == 526:
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
        elif self.__id__ == 527:
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
        elif self.__id__ == 528:
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
        elif self.__id__ == 529:
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
        elif self.__id__ == 545:
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
        elif self.__id__ == 546:
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
        elif self.__id__ == 547:
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
        elif self.__id__ == 548:
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
        elif self.__id__ == 549:
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
        elif self.__id__ == 550:
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
        elif self.__id__ == 551:
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
        elif self.__id__ == 552:
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
        elif self.__id__ == 553:
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
        elif self.__id__ == 554:
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
        elif self.__id__ == 555:
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
        elif self.__id__ == 556:
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
        elif self.__id__ == 557:
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
        elif self.__id__ == 558:
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
        elif self.__id__ == 559:
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
        elif self.__id__ == 377:
            return u'Microsoft Virtual Keyboard'
        elif self.__id__ == 378:
            return u'Microsoft Virtual PS2 Mouse'
        elif self.__id__ == 379:
            return u'Microsoft S3 Display Controller'
        elif self.__id__ == 380:
            return u'Microsoft Synthetic Diskette Drive'
        elif self.__id__ == 381:
            return None
        elif self.__id__ == 382:
            return u'Microsoft Serial Controller'
        elif self.__id__ == 383:
            return u'Microsoft Serial Port'
        elif self.__id__ == 384:
            return u'Microsoft Serial Port'
        elif self.__id__ == 385:
            return u'Microsoft Synthetic Disk Drive'
        elif self.__id__ == 386:
            return u'Microsoft Virtual Hard Disk'
        elif self.__id__ == 387:
            return u'Microsoft Emulated IDE Controller'
        elif self.__id__ == 388:
            return u'Microsoft Emulated IDE Controller'
        elif self.__id__ == 389:
            return u'Microsoft Synthetic Mouse'
        elif self.__id__ == 390:
            return u'Microsoft Synthetic Display Controller'
        elif self.__id__ == 391:
            return u'Microsoft Synthetic SCSI Controller'

    @ResourceSubType.setter
    def ResourceSubType(self, value):
        pass

    @property
    def DefineVirtualSystem(self):
        if self.__id__ == 36:
            v = _wmi_method(39)
            return v

    @DefineVirtualSystem.setter
    def DefineVirtualSystem(self, value):
        pass

    @property
    def SettingType(self):
        if self.__id__ == 42:
            return 3

    @SettingType.setter
    def SettingType(self, value):
        pass

    def associators(self, wmi_association_class='', wmi_result_class=''):
        if self.__id__ == 51 and wmi_result_class ==\
 'MSVM_ResourceAllocationSettingData':
            v = []
            v1 = _wmi_object(52)
            v.append(v1)
            v1 = _wmi_object(53)
            v.append(v1)
            v1 = _wmi_object(54)
            v.append(v1)
            v1 = _wmi_object(55)
            v.append(v1)
            v1 = _wmi_object(56)
            v.append(v1)
            v1 = _wmi_object(57)
            v.append(v1)
            v1 = _wmi_object(58)
            v.append(v1)
            v1 = _wmi_object(59)
            v.append(v1)
            v1 = _wmi_object(60)
            v.append(v1)
            v1 = _wmi_object(61)
            v.append(v1)
            v1 = _wmi_object(62)
            v.append(v1)
            v1 = _wmi_object(63)
            v.append(v1)
            return v
        elif self.__id__ == 50 and wmi_result_class ==\
 'Msvm_VirtualSystemSettingData':
            v = []
            v1 = _wmi_object(51)
            v.append(v1)
            return v
        elif self.__id__ == 42 and wmi_result_class ==\
 'Msvm_MemorySettingData':
            v = []
            v1 = _wmi_object(43)
            v.append(v1)
            return v
        elif self.__id__ == 42 and wmi_result_class ==\
 'Msvm_ProcessorSettingData':
            v = []
            v1 = _wmi_object(46)
            v.append(v1)
            return v
        elif self.__id__ == 41 and wmi_result_class ==\
 'Msvm_VirtualSystemSettingData':
            v = []
            v1 = _wmi_object(42)
            v.append(v1)
            return v
        elif self.__id__ == 514 and wmi_result_class ==\
 'MSVM_ResourceAllocationSettingData':
            v = []
            v1 = _wmi_object(515)
            v.append(v1)
            v1 = _wmi_object(516)
            v.append(v1)
            v1 = _wmi_object(517)
            v.append(v1)
            v1 = _wmi_object(518)
            v.append(v1)
            v1 = _wmi_object(519)
            v.append(v1)
            v1 = _wmi_object(520)
            v.append(v1)
            v1 = _wmi_object(521)
            v.append(v1)
            v1 = _wmi_object(522)
            v.append(v1)
            v1 = _wmi_object(523)
            v.append(v1)
            v1 = _wmi_object(524)
            v.append(v1)
            v1 = _wmi_object(525)
            v.append(v1)
            v1 = _wmi_object(526)
            v.append(v1)
            v1 = _wmi_object(527)
            v.append(v1)
            v1 = _wmi_object(528)
            v.append(v1)
            v1 = _wmi_object(529)
            v.append(v1)
            return v
        elif self.__id__ == 513 and wmi_result_class ==\
 'Msvm_VirtualSystemSettingData':
            v = []
            v1 = _wmi_object(514)
            v.append(v1)
            return v
        elif self.__id__ == 544 and wmi_result_class ==\
 'MSVM_ResourceAllocationSettingData':
            v = []
            v1 = _wmi_object(545)
            v.append(v1)
            v1 = _wmi_object(546)
            v.append(v1)
            v1 = _wmi_object(547)
            v.append(v1)
            v1 = _wmi_object(548)
            v.append(v1)
            v1 = _wmi_object(549)
            v.append(v1)
            v1 = _wmi_object(550)
            v.append(v1)
            v1 = _wmi_object(551)
            v.append(v1)
            v1 = _wmi_object(552)
            v.append(v1)
            v1 = _wmi_object(553)
            v.append(v1)
            v1 = _wmi_object(554)
            v.append(v1)
            v1 = _wmi_object(555)
            v.append(v1)
            v1 = _wmi_object(556)
            v.append(v1)
            v1 = _wmi_object(557)
            v.append(v1)
            v1 = _wmi_object(558)
            v.append(v1)
            v1 = _wmi_object(559)
            v.append(v1)
            return v
        elif self.__id__ == 543 and wmi_result_class ==\
 'Msvm_VirtualSystemSettingData':
            v = []
            v1 = _wmi_object(544)
            v.append(v1)
            return v
        elif self.__id__ == 376 and wmi_result_class ==\
 'MSVM_ResourceAllocationSettingData':
            v = []
            v1 = _wmi_object(377)
            v.append(v1)
            v1 = _wmi_object(378)
            v.append(v1)
            v1 = _wmi_object(379)
            v.append(v1)
            v1 = _wmi_object(380)
            v.append(v1)
            v1 = _wmi_object(381)
            v.append(v1)
            v1 = _wmi_object(382)
            v.append(v1)
            v1 = _wmi_object(383)
            v.append(v1)
            v1 = _wmi_object(384)
            v.append(v1)
            v1 = _wmi_object(385)
            v.append(v1)
            v1 = _wmi_object(386)
            v.append(v1)
            v1 = _wmi_object(387)
            v.append(v1)
            v1 = _wmi_object(388)
            v.append(v1)
            v1 = _wmi_object(389)
            v.append(v1)
            v1 = _wmi_object(390)
            v.append(v1)
            v1 = _wmi_object(391)
            v.append(v1)
            return v
        elif self.__id__ == 375 and wmi_result_class ==\
 'Msvm_VirtualSystemSettingData':
            v = []
            v1 = _wmi_object(376)
            v.append(v1)
            return v

    def GetText_(self, iObjectTextFormat='<PyOleMissing object at\
 0x03237588>', iFlags=0, objWbemNamedValueSet=None):
        if self.__id__ == 43 and iObjectTextFormat == 1:
            return u'<INSTANCE CLASSNAME="Msvm_MemorySettingData"><PROPERTY\
 NAME="__PATH" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>\\\\HV12OSDEMO1\\root\\virtualization:Msvm_MemorySetting\
Data.InstanceID="Microsoft:04FB9E92-46A2-4F69-9555-6E4323312DA2\\\\4764334d-e0\
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
 TYPE="string"><VALUE>Msvm_MemorySettingData.InstanceID="Microsoft:04FB9E92-46\
A2-4F69-9555-6E4323312DA2\\\\4764334d-e001-4176-82ee-5594ec9b530e"</VALUE></PR\
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
 TYPE="string"><VALUE>Microsoft:04FB9E92-46A2-4F69-9555-6E4323312DA2\\4764334d\
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
ingData.InstanceID="Microsoft:04FB9E92-46A2-4F69-9555-6E4323312DA2\\\\b637f346\
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
 TYPE="string"><VALUE>Msvm_ProcessorSettingData.InstanceID="Microsoft:04FB9E92\
-46A2-4F69-9555-6E4323312DA2\\\\b637f346-6a0e-4dec-af52-bd70cb80a21d\\\\0"</VA\
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
 TYPE="string"><VALUE>Microsoft:04FB9E92-46A2-4F69-9555-6E4323312DA2\\b637f346\
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
 TYPE="string"><VALUE>openstack_unit_test_vm_82c326ef-3696-41c4-ad51-9fd855bd8\
fa7</VALUE></PROPERTY><PROPERTY NAME="ExternalDataRoot"\
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
ationSettingData.InstanceID="Microsoft:04FB9E92-46A2-4F69-9555-6E4323312DA2\
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
 TYPE="string"><VALUE.ARRAY><VALUE>d30e8e8f-803a-48b5-9f80-b8316434233b</VALUE\
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
t_test_vm_82c326ef-3696-41c4-ad51-9fd855bd8fa7\\openstack_unit_test_vm_82c326e\
f-3696-41c4-ad51-9fd855bd8fa7.vhd</VALUE></VALUE.ARRAY></PROPERTY.ARRAY><PROPE\
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
ationSettingData.InstanceID="Microsoft:04FB9E92-46A2-4F69-9555-6E4323312DA2\
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
 TYPE="string"><VALUE.ARRAY><VALUE>205ef3f7-5b1e-4bd0-837a-4bafca28dc24</VALUE\
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
 TYPE="string"><VALUE.ARRAY><VALUE>{156a72fd-5398-4979-8828-a227dabe7e09}</VAL\
UE></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>'
        elif self.__id__ == 395 and iObjectTextFormat == 1:
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
:Definition\\\\353B3BE8-310C-4CF4-839E-4E1B14616136\\\\Default"</VALUE></PROPE\
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
 Microsoft Physical Hard Drive.</VALUE></PROPERTY><PROPERTY NAME="ElementName"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>Hard\
 Drive</VALUE></PROPERTY><PROPERTY.ARRAY NAME="HostResource"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE.ARRAY><VALUE>\\\\HV12OSDEMO1\\root\\virtualization:Msvm_\
DiskDrive.CreationClassName="Msvm_DiskDrive",DeviceID="Microsoft:353B3BE8-310C\
-4cf4-839E-4E1B14616136\\\\1",SystemCreationClassName="Msvm_ComputerSystem",Sy\
stemName="HV12OSDEMO1"</VALUE></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY\
 NAME="InstanceID" CLASSORIGIN="CIM_SettingData"\
 TYPE="string"><VALUE>Microsoft:Definition\\353B3BE8-310C-4CF4-839E-4E1B146161\
36\\Default</VALUE></PROPERTY><PROPERTY NAME="Limit"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="MappingBehavior"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="OtherResourceType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="Parent"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAlloc\
ationSettingData.InstanceID="Microsoft:04FB9E92-46A2-4F69-9555-6E4323312DA2\
\\\\5F053DDB-3C35-4A44-8E4E-2056CC3A440A\\\\0"</VALUE></PROPERTY><PROPERTY\
 NAME="PoolID" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\\Root</VA\
LUE></PROPERTY><PROPERTY NAME="Reservation"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="ResourceSubType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Microsoft Physical Disk\
 Drive</VALUE></PROPERTY><PROPERTY NAME="ResourceType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"><VALUE>22</VALUE></PROPERTY><PROPERTY NAME="VirtualQuantity"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY.ARRAY\
 NAME="VirtualSystemIdentifiers"\
 CLASSORIGIN="Msvm_ResourceAllocationSettingData"\
 TYPE="string"><VALUE.ARRAY><VALUE>88188539-287b-4e7d-8eba-1255aefafb8b</VALUE\
></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>'


class _wmi_method(object):

    def __init__(self, instance_id=1, *args, **kwargs):
        self.__instance_id__ = instance_id

    @property
    def __id__(self):
        return self.__instance_id__

    def __call__(self, *args, **kwargs):
        if len(args) == 0 and self.__id__ == 510:
            v = ()
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 0 and self.__id__ == 366 and\
 kwargs.get('IsPersistent') is True and kwargs.get('NodeAddress') ==\
 'iqn.2010-10.org.openstack:volume-ccb39627-34fa-4f47-968b-6580d9d7ee2b':
            v = ()
            v1 = CDispatch(367)
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 0 and self.__id__ == 511:
            v = ()
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 0 and self.__id__ == 363 and\
 kwargs.get('TargetPortalAddress') == 'testtargetportal' and\
 kwargs.get('TargetPortalPortNumber') == '3260':
            v = ()
            v1 = CDispatch(364)
            v += (v1,)
            v1 = None
            v += (v1,)
            return v
        elif len(args) == 0 and self.__id__ == 565:
            v = ()
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 0 and self.__id__ == 24 and kwargs.get('Path') ==\
 'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_82c326ef-3696-41c4-ad51\
-9fd855bd8fa7\\openstack_unit_test_vm_82c326ef-3696-41c4-ad51-9fd855bd8fa7.vhd\
' and kwargs.get('ParentPath') == 'C:\\Hyper-V\\test\\instances\\_base\\1.vhd':
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_StorageJob.InstanceID="86DCA9CA-\
88CB-4D38-8A87-4F1657077E40"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v
        elif len(args) == 1 and self.__id__ == 354 and args[0] == 2:
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ConcreteJob.InstanceID="B799C1C0\
-6268-40AD-8499-21064DDA27D1"'
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
 TYPE="string"><VALUE>openstack_unit_test_vm_82c326ef-3696-41c4-ad51-9fd855bd8\
fa7</VALUE></PROPERTY><PROPERTY NAME="ExternalDataRoot"\
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
="Msvm_ComputerSystem",Name="04FB9E92-46A2-4F69-9555-6E4323312DA2"'
            v += (v1,)
            v1 = None
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 2 and self.__id__ == 44 and args[0] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="04FB9E92-46A2-4F69-9555-6E4323312DA2"' and\
 str(args[1]) == '[u\'<INSTANCE CLASSNAME="Msvm_MemorySettingData"><PROPERTY\
 NAME="__PATH" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>\\\\\\\\HV12OSDEMO1\\\\root\\\\virtualization:Msvm_Memor\
ySettingData.InstanceID="Microsoft:04FB9E92-46A2-4F69-9555-6E4323312DA2\
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
 TYPE="string"><VALUE>Msvm_MemorySettingData.InstanceID="Microsoft:04FB9E92-46\
A2-4F69-9555-6E4323312DA2\\\\\\\\4764334d-e001-4176-82ee-5594ec9b530e"</VALUE>\
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
 TYPE="string"><VALUE>Microsoft:04FB9E92-46A2-4F69-9555-6E4323312DA2\\\\476433\
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
="Msvm_ComputerSystem",Name="04FB9E92-46A2-4F69-9555-6E4323312DA2"' and\
 str(args[1]) == '[u\'<INSTANCE\
 CLASSNAME="Msvm_ProcessorSettingData"><PROPERTY NAME="__PATH"\
 CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>\\\\\\\\HV12OSDEMO1\\\\root\\\\virtualization:Msvm_Proce\
ssorSettingData.InstanceID="Microsoft:04FB9E92-46A2-4F69-9555-6E4323312DA2\
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
 TYPE="string"><VALUE>Msvm_ProcessorSettingData.InstanceID="Microsoft:04FB9E92\
-46A2-4F69-9555-6E4323312DA2\\\\\\\\b637f346-6a0e-4dec-af52-bd70cb80a21d\
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
 TYPE="string"><VALUE>Microsoft:04FB9E92-46A2-4F69-9555-6E4323312DA2\\\\b637f3\
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
rceAllocationSettingData.InstanceID="Microsoft:04FB9E92-46A2-4F69-9555-6E43233\
12DA2\\\\\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\\\\\0"</VALUE></PROPERTY>\
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
 TYPE="string"><VALUE.ARRAY><VALUE>d30e8e8f-803a-48b5-9f80-b8316434233b</VALUE\
></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="04FB9E92-46A2-4F69-9555-6E4323312DA2"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:04FB9E92-46A2-4F69-9555-6E4323312DA2\\\\83F8638B-8DCA-4152\
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
tack_unit_test_vm_82c326ef-3696-41c4-ad51-9fd855bd8fa7\\\\openstack_unit_test_\
vm_82c326ef-3696-41c4-ad51-9fd855bd8fa7.vhd</VALUE></VALUE.ARRAY></PROPERTY.AR\
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
rceAllocationSettingData.InstanceID="Microsoft:04FB9E92-46A2-4F69-9555-6E43233\
12DA2\\\\\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\\\\\0\\\\\\\\0\\\\\\\\D"<\
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
 TYPE="string"><VALUE.ARRAY><VALUE>205ef3f7-5b1e-4bd0-837a-4bafca28dc24</VALUE\
></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="04FB9E92-46A2-4F69-9555-6E4323312DA2"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:04FB9E92-46A2-4F69-9555-6E4323312DA2\\\\83F8638B-8DCA-4152\
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
 TYPE="string"><VALUE.ARRAY><VALUE>{156a72fd-5398-4979-8828-a227dabe7e09}</VAL\
UE></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="04FB9E92-46A2-4F69-9555-6E4323312DA2"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:04FB9E92-46A2-4F69-9555-6E4323312DA2\\\\5F053DDB-3C35-4A44\
-8E4E-2056CC3A440A\\\\0"'
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
 TYPE="string"><VALUE.ARRAY><VALUE>{0750ac55-6d63-4d63-b214-03866d8be3f2}</VAL\
UE></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="04FB9E92-46A2-4F69-9555-6E4323312DA2"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_SyntheticEthernetPortSettingData\
.InstanceID="Microsoft:04FB9E92-46A2-4F69-9555-6E4323312DA2\\\\EBB5DA1E-34EC-4\
E32-AADB-DFE338FAA5EB"'
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
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_StorageJob.InstanceID="D2D9F35C-\
C5DF-4289-B392-DD62EB58B98B"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v
        elif len(args) == 1 and self.__id__ == 539 and args[0] == 3:
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ConcreteJob.InstanceID="947AAABB\
-C582-4C88-8869-6B5B48E9FF86"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v
        elif len(args) == 1 and self.__id__ == 560 and args[0] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="04FB9E92-46A2-4F69-9555-6E4323312DA2"':
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ConcreteJob.InstanceID="28789C5D\
-CD33-4A2C-BE31-85CF6328CA5E"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v
        elif len(args) == 2 and self.__id__ == 486 and str(args[0]) ==\
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
:Definition\\\\\\\\353B3BE8-310C-4CF4-839E-4E1B14616136\\\\\\\\Default"</VALUE\
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
 Microsoft Physical Hard Drive.</VALUE></PROPERTY><PROPERTY NAME="ElementName"\
 CLASSORIGIN="CIM_ManagedElement" TYPE="string"><VALUE>Hard\
 Drive</VALUE></PROPERTY><PROPERTY.ARRAY NAME="HostResource"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE.ARRAY><VALUE>\\\\\\\\HV12OSDEMO1\\\\root\\\\virtualizati\
on:Msvm_DiskDrive.CreationClassName="Msvm_DiskDrive",DeviceID="Microsoft:353B3\
BE8-310C-4cf4-839E-4E1B14616136\\\\\\\\1",SystemCreationClassName="Msvm_Comput\
erSystem",SystemName="HV12OSDEMO1"</VALUE></VALUE.ARRAY></PROPERTY.ARRAY><PROP\
ERTY NAME="InstanceID" CLASSORIGIN="CIM_SettingData"\
 TYPE="string"><VALUE>Microsoft:Definition\\\\353B3BE8-310C-4CF4-839E-4E1B1461\
6136\\\\Default</VALUE></PROPERTY><PROPERTY NAME="Limit"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="MappingBehavior"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"></PROPERTY><PROPERTY NAME="OtherResourceType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"></PROPERTY><PROPERTY NAME="Parent"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>\\\\\\\\HV12OSDEMO1\\\\root\\\\virtualization:Msvm_Resou\
rceAllocationSettingData.InstanceID="Microsoft:04FB9E92-46A2-4F69-9555-6E43233\
12DA2\\\\\\\\5F053DDB-3C35-4A44-8E4E-2056CC3A440A\\\\\\\\0"</VALUE></PROPERTY>\
<PROPERTY NAME="PoolID" CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\\\\Root</\
VALUE></PROPERTY><PROPERTY NAME="Reservation"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY NAME="ResourceSubType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="string"><VALUE>Microsoft Physical Disk\
 Drive</VALUE></PROPERTY><PROPERTY NAME="ResourceType"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint16"><VALUE>22</VALUE></PROPERTY><PROPERTY NAME="VirtualQuantity"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint64"><VALUE>1</VALUE></PROPERTY><PROPERTY.ARRAY\
 NAME="VirtualSystemIdentifiers"\
 CLASSORIGIN="Msvm_ResourceAllocationSettingData"\
 TYPE="string"><VALUE.ARRAY><VALUE>88188539-287b-4e7d-8eba-1255aefafb8b</VALUE\
></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="04FB9E92-46A2-4F69-9555-6E4323312DA2"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:04FB9E92-46A2-4F69-9555-6E4323312DA2\\\\5F053DDB-3C35-4A44\
-8E4E-2056CC3A440A\\\\0\\\\0\\\\D"'
            v1.append(v2)
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 2 and self.__id__ == 503 and str(args[0]) ==\
 '[u\'\\\\\\\\HV12OSDEMO1\\\\root\\\\virtualization:Msvm_ResourceAllocationSet\
tingData.InstanceID="Microsoft:04FB9E92-46A2-4F69-9555-6E4323312DA2\\\\\\\\5F0\
53DDB-3C35-4A44-8E4E-2056CC3A440A\\\\\\\\0\\\\\\\\0\\\\\\\\D"\']' and args[1]\
 ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="04FB9E92-46A2-4F69-9555-6E4323312DA2"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v


class CDispatch(object):

    def __init__(self, instance_id=1, *args, **kwargs):
        self.__instance_id__ = instance_id

    @property
    def __id__(self):
        return self.__instance_id__

    @property
    def InitiatorName(self):
        if self.__id__ == 369:
            return u'ROOT\\ISCSIPRT\\0000_0'
        elif self.__id__ == 370:
            return u'ROOT\\ISCSIPRT\\0000_0'
        elif self.__id__ == 489:
            return u'ROOT\\ISCSIPRT\\0000_0'
        elif self.__id__ == 490:
            return u'ROOT\\ISCSIPRT\\0000_0'

    @InitiatorName.setter
    def InitiatorName(self, value):
        pass

    @property
    def ScsiLun(self):
        if self.__id__ == 369:
            ret_value = None
            if not hasattr(self, '_ScsiLun_count_0'):
                self._ScsiLun_count_0 = 0
            if self._ScsiLun_count_0 == 0:
                v = 0
            elif self._ScsiLun_count_0 == 1:
                v = 0
            self._ScsiLun_count_0 += 1
            return v
        elif self.__id__ == 370:
            ret_value = None
            if not hasattr(self, '_ScsiLun_count_1'):
                self._ScsiLun_count_1 = 0
            if self._ScsiLun_count_1 == 0:
                v = 1
            elif self._ScsiLun_count_1 == 1:
                v = 1
            self._ScsiLun_count_1 += 1
            return v
        elif self.__id__ == 489:
            ret_value = None
            if not hasattr(self, '_ScsiLun_count_2'):
                self._ScsiLun_count_2 = 0
            if self._ScsiLun_count_2 == 0:
                v = 0
            elif self._ScsiLun_count_2 == 1:
                v = 0
            self._ScsiLun_count_2 += 1
            return v
        elif self.__id__ == 490:
            ret_value = None
            if not hasattr(self, '_ScsiLun_count_3'):
                self._ScsiLun_count_3 = 0
            if self._ScsiLun_count_3 == 0:
                v = 1
            elif self._ScsiLun_count_3 == 1:
                v = 1
            self._ScsiLun_count_3 += 1
            return v

    @ScsiLun.setter
    def ScsiLun(self, value):
        pass

    @property
    def PartitionNumber(self):
        if self.__id__ == 369:
            return -1
        elif self.__id__ == 370:
            return 0
        elif self.__id__ == 489:
            return -1
        elif self.__id__ == 490:
            return 0

    @PartitionNumber.setter
    def PartitionNumber(self, value):
        pass

    @property
    def ScsiTargetId(self):
        if self.__id__ == 369:
            return 0
        elif self.__id__ == 370:
            return 0
        elif self.__id__ == 489:
            return 0
        elif self.__id__ == 490:
            return 0

    @ScsiTargetId.setter
    def ScsiTargetId(self, value):
        pass

    @property
    def DeviceNumber(self):
        if self.__id__ == 369:
            return -1
        elif self.__id__ == 370:
            ret_value = None
            if not hasattr(self, '_DeviceNumber_count_1'):
                self._DeviceNumber_count_1 = 0
            if self._DeviceNumber_count_1 == 0:
                v = 1
            elif self._DeviceNumber_count_1 == 1:
                v = 1
            self._DeviceNumber_count_1 += 1
            return v
        elif self.__id__ == 489:
            return -1
        elif self.__id__ == 490:
            ret_value = None
            if not hasattr(self, '_DeviceNumber_count_3'):
                self._DeviceNumber_count_3 = 0
            if self._DeviceNumber_count_3 == 0:
                v = 1
            elif self._DeviceNumber_count_3 == 1:
                v = 1
            self._DeviceNumber_count_3 += 1
            return v

    @DeviceNumber.setter
    def DeviceNumber(self, value):
        pass

    @property
    def DeviceInterfaceGuid(self):
        if self.__id__ == 369:
            return u'0-0-0-00000000'
        elif self.__id__ == 370:
            return u'53f56307-b6bf-11d0-94f20a0c91efb8b'
        elif self.__id__ == 489:
            return u'0-0-0-00000000'
        elif self.__id__ == 490:
            return u'53f56307-b6bf-11d0-94f20a0c91efb8b'

    @DeviceInterfaceGuid.setter
    def DeviceInterfaceGuid(self, value):
        pass

    @property
    def DeviceType(self):
        if self.__id__ == 369:
            return 34
        elif self.__id__ == 370:
            return 7
        elif self.__id__ == 489:
            return 34
        elif self.__id__ == 490:
            return 7

    @DeviceType.setter
    def DeviceType(self, value):
        pass

    @property
    def LegacyName(self):
        if self.__id__ == 369:
            return u''
        elif self.__id__ == 370:
            return u'\\\\.\\PhysicalDrive1'
        elif self.__id__ == 489:
            return u''
        elif self.__id__ == 490:
            return u'\\\\.\\PhysicalDrive1'

    @LegacyName.setter
    def LegacyName(self, value):
        pass

    @property
    def ScsiPathId(self):
        if self.__id__ == 369:
            return 0
        elif self.__id__ == 370:
            return 0
        elif self.__id__ == 489:
            return 0
        elif self.__id__ == 490:
            return 0

    @ScsiPathId.setter
    def ScsiPathId(self, value):
        pass

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
        elif self.__id__ == 397:
            return\
 u'Microsoft:Definition\\353B3BE8-310C-4CF4-839E-4E1B14616136\\Default'
        elif self.__id__ == 401:
            return u'Microsoft Physical Disk Drive'
        elif self.__id__ == 405:
            return None
        elif self.__id__ == 409:
            return u'Hard Drive'
        elif self.__id__ == 413:
            return u'Settings for the Microsoft Physical Hard Drive.'
        elif self.__id__ == 417:
            return None
        elif self.__id__ == 421:
            return u'1'
        elif self.__id__ == 425:
            return True
        elif self.__id__ == 429:
            return True
        elif self.__id__ == 433:
            return u'Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\\Root'
        elif self.__id__ == 437:
            return u'1'
        elif self.__id__ == 441:
            return u'Hard Drives'
        elif self.__id__ == 445:
            return None
        elif self.__id__ == 449:
            return None
        elif self.__id__ == 453:
            return None
        elif self.__id__ == 457:
            return u'Hard Drive'
        elif self.__id__ == 461:
            return None
        elif self.__id__ == 465:
            return u'1'
        elif self.__id__ == 469:
            return 22
        elif self.__id__ == 473:
            return 0
        elif self.__id__ == 479:
            return None

    @Value.setter
    def Value(self, value):
        pass

    @property
    def TargetName(self):
        if self.__id__ == 369:
            return\
 u'iqn.2010-10.org.openstack:volume-ccb39627-34fa-4f47-968b-6580d9d7ee2b'
        elif self.__id__ == 370:
            return\
 u'iqn.2010-10.org.openstack:volume-ccb39627-34fa-4f47-968b-6580d9d7ee2b'
        elif self.__id__ == 489:
            return\
 u'iqn.2010-10.org.openstack:volume-ccb39627-34fa-4f47-968b-6580d9d7ee2b'
        elif self.__id__ == 490:
            return\
 u'iqn.2010-10.org.openstack:volume-ccb39627-34fa-4f47-968b-6580d9d7ee2b'

    @TargetName.setter
    def TargetName(self, value):
        pass

    @property
    def DeviceInterfaceName(self):
        if self.__id__ == 369:
            return u''
        elif self.__id__ == 370:
            return\
 u'\\\\?\\scsi#disk&ven_iet&prod_virtual-disk#1&1c121344&0&000001#{53f56307-b6\
bf-11d0-94f2-00a0c91efb8b}'
        elif self.__id__ == 489:
            return u''
        elif self.__id__ == 490:
            return\
 u'\\\\?\\scsi#disk&ven_iet&prod_virtual-disk#1&1c121344&0&000001#{53f56307-b6\
bf-11d0-94f2-00a0c91efb8b}'

    @DeviceInterfaceName.setter
    def DeviceInterfaceName(self, value):
        pass

    @property
    def ScsiPortNumber(self):
        if self.__id__ == 369:
            return 3
        elif self.__id__ == 370:
            return 3
        elif self.__id__ == 489:
            return 3
        elif self.__id__ == 490:
            return 3

    @ScsiPortNumber.setter
    def ScsiPortNumber(self, value):
        pass

    def __call__(self, *args):
        if len(args) == 0 and self.__id__ == 153:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:04FB9E92-46A2-4F69-9555-6E4323312DA2\\\\83F8638B-8DCA-4152\
-9EDA-2CA8B33039B4\\\\0"'
        elif len(args) == 0 and self.__id__ == 157:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="04FB9E92-46A2-4F69-9555-6E4323312DA2"'
        elif len(args) == 0 and self.__id__ == 250:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="04FB9E92-46A2-4F69-9555-6E4323312DA2"'
        elif len(args) == 0 and self.__id__ == 345:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="04FB9E92-46A2-4F69-9555-6E4323312DA2"'
        elif len(args) == 0 and self.__id__ == 45:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="04FB9E92-46A2-4F69-9555-6E4323312DA2"'
        elif len(args) == 0 and self.__id__ == 48:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="04FB9E92-46A2-4F69-9555-6E4323312DA2"'
        elif len(args) == 0 and self.__id__ == 351:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="04FB9E92-46A2-4F69-9555-6E4323312DA2"'
        elif len(args) == 0 and self.__id__ == 561:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="04FB9E92-46A2-4F69-9555-6E4323312DA2"'
        elif len(args) == 0 and self.__id__ == 483:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_DiskDrive.CreationClassName="Msv\
m_DiskDrive",DeviceID="Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\\\\1",Sy\
stemCreationClassName="Msvm_ComputerSystem",SystemName="HV12OSDEMO1"'
        elif len(args) == 0 and self.__id__ == 498:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_DiskDrive.CreationClassName="Msv\
m_DiskDrive",DeviceID="Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\\\\1",Sy\
stemCreationClassName="Msvm_ComputerSystem",SystemName="HV12OSDEMO1"'
        elif len(args) == 0 and self.__id__ == 504:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:04FB9E92-46A2-4F69-9555-6E4323312DA2\\\\5F053DDB-3C35-4A44\
-8E4E-2056CC3A440A\\\\0\\\\0\\\\D"'
        elif len(args) == 0 and self.__id__ == 392:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:04FB9E92-46A2-4F69-9555-6E4323312DA2\\\\5F053DDB-3C35-4A44\
-8E4E-2056CC3A440A\\\\0"'
        elif len(args) == 0 and self.__id__ == 482:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:04FB9E92-46A2-4F69-9555-6E4323312DA2\\\\5F053DDB-3C35-4A44\
-8E4E-2056CC3A440A\\\\0"'
        elif len(args) == 0 and self.__id__ == 487:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="04FB9E92-46A2-4F69-9555-6E4323312DA2"'
        elif len(args) == 0 and self.__id__ == 505:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="04FB9E92-46A2-4F69-9555-6E4323312DA2"'

    def Item(self, strName='<PyOleMissing object at 0x03237588>', iFlags=0):
        if self.__id__ == 67 and strName == u'InstanceID':
            v = CDispatch(68)
            return v
        elif self.__id__ == 71 and strName == u'ResourceSubType':
            v = CDispatch(72)
            return v
        elif self.__id__ == 75 and strName == u'HostResource':
            v = CDispatch(76)
            return v
        elif self.__id__ == 79 and strName == u'ElementName':
            v = CDispatch(80)
            return v
        elif self.__id__ == 83 and strName == u'Description':
            v = CDispatch(84)
            return v
        elif self.__id__ == 87 and strName == u'Parent':
            v = CDispatch(88)
            return v
        elif self.__id__ == 91 and strName == u'VirtualQuantity':
            v = CDispatch(92)
            return v
        elif self.__id__ == 95 and strName == u'AutomaticDeallocation':
            v = CDispatch(96)
            return v
        elif self.__id__ == 99 and strName == u'AutomaticAllocation':
            v = CDispatch(100)
            return v
        elif self.__id__ == 103 and strName == u'PoolID':
            v = CDispatch(104)
            return v
        elif self.__id__ == 107 and strName == u'Reservation':
            v = CDispatch(108)
            return v
        elif self.__id__ == 111 and strName == u'AllocationUnits':
            v = CDispatch(112)
            return v
        elif self.__id__ == 115 and strName == u'MappingBehavior':
            v = CDispatch(116)
            return v
        elif self.__id__ == 119 and strName == u'Address':
            v = CDispatch(120)
            return v
        elif self.__id__ == 123 and strName == u'OtherResourceType':
            v = CDispatch(124)
            return v
        elif self.__id__ == 127 and strName == u'Caption':
            v = CDispatch(128)
            return v
        elif self.__id__ == 131 and strName == u'ConsumerVisibility':
            v = CDispatch(132)
            return v
        elif self.__id__ == 135 and strName == u'Limit':
            v = CDispatch(136)
            return v
        elif self.__id__ == 139 and strName == u'ResourceType':
            v = CDispatch(140)
            return v
        elif self.__id__ == 143 and strName == u'Weight':
            v = CDispatch(144)
            return v
        elif self.__id__ == 149 and strName == u'Connection':
            v = CDispatch(150)
            return v
        elif self.__id__ == 161 and strName == u'InstanceID':
            v = CDispatch(162)
            return v
        elif self.__id__ == 165 and strName == u'ResourceSubType':
            v = CDispatch(166)
            return v
        elif self.__id__ == 169 and strName == u'HostResource':
            v = CDispatch(170)
            return v
        elif self.__id__ == 173 and strName == u'ElementName':
            v = CDispatch(174)
            return v
        elif self.__id__ == 177 and strName == u'Description':
            v = CDispatch(178)
            return v
        elif self.__id__ == 181 and strName == u'Parent':
            v = CDispatch(182)
            return v
        elif self.__id__ == 185 and strName == u'VirtualQuantity':
            v = CDispatch(186)
            return v
        elif self.__id__ == 189 and strName == u'AutomaticDeallocation':
            v = CDispatch(190)
            return v
        elif self.__id__ == 193 and strName == u'AutomaticAllocation':
            v = CDispatch(194)
            return v
        elif self.__id__ == 197 and strName == u'PoolID':
            v = CDispatch(198)
            return v
        elif self.__id__ == 201 and strName == u'Reservation':
            v = CDispatch(202)
            return v
        elif self.__id__ == 205 and strName == u'AllocationUnits':
            v = CDispatch(206)
            return v
        elif self.__id__ == 209 and strName == u'MappingBehavior':
            v = CDispatch(210)
            return v
        elif self.__id__ == 213 and strName == u'Address':
            v = CDispatch(214)
            return v
        elif self.__id__ == 217 and strName == u'OtherResourceType':
            v = CDispatch(218)
            return v
        elif self.__id__ == 221 and strName == u'Caption':
            v = CDispatch(222)
            return v
        elif self.__id__ == 225 and strName == u'ConsumerVisibility':
            v = CDispatch(226)
            return v
        elif self.__id__ == 229 and strName == u'Limit':
            v = CDispatch(230)
            return v
        elif self.__id__ == 233 and strName == u'ResourceType':
            v = CDispatch(234)
            return v
        elif self.__id__ == 237 and strName == u'Weight':
            v = CDispatch(238)
            return v
        elif self.__id__ == 243 and strName == u'Connection':
            v = CDispatch(244)
            return v
        elif self.__id__ == 256 and strName == u'InstanceID':
            v = CDispatch(257)
            return v
        elif self.__id__ == 260 and strName == u'ResourceSubType':
            v = CDispatch(261)
            return v
        elif self.__id__ == 264 and strName == u'HostResource':
            v = CDispatch(265)
            return v
        elif self.__id__ == 268 and strName == u'ElementName':
            v = CDispatch(269)
            return v
        elif self.__id__ == 272 and strName == u'Description':
            v = CDispatch(273)
            return v
        elif self.__id__ == 276 and strName == u'Parent':
            v = CDispatch(277)
            return v
        elif self.__id__ == 280 and strName == u'VirtualQuantity':
            v = CDispatch(281)
            return v
        elif self.__id__ == 284 and strName == u'AutomaticDeallocation':
            v = CDispatch(285)
            return v
        elif self.__id__ == 288 and strName == u'AutomaticAllocation':
            v = CDispatch(289)
            return v
        elif self.__id__ == 292 and strName == u'PoolID':
            v = CDispatch(293)
            return v
        elif self.__id__ == 296 and strName == u'Reservation':
            v = CDispatch(297)
            return v
        elif self.__id__ == 300 and strName == u'AllocationUnits':
            v = CDispatch(301)
            return v
        elif self.__id__ == 304 and strName == u'MappingBehavior':
            v = CDispatch(305)
            return v
        elif self.__id__ == 308 and strName == u'Address':
            v = CDispatch(309)
            return v
        elif self.__id__ == 312 and strName == u'OtherResourceType':
            v = CDispatch(313)
            return v
        elif self.__id__ == 316 and strName == u'Caption':
            v = CDispatch(317)
            return v
        elif self.__id__ == 320 and strName == u'ConsumerVisibility':
            v = CDispatch(321)
            return v
        elif self.__id__ == 324 and strName == u'Limit':
            v = CDispatch(325)
            return v
        elif self.__id__ == 328 and strName == u'ResourceType':
            v = CDispatch(329)
            return v
        elif self.__id__ == 332 and strName == u'Weight':
            v = CDispatch(333)
            return v
        elif self.__id__ == 338 and strName == u'Connection':
            v = CDispatch(339)
            return v
        elif self.__id__ == 69 and strName == u'InstanceID':
            v = CDispatch(70)
            return v
        elif self.__id__ == 73 and strName == u'ResourceSubType':
            v = CDispatch(74)
            return v
        elif self.__id__ == 77 and strName == u'HostResource':
            v = CDispatch(78)
            return v
        elif self.__id__ == 81 and strName == u'ElementName':
            v = CDispatch(82)
            return v
        elif self.__id__ == 85 and strName == u'Description':
            v = CDispatch(86)
            return v
        elif self.__id__ == 89 and strName == u'Parent':
            v = CDispatch(90)
            return v
        elif self.__id__ == 93 and strName == u'VirtualQuantity':
            v = CDispatch(94)
            return v
        elif self.__id__ == 97 and strName == u'AutomaticDeallocation':
            v = CDispatch(98)
            return v
        elif self.__id__ == 101 and strName == u'AutomaticAllocation':
            v = CDispatch(102)
            return v
        elif self.__id__ == 105 and strName == u'PoolID':
            v = CDispatch(106)
            return v
        elif self.__id__ == 109 and strName == u'Reservation':
            v = CDispatch(110)
            return v
        elif self.__id__ == 113 and strName == u'AllocationUnits':
            v = CDispatch(114)
            return v
        elif self.__id__ == 117 and strName == u'MappingBehavior':
            v = CDispatch(118)
            return v
        elif self.__id__ == 121 and strName == u'Address':
            v = CDispatch(122)
            return v
        elif self.__id__ == 125 and strName == u'OtherResourceType':
            v = CDispatch(126)
            return v
        elif self.__id__ == 129 and strName == u'Caption':
            v = CDispatch(130)
            return v
        elif self.__id__ == 133 and strName == u'ConsumerVisibility':
            v = CDispatch(134)
            return v
        elif self.__id__ == 137 and strName == u'Limit':
            v = CDispatch(138)
            return v
        elif self.__id__ == 141 and strName == u'ResourceType':
            v = CDispatch(142)
            return v
        elif self.__id__ == 145 and strName == u'Weight':
            v = CDispatch(146)
            return v
        elif self.__id__ == 147 and strName == u'VirtualSystemIdentifiers':
            v = CDispatch(148)
            return v
        elif self.__id__ == 151 and strName == u'Connection':
            v = CDispatch(152)
            return v
        elif self.__id__ == 163 and strName == u'InstanceID':
            v = CDispatch(164)
            return v
        elif self.__id__ == 167 and strName == u'ResourceSubType':
            v = CDispatch(168)
            return v
        elif self.__id__ == 171 and strName == u'HostResource':
            v = CDispatch(172)
            return v
        elif self.__id__ == 175 and strName == u'ElementName':
            v = CDispatch(176)
            return v
        elif self.__id__ == 179 and strName == u'Description':
            v = CDispatch(180)
            return v
        elif self.__id__ == 183 and strName == u'Parent':
            v = CDispatch(184)
            return v
        elif self.__id__ == 187 and strName == u'VirtualQuantity':
            v = CDispatch(188)
            return v
        elif self.__id__ == 191 and strName == u'AutomaticDeallocation':
            v = CDispatch(192)
            return v
        elif self.__id__ == 195 and strName == u'AutomaticAllocation':
            v = CDispatch(196)
            return v
        elif self.__id__ == 199 and strName == u'PoolID':
            v = CDispatch(200)
            return v
        elif self.__id__ == 203 and strName == u'Reservation':
            v = CDispatch(204)
            return v
        elif self.__id__ == 207 and strName == u'AllocationUnits':
            v = CDispatch(208)
            return v
        elif self.__id__ == 211 and strName == u'MappingBehavior':
            v = CDispatch(212)
            return v
        elif self.__id__ == 215 and strName == u'Address':
            v = CDispatch(216)
            return v
        elif self.__id__ == 219 and strName == u'OtherResourceType':
            v = CDispatch(220)
            return v
        elif self.__id__ == 223 and strName == u'Caption':
            v = CDispatch(224)
            return v
        elif self.__id__ == 227 and strName == u'ConsumerVisibility':
            v = CDispatch(228)
            return v
        elif self.__id__ == 231 and strName == u'Limit':
            v = CDispatch(232)
            return v
        elif self.__id__ == 235 and strName == u'ResourceType':
            v = CDispatch(236)
            return v
        elif self.__id__ == 239 and strName == u'Weight':
            v = CDispatch(240)
            return v
        elif self.__id__ == 241 and strName == u'VirtualSystemIdentifiers':
            v = CDispatch(242)
            return v
        elif self.__id__ == 245 and strName == u'Connection':
            v = CDispatch(246)
            return v
        elif self.__id__ == 258 and strName == u'InstanceID':
            v = CDispatch(259)
            return v
        elif self.__id__ == 262 and strName == u'ResourceSubType':
            v = CDispatch(263)
            return v
        elif self.__id__ == 266 and strName == u'HostResource':
            v = CDispatch(267)
            return v
        elif self.__id__ == 270 and strName == u'ElementName':
            v = CDispatch(271)
            return v
        elif self.__id__ == 274 and strName == u'Description':
            v = CDispatch(275)
            return v
        elif self.__id__ == 278 and strName == u'Parent':
            v = CDispatch(279)
            return v
        elif self.__id__ == 282 and strName == u'VirtualQuantity':
            v = CDispatch(283)
            return v
        elif self.__id__ == 286 and strName == u'AutomaticDeallocation':
            v = CDispatch(287)
            return v
        elif self.__id__ == 290 and strName == u'AutomaticAllocation':
            v = CDispatch(291)
            return v
        elif self.__id__ == 294 and strName == u'PoolID':
            v = CDispatch(295)
            return v
        elif self.__id__ == 298 and strName == u'Reservation':
            v = CDispatch(299)
            return v
        elif self.__id__ == 302 and strName == u'AllocationUnits':
            v = CDispatch(303)
            return v
        elif self.__id__ == 306 and strName == u'MappingBehavior':
            v = CDispatch(307)
            return v
        elif self.__id__ == 310 and strName == u'Address':
            v = CDispatch(311)
            return v
        elif self.__id__ == 314 and strName == u'OtherResourceType':
            v = CDispatch(315)
            return v
        elif self.__id__ == 318 and strName == u'Caption':
            v = CDispatch(319)
            return v
        elif self.__id__ == 322 and strName == u'ConsumerVisibility':
            v = CDispatch(323)
            return v
        elif self.__id__ == 326 and strName == u'Limit':
            v = CDispatch(327)
            return v
        elif self.__id__ == 330 and strName == u'ResourceType':
            v = CDispatch(331)
            return v
        elif self.__id__ == 334 and strName == u'Weight':
            v = CDispatch(335)
            return v
        elif self.__id__ == 336 and strName == u'VirtualSystemIdentifiers':
            v = CDispatch(337)
            return v
        elif self.__id__ == 340 and strName == u'Connection':
            v = CDispatch(341)
            return v
        elif self.__id__ == 396 and strName == u'InstanceID':
            v = CDispatch(397)
            return v
        elif self.__id__ == 400 and strName == u'ResourceSubType':
            v = CDispatch(401)
            return v
        elif self.__id__ == 404 and strName == u'HostResource':
            v = CDispatch(405)
            return v
        elif self.__id__ == 408 and strName == u'ElementName':
            v = CDispatch(409)
            return v
        elif self.__id__ == 412 and strName == u'Description':
            v = CDispatch(413)
            return v
        elif self.__id__ == 416 and strName == u'Parent':
            v = CDispatch(417)
            return v
        elif self.__id__ == 420 and strName == u'VirtualQuantity':
            v = CDispatch(421)
            return v
        elif self.__id__ == 424 and strName == u'AutomaticDeallocation':
            v = CDispatch(425)
            return v
        elif self.__id__ == 428 and strName == u'AutomaticAllocation':
            v = CDispatch(429)
            return v
        elif self.__id__ == 432 and strName == u'PoolID':
            v = CDispatch(433)
            return v
        elif self.__id__ == 436 and strName == u'Reservation':
            v = CDispatch(437)
            return v
        elif self.__id__ == 440 and strName == u'AllocationUnits':
            v = CDispatch(441)
            return v
        elif self.__id__ == 444 and strName == u'MappingBehavior':
            v = CDispatch(445)
            return v
        elif self.__id__ == 448 and strName == u'Address':
            v = CDispatch(449)
            return v
        elif self.__id__ == 452 and strName == u'OtherResourceType':
            v = CDispatch(453)
            return v
        elif self.__id__ == 456 and strName == u'Caption':
            v = CDispatch(457)
            return v
        elif self.__id__ == 460 and strName == u'ConsumerVisibility':
            v = CDispatch(461)
            return v
        elif self.__id__ == 464 and strName == u'Limit':
            v = CDispatch(465)
            return v
        elif self.__id__ == 468 and strName == u'ResourceType':
            v = CDispatch(469)
            return v
        elif self.__id__ == 472 and strName == u'Weight':
            v = CDispatch(473)
            return v
        elif self.__id__ == 478 and strName == u'Connection':
            v = CDispatch(479)
            return v
        elif self.__id__ == 398 and strName == u'InstanceID':
            v = CDispatch(399)
            return v
        elif self.__id__ == 402 and strName == u'ResourceSubType':
            v = CDispatch(403)
            return v
        elif self.__id__ == 406 and strName == u'HostResource':
            v = CDispatch(407)
            return v
        elif self.__id__ == 410 and strName == u'ElementName':
            v = CDispatch(411)
            return v
        elif self.__id__ == 414 and strName == u'Description':
            v = CDispatch(415)
            return v
        elif self.__id__ == 418 and strName == u'Parent':
            v = CDispatch(419)
            return v
        elif self.__id__ == 422 and strName == u'VirtualQuantity':
            v = CDispatch(423)
            return v
        elif self.__id__ == 426 and strName == u'AutomaticDeallocation':
            v = CDispatch(427)
            return v
        elif self.__id__ == 430 and strName == u'AutomaticAllocation':
            v = CDispatch(431)
            return v
        elif self.__id__ == 434 and strName == u'PoolID':
            v = CDispatch(435)
            return v
        elif self.__id__ == 438 and strName == u'Reservation':
            v = CDispatch(439)
            return v
        elif self.__id__ == 442 and strName == u'AllocationUnits':
            v = CDispatch(443)
            return v
        elif self.__id__ == 446 and strName == u'MappingBehavior':
            v = CDispatch(447)
            return v
        elif self.__id__ == 450 and strName == u'Address':
            v = CDispatch(451)
            return v
        elif self.__id__ == 454 and strName == u'OtherResourceType':
            v = CDispatch(455)
            return v
        elif self.__id__ == 458 and strName == u'Caption':
            v = CDispatch(459)
            return v
        elif self.__id__ == 462 and strName == u'ConsumerVisibility':
            v = CDispatch(463)
            return v
        elif self.__id__ == 466 and strName == u'Limit':
            v = CDispatch(467)
            return v
        elif self.__id__ == 470 and strName == u'ResourceType':
            v = CDispatch(471)
            return v
        elif self.__id__ == 474 and strName == u'Weight':
            v = CDispatch(475)
            return v
        elif self.__id__ == 476 and strName == u'VirtualSystemIdentifiers':
            v = CDispatch(477)
            return v
        elif self.__id__ == 480 and strName == u'Connection':
            v = CDispatch(481)
            return v
