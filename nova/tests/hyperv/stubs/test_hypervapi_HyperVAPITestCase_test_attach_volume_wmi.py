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
            v = _wmi_namespace(509)
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
            v = _wmi_namespace(370)
        _WMI_count_3 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_StorageJob.InstanceID="FFDC5EB3-3577\
-487D-8694-BA37BEFDE5AE"':
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
 u'//HV12OSDEMO1/root/virtualization:Msvm_StorageJob.InstanceID="C237EDD6-75BC\
-48B6-85C8-7979AF83AE67"':
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
        _WMI_count_5 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_ConcreteJob.InstanceID="4DA7F6B3-B17\
B-4568-ADEB-86104A365C3B"':
        ret_value = None
        global _WMI_count_6
        if not '_WMI_count_6' in globals():
            _WMI_count_6 = 0
        if _WMI_count_6 == 0:
            v = _wmi_object(354)
        elif _WMI_count_6 == 1:
            v = _wmi_object(355)
        elif _WMI_count_6 == 2:
            v = _wmi_object(356)
        elif _WMI_count_6 == 3:
            v = _wmi_object(357)
        elif _WMI_count_6 == 4:
            v = _wmi_object(358)
        elif _WMI_count_6 == 5:
            v = _wmi_object(359)
        elif _WMI_count_6 == 6:
            v = _wmi_object(360)
        _WMI_count_6 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_ConcreteJob.InstanceID="2F925A6E-F7A\
2-4906-B45F-9BE530898593"':
        ret_value = None
        global _WMI_count_7
        if not '_WMI_count_7' in globals():
            _WMI_count_7 = 0
        if _WMI_count_7 == 0:
            v = _wmi_object(517)
        elif _WMI_count_7 == 1:
            v = _wmi_object(518)
        _WMI_count_7 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_ConcreteJob.InstanceID="1C3D7F8E-567\
0-4015-9E32-FFD7614A4784"':
        ret_value = None
        global _WMI_count_8
        if not '_WMI_count_8' in globals():
            _WMI_count_8 = 0
        if _WMI_count_8 == 0:
            v = _wmi_object(540)
        elif _WMI_count_8 == 1:
            v = _wmi_object(541)
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
        if self.__id__ == 2:
            v = _wmi_class(545)
            return v
        elif self.__id__ == 7:
            v = _wmi_class(364)
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
                v = _wmi_class(64)
            elif self._Msvm_ResourceAllocationSettingData_count_0 == 1:
                v = _wmi_class(158)
            elif self._Msvm_ResourceAllocationSettingData_count_0 == 2:
                v = _wmi_class(253)
            self._Msvm_ResourceAllocationSettingData_count_0 += 1
            return v
        elif self.__id__ == 370:
            v = _wmi_class(393)
            return v

    @Msvm_ResourceAllocationSettingData.setter
    def Msvm_ResourceAllocationSettingData(self, value):
        pass

    @property
    def MSFT_iSCSITargetPortal(self):
        if self.__id__ == 7:
            v = _wmi_class(361)
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
                v = _wmi_class(34)
            elif self._Msvm_VirtualSystemManagementService_count_0 == 1:
                v = _wmi_class(153)
            elif self._Msvm_VirtualSystemManagementService_count_0 == 2:
                v = _wmi_class(246)
            elif self._Msvm_VirtualSystemManagementService_count_0 == 3:
                v = _wmi_class(341)
            elif self._Msvm_VirtualSystemManagementService_count_0 == 4:
                v = _wmi_class(347)
            self._Msvm_VirtualSystemManagementService_count_0 += 1
            return v
        elif self.__id__ == 11:
            v = _wmi_class(512)
            return v
        elif self.__id__ == 370:
            v = _wmi_class(483)
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
                v = _wmi_class(39)
            elif self._Msvm_ComputerSystem_count_0 == 2:
                v = _wmi_class(345)
            elif self._Msvm_ComputerSystem_count_0 == 3:
                v = _wmi_class(351)
            self._Msvm_ComputerSystem_count_0 += 1
            return v
        elif self.__id__ == 11:
            ret_value = None
            if not hasattr(self, '_Msvm_ComputerSystem_count_1'):
                self._Msvm_ComputerSystem_count_1 = 0
            if self._Msvm_ComputerSystem_count_1 == 0:
                v = _wmi_class(487)
            elif self._Msvm_ComputerSystem_count_1 == 1:
                v = _wmi_class(507)
            elif self._Msvm_ComputerSystem_count_1 == 2:
                v = _wmi_class(510)
            elif self._Msvm_ComputerSystem_count_1 == 3:
                v = _wmi_class(514)
            elif self._Msvm_ComputerSystem_count_1 == 4:
                v = _wmi_class(519)
            self._Msvm_ComputerSystem_count_1 += 1
            return v

    @Msvm_ComputerSystem.setter
    def Msvm_ComputerSystem(self, value):
        pass

    @property
    def Msvm_VirtualSystemGlobalSettingData(self):
        if self.__id__ == 9:
            v = _wmi_class(36)
            return v

    @Msvm_VirtualSystemGlobalSettingData.setter
    def Msvm_VirtualSystemGlobalSettingData(self, value):
        pass

    @property
    def MSFT_iSCSISession(self):
        if self.__id__ == 2:
            v = _wmi_class(547)
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
                v = _wmi_class(48)
            elif self._MSVM_ComputerSystem_count_0 == 1:
                v = _wmi_class(250)
            self._MSVM_ComputerSystem_count_0 += 1
            return v
        elif self.__id__ == 370:
            v = _wmi_class(373)
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
                v1 = _wmi_object(506)
                v.append(v1)
            elif self._query_count_0 == 1:
                v = []
                v1 = _wmi_object(544)
                v.append(v1)
            self._query_count_0 += 1
            return v
        elif self.__id__ == 8 and wql == 'SELECT * FROM\
 MSiSCSIInitiator_SessionClass                 WHERE\
 TargetName=\'iqn.2010-10.org.openstack:volume-ccb39627-34fa-4f47-968b-6580d9d\
7ee2b\'':
            v = []
            v1 = _wmi_object(367)
            v.append(v1)
            return v
        elif self.__id__ == 509 and wql == u'Select * from CIM_DataFile where\
 Name =\
 \'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_67a39e13-209c-4108-8bd\
8-54c0ea5832bb\\openstack_unit_test_vm_67a39e13-209c-4108-8bd8-54c0ea5832bb.vh\
d\'':
            v = []
            v1 = _wmi_object(542)
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
            v1 = _wmi_object(63)
            v.append(v1)
            return v
        elif self.__id__ == 9 and wql == 'SELECT * FROM\
 Msvm_ResourceAllocationSettingData                  WHERE ResourceSubType\
 LIKE \'Microsoft Virtual Hard Disk\' AND                  InstanceID LIKE\
 \'%Default%\' ':
            v = []
            v1 = _wmi_object(157)
            v.append(v1)
            return v
        elif self.__id__ == 9 and wql == 'SELECT * FROM\
 Msvm_ResourceAllocationSettingData                 WHERE ResourceSubType =\
 \'Microsoft Synthetic SCSI Controller\'                AND InstanceID LIKE\
 \'%Default%\'':
            v = []
            v1 = _wmi_object(252)
            v.append(v1)
            return v
        elif self.__id__ == 11 and wql == 'Select * from\
 Msvm_ImageManagementService':
            v = []
            v1 = _wmi_object(12)
            v.append(v1)
            return v
        elif self.__id__ == 370 and wql == 'SELECT * FROM Msvm_DiskDrive WHERE\
 DriveNumber=1':
            ret_value = None
            if not hasattr(self, '_query_count_8'):
                self._query_count_8 = 0
            if self._query_count_8 == 0:
                v = []
                v1 = _wmi_object(371)
                v.append(v1)
            elif self._query_count_8 == 1:
                v = []
                v1 = _wmi_object(372)
                v.append(v1)
            self._query_count_8 += 1
            return v
        elif self.__id__ == 370 and wql == u'SELECT * FROM\
 Msvm_ResourceAllocationSettingData                 WHERE ResourceSubType LIKE\
 \'Microsoft Physical Disk Drive\'                AND Parent =\
 \'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:8F9341AA-8208-4B0D-9E5B-9D70879E39EC\\\\9BE8AEC0-673A-4A38\
-9B7B-38221FD78B44\\\\0"\'':
            v = []
            return v
        elif self.__id__ == 370 and wql == 'SELECT * FROM\
 Msvm_ResourceAllocationSettingData                 WHERE ResourceSubType LIKE\
 \'Microsoft Physical Disk Drive\'                AND InstanceID LIKE\
 \'%Default%\'':
            v = []
            v1 = _wmi_object(392)
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
        if self.__id__ == 361:
            v = _wmi_method(362)
            return v

    @New.setter
    def New(self, value):
        pass

    @property
    def Connect(self):
        if self.__id__ == 364:
            v = _wmi_method(365)
            return v

    @Connect.setter
    def Connect(self, value):
        pass

    def __call__(self, fields='[]', **where_clause):
        if self.__id__ == 547 and where_clause.get('TargetNodeAddress') ==\
 'iqn.2010-10.org.openstack:volume-ccb39627-34fa-4f47-968b-6580d9d7ee2b':
            v = []
            v1 = _wmi_object(548)
            v.append(v1)
            return v
        elif self.__id__ == 545 and where_clause.get('NodeAddress') ==\
 'iqn.2010-10.org.openstack:volume-ccb39627-34fa-4f47-968b-6580d9d7ee2b':
            v = []
            v1 = _wmi_object(546)
            v.append(v1)
            return v
        elif self.__id__ == 5:
            v = []
            v1 = _wmi_object(6)
            v.append(v1)
            return v
        elif self.__id__ == 48 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_67a39e13-209c-4108-8bd8-54c0ea5832bb':
            v = []
            v1 = _wmi_object(49)
            v.append(v1)
            return v
        elif self.__id__ == 250 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_67a39e13-209c-4108-8bd8-54c0ea5832bb':
            v = []
            v1 = _wmi_object(251)
            v.append(v1)
            return v
        elif self.__id__ == 10 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_67a39e13-209c-4108-8bd8-54c0ea5832bb':
            v = []
            return v
        elif self.__id__ == 39 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_67a39e13-209c-4108-8bd8-54c0ea5832bb':
            v = []
            v1 = _wmi_object(40)
            v.append(v1)
            return v
        elif self.__id__ == 345 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_67a39e13-209c-4108-8bd8-54c0ea5832bb':
            v = []
            v1 = _wmi_object(346)
            v.append(v1)
            return v
        elif self.__id__ == 351 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_67a39e13-209c-4108-8bd8-54c0ea5832bb':
            v = []
            v1 = _wmi_object(352)
            v.append(v1)
            return v
        elif self.__id__ == 34:
            v = []
            v1 = _wmi_object(35)
            v.append(v1)
            return v
        elif self.__id__ == 153:
            v = []
            v1 = _wmi_object(154)
            v.append(v1)
            return v
        elif self.__id__ == 246:
            v = []
            v1 = _wmi_object(247)
            v.append(v1)
            return v
        elif self.__id__ == 341:
            v = []
            v1 = _wmi_object(342)
            v.append(v1)
            return v
        elif self.__id__ == 347:
            v = []
            v1 = _wmi_object(348)
            v.append(v1)
            return v
        elif self.__id__ == 487 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_67a39e13-209c-4108-8bd8-54c0ea5832bb':
            v = []
            v1 = _wmi_object(488)
            v.append(v1)
            return v
        elif self.__id__ == 507 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_67a39e13-209c-4108-8bd8-54c0ea5832bb':
            v = []
            v1 = _wmi_object(508)
            v.append(v1)
            return v
        elif self.__id__ == 510 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_67a39e13-209c-4108-8bd8-54c0ea5832bb':
            v = []
            v1 = _wmi_object(511)
            v.append(v1)
            return v
        elif self.__id__ == 514 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_67a39e13-209c-4108-8bd8-54c0ea5832bb':
            v = []
            v1 = _wmi_object(515)
            v.append(v1)
            return v
        elif self.__id__ == 519 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_67a39e13-209c-4108-8bd8-54c0ea5832bb':
            v = []
            v1 = _wmi_object(520)
            v.append(v1)
            return v
        elif self.__id__ == 512:
            v = []
            v1 = _wmi_object(513)
            v.append(v1)
            return v
        elif self.__id__ == 373 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_67a39e13-209c-4108-8bd8-54c0ea5832bb':
            v = []
            v1 = _wmi_object(374)
            v.append(v1)
            return v
        elif self.__id__ == 483:
            v = []
            v1 = _wmi_object(484)
            v.append(v1)
            return v

    def new(self, **kwargs):
        if self.__id__ == 36:
            v = _wmi_object(37)
            return v
        elif self.__id__ == 64:
            v = _wmi_object(65)
            return v
        elif self.__id__ == 158:
            v = _wmi_object(159)
            return v
        elif self.__id__ == 253:
            v = _wmi_object(254)
            return v
        elif self.__id__ == 393:
            v = _wmi_object(394)
            return v


class _wmi_object(object):

    def __init__(self, instance_id=1, *args, **kwargs):
        self.__instance_id__ = instance_id

    @property
    def __id__(self):
        return self.__instance_id__

    @property
    def Disconnect(self):
        if self.__id__ == 546:
            v = _wmi_method(550)
            return v

    @Disconnect.setter
    def Disconnect(self, value):
        pass

    @property
    def path_(self):
        if self.__id__ == 59:
            v = CDispatch(152)
            return v
        elif self.__id__ == 49:
            ret_value = None
            if not hasattr(self, '_path__count_1'):
                self._path__count_1 = 0
            if self._path__count_1 == 0:
                v = CDispatch(156)
            elif self._path__count_1 == 1:
                v = CDispatch(249)
            self._path__count_1 += 1
            return v
        elif self.__id__ == 251:
            v = CDispatch(344)
            return v
        elif self.__id__ == 40:
            ret_value = None
            if not hasattr(self, '_path__count_3'):
                self._path__count_3 = 0
            if self._path__count_3 == 0:
                v = CDispatch(44)
            elif self._path__count_3 == 1:
                v = CDispatch(47)
            self._path__count_3 += 1
            return v
        elif self.__id__ == 346:
            v = CDispatch(350)
            return v
        elif self.__id__ == 511:
            v = CDispatch(539)
            return v
        elif self.__id__ == 372:
            v = CDispatch(482)
            return v
        elif self.__id__ == 390:
            ret_value = None
            if not hasattr(self, '_path__count_7'):
                self._path__count_7 = 0
            if self._path__count_7 == 0:
                v = CDispatch(391)
            elif self._path__count_7 == 1:
                v = CDispatch(481)
            self._path__count_7 += 1
            return v
        elif self.__id__ == 374:
            v = CDispatch(486)
            return v

    @path_.setter
    def path_(self, value):
        pass

    @property
    def HostResource(self):
        if self.__id__ == 504:
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_DiskDrive.CreationClassName="Msv\
m_DiskDrive",DeviceID="Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\\\\1",Sy\
stemCreationClassName="Msvm_ComputerSystem",SystemName="HV12OSDEMO1"'
            v += (v1,)
            return v
        elif self.__id__ == 536:
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
        if self.__id__ == 35:
            ret_value = None
            if not hasattr(self, '_ModifyVirtualSystemResources_count_0'):
                self._ModifyVirtualSystemResources_count_0 = 0
            if self._ModifyVirtualSystemResources_count_0 == 0:
                v = _wmi_method(43)
            elif self._ModifyVirtualSystemResources_count_0 == 1:
                v = _wmi_method(46)
            self._ModifyVirtualSystemResources_count_0 += 1
            return v

    @ModifyVirtualSystemResources.setter
    def ModifyVirtualSystemResources(self, value):
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
        elif self.__id__ == 517:
            return 4
        elif self.__id__ == 518:
            ret_value = None
            if not hasattr(self, '_JobState_count_26'):
                self._JobState_count_26 = 0
            if self._JobState_count_26 == 0:
                v = 7
            elif self._JobState_count_26 == 1:
                v = 7
            self._JobState_count_26 += 1
            return v
        elif self.__id__ == 540:
            return 4
        elif self.__id__ == 541:
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
    def Description(self):
        if self.__id__ == 33:
            return u'Creating Virtual Hard Disk'
        elif self.__id__ == 360:
            return u'Initializing and Starting Virtual Machine'

    @Description.setter
    def Description(self, value):
        pass

    @property
    def AddVirtualSystemResources(self):
        if self.__id__ == 154:
            v = _wmi_method(155)
            return v
        elif self.__id__ == 247:
            v = _wmi_method(248)
            return v
        elif self.__id__ == 342:
            v = _wmi_method(343)
            return v
        elif self.__id__ == 348:
            v = _wmi_method(349)
            return v
        elif self.__id__ == 484:
            v = _wmi_method(485)
            return v

    @AddVirtualSystemResources.setter
    def AddVirtualSystemResources(self, value):
        pass

    @property
    def IsConnected(self):
        if self.__id__ == 546:
            return True

    @IsConnected.setter
    def IsConnected(self, value):
        pass

    @property
    def Properties_(self):
        if self.__id__ == 63:
            ret_value = None
            if not hasattr(self, '_Properties__count_0'):
                self._Properties__count_0 = 0
            if self._Properties__count_0 == 0:
                v = CDispatch(66)
            elif self._Properties__count_0 == 1:
                v = CDispatch(70)
            elif self._Properties__count_0 == 2:
                v = CDispatch(74)
            elif self._Properties__count_0 == 3:
                v = CDispatch(78)
            elif self._Properties__count_0 == 4:
                v = CDispatch(82)
            elif self._Properties__count_0 == 5:
                v = CDispatch(86)
            elif self._Properties__count_0 == 6:
                v = CDispatch(90)
            elif self._Properties__count_0 == 7:
                v = CDispatch(94)
            elif self._Properties__count_0 == 8:
                v = CDispatch(98)
            elif self._Properties__count_0 == 9:
                v = CDispatch(102)
            elif self._Properties__count_0 == 10:
                v = CDispatch(106)
            elif self._Properties__count_0 == 11:
                v = CDispatch(110)
            elif self._Properties__count_0 == 12:
                v = CDispatch(114)
            elif self._Properties__count_0 == 13:
                v = CDispatch(118)
            elif self._Properties__count_0 == 14:
                v = CDispatch(122)
            elif self._Properties__count_0 == 15:
                v = CDispatch(126)
            elif self._Properties__count_0 == 16:
                v = CDispatch(130)
            elif self._Properties__count_0 == 17:
                v = CDispatch(134)
            elif self._Properties__count_0 == 18:
                v = CDispatch(138)
            elif self._Properties__count_0 == 19:
                v = CDispatch(142)
            elif self._Properties__count_0 == 20:
                v = CDispatch(148)
            self._Properties__count_0 += 1
            return v
        elif self.__id__ == 157:
            ret_value = None
            if not hasattr(self, '_Properties__count_1'):
                self._Properties__count_1 = 0
            if self._Properties__count_1 == 0:
                v = CDispatch(160)
            elif self._Properties__count_1 == 1:
                v = CDispatch(164)
            elif self._Properties__count_1 == 2:
                v = CDispatch(168)
            elif self._Properties__count_1 == 3:
                v = CDispatch(172)
            elif self._Properties__count_1 == 4:
                v = CDispatch(176)
            elif self._Properties__count_1 == 5:
                v = CDispatch(180)
            elif self._Properties__count_1 == 6:
                v = CDispatch(184)
            elif self._Properties__count_1 == 7:
                v = CDispatch(188)
            elif self._Properties__count_1 == 8:
                v = CDispatch(192)
            elif self._Properties__count_1 == 9:
                v = CDispatch(196)
            elif self._Properties__count_1 == 10:
                v = CDispatch(200)
            elif self._Properties__count_1 == 11:
                v = CDispatch(204)
            elif self._Properties__count_1 == 12:
                v = CDispatch(208)
            elif self._Properties__count_1 == 13:
                v = CDispatch(212)
            elif self._Properties__count_1 == 14:
                v = CDispatch(216)
            elif self._Properties__count_1 == 15:
                v = CDispatch(220)
            elif self._Properties__count_1 == 16:
                v = CDispatch(224)
            elif self._Properties__count_1 == 17:
                v = CDispatch(228)
            elif self._Properties__count_1 == 18:
                v = CDispatch(232)
            elif self._Properties__count_1 == 19:
                v = CDispatch(236)
            elif self._Properties__count_1 == 20:
                v = CDispatch(242)
            self._Properties__count_1 += 1
            return v
        elif self.__id__ == 252:
            ret_value = None
            if not hasattr(self, '_Properties__count_2'):
                self._Properties__count_2 = 0
            if self._Properties__count_2 == 0:
                v = CDispatch(255)
            elif self._Properties__count_2 == 1:
                v = CDispatch(259)
            elif self._Properties__count_2 == 2:
                v = CDispatch(263)
            elif self._Properties__count_2 == 3:
                v = CDispatch(267)
            elif self._Properties__count_2 == 4:
                v = CDispatch(271)
            elif self._Properties__count_2 == 5:
                v = CDispatch(275)
            elif self._Properties__count_2 == 6:
                v = CDispatch(279)
            elif self._Properties__count_2 == 7:
                v = CDispatch(283)
            elif self._Properties__count_2 == 8:
                v = CDispatch(287)
            elif self._Properties__count_2 == 9:
                v = CDispatch(291)
            elif self._Properties__count_2 == 10:
                v = CDispatch(295)
            elif self._Properties__count_2 == 11:
                v = CDispatch(299)
            elif self._Properties__count_2 == 12:
                v = CDispatch(303)
            elif self._Properties__count_2 == 13:
                v = CDispatch(307)
            elif self._Properties__count_2 == 14:
                v = CDispatch(311)
            elif self._Properties__count_2 == 15:
                v = CDispatch(315)
            elif self._Properties__count_2 == 16:
                v = CDispatch(319)
            elif self._Properties__count_2 == 17:
                v = CDispatch(323)
            elif self._Properties__count_2 == 18:
                v = CDispatch(327)
            elif self._Properties__count_2 == 19:
                v = CDispatch(331)
            elif self._Properties__count_2 == 20:
                v = CDispatch(337)
            self._Properties__count_2 += 1
            return v
        elif self.__id__ == 65:
            ret_value = None
            if not hasattr(self, '_Properties__count_3'):
                self._Properties__count_3 = 0
            if self._Properties__count_3 == 0:
                v = CDispatch(68)
            elif self._Properties__count_3 == 1:
                v = CDispatch(72)
            elif self._Properties__count_3 == 2:
                v = CDispatch(76)
            elif self._Properties__count_3 == 3:
                v = CDispatch(80)
            elif self._Properties__count_3 == 4:
                v = CDispatch(84)
            elif self._Properties__count_3 == 5:
                v = CDispatch(88)
            elif self._Properties__count_3 == 6:
                v = CDispatch(92)
            elif self._Properties__count_3 == 7:
                v = CDispatch(96)
            elif self._Properties__count_3 == 8:
                v = CDispatch(100)
            elif self._Properties__count_3 == 9:
                v = CDispatch(104)
            elif self._Properties__count_3 == 10:
                v = CDispatch(108)
            elif self._Properties__count_3 == 11:
                v = CDispatch(112)
            elif self._Properties__count_3 == 12:
                v = CDispatch(116)
            elif self._Properties__count_3 == 13:
                v = CDispatch(120)
            elif self._Properties__count_3 == 14:
                v = CDispatch(124)
            elif self._Properties__count_3 == 15:
                v = CDispatch(128)
            elif self._Properties__count_3 == 16:
                v = CDispatch(132)
            elif self._Properties__count_3 == 17:
                v = CDispatch(136)
            elif self._Properties__count_3 == 18:
                v = CDispatch(140)
            elif self._Properties__count_3 == 19:
                v = CDispatch(144)
            elif self._Properties__count_3 == 20:
                v = CDispatch(146)
            elif self._Properties__count_3 == 21:
                v = CDispatch(150)
            self._Properties__count_3 += 1
            return v
        elif self.__id__ == 159:
            ret_value = None
            if not hasattr(self, '_Properties__count_4'):
                self._Properties__count_4 = 0
            if self._Properties__count_4 == 0:
                v = CDispatch(162)
            elif self._Properties__count_4 == 1:
                v = CDispatch(166)
            elif self._Properties__count_4 == 2:
                v = CDispatch(170)
            elif self._Properties__count_4 == 3:
                v = CDispatch(174)
            elif self._Properties__count_4 == 4:
                v = CDispatch(178)
            elif self._Properties__count_4 == 5:
                v = CDispatch(182)
            elif self._Properties__count_4 == 6:
                v = CDispatch(186)
            elif self._Properties__count_4 == 7:
                v = CDispatch(190)
            elif self._Properties__count_4 == 8:
                v = CDispatch(194)
            elif self._Properties__count_4 == 9:
                v = CDispatch(198)
            elif self._Properties__count_4 == 10:
                v = CDispatch(202)
            elif self._Properties__count_4 == 11:
                v = CDispatch(206)
            elif self._Properties__count_4 == 12:
                v = CDispatch(210)
            elif self._Properties__count_4 == 13:
                v = CDispatch(214)
            elif self._Properties__count_4 == 14:
                v = CDispatch(218)
            elif self._Properties__count_4 == 15:
                v = CDispatch(222)
            elif self._Properties__count_4 == 16:
                v = CDispatch(226)
            elif self._Properties__count_4 == 17:
                v = CDispatch(230)
            elif self._Properties__count_4 == 18:
                v = CDispatch(234)
            elif self._Properties__count_4 == 19:
                v = CDispatch(238)
            elif self._Properties__count_4 == 20:
                v = CDispatch(240)
            elif self._Properties__count_4 == 21:
                v = CDispatch(244)
            self._Properties__count_4 += 1
            return v
        elif self.__id__ == 254:
            ret_value = None
            if not hasattr(self, '_Properties__count_5'):
                self._Properties__count_5 = 0
            if self._Properties__count_5 == 0:
                v = CDispatch(257)
            elif self._Properties__count_5 == 1:
                v = CDispatch(261)
            elif self._Properties__count_5 == 2:
                v = CDispatch(265)
            elif self._Properties__count_5 == 3:
                v = CDispatch(269)
            elif self._Properties__count_5 == 4:
                v = CDispatch(273)
            elif self._Properties__count_5 == 5:
                v = CDispatch(277)
            elif self._Properties__count_5 == 6:
                v = CDispatch(281)
            elif self._Properties__count_5 == 7:
                v = CDispatch(285)
            elif self._Properties__count_5 == 8:
                v = CDispatch(289)
            elif self._Properties__count_5 == 9:
                v = CDispatch(293)
            elif self._Properties__count_5 == 10:
                v = CDispatch(297)
            elif self._Properties__count_5 == 11:
                v = CDispatch(301)
            elif self._Properties__count_5 == 12:
                v = CDispatch(305)
            elif self._Properties__count_5 == 13:
                v = CDispatch(309)
            elif self._Properties__count_5 == 14:
                v = CDispatch(313)
            elif self._Properties__count_5 == 15:
                v = CDispatch(317)
            elif self._Properties__count_5 == 16:
                v = CDispatch(321)
            elif self._Properties__count_5 == 17:
                v = CDispatch(325)
            elif self._Properties__count_5 == 18:
                v = CDispatch(329)
            elif self._Properties__count_5 == 19:
                v = CDispatch(333)
            elif self._Properties__count_5 == 20:
                v = CDispatch(335)
            elif self._Properties__count_5 == 21:
                v = CDispatch(339)
            self._Properties__count_5 += 1
            return v
        elif self.__id__ == 392:
            ret_value = None
            if not hasattr(self, '_Properties__count_6'):
                self._Properties__count_6 = 0
            if self._Properties__count_6 == 0:
                v = CDispatch(395)
            elif self._Properties__count_6 == 1:
                v = CDispatch(399)
            elif self._Properties__count_6 == 2:
                v = CDispatch(403)
            elif self._Properties__count_6 == 3:
                v = CDispatch(407)
            elif self._Properties__count_6 == 4:
                v = CDispatch(411)
            elif self._Properties__count_6 == 5:
                v = CDispatch(415)
            elif self._Properties__count_6 == 6:
                v = CDispatch(419)
            elif self._Properties__count_6 == 7:
                v = CDispatch(423)
            elif self._Properties__count_6 == 8:
                v = CDispatch(427)
            elif self._Properties__count_6 == 9:
                v = CDispatch(431)
            elif self._Properties__count_6 == 10:
                v = CDispatch(435)
            elif self._Properties__count_6 == 11:
                v = CDispatch(439)
            elif self._Properties__count_6 == 12:
                v = CDispatch(443)
            elif self._Properties__count_6 == 13:
                v = CDispatch(447)
            elif self._Properties__count_6 == 14:
                v = CDispatch(451)
            elif self._Properties__count_6 == 15:
                v = CDispatch(455)
            elif self._Properties__count_6 == 16:
                v = CDispatch(459)
            elif self._Properties__count_6 == 17:
                v = CDispatch(463)
            elif self._Properties__count_6 == 18:
                v = CDispatch(467)
            elif self._Properties__count_6 == 19:
                v = CDispatch(471)
            elif self._Properties__count_6 == 20:
                v = CDispatch(477)
            self._Properties__count_6 += 1
            return v
        elif self.__id__ == 394:
            ret_value = None
            if not hasattr(self, '_Properties__count_7'):
                self._Properties__count_7 = 0
            if self._Properties__count_7 == 0:
                v = CDispatch(397)
            elif self._Properties__count_7 == 1:
                v = CDispatch(401)
            elif self._Properties__count_7 == 2:
                v = CDispatch(405)
            elif self._Properties__count_7 == 3:
                v = CDispatch(409)
            elif self._Properties__count_7 == 4:
                v = CDispatch(413)
            elif self._Properties__count_7 == 5:
                v = CDispatch(417)
            elif self._Properties__count_7 == 6:
                v = CDispatch(421)
            elif self._Properties__count_7 == 7:
                v = CDispatch(425)
            elif self._Properties__count_7 == 8:
                v = CDispatch(429)
            elif self._Properties__count_7 == 9:
                v = CDispatch(433)
            elif self._Properties__count_7 == 10:
                v = CDispatch(437)
            elif self._Properties__count_7 == 11:
                v = CDispatch(441)
            elif self._Properties__count_7 == 12:
                v = CDispatch(445)
            elif self._Properties__count_7 == 13:
                v = CDispatch(449)
            elif self._Properties__count_7 == 14:
                v = CDispatch(453)
            elif self._Properties__count_7 == 15:
                v = CDispatch(457)
            elif self._Properties__count_7 == 16:
                v = CDispatch(461)
            elif self._Properties__count_7 == 17:
                v = CDispatch(465)
            elif self._Properties__count_7 == 18:
                v = CDispatch(469)
            elif self._Properties__count_7 == 19:
                v = CDispatch(473)
            elif self._Properties__count_7 == 20:
                v = CDispatch(475)
            elif self._Properties__count_7 == 21:
                v = CDispatch(479)
            self._Properties__count_7 += 1
            return v

    @Properties_.setter
    def Properties_(self, value):
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
    def RequestStateChange(self):
        if self.__id__ == 352:
            v = _wmi_method(353)
            return v
        elif self.__id__ == 515:
            v = _wmi_method(516)
            return v

    @RequestStateChange.setter
    def RequestStateChange(self, value):
        pass

    @property
    def Unregister(self):
        if self.__id__ == 548:
            v = _wmi_method(549)
            return v

    @Unregister.setter
    def Unregister(self, value):
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
        elif self.__id__ == 392:
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
        if self.__id__ == 367:
            v = ()
            v1 = CDispatch(368)
            v += (v1,)
            v1 = CDispatch(369)
            v += (v1,)
            return v

    @Devices.setter
    def Devices(self, value):
        pass

    @property
    def ElapsedTime(self):
        if self.__id__ == 33:
            return u'00000000000001.009611:000'
        elif self.__id__ == 360:
            return u'00000000000001.272011:000'

    @ElapsedTime.setter
    def ElapsedTime(self, value):
        pass

    @property
    def Connection(self):
        if self.__id__ == 499:
            v = ()
            v1 =\
 u'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_67a39e13-209c-4108-8bd\
8-54c0ea5832bb\\openstack_unit_test_vm_67a39e13-209c-4108-8bd8-54c0ea5832bb.vh\
d'
            v += (v1,)
            return v
        elif self.__id__ == 531:
            v = ()
            v1 =\
 u'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_67a39e13-209c-4108-8bd\
8-54c0ea5832bb\\openstack_unit_test_vm_67a39e13-209c-4108-8bd8-54c0ea5832bb.vh\
d'
            v += (v1,)
            return v

    @Connection.setter
    def Connection(self, value):
        pass

    @property
    def Delete(self):
        if self.__id__ == 542:
            v = _wmi_method(543)
            return v

    @Delete.setter
    def Delete(self, value):
        pass

    @property
    def IsPersistent(self):
        if self.__id__ == 548:
            return True

    @IsPersistent.setter
    def IsPersistent(self, value):
        pass

    @property
    def DestroyVirtualSystem(self):
        if self.__id__ == 513:
            v = _wmi_method(538)
            return v

    @DestroyVirtualSystem.setter
    def DestroyVirtualSystem(self, value):
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
        elif self.__id__ == 490:
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
        elif self.__id__ == 491:
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
        elif self.__id__ == 492:
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
        elif self.__id__ == 493:
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
        elif self.__id__ == 494:
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
        elif self.__id__ == 495:
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
        elif self.__id__ == 496:
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
        elif self.__id__ == 497:
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
        elif self.__id__ == 498:
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
        elif self.__id__ == 499:
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
        elif self.__id__ == 500:
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
        elif self.__id__ == 501:
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
        elif self.__id__ == 502:
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
        elif self.__id__ == 503:
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
        elif self.__id__ == 504:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_26'):
                self._ResourceSubType_count_26 = 0
            if self._ResourceSubType_count_26 == 0:
                v = u'Microsoft Physical Disk Drive'
            elif self._ResourceSubType_count_26 == 1:
                v = u'Microsoft Physical Disk Drive'
            elif self._ResourceSubType_count_26 == 2:
                v = u'Microsoft Physical Disk Drive'
            self._ResourceSubType_count_26 += 1
            return v
        elif self.__id__ == 505:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_27'):
                self._ResourceSubType_count_27 = 0
            if self._ResourceSubType_count_27 == 0:
                v = u'Microsoft Synthetic SCSI Controller'
            elif self._ResourceSubType_count_27 == 1:
                v = u'Microsoft Synthetic SCSI Controller'
            elif self._ResourceSubType_count_27 == 2:
                v = u'Microsoft Synthetic SCSI Controller'
            self._ResourceSubType_count_27 += 1
            return v
        elif self.__id__ == 522:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_28'):
                self._ResourceSubType_count_28 = 0
            if self._ResourceSubType_count_28 == 0:
                v = u'Microsoft Virtual Keyboard'
            elif self._ResourceSubType_count_28 == 1:
                v = u'Microsoft Virtual Keyboard'
            elif self._ResourceSubType_count_28 == 2:
                v = u'Microsoft Virtual Keyboard'
            self._ResourceSubType_count_28 += 1
            return v
        elif self.__id__ == 523:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_29'):
                self._ResourceSubType_count_29 = 0
            if self._ResourceSubType_count_29 == 0:
                v = u'Microsoft Virtual PS2 Mouse'
            elif self._ResourceSubType_count_29 == 1:
                v = u'Microsoft Virtual PS2 Mouse'
            elif self._ResourceSubType_count_29 == 2:
                v = u'Microsoft Virtual PS2 Mouse'
            self._ResourceSubType_count_29 += 1
            return v
        elif self.__id__ == 524:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_30'):
                self._ResourceSubType_count_30 = 0
            if self._ResourceSubType_count_30 == 0:
                v = u'Microsoft S3 Display Controller'
            elif self._ResourceSubType_count_30 == 1:
                v = u'Microsoft S3 Display Controller'
            elif self._ResourceSubType_count_30 == 2:
                v = u'Microsoft S3 Display Controller'
            self._ResourceSubType_count_30 += 1
            return v
        elif self.__id__ == 525:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_31'):
                self._ResourceSubType_count_31 = 0
            if self._ResourceSubType_count_31 == 0:
                v = u'Microsoft Synthetic Diskette Drive'
            elif self._ResourceSubType_count_31 == 1:
                v = u'Microsoft Synthetic Diskette Drive'
            elif self._ResourceSubType_count_31 == 2:
                v = u'Microsoft Synthetic Diskette Drive'
            self._ResourceSubType_count_31 += 1
            return v
        elif self.__id__ == 526:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_32'):
                self._ResourceSubType_count_32 = 0
            if self._ResourceSubType_count_32 == 0:
                v = None
            elif self._ResourceSubType_count_32 == 1:
                v = None
            elif self._ResourceSubType_count_32 == 2:
                v = None
            self._ResourceSubType_count_32 += 1
            return v
        elif self.__id__ == 527:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_33'):
                self._ResourceSubType_count_33 = 0
            if self._ResourceSubType_count_33 == 0:
                v = u'Microsoft Serial Controller'
            elif self._ResourceSubType_count_33 == 1:
                v = u'Microsoft Serial Controller'
            elif self._ResourceSubType_count_33 == 2:
                v = u'Microsoft Serial Controller'
            self._ResourceSubType_count_33 += 1
            return v
        elif self.__id__ == 528:
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
        elif self.__id__ == 529:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_35'):
                self._ResourceSubType_count_35 = 0
            if self._ResourceSubType_count_35 == 0:
                v = u'Microsoft Serial Port'
            elif self._ResourceSubType_count_35 == 1:
                v = u'Microsoft Serial Port'
            elif self._ResourceSubType_count_35 == 2:
                v = u'Microsoft Serial Port'
            self._ResourceSubType_count_35 += 1
            return v
        elif self.__id__ == 530:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_36'):
                self._ResourceSubType_count_36 = 0
            if self._ResourceSubType_count_36 == 0:
                v = u'Microsoft Synthetic Disk Drive'
            elif self._ResourceSubType_count_36 == 1:
                v = u'Microsoft Synthetic Disk Drive'
            elif self._ResourceSubType_count_36 == 2:
                v = u'Microsoft Synthetic Disk Drive'
            self._ResourceSubType_count_36 += 1
            return v
        elif self.__id__ == 531:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_37'):
                self._ResourceSubType_count_37 = 0
            if self._ResourceSubType_count_37 == 0:
                v = u'Microsoft Virtual Hard Disk'
            elif self._ResourceSubType_count_37 == 1:
                v = u'Microsoft Virtual Hard Disk'
            elif self._ResourceSubType_count_37 == 2:
                v = u'Microsoft Virtual Hard Disk'
            self._ResourceSubType_count_37 += 1
            return v
        elif self.__id__ == 532:
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
        elif self.__id__ == 533:
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
        elif self.__id__ == 534:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_40'):
                self._ResourceSubType_count_40 = 0
            if self._ResourceSubType_count_40 == 0:
                v = u'Microsoft Synthetic Mouse'
            elif self._ResourceSubType_count_40 == 1:
                v = u'Microsoft Synthetic Mouse'
            elif self._ResourceSubType_count_40 == 2:
                v = u'Microsoft Synthetic Mouse'
            self._ResourceSubType_count_40 += 1
            return v
        elif self.__id__ == 535:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_41'):
                self._ResourceSubType_count_41 = 0
            if self._ResourceSubType_count_41 == 0:
                v = u'Microsoft Synthetic Display Controller'
            elif self._ResourceSubType_count_41 == 1:
                v = u'Microsoft Synthetic Display Controller'
            elif self._ResourceSubType_count_41 == 2:
                v = u'Microsoft Synthetic Display Controller'
            self._ResourceSubType_count_41 += 1
            return v
        elif self.__id__ == 536:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_42'):
                self._ResourceSubType_count_42 = 0
            if self._ResourceSubType_count_42 == 0:
                v = u'Microsoft Physical Disk Drive'
            elif self._ResourceSubType_count_42 == 1:
                v = u'Microsoft Physical Disk Drive'
            elif self._ResourceSubType_count_42 == 2:
                v = u'Microsoft Physical Disk Drive'
            self._ResourceSubType_count_42 += 1
            return v
        elif self.__id__ == 537:
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
        elif self.__id__ == 376:
            return u'Microsoft Virtual Keyboard'
        elif self.__id__ == 377:
            return u'Microsoft Virtual PS2 Mouse'
        elif self.__id__ == 378:
            return u'Microsoft S3 Display Controller'
        elif self.__id__ == 379:
            return u'Microsoft Synthetic Diskette Drive'
        elif self.__id__ == 380:
            return None
        elif self.__id__ == 381:
            return u'Microsoft Serial Controller'
        elif self.__id__ == 382:
            return u'Microsoft Serial Port'
        elif self.__id__ == 383:
            return u'Microsoft Serial Port'
        elif self.__id__ == 384:
            return u'Microsoft Synthetic Disk Drive'
        elif self.__id__ == 385:
            return u'Microsoft Virtual Hard Disk'
        elif self.__id__ == 386:
            return u'Microsoft Emulated IDE Controller'
        elif self.__id__ == 387:
            return u'Microsoft Emulated IDE Controller'
        elif self.__id__ == 388:
            return u'Microsoft Synthetic Mouse'
        elif self.__id__ == 389:
            return u'Microsoft Synthetic Display Controller'
        elif self.__id__ == 390:
            return u'Microsoft Synthetic SCSI Controller'

    @ResourceSubType.setter
    def ResourceSubType(self, value):
        pass

    @property
    def DefineVirtualSystem(self):
        if self.__id__ == 35:
            v = _wmi_method(38)
            return v

    @DefineVirtualSystem.setter
    def DefineVirtualSystem(self, value):
        pass

    @property
    def SettingType(self):
        if self.__id__ == 41:
            return 3

    @SettingType.setter
    def SettingType(self, value):
        pass

    def associators(self, wmi_association_class='', wmi_result_class=''):
        if self.__id__ == 50 and wmi_result_class ==\
 'MSVM_ResourceAllocationSettingData':
            v = []
            v1 = _wmi_object(51)
            v.append(v1)
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
            return v
        elif self.__id__ == 49 and wmi_result_class ==\
 'Msvm_VirtualSystemSettingData':
            v = []
            v1 = _wmi_object(50)
            v.append(v1)
            return v
        elif self.__id__ == 41 and wmi_result_class ==\
 'Msvm_MemorySettingData':
            v = []
            v1 = _wmi_object(42)
            v.append(v1)
            return v
        elif self.__id__ == 41 and wmi_result_class ==\
 'Msvm_ProcessorSettingData':
            v = []
            v1 = _wmi_object(45)
            v.append(v1)
            return v
        elif self.__id__ == 40 and wmi_result_class ==\
 'Msvm_VirtualSystemSettingData':
            v = []
            v1 = _wmi_object(41)
            v.append(v1)
            return v
        elif self.__id__ == 489 and wmi_result_class ==\
 'MSVM_ResourceAllocationSettingData':
            v = []
            v1 = _wmi_object(490)
            v.append(v1)
            v1 = _wmi_object(491)
            v.append(v1)
            v1 = _wmi_object(492)
            v.append(v1)
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
            v1 = _wmi_object(498)
            v.append(v1)
            v1 = _wmi_object(499)
            v.append(v1)
            v1 = _wmi_object(500)
            v.append(v1)
            v1 = _wmi_object(501)
            v.append(v1)
            v1 = _wmi_object(502)
            v.append(v1)
            v1 = _wmi_object(503)
            v.append(v1)
            v1 = _wmi_object(504)
            v.append(v1)
            v1 = _wmi_object(505)
            v.append(v1)
            return v
        elif self.__id__ == 488 and wmi_result_class ==\
 'Msvm_VirtualSystemSettingData':
            v = []
            v1 = _wmi_object(489)
            v.append(v1)
            return v
        elif self.__id__ == 521 and wmi_result_class ==\
 'MSVM_ResourceAllocationSettingData':
            v = []
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
            v1 = _wmi_object(530)
            v.append(v1)
            v1 = _wmi_object(531)
            v.append(v1)
            v1 = _wmi_object(532)
            v.append(v1)
            v1 = _wmi_object(533)
            v.append(v1)
            v1 = _wmi_object(534)
            v.append(v1)
            v1 = _wmi_object(535)
            v.append(v1)
            v1 = _wmi_object(536)
            v.append(v1)
            v1 = _wmi_object(537)
            v.append(v1)
            return v
        elif self.__id__ == 520 and wmi_result_class ==\
 'Msvm_VirtualSystemSettingData':
            v = []
            v1 = _wmi_object(521)
            v.append(v1)
            return v
        elif self.__id__ == 375 and wmi_result_class ==\
 'MSVM_ResourceAllocationSettingData':
            v = []
            v1 = _wmi_object(376)
            v.append(v1)
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
            return v
        elif self.__id__ == 374 and wmi_result_class ==\
 'Msvm_VirtualSystemSettingData':
            v = []
            v1 = _wmi_object(375)
            v.append(v1)
            return v

    def GetText_(self, iObjectTextFormat='<PyOleMissing object at\
 0x03237588>', iFlags=0, objWbemNamedValueSet=None):
        if self.__id__ == 42 and iObjectTextFormat == 1:
            return u'<INSTANCE CLASSNAME="Msvm_MemorySettingData"><PROPERTY\
 NAME="__PATH" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>\\\\HV12OSDEMO1\\root\\virtualization:Msvm_MemorySetting\
Data.InstanceID="Microsoft:8F9341AA-8208-4B0D-9E5B-9D70879E39EC\\\\4764334d-e0\
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
 TYPE="string"><VALUE>Msvm_MemorySettingData.InstanceID="Microsoft:8F9341AA-82\
08-4B0D-9E5B-9D70879E39EC\\\\4764334d-e001-4176-82ee-5594ec9b530e"</VALUE></PR\
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
 TYPE="string"><VALUE>Microsoft:8F9341AA-8208-4B0D-9E5B-9D70879E39EC\\4764334d\
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
ingData.InstanceID="Microsoft:8F9341AA-8208-4B0D-9E5B-9D70879E39EC\\\\b637f346\
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
 TYPE="string"><VALUE>Msvm_ProcessorSettingData.InstanceID="Microsoft:8F9341AA\
-8208-4B0D-9E5B-9D70879E39EC\\\\b637f346-6a0e-4dec-af52-bd70cb80a21d\\\\0"</VA\
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
 TYPE="string"><VALUE>Microsoft:8F9341AA-8208-4B0D-9E5B-9D70879E39EC\\b637f346\
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
 TYPE="string"><VALUE>openstack_unit_test_vm_67a39e13-209c-4108-8bd8-54c0ea583\
2bb</VALUE></PROPERTY><PROPERTY NAME="ExternalDataRoot"\
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
ationSettingData.InstanceID="Microsoft:8F9341AA-8208-4B0D-9E5B-9D70879E39EC\
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
 TYPE="string"><VALUE.ARRAY><VALUE>4a94bb43-4fbd-40ab-b174-68f48097e0db</VALUE\
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
t_test_vm_67a39e13-209c-4108-8bd8-54c0ea5832bb\\openstack_unit_test_vm_67a39e1\
3-209c-4108-8bd8-54c0ea5832bb.vhd</VALUE></VALUE.ARRAY></PROPERTY.ARRAY><PROPE\
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
ationSettingData.InstanceID="Microsoft:8F9341AA-8208-4B0D-9E5B-9D70879E39EC\
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
 TYPE="string"><VALUE.ARRAY><VALUE>179f705a-d9dd-490f-b94d-81fc0cd54788</VALUE\
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
 TYPE="string"><VALUE.ARRAY><VALUE>{5dc852bd-4fc9-488e-9907-7c1f51940c4c}</VAL\
UE></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>'
        elif self.__id__ == 394 and iObjectTextFormat == 1:
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
ationSettingData.InstanceID="Microsoft:8F9341AA-8208-4B0D-9E5B-9D70879E39EC\
\\\\9BE8AEC0-673A-4A38-9B7B-38221FD78B44\\\\0"</VALUE></PROPERTY><PROPERTY\
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
 TYPE="string"><VALUE.ARRAY><VALUE>96a27d1d-74ad-4054-9450-1bb9887d15ea</VALUE\
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
        if len(args) == 0 and self.__id__ == 549:
            v = ()
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 0 and self.__id__ == 550:
            v = ()
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 0 and self.__id__ == 365 and\
 kwargs.get('IsPersistent') is True and kwargs.get('NodeAddress') ==\
 'iqn.2010-10.org.openstack:volume-ccb39627-34fa-4f47-968b-6580d9d7ee2b':
            v = ()
            v1 = CDispatch(366)
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 0 and self.__id__ == 362 and\
 kwargs.get('TargetPortalAddress') == 'testtargetportal' and\
 kwargs.get('TargetPortalPortNumber') == '3260':
            v = ()
            v1 = CDispatch(363)
            v += (v1,)
            v1 = None
            v += (v1,)
            return v
        elif len(args) == 0 and self.__id__ == 543:
            v = ()
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 0 and self.__id__ == 24 and kwargs.get('Path') ==\
 'C:\\Hyper-V\\test\\instances\\openstack_unit_test_vm_67a39e13-209c-4108-8bd8\
-54c0ea5832bb\\openstack_unit_test_vm_67a39e13-209c-4108-8bd8-54c0ea5832bb.vhd\
' and kwargs.get('ParentPath') == 'C:\\Hyper-V\\test\\instances\\_base\\1.vhd':
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_StorageJob.InstanceID="C237EDD6-\
75BC-48B6-85C8-7979AF83AE67"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v
        elif len(args) == 1 and self.__id__ == 353 and args[0] == 2:
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ConcreteJob.InstanceID="4DA7F6B3\
-B17B-4568-ADEB-86104A365C3B"'
            v += (v1,)
            v1 = 4096
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
 TYPE="string"><VALUE>openstack_unit_test_vm_67a39e13-209c-4108-8bd8-54c0ea583\
2bb</VALUE></PROPERTY><PROPERTY NAME="ExternalDataRoot"\
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
="Msvm_ComputerSystem",Name="8F9341AA-8208-4B0D-9E5B-9D70879E39EC"'
            v += (v1,)
            v1 = None
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 2 and self.__id__ == 43 and args[0] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="8F9341AA-8208-4B0D-9E5B-9D70879E39EC"' and\
 str(args[1]) == '[u\'<INSTANCE CLASSNAME="Msvm_MemorySettingData"><PROPERTY\
 NAME="__PATH" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>\\\\\\\\HV12OSDEMO1\\\\root\\\\virtualization:Msvm_Memor\
ySettingData.InstanceID="Microsoft:8F9341AA-8208-4B0D-9E5B-9D70879E39EC\
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
 TYPE="string"><VALUE>Msvm_MemorySettingData.InstanceID="Microsoft:8F9341AA-82\
08-4B0D-9E5B-9D70879E39EC\\\\\\\\4764334d-e001-4176-82ee-5594ec9b530e"</VALUE>\
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
 TYPE="string"><VALUE>Microsoft:8F9341AA-8208-4B0D-9E5B-9D70879E39EC\\\\476433\
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
="Msvm_ComputerSystem",Name="8F9341AA-8208-4B0D-9E5B-9D70879E39EC"' and\
 str(args[1]) == '[u\'<INSTANCE\
 CLASSNAME="Msvm_ProcessorSettingData"><PROPERTY NAME="__PATH"\
 CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>\\\\\\\\HV12OSDEMO1\\\\root\\\\virtualization:Msvm_Proce\
ssorSettingData.InstanceID="Microsoft:8F9341AA-8208-4B0D-9E5B-9D70879E39EC\
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
 TYPE="string"><VALUE>Msvm_ProcessorSettingData.InstanceID="Microsoft:8F9341AA\
-8208-4B0D-9E5B-9D70879E39EC\\\\\\\\b637f346-6a0e-4dec-af52-bd70cb80a21d\
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
 TYPE="string"><VALUE>Microsoft:8F9341AA-8208-4B0D-9E5B-9D70879E39EC\\\\b637f3\
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
rceAllocationSettingData.InstanceID="Microsoft:8F9341AA-8208-4B0D-9E5B-9D70879\
E39EC\\\\\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\\\\\0"</VALUE></PROPERTY>\
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
 TYPE="string"><VALUE.ARRAY><VALUE>4a94bb43-4fbd-40ab-b174-68f48097e0db</VALUE\
></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="8F9341AA-8208-4B0D-9E5B-9D70879E39EC"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:8F9341AA-8208-4B0D-9E5B-9D70879E39EC\\\\83F8638B-8DCA-4152\
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
tack_unit_test_vm_67a39e13-209c-4108-8bd8-54c0ea5832bb\\\\openstack_unit_test_\
vm_67a39e13-209c-4108-8bd8-54c0ea5832bb.vhd</VALUE></VALUE.ARRAY></PROPERTY.AR\
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
rceAllocationSettingData.InstanceID="Microsoft:8F9341AA-8208-4B0D-9E5B-9D70879\
E39EC\\\\\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\\\\\0\\\\\\\\0\\\\\\\\D"<\
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
 TYPE="string"><VALUE.ARRAY><VALUE>179f705a-d9dd-490f-b94d-81fc0cd54788</VALUE\
></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="8F9341AA-8208-4B0D-9E5B-9D70879E39EC"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:8F9341AA-8208-4B0D-9E5B-9D70879E39EC\\\\83F8638B-8DCA-4152\
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
 TYPE="string"><VALUE.ARRAY><VALUE>{5dc852bd-4fc9-488e-9907-7c1f51940c4c}</VAL\
UE></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="8F9341AA-8208-4B0D-9E5B-9D70879E39EC"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:8F9341AA-8208-4B0D-9E5B-9D70879E39EC\\\\9BE8AEC0-673A-4A38\
-9B7B-38221FD78B44\\\\0"'
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
 TYPE="string"><VALUE.ARRAY><VALUE>{a9196905-c530-4bb5-bf89-21584ec59c67}</VAL\
UE></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="8F9341AA-8208-4B0D-9E5B-9D70879E39EC"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_SyntheticEthernetPortSettingData\
.InstanceID="Microsoft:8F9341AA-8208-4B0D-9E5B-9D70879E39EC\\\\F0B1D437-2012-4\
9BA-9C3F-79690051B923"'
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
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_StorageJob.InstanceID="FFDC5EB3-\
3577-487D-8694-BA37BEFDE5AE"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v
        elif len(args) == 1 and self.__id__ == 516 and args[0] == 3:
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ConcreteJob.InstanceID="2F925A6E\
-F7A2-4906-B45F-9BE530898593"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v
        elif len(args) == 1 and self.__id__ == 538 and args[0] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="8F9341AA-8208-4B0D-9E5B-9D70879E39EC"':
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ConcreteJob.InstanceID="1C3D7F8E\
-5670-4015-9E32-FFD7614A4784"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v
        elif len(args) == 2 and self.__id__ == 485 and str(args[0]) ==\
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
rceAllocationSettingData.InstanceID="Microsoft:8F9341AA-8208-4B0D-9E5B-9D70879\
E39EC\\\\\\\\9BE8AEC0-673A-4A38-9B7B-38221FD78B44\\\\\\\\0"</VALUE></PROPERTY>\
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
 TYPE="string"><VALUE.ARRAY><VALUE>96a27d1d-74ad-4054-9450-1bb9887d15ea</VALUE\
></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="8F9341AA-8208-4B0D-9E5B-9D70879E39EC"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:8F9341AA-8208-4B0D-9E5B-9D70879E39EC\\\\9BE8AEC0-673A-4A38\
-9B7B-38221FD78B44\\\\0\\\\0\\\\D"'
            v1.append(v2)
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
        if self.__id__ == 368:
            return u'ROOT\\ISCSIPRT\\0000_0'
        elif self.__id__ == 369:
            return u'ROOT\\ISCSIPRT\\0000_0'

    @InitiatorName.setter
    def InitiatorName(self, value):
        pass

    @property
    def ScsiLun(self):
        if self.__id__ == 368:
            ret_value = None
            if not hasattr(self, '_ScsiLun_count_0'):
                self._ScsiLun_count_0 = 0
            if self._ScsiLun_count_0 == 0:
                v = 0
            elif self._ScsiLun_count_0 == 1:
                v = 0
            self._ScsiLun_count_0 += 1
            return v
        elif self.__id__ == 369:
            ret_value = None
            if not hasattr(self, '_ScsiLun_count_1'):
                self._ScsiLun_count_1 = 0
            if self._ScsiLun_count_1 == 0:
                v = 1
            elif self._ScsiLun_count_1 == 1:
                v = 1
            self._ScsiLun_count_1 += 1
            return v

    @ScsiLun.setter
    def ScsiLun(self, value):
        pass

    @property
    def PartitionNumber(self):
        if self.__id__ == 368:
            return -1
        elif self.__id__ == 369:
            return 0

    @PartitionNumber.setter
    def PartitionNumber(self, value):
        pass

    @property
    def ScsiTargetId(self):
        if self.__id__ == 368:
            return 0
        elif self.__id__ == 369:
            return 0

    @ScsiTargetId.setter
    def ScsiTargetId(self, value):
        pass

    @property
    def DeviceNumber(self):
        if self.__id__ == 368:
            return -1
        elif self.__id__ == 369:
            ret_value = None
            if not hasattr(self, '_DeviceNumber_count_1'):
                self._DeviceNumber_count_1 = 0
            if self._DeviceNumber_count_1 == 0:
                v = 1
            elif self._DeviceNumber_count_1 == 1:
                v = 1
            self._DeviceNumber_count_1 += 1
            return v

    @DeviceNumber.setter
    def DeviceNumber(self, value):
        pass

    @property
    def DeviceInterfaceGuid(self):
        if self.__id__ == 368:
            return u'0-0-0-00000000'
        elif self.__id__ == 369:
            return u'53f56307-b6bf-11d0-94f20a0c91efb8b'

    @DeviceInterfaceGuid.setter
    def DeviceInterfaceGuid(self, value):
        pass

    @property
    def DeviceType(self):
        if self.__id__ == 368:
            return 34
        elif self.__id__ == 369:
            return 7

    @DeviceType.setter
    def DeviceType(self, value):
        pass

    @property
    def LegacyName(self):
        if self.__id__ == 368:
            return u''
        elif self.__id__ == 369:
            return u'\\\\.\\PhysicalDrive1'

    @LegacyName.setter
    def LegacyName(self, value):
        pass

    @property
    def ScsiPathId(self):
        if self.__id__ == 368:
            return 0
        elif self.__id__ == 369:
            return 0

    @ScsiPathId.setter
    def ScsiPathId(self, value):
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
        elif self.__id__ == 396:
            return\
 u'Microsoft:Definition\\353B3BE8-310C-4CF4-839E-4E1B14616136\\Default'
        elif self.__id__ == 400:
            return u'Microsoft Physical Disk Drive'
        elif self.__id__ == 404:
            return None
        elif self.__id__ == 408:
            return u'Hard Drive'
        elif self.__id__ == 412:
            return u'Settings for the Microsoft Physical Hard Drive.'
        elif self.__id__ == 416:
            return None
        elif self.__id__ == 420:
            return u'1'
        elif self.__id__ == 424:
            return True
        elif self.__id__ == 428:
            return True
        elif self.__id__ == 432:
            return u'Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\\Root'
        elif self.__id__ == 436:
            return u'1'
        elif self.__id__ == 440:
            return u'Hard Drives'
        elif self.__id__ == 444:
            return None
        elif self.__id__ == 448:
            return None
        elif self.__id__ == 452:
            return None
        elif self.__id__ == 456:
            return u'Hard Drive'
        elif self.__id__ == 460:
            return None
        elif self.__id__ == 464:
            return u'1'
        elif self.__id__ == 468:
            return 22
        elif self.__id__ == 472:
            return 0
        elif self.__id__ == 478:
            return None

    @Value.setter
    def Value(self, value):
        pass

    @property
    def TargetName(self):
        if self.__id__ == 368:
            return\
 u'iqn.2010-10.org.openstack:volume-ccb39627-34fa-4f47-968b-6580d9d7ee2b'
        elif self.__id__ == 369:
            return\
 u'iqn.2010-10.org.openstack:volume-ccb39627-34fa-4f47-968b-6580d9d7ee2b'

    @TargetName.setter
    def TargetName(self, value):
        pass

    @property
    def DeviceInterfaceName(self):
        if self.__id__ == 368:
            return u''
        elif self.__id__ == 369:
            return\
 u'\\\\?\\scsi#disk&ven_iet&prod_virtual-disk#1&1c121344&0&000001#{53f56307-b6\
bf-11d0-94f2-00a0c91efb8b}'

    @DeviceInterfaceName.setter
    def DeviceInterfaceName(self, value):
        pass

    @property
    def ScsiPortNumber(self):
        if self.__id__ == 368:
            return 3
        elif self.__id__ == 369:
            return 3

    @ScsiPortNumber.setter
    def ScsiPortNumber(self, value):
        pass

    def __call__(self, *args):
        if len(args) == 0 and self.__id__ == 152:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:8F9341AA-8208-4B0D-9E5B-9D70879E39EC\\\\83F8638B-8DCA-4152\
-9EDA-2CA8B33039B4\\\\0"'
        elif len(args) == 0 and self.__id__ == 156:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="8F9341AA-8208-4B0D-9E5B-9D70879E39EC"'
        elif len(args) == 0 and self.__id__ == 249:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="8F9341AA-8208-4B0D-9E5B-9D70879E39EC"'
        elif len(args) == 0 and self.__id__ == 344:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="8F9341AA-8208-4B0D-9E5B-9D70879E39EC"'
        elif len(args) == 0 and self.__id__ == 44:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="8F9341AA-8208-4B0D-9E5B-9D70879E39EC"'
        elif len(args) == 0 and self.__id__ == 47:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="8F9341AA-8208-4B0D-9E5B-9D70879E39EC"'
        elif len(args) == 0 and self.__id__ == 350:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="8F9341AA-8208-4B0D-9E5B-9D70879E39EC"'
        elif len(args) == 0 and self.__id__ == 539:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="8F9341AA-8208-4B0D-9E5B-9D70879E39EC"'
        elif len(args) == 0 and self.__id__ == 482:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_DiskDrive.CreationClassName="Msv\
m_DiskDrive",DeviceID="Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\\\\1",Sy\
stemCreationClassName="Msvm_ComputerSystem",SystemName="HV12OSDEMO1"'
        elif len(args) == 0 and self.__id__ == 391:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:8F9341AA-8208-4B0D-9E5B-9D70879E39EC\\\\9BE8AEC0-673A-4A38\
-9B7B-38221FD78B44\\\\0"'
        elif len(args) == 0 and self.__id__ == 481:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:8F9341AA-8208-4B0D-9E5B-9D70879E39EC\\\\9BE8AEC0-673A-4A38\
-9B7B-38221FD78B44\\\\0"'
        elif len(args) == 0 and self.__id__ == 486:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="8F9341AA-8208-4B0D-9E5B-9D70879E39EC"'

    def Item(self, strName='<PyOleMissing object at 0x03237588>', iFlags=0):
        if self.__id__ == 66 and strName == u'InstanceID':
            v = CDispatch(67)
            return v
        elif self.__id__ == 70 and strName == u'ResourceSubType':
            v = CDispatch(71)
            return v
        elif self.__id__ == 74 and strName == u'HostResource':
            v = CDispatch(75)
            return v
        elif self.__id__ == 78 and strName == u'ElementName':
            v = CDispatch(79)
            return v
        elif self.__id__ == 82 and strName == u'Description':
            v = CDispatch(83)
            return v
        elif self.__id__ == 86 and strName == u'Parent':
            v = CDispatch(87)
            return v
        elif self.__id__ == 90 and strName == u'VirtualQuantity':
            v = CDispatch(91)
            return v
        elif self.__id__ == 94 and strName == u'AutomaticDeallocation':
            v = CDispatch(95)
            return v
        elif self.__id__ == 98 and strName == u'AutomaticAllocation':
            v = CDispatch(99)
            return v
        elif self.__id__ == 102 and strName == u'PoolID':
            v = CDispatch(103)
            return v
        elif self.__id__ == 106 and strName == u'Reservation':
            v = CDispatch(107)
            return v
        elif self.__id__ == 110 and strName == u'AllocationUnits':
            v = CDispatch(111)
            return v
        elif self.__id__ == 114 and strName == u'MappingBehavior':
            v = CDispatch(115)
            return v
        elif self.__id__ == 118 and strName == u'Address':
            v = CDispatch(119)
            return v
        elif self.__id__ == 122 and strName == u'OtherResourceType':
            v = CDispatch(123)
            return v
        elif self.__id__ == 126 and strName == u'Caption':
            v = CDispatch(127)
            return v
        elif self.__id__ == 130 and strName == u'ConsumerVisibility':
            v = CDispatch(131)
            return v
        elif self.__id__ == 134 and strName == u'Limit':
            v = CDispatch(135)
            return v
        elif self.__id__ == 138 and strName == u'ResourceType':
            v = CDispatch(139)
            return v
        elif self.__id__ == 142 and strName == u'Weight':
            v = CDispatch(143)
            return v
        elif self.__id__ == 148 and strName == u'Connection':
            v = CDispatch(149)
            return v
        elif self.__id__ == 160 and strName == u'InstanceID':
            v = CDispatch(161)
            return v
        elif self.__id__ == 164 and strName == u'ResourceSubType':
            v = CDispatch(165)
            return v
        elif self.__id__ == 168 and strName == u'HostResource':
            v = CDispatch(169)
            return v
        elif self.__id__ == 172 and strName == u'ElementName':
            v = CDispatch(173)
            return v
        elif self.__id__ == 176 and strName == u'Description':
            v = CDispatch(177)
            return v
        elif self.__id__ == 180 and strName == u'Parent':
            v = CDispatch(181)
            return v
        elif self.__id__ == 184 and strName == u'VirtualQuantity':
            v = CDispatch(185)
            return v
        elif self.__id__ == 188 and strName == u'AutomaticDeallocation':
            v = CDispatch(189)
            return v
        elif self.__id__ == 192 and strName == u'AutomaticAllocation':
            v = CDispatch(193)
            return v
        elif self.__id__ == 196 and strName == u'PoolID':
            v = CDispatch(197)
            return v
        elif self.__id__ == 200 and strName == u'Reservation':
            v = CDispatch(201)
            return v
        elif self.__id__ == 204 and strName == u'AllocationUnits':
            v = CDispatch(205)
            return v
        elif self.__id__ == 208 and strName == u'MappingBehavior':
            v = CDispatch(209)
            return v
        elif self.__id__ == 212 and strName == u'Address':
            v = CDispatch(213)
            return v
        elif self.__id__ == 216 and strName == u'OtherResourceType':
            v = CDispatch(217)
            return v
        elif self.__id__ == 220 and strName == u'Caption':
            v = CDispatch(221)
            return v
        elif self.__id__ == 224 and strName == u'ConsumerVisibility':
            v = CDispatch(225)
            return v
        elif self.__id__ == 228 and strName == u'Limit':
            v = CDispatch(229)
            return v
        elif self.__id__ == 232 and strName == u'ResourceType':
            v = CDispatch(233)
            return v
        elif self.__id__ == 236 and strName == u'Weight':
            v = CDispatch(237)
            return v
        elif self.__id__ == 242 and strName == u'Connection':
            v = CDispatch(243)
            return v
        elif self.__id__ == 255 and strName == u'InstanceID':
            v = CDispatch(256)
            return v
        elif self.__id__ == 259 and strName == u'ResourceSubType':
            v = CDispatch(260)
            return v
        elif self.__id__ == 263 and strName == u'HostResource':
            v = CDispatch(264)
            return v
        elif self.__id__ == 267 and strName == u'ElementName':
            v = CDispatch(268)
            return v
        elif self.__id__ == 271 and strName == u'Description':
            v = CDispatch(272)
            return v
        elif self.__id__ == 275 and strName == u'Parent':
            v = CDispatch(276)
            return v
        elif self.__id__ == 279 and strName == u'VirtualQuantity':
            v = CDispatch(280)
            return v
        elif self.__id__ == 283 and strName == u'AutomaticDeallocation':
            v = CDispatch(284)
            return v
        elif self.__id__ == 287 and strName == u'AutomaticAllocation':
            v = CDispatch(288)
            return v
        elif self.__id__ == 291 and strName == u'PoolID':
            v = CDispatch(292)
            return v
        elif self.__id__ == 295 and strName == u'Reservation':
            v = CDispatch(296)
            return v
        elif self.__id__ == 299 and strName == u'AllocationUnits':
            v = CDispatch(300)
            return v
        elif self.__id__ == 303 and strName == u'MappingBehavior':
            v = CDispatch(304)
            return v
        elif self.__id__ == 307 and strName == u'Address':
            v = CDispatch(308)
            return v
        elif self.__id__ == 311 and strName == u'OtherResourceType':
            v = CDispatch(312)
            return v
        elif self.__id__ == 315 and strName == u'Caption':
            v = CDispatch(316)
            return v
        elif self.__id__ == 319 and strName == u'ConsumerVisibility':
            v = CDispatch(320)
            return v
        elif self.__id__ == 323 and strName == u'Limit':
            v = CDispatch(324)
            return v
        elif self.__id__ == 327 and strName == u'ResourceType':
            v = CDispatch(328)
            return v
        elif self.__id__ == 331 and strName == u'Weight':
            v = CDispatch(332)
            return v
        elif self.__id__ == 337 and strName == u'Connection':
            v = CDispatch(338)
            return v
        elif self.__id__ == 68 and strName == u'InstanceID':
            v = CDispatch(69)
            return v
        elif self.__id__ == 72 and strName == u'ResourceSubType':
            v = CDispatch(73)
            return v
        elif self.__id__ == 76 and strName == u'HostResource':
            v = CDispatch(77)
            return v
        elif self.__id__ == 80 and strName == u'ElementName':
            v = CDispatch(81)
            return v
        elif self.__id__ == 84 and strName == u'Description':
            v = CDispatch(85)
            return v
        elif self.__id__ == 88 and strName == u'Parent':
            v = CDispatch(89)
            return v
        elif self.__id__ == 92 and strName == u'VirtualQuantity':
            v = CDispatch(93)
            return v
        elif self.__id__ == 96 and strName == u'AutomaticDeallocation':
            v = CDispatch(97)
            return v
        elif self.__id__ == 100 and strName == u'AutomaticAllocation':
            v = CDispatch(101)
            return v
        elif self.__id__ == 104 and strName == u'PoolID':
            v = CDispatch(105)
            return v
        elif self.__id__ == 108 and strName == u'Reservation':
            v = CDispatch(109)
            return v
        elif self.__id__ == 112 and strName == u'AllocationUnits':
            v = CDispatch(113)
            return v
        elif self.__id__ == 116 and strName == u'MappingBehavior':
            v = CDispatch(117)
            return v
        elif self.__id__ == 120 and strName == u'Address':
            v = CDispatch(121)
            return v
        elif self.__id__ == 124 and strName == u'OtherResourceType':
            v = CDispatch(125)
            return v
        elif self.__id__ == 128 and strName == u'Caption':
            v = CDispatch(129)
            return v
        elif self.__id__ == 132 and strName == u'ConsumerVisibility':
            v = CDispatch(133)
            return v
        elif self.__id__ == 136 and strName == u'Limit':
            v = CDispatch(137)
            return v
        elif self.__id__ == 140 and strName == u'ResourceType':
            v = CDispatch(141)
            return v
        elif self.__id__ == 144 and strName == u'Weight':
            v = CDispatch(145)
            return v
        elif self.__id__ == 146 and strName == u'VirtualSystemIdentifiers':
            v = CDispatch(147)
            return v
        elif self.__id__ == 150 and strName == u'Connection':
            v = CDispatch(151)
            return v
        elif self.__id__ == 162 and strName == u'InstanceID':
            v = CDispatch(163)
            return v
        elif self.__id__ == 166 and strName == u'ResourceSubType':
            v = CDispatch(167)
            return v
        elif self.__id__ == 170 and strName == u'HostResource':
            v = CDispatch(171)
            return v
        elif self.__id__ == 174 and strName == u'ElementName':
            v = CDispatch(175)
            return v
        elif self.__id__ == 178 and strName == u'Description':
            v = CDispatch(179)
            return v
        elif self.__id__ == 182 and strName == u'Parent':
            v = CDispatch(183)
            return v
        elif self.__id__ == 186 and strName == u'VirtualQuantity':
            v = CDispatch(187)
            return v
        elif self.__id__ == 190 and strName == u'AutomaticDeallocation':
            v = CDispatch(191)
            return v
        elif self.__id__ == 194 and strName == u'AutomaticAllocation':
            v = CDispatch(195)
            return v
        elif self.__id__ == 198 and strName == u'PoolID':
            v = CDispatch(199)
            return v
        elif self.__id__ == 202 and strName == u'Reservation':
            v = CDispatch(203)
            return v
        elif self.__id__ == 206 and strName == u'AllocationUnits':
            v = CDispatch(207)
            return v
        elif self.__id__ == 210 and strName == u'MappingBehavior':
            v = CDispatch(211)
            return v
        elif self.__id__ == 214 and strName == u'Address':
            v = CDispatch(215)
            return v
        elif self.__id__ == 218 and strName == u'OtherResourceType':
            v = CDispatch(219)
            return v
        elif self.__id__ == 222 and strName == u'Caption':
            v = CDispatch(223)
            return v
        elif self.__id__ == 226 and strName == u'ConsumerVisibility':
            v = CDispatch(227)
            return v
        elif self.__id__ == 230 and strName == u'Limit':
            v = CDispatch(231)
            return v
        elif self.__id__ == 234 and strName == u'ResourceType':
            v = CDispatch(235)
            return v
        elif self.__id__ == 238 and strName == u'Weight':
            v = CDispatch(239)
            return v
        elif self.__id__ == 240 and strName == u'VirtualSystemIdentifiers':
            v = CDispatch(241)
            return v
        elif self.__id__ == 244 and strName == u'Connection':
            v = CDispatch(245)
            return v
        elif self.__id__ == 257 and strName == u'InstanceID':
            v = CDispatch(258)
            return v
        elif self.__id__ == 261 and strName == u'ResourceSubType':
            v = CDispatch(262)
            return v
        elif self.__id__ == 265 and strName == u'HostResource':
            v = CDispatch(266)
            return v
        elif self.__id__ == 269 and strName == u'ElementName':
            v = CDispatch(270)
            return v
        elif self.__id__ == 273 and strName == u'Description':
            v = CDispatch(274)
            return v
        elif self.__id__ == 277 and strName == u'Parent':
            v = CDispatch(278)
            return v
        elif self.__id__ == 281 and strName == u'VirtualQuantity':
            v = CDispatch(282)
            return v
        elif self.__id__ == 285 and strName == u'AutomaticDeallocation':
            v = CDispatch(286)
            return v
        elif self.__id__ == 289 and strName == u'AutomaticAllocation':
            v = CDispatch(290)
            return v
        elif self.__id__ == 293 and strName == u'PoolID':
            v = CDispatch(294)
            return v
        elif self.__id__ == 297 and strName == u'Reservation':
            v = CDispatch(298)
            return v
        elif self.__id__ == 301 and strName == u'AllocationUnits':
            v = CDispatch(302)
            return v
        elif self.__id__ == 305 and strName == u'MappingBehavior':
            v = CDispatch(306)
            return v
        elif self.__id__ == 309 and strName == u'Address':
            v = CDispatch(310)
            return v
        elif self.__id__ == 313 and strName == u'OtherResourceType':
            v = CDispatch(314)
            return v
        elif self.__id__ == 317 and strName == u'Caption':
            v = CDispatch(318)
            return v
        elif self.__id__ == 321 and strName == u'ConsumerVisibility':
            v = CDispatch(322)
            return v
        elif self.__id__ == 325 and strName == u'Limit':
            v = CDispatch(326)
            return v
        elif self.__id__ == 329 and strName == u'ResourceType':
            v = CDispatch(330)
            return v
        elif self.__id__ == 333 and strName == u'Weight':
            v = CDispatch(334)
            return v
        elif self.__id__ == 335 and strName == u'VirtualSystemIdentifiers':
            v = CDispatch(336)
            return v
        elif self.__id__ == 339 and strName == u'Connection':
            v = CDispatch(340)
            return v
        elif self.__id__ == 395 and strName == u'InstanceID':
            v = CDispatch(396)
            return v
        elif self.__id__ == 399 and strName == u'ResourceSubType':
            v = CDispatch(400)
            return v
        elif self.__id__ == 403 and strName == u'HostResource':
            v = CDispatch(404)
            return v
        elif self.__id__ == 407 and strName == u'ElementName':
            v = CDispatch(408)
            return v
        elif self.__id__ == 411 and strName == u'Description':
            v = CDispatch(412)
            return v
        elif self.__id__ == 415 and strName == u'Parent':
            v = CDispatch(416)
            return v
        elif self.__id__ == 419 and strName == u'VirtualQuantity':
            v = CDispatch(420)
            return v
        elif self.__id__ == 423 and strName == u'AutomaticDeallocation':
            v = CDispatch(424)
            return v
        elif self.__id__ == 427 and strName == u'AutomaticAllocation':
            v = CDispatch(428)
            return v
        elif self.__id__ == 431 and strName == u'PoolID':
            v = CDispatch(432)
            return v
        elif self.__id__ == 435 and strName == u'Reservation':
            v = CDispatch(436)
            return v
        elif self.__id__ == 439 and strName == u'AllocationUnits':
            v = CDispatch(440)
            return v
        elif self.__id__ == 443 and strName == u'MappingBehavior':
            v = CDispatch(444)
            return v
        elif self.__id__ == 447 and strName == u'Address':
            v = CDispatch(448)
            return v
        elif self.__id__ == 451 and strName == u'OtherResourceType':
            v = CDispatch(452)
            return v
        elif self.__id__ == 455 and strName == u'Caption':
            v = CDispatch(456)
            return v
        elif self.__id__ == 459 and strName == u'ConsumerVisibility':
            v = CDispatch(460)
            return v
        elif self.__id__ == 463 and strName == u'Limit':
            v = CDispatch(464)
            return v
        elif self.__id__ == 467 and strName == u'ResourceType':
            v = CDispatch(468)
            return v
        elif self.__id__ == 471 and strName == u'Weight':
            v = CDispatch(472)
            return v
        elif self.__id__ == 477 and strName == u'Connection':
            v = CDispatch(478)
            return v
        elif self.__id__ == 397 and strName == u'InstanceID':
            v = CDispatch(398)
            return v
        elif self.__id__ == 401 and strName == u'ResourceSubType':
            v = CDispatch(402)
            return v
        elif self.__id__ == 405 and strName == u'HostResource':
            v = CDispatch(406)
            return v
        elif self.__id__ == 409 and strName == u'ElementName':
            v = CDispatch(410)
            return v
        elif self.__id__ == 413 and strName == u'Description':
            v = CDispatch(414)
            return v
        elif self.__id__ == 417 and strName == u'Parent':
            v = CDispatch(418)
            return v
        elif self.__id__ == 421 and strName == u'VirtualQuantity':
            v = CDispatch(422)
            return v
        elif self.__id__ == 425 and strName == u'AutomaticDeallocation':
            v = CDispatch(426)
            return v
        elif self.__id__ == 429 and strName == u'AutomaticAllocation':
            v = CDispatch(430)
            return v
        elif self.__id__ == 433 and strName == u'PoolID':
            v = CDispatch(434)
            return v
        elif self.__id__ == 437 and strName == u'Reservation':
            v = CDispatch(438)
            return v
        elif self.__id__ == 441 and strName == u'AllocationUnits':
            v = CDispatch(442)
            return v
        elif self.__id__ == 445 and strName == u'MappingBehavior':
            v = CDispatch(446)
            return v
        elif self.__id__ == 449 and strName == u'Address':
            v = CDispatch(450)
            return v
        elif self.__id__ == 453 and strName == u'OtherResourceType':
            v = CDispatch(454)
            return v
        elif self.__id__ == 457 and strName == u'Caption':
            v = CDispatch(458)
            return v
        elif self.__id__ == 461 and strName == u'ConsumerVisibility':
            v = CDispatch(462)
            return v
        elif self.__id__ == 465 and strName == u'Limit':
            v = CDispatch(466)
            return v
        elif self.__id__ == 469 and strName == u'ResourceType':
            v = CDispatch(470)
            return v
        elif self.__id__ == 473 and strName == u'Weight':
            v = CDispatch(474)
            return v
        elif self.__id__ == 475 and strName == u'VirtualSystemIdentifiers':
            v = CDispatch(476)
            return v
        elif self.__id__ == 479 and strName == u'Connection':
            v = CDispatch(480)
            return v
