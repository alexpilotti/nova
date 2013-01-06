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
            v.__instance_id__ = 278
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
            v.__instance_id__ = 34
        elif _WMI_count_3 == 2:
            v = _wmi_namespace()
            v.__instance_id__ = 257
        _WMI_count_3 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_ConcreteJob.InstanceID="F1C1B540-3C9\
D-4A18-82A5-F38DA0D10BEC"':
        ret_value = None
        global _WMI_count_4
        if not '_WMI_count_4' in globals():
            _WMI_count_4 = 0
        if _WMI_count_4 == 0:
            v = _wmi_object()
            v.__instance_id__ = 251
        elif _WMI_count_4 == 1:
            v = _wmi_object()
            v.__instance_id__ = 252
        elif _WMI_count_4 == 2:
            v = _wmi_object()
            v.__instance_id__ = 253
        elif _WMI_count_4 == 3:
            v = _wmi_object()
            v.__instance_id__ = 254
        elif _WMI_count_4 == 4:
            v = _wmi_object()
            v.__instance_id__ = 255
        elif _WMI_count_4 == 5:
            v = _wmi_object()
            v.__instance_id__ = 256
        _WMI_count_4 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_ConcreteJob.InstanceID="9DB52552-94C\
7-4BBB-8364-09484D8A67E3"':
        ret_value = None
        global _WMI_count_5
        if not '_WMI_count_5' in globals():
            _WMI_count_5 = 0
        if _WMI_count_5 == 0:
            v = _wmi_object()
            v.__instance_id__ = 286
        elif _WMI_count_5 == 1:
            v = _wmi_object()
            v.__instance_id__ = 287
        _WMI_count_5 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_ConcreteJob.InstanceID="E3D9EB9F-D8D\
F-4799-9DEB-B0845C771D20"':
        ret_value = None
        global _WMI_count_6
        if not '_WMI_count_6' in globals():
            _WMI_count_6 = 0
        if _WMI_count_6 == 0:
            v = _wmi_object()
            v.__instance_id__ = 307
        elif _WMI_count_6 == 1:
            v = _wmi_object()
            v.__instance_id__ = 308
        _WMI_count_6 += 1
        return v


class _wmi_namespace(object):

    def __init__(self, *args, **kwargs):
        pass

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
    def MSFT_iSCSITarget(self):
        if self.__id__ == 2:
            v = _wmi_class()
            v.__instance_id__ = 310
            return v
        elif self.__id__ == 7:
            v = _wmi_class()
            v.__instance_id__ = 28
            return v

    @MSFT_iSCSITarget.setter
    def MSFT_iSCSITarget(self, value):
        pass

    @property
    def Msvm_ResourceAllocationSettingData(self):
        if self.__id__ == 9:
            v = _wmi_class()
            v.__instance_id__ = 150
            return v
        elif self.__id__ == 34:
            v = _wmi_class()
            v.__instance_id__ = 53
            return v

    @Msvm_ResourceAllocationSettingData.setter
    def Msvm_ResourceAllocationSettingData(self, value):
        pass

    @property
    def MSFT_iSCSITargetPortal(self):
        if self.__id__ == 7:
            v = _wmi_class()
            v.__instance_id__ = 25
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
                v = _wmi_class()
                v.__instance_id__ = 11
            elif self._Msvm_VirtualSystemManagementService_count_0 == 1:
                v = _wmi_class()
                v.__instance_id__ = 238
            elif self._Msvm_VirtualSystemManagementService_count_0 == 2:
                v = _wmi_class()
                v.__instance_id__ = 244
            self._Msvm_VirtualSystemManagementService_count_0 += 1
            return v
        elif self.__id__ == 34:
            v = _wmi_class()
            v.__instance_id__ = 143
            return v
        elif self.__id__ == 257:
            v = _wmi_class()
            v.__instance_id__ = 281
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
                v = _wmi_class()
                v.__instance_id__ = 10
            elif self._Msvm_ComputerSystem_count_0 == 1:
                v = _wmi_class()
                v.__instance_id__ = 16
            elif self._Msvm_ComputerSystem_count_0 == 2:
                v = _wmi_class()
                v.__instance_id__ = 242
            elif self._Msvm_ComputerSystem_count_0 == 3:
                v = _wmi_class()
                v.__instance_id__ = 248
            self._Msvm_ComputerSystem_count_0 += 1
            return v
        elif self.__id__ == 257:
            ret_value = None
            if not hasattr(self, '_Msvm_ComputerSystem_count_1'):
                self._Msvm_ComputerSystem_count_1 = 0
            if self._Msvm_ComputerSystem_count_1 == 0:
                v = _wmi_class()
                v.__instance_id__ = 258
            elif self._Msvm_ComputerSystem_count_1 == 1:
                v = _wmi_class()
                v.__instance_id__ = 276
            elif self._Msvm_ComputerSystem_count_1 == 2:
                v = _wmi_class()
                v.__instance_id__ = 279
            elif self._Msvm_ComputerSystem_count_1 == 3:
                v = _wmi_class()
                v.__instance_id__ = 283
            elif self._Msvm_ComputerSystem_count_1 == 4:
                v = _wmi_class()
                v.__instance_id__ = 288
            self._Msvm_ComputerSystem_count_1 += 1
            return v

    @Msvm_ComputerSystem.setter
    def Msvm_ComputerSystem(self, value):
        pass

    @property
    def Msvm_VirtualSystemGlobalSettingData(self):
        if self.__id__ == 9:
            v = _wmi_class()
            v.__instance_id__ = 13
            return v

    @Msvm_VirtualSystemGlobalSettingData.setter
    def Msvm_VirtualSystemGlobalSettingData(self, value):
        pass

    @property
    def MSFT_iSCSISession(self):
        if self.__id__ == 2:
            v = _wmi_class()
            v.__instance_id__ = 312
            return v

    @MSFT_iSCSISession.setter
    def MSFT_iSCSISession(self, value):
        pass

    @property
    def MSVM_ComputerSystem(self):
        if self.__id__ == 9:
            v = _wmi_class()
            v.__instance_id__ = 147
            return v
        elif self.__id__ == 34:
            v = _wmi_class()
            v.__instance_id__ = 37
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
                v1 = _wmi_object()
                v1.__instance_id__ = 275
                v.append(v1)
            elif self._query_count_0 == 1:
                v = []
                v1 = _wmi_object()
                v1.__instance_id__ = 309
                v.append(v1)
            self._query_count_0 += 1
            return v
        elif self.__id__ == 8 and wql == 'SELECT * FROM\
 MSiSCSIInitiator_SessionClass                 WHERE\
 TargetName=\'iqn.2010-10.org.openstack:volume-ccb39627-34fa-4f47-968b-6580d9d\
7ee2b\'':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 31
            v.append(v1)
            return v
        elif self.__id__ == 9 and wql == 'SELECT * FROM\
 Msvm_ResourceAllocationSettingData                 WHERE ResourceSubType =\
 \'Microsoft Synthetic SCSI Controller\'                AND InstanceID LIKE\
 \'%Default%\'':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 149
            v.append(v1)
            return v
        elif self.__id__ == 34 and wql == 'SELECT * FROM Msvm_DiskDrive WHERE\
 DriveNumber=1':
            ret_value = None
            if not hasattr(self, '_query_count_3'):
                self._query_count_3 = 0
            if self._query_count_3 == 0:
                v = []
                v1 = _wmi_object()
                v1.__instance_id__ = 35
                v.append(v1)
            elif self._query_count_3 == 1:
                v = []
                v1 = _wmi_object()
                v1.__instance_id__ = 36
                v.append(v1)
            self._query_count_3 += 1
            return v
        elif self.__id__ == 34 and wql == 'SELECT * FROM\
 Msvm_ResourceAllocationSettingData                 WHERE ResourceSubType LIKE\
 \'Microsoft Physical Disk Drive\'                AND InstanceID LIKE\
 \'%Default%\'':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 52
            v.append(v1)
            return v


class _wmi_class(object):

    def __init__(self, *args, **kwargs):
        pass

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__

    @property
    def New(self):
        if self.__id__ == 25:
            v = _wmi_method()
            v.__instance_id__ = 26
            return v

    @New.setter
    def New(self, value):
        pass

    @property
    def Connect(self):
        if self.__id__ == 28:
            v = _wmi_method()
            v.__instance_id__ = 29
            return v

    @Connect.setter
    def Connect(self, value):
        pass


    def __call__(self, fields='[]', **where_clause):
        if self.__id__ == 312 and where_clause.get('TargetNodeAddress') ==\
 'iqn.2010-10.org.openstack:volume-ccb39627-34fa-4f47-968b-6580d9d7ee2b':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 313
            v.append(v1)
            return v
        elif self.__id__ == 310 and where_clause.get('NodeAddress') ==\
 'iqn.2010-10.org.openstack:volume-ccb39627-34fa-4f47-968b-6580d9d7ee2b':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 311
            v.append(v1)
            return v
        elif self.__id__ == 5:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 6
            v.append(v1)
            return v
        elif self.__id__ == 147 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_fbae78d4-0c5a-4c43-9b3e-c3aacd72b401':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 148
            v.append(v1)
            return v
        elif self.__id__ == 10 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_fbae78d4-0c5a-4c43-9b3e-c3aacd72b401':
            v = []
            return v
        elif self.__id__ == 16 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_fbae78d4-0c5a-4c43-9b3e-c3aacd72b401':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 17
            v.append(v1)
            return v
        elif self.__id__ == 242 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_fbae78d4-0c5a-4c43-9b3e-c3aacd72b401':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 243
            v.append(v1)
            return v
        elif self.__id__ == 248 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_fbae78d4-0c5a-4c43-9b3e-c3aacd72b401':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 249
            v.append(v1)
            return v
        elif self.__id__ == 11:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 12
            v.append(v1)
            return v
        elif self.__id__ == 238:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 239
            v.append(v1)
            return v
        elif self.__id__ == 244:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 245
            v.append(v1)
            return v
        elif self.__id__ == 37 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_fbae78d4-0c5a-4c43-9b3e-c3aacd72b401':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 38
            v.append(v1)
            return v
        elif self.__id__ == 143:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 144
            v.append(v1)
            return v
        elif self.__id__ == 258 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_fbae78d4-0c5a-4c43-9b3e-c3aacd72b401':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 259
            v.append(v1)
            return v
        elif self.__id__ == 276 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_fbae78d4-0c5a-4c43-9b3e-c3aacd72b401':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 277
            v.append(v1)
            return v
        elif self.__id__ == 279 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_fbae78d4-0c5a-4c43-9b3e-c3aacd72b401':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 280
            v.append(v1)
            return v
        elif self.__id__ == 283 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_fbae78d4-0c5a-4c43-9b3e-c3aacd72b401':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 284
            v.append(v1)
            return v
        elif self.__id__ == 288 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_fbae78d4-0c5a-4c43-9b3e-c3aacd72b401':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 289
            v.append(v1)
            return v
        elif self.__id__ == 281:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 282
            v.append(v1)
            return v


    def new(self, **kwargs):
        if self.__id__ == 13:
            v = _wmi_object()
            v.__instance_id__ = 14
            return v
        elif self.__id__ == 150:
            v = _wmi_object()
            v.__instance_id__ = 151
            return v
        elif self.__id__ == 53:
            v = _wmi_object()
            v.__instance_id__ = 54
            return v


class _wmi_object(object):

    def __init__(self, *args, **kwargs):
        pass

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__

    @property
    def RequestStateChange(self):
        if self.__id__ == 249:
            v = _wmi_method()
            v.__instance_id__ = 250
            return v
        elif self.__id__ == 284:
            v = _wmi_method()
            v.__instance_id__ = 285
            return v

    @RequestStateChange.setter
    def RequestStateChange(self, value):
        pass

    @property
    def IsPersistent(self):
        if self.__id__ == 313:
            return True

    @IsPersistent.setter
    def IsPersistent(self, value):
        pass

    @property
    def Disconnect(self):
        if self.__id__ == 311:
            v = _wmi_method()
            v.__instance_id__ = 315
            return v

    @Disconnect.setter
    def Disconnect(self, value):
        pass

    @property
    def Address(self):
        if self.__id__ == 48:
            return u'0'
        elif self.__id__ == 49:
            return u'1'

    @Address.setter
    def Address(self, value):
        pass

    @property
    def JobState(self):
        if self.__id__ == 251:
            return 4
        elif self.__id__ == 252:
            return 4
        elif self.__id__ == 253:
            return 4
        elif self.__id__ == 254:
            return 4
        elif self.__id__ == 255:
            return 4
        elif self.__id__ == 256:
            ret_value = None
            if not hasattr(self, '_JobState_count_5'):
                self._JobState_count_5 = 0
            if self._JobState_count_5 == 0:
                v = 7
            elif self._JobState_count_5 == 1:
                v = 7
            self._JobState_count_5 += 1
            return v
        elif self.__id__ == 286:
            return 4
        elif self.__id__ == 287:
            ret_value = None
            if not hasattr(self, '_JobState_count_7'):
                self._JobState_count_7 = 0
            if self._JobState_count_7 == 0:
                v = 7
            elif self._JobState_count_7 == 1:
                v = 7
            self._JobState_count_7 += 1
            return v
        elif self.__id__ == 307:
            return 4
        elif self.__id__ == 308:
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

    @property
    def Unregister(self):
        if self.__id__ == 313:
            v = _wmi_method()
            v.__instance_id__ = 314
            return v

    @Unregister.setter
    def Unregister(self, value):
        pass

    @property
    def AddVirtualSystemResources(self):
        if self.__id__ == 239:
            v = _wmi_method()
            v.__instance_id__ = 240
            return v
        elif self.__id__ == 245:
            v = _wmi_method()
            v.__instance_id__ = 246
            return v
        elif self.__id__ == 144:
            v = _wmi_method()
            v.__instance_id__ = 145
            return v

    @AddVirtualSystemResources.setter
    def AddVirtualSystemResources(self, value):
        pass

    @property
    def SettingType(self):
        if self.__id__ == 18:
            return 3

    @SettingType.setter
    def SettingType(self, value):
        pass

    @property
    def path_(self):
        if self.__id__ == 148:
            v = CDispatch()
            v.__instance_id__ = 241
            return v
        elif self.__id__ == 17:
            ret_value = None
            if not hasattr(self, '_path__count_1'):
                self._path__count_1 = 0
            if self._path__count_1 == 0:
                v = CDispatch()
                v.__instance_id__ = 21
            elif self._path__count_1 == 1:
                v = CDispatch()
                v.__instance_id__ = 24
            self._path__count_1 += 1
            return v
        elif self.__id__ == 243:
            v = CDispatch()
            v.__instance_id__ = 247
            return v
        elif self.__id__ == 36:
            v = CDispatch()
            v.__instance_id__ = 142
            return v
        elif self.__id__ == 48:
            v = CDispatch()
            v.__instance_id__ = 141
            return v
        elif self.__id__ == 38:
            v = CDispatch()
            v.__instance_id__ = 146
            return v
        elif self.__id__ == 280:
            v = CDispatch()
            v.__instance_id__ = 306
            return v

    @path_.setter
    def path_(self, value):
        pass

    @property
    def Devices(self):
        if self.__id__ == 31:
            v = ()
            v1 = CDispatch()
            v1.__instance_id__ = 32
            v += (v1,)
            v1 = CDispatch()
            v1.__instance_id__ = 33
            v += (v1,)
            return v

    @Devices.setter
    def Devices(self, value):
        pass

    @property
    def ResourceSubType(self):
        if self.__id__ == 40:
            return u'Microsoft Virtual Keyboard'
        elif self.__id__ == 41:
            return u'Microsoft Virtual PS2 Mouse'
        elif self.__id__ == 42:
            return u'Microsoft S3 Display Controller'
        elif self.__id__ == 43:
            return u'Microsoft Synthetic Diskette Drive'
        elif self.__id__ == 44:
            return None
        elif self.__id__ == 45:
            return u'Microsoft Serial Controller'
        elif self.__id__ == 46:
            return u'Microsoft Serial Port'
        elif self.__id__ == 47:
            return u'Microsoft Serial Port'
        elif self.__id__ == 48:
            return u'Microsoft Emulated IDE Controller'
        elif self.__id__ == 49:
            return u'Microsoft Emulated IDE Controller'
        elif self.__id__ == 50:
            return u'Microsoft Synthetic Mouse'
        elif self.__id__ == 51:
            return u'Microsoft Synthetic Display Controller'
        elif self.__id__ == 261:
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
        elif self.__id__ == 262:
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
        elif self.__id__ == 263:
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
        elif self.__id__ == 264:
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
        elif self.__id__ == 265:
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
        elif self.__id__ == 266:
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
        elif self.__id__ == 267:
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
        elif self.__id__ == 268:
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
        elif self.__id__ == 269:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_20'):
                self._ResourceSubType_count_20 = 0
            if self._ResourceSubType_count_20 == 0:
                v = u'Microsoft Physical Disk Drive'
            elif self._ResourceSubType_count_20 == 1:
                v = u'Microsoft Physical Disk Drive'
            elif self._ResourceSubType_count_20 == 2:
                v = u'Microsoft Physical Disk Drive'
            self._ResourceSubType_count_20 += 1
            return v
        elif self.__id__ == 270:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_21'):
                self._ResourceSubType_count_21 = 0
            if self._ResourceSubType_count_21 == 0:
                v = u'Microsoft Emulated IDE Controller'
            elif self._ResourceSubType_count_21 == 1:
                v = u'Microsoft Emulated IDE Controller'
            elif self._ResourceSubType_count_21 == 2:
                v = u'Microsoft Emulated IDE Controller'
            self._ResourceSubType_count_21 += 1
            return v
        elif self.__id__ == 271:
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
        elif self.__id__ == 272:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_23'):
                self._ResourceSubType_count_23 = 0
            if self._ResourceSubType_count_23 == 0:
                v = u'Microsoft Synthetic Mouse'
            elif self._ResourceSubType_count_23 == 1:
                v = u'Microsoft Synthetic Mouse'
            elif self._ResourceSubType_count_23 == 2:
                v = u'Microsoft Synthetic Mouse'
            self._ResourceSubType_count_23 += 1
            return v
        elif self.__id__ == 273:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_24'):
                self._ResourceSubType_count_24 = 0
            if self._ResourceSubType_count_24 == 0:
                v = u'Microsoft Synthetic Display Controller'
            elif self._ResourceSubType_count_24 == 1:
                v = u'Microsoft Synthetic Display Controller'
            elif self._ResourceSubType_count_24 == 2:
                v = u'Microsoft Synthetic Display Controller'
            self._ResourceSubType_count_24 += 1
            return v
        elif self.__id__ == 274:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_25'):
                self._ResourceSubType_count_25 = 0
            if self._ResourceSubType_count_25 == 0:
                v = u'Microsoft Synthetic SCSI Controller'
            elif self._ResourceSubType_count_25 == 1:
                v = u'Microsoft Synthetic SCSI Controller'
            elif self._ResourceSubType_count_25 == 2:
                v = u'Microsoft Synthetic SCSI Controller'
            self._ResourceSubType_count_25 += 1
            return v
        elif self.__id__ == 291:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_26'):
                self._ResourceSubType_count_26 = 0
            if self._ResourceSubType_count_26 == 0:
                v = u'Microsoft Virtual Keyboard'
            elif self._ResourceSubType_count_26 == 1:
                v = u'Microsoft Virtual Keyboard'
            elif self._ResourceSubType_count_26 == 2:
                v = u'Microsoft Virtual Keyboard'
            self._ResourceSubType_count_26 += 1
            return v
        elif self.__id__ == 292:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_27'):
                self._ResourceSubType_count_27 = 0
            if self._ResourceSubType_count_27 == 0:
                v = u'Microsoft Virtual PS2 Mouse'
            elif self._ResourceSubType_count_27 == 1:
                v = u'Microsoft Virtual PS2 Mouse'
            elif self._ResourceSubType_count_27 == 2:
                v = u'Microsoft Virtual PS2 Mouse'
            self._ResourceSubType_count_27 += 1
            return v
        elif self.__id__ == 293:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_28'):
                self._ResourceSubType_count_28 = 0
            if self._ResourceSubType_count_28 == 0:
                v = u'Microsoft S3 Display Controller'
            elif self._ResourceSubType_count_28 == 1:
                v = u'Microsoft S3 Display Controller'
            elif self._ResourceSubType_count_28 == 2:
                v = u'Microsoft S3 Display Controller'
            self._ResourceSubType_count_28 += 1
            return v
        elif self.__id__ == 294:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_29'):
                self._ResourceSubType_count_29 = 0
            if self._ResourceSubType_count_29 == 0:
                v = u'Microsoft Synthetic Diskette Drive'
            elif self._ResourceSubType_count_29 == 1:
                v = u'Microsoft Synthetic Diskette Drive'
            elif self._ResourceSubType_count_29 == 2:
                v = u'Microsoft Synthetic Diskette Drive'
            self._ResourceSubType_count_29 += 1
            return v
        elif self.__id__ == 295:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_30'):
                self._ResourceSubType_count_30 = 0
            if self._ResourceSubType_count_30 == 0:
                v = None
            elif self._ResourceSubType_count_30 == 1:
                v = None
            elif self._ResourceSubType_count_30 == 2:
                v = None
            self._ResourceSubType_count_30 += 1
            return v
        elif self.__id__ == 296:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_31'):
                self._ResourceSubType_count_31 = 0
            if self._ResourceSubType_count_31 == 0:
                v = u'Microsoft Serial Controller'
            elif self._ResourceSubType_count_31 == 1:
                v = u'Microsoft Serial Controller'
            elif self._ResourceSubType_count_31 == 2:
                v = u'Microsoft Serial Controller'
            self._ResourceSubType_count_31 += 1
            return v
        elif self.__id__ == 297:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_32'):
                self._ResourceSubType_count_32 = 0
            if self._ResourceSubType_count_32 == 0:
                v = u'Microsoft Serial Port'
            elif self._ResourceSubType_count_32 == 1:
                v = u'Microsoft Serial Port'
            elif self._ResourceSubType_count_32 == 2:
                v = u'Microsoft Serial Port'
            self._ResourceSubType_count_32 += 1
            return v
        elif self.__id__ == 298:
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
        elif self.__id__ == 299:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_34'):
                self._ResourceSubType_count_34 = 0
            if self._ResourceSubType_count_34 == 0:
                v = u'Microsoft Physical Disk Drive'
            elif self._ResourceSubType_count_34 == 1:
                v = u'Microsoft Physical Disk Drive'
            elif self._ResourceSubType_count_34 == 2:
                v = u'Microsoft Physical Disk Drive'
            self._ResourceSubType_count_34 += 1
            return v
        elif self.__id__ == 300:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_35'):
                self._ResourceSubType_count_35 = 0
            if self._ResourceSubType_count_35 == 0:
                v = u'Microsoft Emulated IDE Controller'
            elif self._ResourceSubType_count_35 == 1:
                v = u'Microsoft Emulated IDE Controller'
            elif self._ResourceSubType_count_35 == 2:
                v = u'Microsoft Emulated IDE Controller'
            self._ResourceSubType_count_35 += 1
            return v
        elif self.__id__ == 301:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_36'):
                self._ResourceSubType_count_36 = 0
            if self._ResourceSubType_count_36 == 0:
                v = u'Microsoft Emulated IDE Controller'
            elif self._ResourceSubType_count_36 == 1:
                v = u'Microsoft Emulated IDE Controller'
            elif self._ResourceSubType_count_36 == 2:
                v = u'Microsoft Emulated IDE Controller'
            self._ResourceSubType_count_36 += 1
            return v
        elif self.__id__ == 302:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_37'):
                self._ResourceSubType_count_37 = 0
            if self._ResourceSubType_count_37 == 0:
                v = u'Microsoft Synthetic Mouse'
            elif self._ResourceSubType_count_37 == 1:
                v = u'Microsoft Synthetic Mouse'
            elif self._ResourceSubType_count_37 == 2:
                v = u'Microsoft Synthetic Mouse'
            self._ResourceSubType_count_37 += 1
            return v
        elif self.__id__ == 303:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_38'):
                self._ResourceSubType_count_38 = 0
            if self._ResourceSubType_count_38 == 0:
                v = u'Microsoft Synthetic Display Controller'
            elif self._ResourceSubType_count_38 == 1:
                v = u'Microsoft Synthetic Display Controller'
            elif self._ResourceSubType_count_38 == 2:
                v = u'Microsoft Synthetic Display Controller'
            self._ResourceSubType_count_38 += 1
            return v
        elif self.__id__ == 304:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_39'):
                self._ResourceSubType_count_39 = 0
            if self._ResourceSubType_count_39 == 0:
                v = u'Microsoft Synthetic SCSI Controller'
            elif self._ResourceSubType_count_39 == 1:
                v = u'Microsoft Synthetic SCSI Controller'
            elif self._ResourceSubType_count_39 == 2:
                v = u'Microsoft Synthetic SCSI Controller'
            self._ResourceSubType_count_39 += 1
            return v

    @ResourceSubType.setter
    def ResourceSubType(self, value):
        pass

    @property
    def ElapsedTime(self):
        if self.__id__ == 256:
            return u'00000000000000.739669:000'

    @ElapsedTime.setter
    def ElapsedTime(self, value):
        pass

    @property
    def Properties_(self):
        if self.__id__ == 149:
            ret_value = None
            if not hasattr(self, '_Properties__count_0'):
                self._Properties__count_0 = 0
            if self._Properties__count_0 == 0:
                v = CDispatch()
                v.__instance_id__ = 152
            elif self._Properties__count_0 == 1:
                v = CDispatch()
                v.__instance_id__ = 156
            elif self._Properties__count_0 == 2:
                v = CDispatch()
                v.__instance_id__ = 160
            elif self._Properties__count_0 == 3:
                v = CDispatch()
                v.__instance_id__ = 164
            elif self._Properties__count_0 == 4:
                v = CDispatch()
                v.__instance_id__ = 168
            elif self._Properties__count_0 == 5:
                v = CDispatch()
                v.__instance_id__ = 172
            elif self._Properties__count_0 == 6:
                v = CDispatch()
                v.__instance_id__ = 176
            elif self._Properties__count_0 == 7:
                v = CDispatch()
                v.__instance_id__ = 180
            elif self._Properties__count_0 == 8:
                v = CDispatch()
                v.__instance_id__ = 184
            elif self._Properties__count_0 == 9:
                v = CDispatch()
                v.__instance_id__ = 188
            elif self._Properties__count_0 == 10:
                v = CDispatch()
                v.__instance_id__ = 192
            elif self._Properties__count_0 == 11:
                v = CDispatch()
                v.__instance_id__ = 196
            elif self._Properties__count_0 == 12:
                v = CDispatch()
                v.__instance_id__ = 200
            elif self._Properties__count_0 == 13:
                v = CDispatch()
                v.__instance_id__ = 204
            elif self._Properties__count_0 == 14:
                v = CDispatch()
                v.__instance_id__ = 208
            elif self._Properties__count_0 == 15:
                v = CDispatch()
                v.__instance_id__ = 212
            elif self._Properties__count_0 == 16:
                v = CDispatch()
                v.__instance_id__ = 216
            elif self._Properties__count_0 == 17:
                v = CDispatch()
                v.__instance_id__ = 220
            elif self._Properties__count_0 == 18:
                v = CDispatch()
                v.__instance_id__ = 224
            elif self._Properties__count_0 == 19:
                v = CDispatch()
                v.__instance_id__ = 228
            elif self._Properties__count_0 == 20:
                v = CDispatch()
                v.__instance_id__ = 234
            self._Properties__count_0 += 1
            return v
        elif self.__id__ == 151:
            ret_value = None
            if not hasattr(self, '_Properties__count_1'):
                self._Properties__count_1 = 0
            if self._Properties__count_1 == 0:
                v = CDispatch()
                v.__instance_id__ = 154
            elif self._Properties__count_1 == 1:
                v = CDispatch()
                v.__instance_id__ = 158
            elif self._Properties__count_1 == 2:
                v = CDispatch()
                v.__instance_id__ = 162
            elif self._Properties__count_1 == 3:
                v = CDispatch()
                v.__instance_id__ = 166
            elif self._Properties__count_1 == 4:
                v = CDispatch()
                v.__instance_id__ = 170
            elif self._Properties__count_1 == 5:
                v = CDispatch()
                v.__instance_id__ = 174
            elif self._Properties__count_1 == 6:
                v = CDispatch()
                v.__instance_id__ = 178
            elif self._Properties__count_1 == 7:
                v = CDispatch()
                v.__instance_id__ = 182
            elif self._Properties__count_1 == 8:
                v = CDispatch()
                v.__instance_id__ = 186
            elif self._Properties__count_1 == 9:
                v = CDispatch()
                v.__instance_id__ = 190
            elif self._Properties__count_1 == 10:
                v = CDispatch()
                v.__instance_id__ = 194
            elif self._Properties__count_1 == 11:
                v = CDispatch()
                v.__instance_id__ = 198
            elif self._Properties__count_1 == 12:
                v = CDispatch()
                v.__instance_id__ = 202
            elif self._Properties__count_1 == 13:
                v = CDispatch()
                v.__instance_id__ = 206
            elif self._Properties__count_1 == 14:
                v = CDispatch()
                v.__instance_id__ = 210
            elif self._Properties__count_1 == 15:
                v = CDispatch()
                v.__instance_id__ = 214
            elif self._Properties__count_1 == 16:
                v = CDispatch()
                v.__instance_id__ = 218
            elif self._Properties__count_1 == 17:
                v = CDispatch()
                v.__instance_id__ = 222
            elif self._Properties__count_1 == 18:
                v = CDispatch()
                v.__instance_id__ = 226
            elif self._Properties__count_1 == 19:
                v = CDispatch()
                v.__instance_id__ = 230
            elif self._Properties__count_1 == 20:
                v = CDispatch()
                v.__instance_id__ = 232
            elif self._Properties__count_1 == 21:
                v = CDispatch()
                v.__instance_id__ = 236
            self._Properties__count_1 += 1
            return v
        elif self.__id__ == 52:
            ret_value = None
            if not hasattr(self, '_Properties__count_2'):
                self._Properties__count_2 = 0
            if self._Properties__count_2 == 0:
                v = CDispatch()
                v.__instance_id__ = 55
            elif self._Properties__count_2 == 1:
                v = CDispatch()
                v.__instance_id__ = 59
            elif self._Properties__count_2 == 2:
                v = CDispatch()
                v.__instance_id__ = 63
            elif self._Properties__count_2 == 3:
                v = CDispatch()
                v.__instance_id__ = 67
            elif self._Properties__count_2 == 4:
                v = CDispatch()
                v.__instance_id__ = 71
            elif self._Properties__count_2 == 5:
                v = CDispatch()
                v.__instance_id__ = 75
            elif self._Properties__count_2 == 6:
                v = CDispatch()
                v.__instance_id__ = 79
            elif self._Properties__count_2 == 7:
                v = CDispatch()
                v.__instance_id__ = 83
            elif self._Properties__count_2 == 8:
                v = CDispatch()
                v.__instance_id__ = 87
            elif self._Properties__count_2 == 9:
                v = CDispatch()
                v.__instance_id__ = 91
            elif self._Properties__count_2 == 10:
                v = CDispatch()
                v.__instance_id__ = 95
            elif self._Properties__count_2 == 11:
                v = CDispatch()
                v.__instance_id__ = 99
            elif self._Properties__count_2 == 12:
                v = CDispatch()
                v.__instance_id__ = 103
            elif self._Properties__count_2 == 13:
                v = CDispatch()
                v.__instance_id__ = 107
            elif self._Properties__count_2 == 14:
                v = CDispatch()
                v.__instance_id__ = 111
            elif self._Properties__count_2 == 15:
                v = CDispatch()
                v.__instance_id__ = 115
            elif self._Properties__count_2 == 16:
                v = CDispatch()
                v.__instance_id__ = 119
            elif self._Properties__count_2 == 17:
                v = CDispatch()
                v.__instance_id__ = 123
            elif self._Properties__count_2 == 18:
                v = CDispatch()
                v.__instance_id__ = 127
            elif self._Properties__count_2 == 19:
                v = CDispatch()
                v.__instance_id__ = 131
            elif self._Properties__count_2 == 20:
                v = CDispatch()
                v.__instance_id__ = 137
            self._Properties__count_2 += 1
            return v
        elif self.__id__ == 54:
            ret_value = None
            if not hasattr(self, '_Properties__count_3'):
                self._Properties__count_3 = 0
            if self._Properties__count_3 == 0:
                v = CDispatch()
                v.__instance_id__ = 57
            elif self._Properties__count_3 == 1:
                v = CDispatch()
                v.__instance_id__ = 61
            elif self._Properties__count_3 == 2:
                v = CDispatch()
                v.__instance_id__ = 65
            elif self._Properties__count_3 == 3:
                v = CDispatch()
                v.__instance_id__ = 69
            elif self._Properties__count_3 == 4:
                v = CDispatch()
                v.__instance_id__ = 73
            elif self._Properties__count_3 == 5:
                v = CDispatch()
                v.__instance_id__ = 77
            elif self._Properties__count_3 == 6:
                v = CDispatch()
                v.__instance_id__ = 81
            elif self._Properties__count_3 == 7:
                v = CDispatch()
                v.__instance_id__ = 85
            elif self._Properties__count_3 == 8:
                v = CDispatch()
                v.__instance_id__ = 89
            elif self._Properties__count_3 == 9:
                v = CDispatch()
                v.__instance_id__ = 93
            elif self._Properties__count_3 == 10:
                v = CDispatch()
                v.__instance_id__ = 97
            elif self._Properties__count_3 == 11:
                v = CDispatch()
                v.__instance_id__ = 101
            elif self._Properties__count_3 == 12:
                v = CDispatch()
                v.__instance_id__ = 105
            elif self._Properties__count_3 == 13:
                v = CDispatch()
                v.__instance_id__ = 109
            elif self._Properties__count_3 == 14:
                v = CDispatch()
                v.__instance_id__ = 113
            elif self._Properties__count_3 == 15:
                v = CDispatch()
                v.__instance_id__ = 117
            elif self._Properties__count_3 == 16:
                v = CDispatch()
                v.__instance_id__ = 121
            elif self._Properties__count_3 == 17:
                v = CDispatch()
                v.__instance_id__ = 125
            elif self._Properties__count_3 == 18:
                v = CDispatch()
                v.__instance_id__ = 129
            elif self._Properties__count_3 == 19:
                v = CDispatch()
                v.__instance_id__ = 133
            elif self._Properties__count_3 == 20:
                v = CDispatch()
                v.__instance_id__ = 135
            elif self._Properties__count_3 == 21:
                v = CDispatch()
                v.__instance_id__ = 139
            self._Properties__count_3 += 1
            return v

    @Properties_.setter
    def Properties_(self, value):
        pass

    @property
    def HostResource(self):
        if self.__id__ == 269:
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_DiskDrive.CreationClassName="Msv\
m_DiskDrive",DeviceID="Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\\\\1",Sy\
stemCreationClassName="Msvm_ComputerSystem",SystemName="HV12OSDEMO1"'
            v += (v1,)
            return v
        elif self.__id__ == 299:
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
    def IsConnected(self):
        if self.__id__ == 311:
            return True

    @IsConnected.setter
    def IsConnected(self, value):
        pass

    @property
    def DefineVirtualSystem(self):
        if self.__id__ == 12:
            v = _wmi_method()
            v.__instance_id__ = 15
            return v

    @DefineVirtualSystem.setter
    def DefineVirtualSystem(self, value):
        pass

    @property
    def _properties(self):
        if self.__id__ == 149:
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
        elif self.__id__ == 52:
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
        if self.__id__ == 282:
            v = _wmi_method()
            v.__instance_id__ = 305
            return v

    @DestroyVirtualSystem.setter
    def DestroyVirtualSystem(self, value):
        pass

    @property
    def ModifyVirtualSystemResources(self):
        if self.__id__ == 12:
            ret_value = None
            if not hasattr(self, '_ModifyVirtualSystemResources_count_0'):
                self._ModifyVirtualSystemResources_count_0 = 0
            if self._ModifyVirtualSystemResources_count_0 == 0:
                v = _wmi_method()
                v.__instance_id__ = 20
            elif self._ModifyVirtualSystemResources_count_0 == 1:
                v = _wmi_method()
                v.__instance_id__ = 23
            self._ModifyVirtualSystemResources_count_0 += 1
            return v

    @ModifyVirtualSystemResources.setter
    def ModifyVirtualSystemResources(self, value):
        pass

    @property
    def Description(self):
        if self.__id__ == 256:
            return u'Initializing and Starting Virtual Machine'

    @Description.setter
    def Description(self, value):
        pass


    def associators(self, wmi_association_class='', wmi_result_class=''):
        if self.__id__ == 18 and wmi_result_class == 'Msvm_MemorySettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 19
            v.append(v1)
            return v
        elif self.__id__ == 18 and wmi_result_class ==\
 'Msvm_ProcessorSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 22
            v.append(v1)
            return v
        elif self.__id__ == 17 and wmi_result_class ==\
 'Msvm_VirtualSystemSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 18
            v.append(v1)
            return v
        elif self.__id__ == 39 and wmi_result_class ==\
 'MSVM_ResourceAllocationSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 40
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 41
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 42
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 43
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 44
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 45
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 46
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 47
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 48
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 49
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 50
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 51
            v.append(v1)
            return v
        elif self.__id__ == 38 and wmi_result_class ==\
 'Msvm_VirtualSystemSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 39
            v.append(v1)
            return v
        elif self.__id__ == 260 and wmi_result_class ==\
 'MSVM_ResourceAllocationSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 261
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 262
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 263
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 264
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 265
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 266
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 267
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 268
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 269
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 270
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 271
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 272
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 273
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 274
            v.append(v1)
            return v
        elif self.__id__ == 259 and wmi_result_class ==\
 'Msvm_VirtualSystemSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 260
            v.append(v1)
            return v
        elif self.__id__ == 290 and wmi_result_class ==\
 'MSVM_ResourceAllocationSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 291
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 292
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 293
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 294
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 295
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 296
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 297
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 298
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 299
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 300
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 301
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 302
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 303
            v.append(v1)
            v1 = _wmi_object()
            v1.__instance_id__ = 304
            v.append(v1)
            return v
        elif self.__id__ == 289 and wmi_result_class ==\
 'Msvm_VirtualSystemSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 290
            v.append(v1)
            return v


    def GetText_(self, iObjectTextFormat='<PyOleMissing object at\
 0x040917C0>', iFlags=0, objWbemNamedValueSet=None):
        if self.__id__ == 19 and iObjectTextFormat == 1:
            return u'<INSTANCE CLASSNAME="Msvm_MemorySettingData"><PROPERTY\
 NAME="__PATH" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>\\\\HV12OSDEMO1\\root\\virtualization:Msvm_MemorySetting\
Data.InstanceID="Microsoft:C887EED7-56F7-4DF6-BF80-0F25B5C79D8B\\\\4764334d-e0\
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
 TYPE="string"><VALUE>Msvm_MemorySettingData.InstanceID="Microsoft:C887EED7-56\
F7-4DF6-BF80-0F25B5C79D8B\\\\4764334d-e001-4176-82ee-5594ec9b530e"</VALUE></PR\
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
 TYPE="string"><VALUE>Microsoft:C887EED7-56F7-4DF6-BF80-0F25B5C79D8B\\4764334d\
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
        elif self.__id__ == 22 and iObjectTextFormat == 1:
            return u'<INSTANCE CLASSNAME="Msvm_ProcessorSettingData"><PROPERTY\
 NAME="__PATH" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ProcessorSett\
ingData.InstanceID="Microsoft:C887EED7-56F7-4DF6-BF80-0F25B5C79D8B\\\\b637f346\
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
 TYPE="string"><VALUE>Msvm_ProcessorSettingData.InstanceID="Microsoft:C887EED7\
-56F7-4DF6-BF80-0F25B5C79D8B\\\\b637f346-6a0e-4dec-af52-bd70cb80a21d\\\\0"</VA\
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
 TYPE="string"><VALUE>Microsoft:C887EED7-56F7-4DF6-BF80-0F25B5C79D8B\\b637f346\
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
        elif self.__id__ == 14 and iObjectTextFormat == 1:
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
 TYPE="string"><VALUE>openstack_unit_test_vm_fbae78d4-0c5a-4c43-9b3e-c3aacd72b\
401</VALUE></PROPERTY><PROPERTY NAME="ExternalDataRoot"\
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
        elif self.__id__ == 151 and iObjectTextFormat == 1:
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
 TYPE="string"><VALUE.ARRAY><VALUE>{61acc9eb-7a8b-43c1-8d30-9bbfafe249c5}</VAL\
UE></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>'
        elif self.__id__ == 54 and iObjectTextFormat == 1:
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
ationSettingData.InstanceID="Microsoft:C887EED7-56F7-4DF6-BF80-0F25B5C79D8B\
\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\0"</VALUE></PROPERTY><PROPERTY\
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
 TYPE="string"><VALUE.ARRAY><VALUE>1331d281-fe2b-4379-a094-27599c38662a</VALUE\
></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>'


class _wmi_method(object):

    def __init__(self, *args, **kwargs):
        pass

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__


    def __call__(self, *args, **kwargs):
        if len(args) == 0 and self.__id__ == 314:
            v = ()
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 0 and self.__id__ == 315:
            v = ()
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 0 and self.__id__ == 29 and\
 kwargs.get('IsPersistent') is True and kwargs.get('NodeAddress') ==\
 'iqn.2010-10.org.openstack:volume-ccb39627-34fa-4f47-968b-6580d9d7ee2b':
            v = ()
            v1 = CDispatch()
            v1.__instance_id__ = 30
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 0 and self.__id__ == 26 and\
 kwargs.get('TargetPortalAddress') == 'testtargetportal' and\
 kwargs.get('TargetPortalPortNumber') == '3260':
            v = ()
            v1 = CDispatch()
            v1.__instance_id__ = 27
            v += (v1,)
            v1 = None
            v += (v1,)
            return v
        elif len(args) == 1 and self.__id__ == 250 and args[0] == 2:
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ConcreteJob.InstanceID="F1C1B540\
-3C9D-4A18-82A5-F38DA0D10BEC"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v
        elif len(args) == 3 and self.__id__ == 15 and str(args[0]) == '[]' and\
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
 TYPE="string"><VALUE>openstack_unit_test_vm_fbae78d4-0c5a-4c43-9b3e-c3aacd72b\
401</VALUE></PROPERTY><PROPERTY NAME="ExternalDataRoot"\
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
="Msvm_ComputerSystem",Name="C887EED7-56F7-4DF6-BF80-0F25B5C79D8B"'
            v += (v1,)
            v1 = None
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 2 and self.__id__ == 20 and args[0] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="C887EED7-56F7-4DF6-BF80-0F25B5C79D8B"' and\
 str(args[1]) == '[u\'<INSTANCE CLASSNAME="Msvm_MemorySettingData"><PROPERTY\
 NAME="__PATH" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>\\\\\\\\HV12OSDEMO1\\\\root\\\\virtualization:Msvm_Memor\
ySettingData.InstanceID="Microsoft:C887EED7-56F7-4DF6-BF80-0F25B5C79D8B\
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
 TYPE="string"><VALUE>Msvm_MemorySettingData.InstanceID="Microsoft:C887EED7-56\
F7-4DF6-BF80-0F25B5C79D8B\\\\\\\\4764334d-e001-4176-82ee-5594ec9b530e"</VALUE>\
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
 TYPE="string"><VALUE>Microsoft:C887EED7-56F7-4DF6-BF80-0F25B5C79D8B\\\\476433\
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
        elif len(args) == 2 and self.__id__ == 23 and args[0] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="C887EED7-56F7-4DF6-BF80-0F25B5C79D8B"' and\
 str(args[1]) == '[u\'<INSTANCE\
 CLASSNAME="Msvm_ProcessorSettingData"><PROPERTY NAME="__PATH"\
 CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>\\\\\\\\HV12OSDEMO1\\\\root\\\\virtualization:Msvm_Proce\
ssorSettingData.InstanceID="Microsoft:C887EED7-56F7-4DF6-BF80-0F25B5C79D8B\
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
 TYPE="string"><VALUE>Msvm_ProcessorSettingData.InstanceID="Microsoft:C887EED7\
-56F7-4DF6-BF80-0F25B5C79D8B\\\\\\\\b637f346-6a0e-4dec-af52-bd70cb80a21d\
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
 TYPE="string"><VALUE>Microsoft:C887EED7-56F7-4DF6-BF80-0F25B5C79D8B\\\\b637f3\
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
        elif len(args) == 2 and self.__id__ == 240 and str(args[0]) ==\
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
 TYPE="string"><VALUE.ARRAY><VALUE>{61acc9eb-7a8b-43c1-8d30-9bbfafe249c5}</VAL\
UE></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="C887EED7-56F7-4DF6-BF80-0F25B5C79D8B"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:C887EED7-56F7-4DF6-BF80-0F25B5C79D8B\\\\589DB2EB-B0EE-4D93\
-A2E6-BD65483F8E75\\\\0"'
            v1.append(v2)
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 2 and self.__id__ == 246 and str(args[0]) ==\
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
 TYPE="string"><VALUE.ARRAY><VALUE>{c509604b-85ce-4b0b-959b-5279815c086c}</VAL\
UE></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="C887EED7-56F7-4DF6-BF80-0F25B5C79D8B"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_SyntheticEthernetPortSettingData\
.InstanceID="Microsoft:C887EED7-56F7-4DF6-BF80-0F25B5C79D8B\\\\7D461E50-8146-4\
B51-8E5C-6F87B80151EF"'
            v1.append(v2)
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 2 and self.__id__ == 145 and str(args[0]) ==\
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
rceAllocationSettingData.InstanceID="Microsoft:C887EED7-56F7-4DF6-BF80-0F25B5C\
79D8B\\\\\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\\\\\0"</VALUE></PROPERTY>\
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
 TYPE="string"><VALUE.ARRAY><VALUE>1331d281-fe2b-4379-a094-27599c38662a</VALUE\
></VALUE.ARRAY></PROPERTY.ARRAY><PROPERTY NAME="Weight"\
 CLASSORIGIN="CIM_ResourceAllocationSettingData"\
 TYPE="uint32"><VALUE>0</VALUE></PROPERTY></INSTANCE>\']' and args[1] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="C887EED7-56F7-4DF6-BF80-0F25B5C79D8B"':
            v = ()
            v1 = None
            v += (v1,)
            v1 = []
            v2 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:C887EED7-56F7-4DF6-BF80-0F25B5C79D8B\\\\83F8638B-8DCA-4152\
-9EDA-2CA8B33039B4\\\\0\\\\0\\\\D"'
            v1.append(v2)
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 1 and self.__id__ == 285 and args[0] == 3:
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ConcreteJob.InstanceID="9DB52552\
-94C7-4BBB-8364-09484D8A67E3"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v
        elif len(args) == 1 and self.__id__ == 305 and args[0] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="C887EED7-56F7-4DF6-BF80-0F25B5C79D8B"':
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ConcreteJob.InstanceID="E3D9EB9F\
-D8DF-4799-9DEB-B0845C771D20"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v


class CDispatch(object):

    def __init__(self, *args, **kwargs):
        pass

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__

    @property
    def InitiatorName(self):
        if self.__id__ == 32:
            return u'ROOT\\ISCSIPRT\\0000_0'
        elif self.__id__ == 33:
            return u'ROOT\\ISCSIPRT\\0000_0'

    @InitiatorName.setter
    def InitiatorName(self, value):
        pass

    @property
    def ScsiLun(self):
        if self.__id__ == 32:
            ret_value = None
            if not hasattr(self, '_ScsiLun_count_0'):
                self._ScsiLun_count_0 = 0
            if self._ScsiLun_count_0 == 0:
                v = 0
            elif self._ScsiLun_count_0 == 1:
                v = 0
            self._ScsiLun_count_0 += 1
            return v
        elif self.__id__ == 33:
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
        if self.__id__ == 32:
            return -1
        elif self.__id__ == 33:
            return 0

    @PartitionNumber.setter
    def PartitionNumber(self, value):
        pass

    @property
    def ScsiTargetId(self):
        if self.__id__ == 32:
            return 0
        elif self.__id__ == 33:
            return 0

    @ScsiTargetId.setter
    def ScsiTargetId(self, value):
        pass

    @property
    def DeviceNumber(self):
        if self.__id__ == 32:
            return -1
        elif self.__id__ == 33:
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
        if self.__id__ == 32:
            return u'0-0-0-00000000'
        elif self.__id__ == 33:
            return u'53f56307-b6bf-11d0-94f20a0c91efb8b'

    @DeviceInterfaceGuid.setter
    def DeviceInterfaceGuid(self, value):
        pass

    @property
    def DeviceType(self):
        if self.__id__ == 32:
            return 34
        elif self.__id__ == 33:
            return 7

    @DeviceType.setter
    def DeviceType(self, value):
        pass

    @property
    def LegacyName(self):
        if self.__id__ == 32:
            return u''
        elif self.__id__ == 33:
            return u'\\\\.\\PhysicalDrive1'

    @LegacyName.setter
    def LegacyName(self, value):
        pass

    @property
    def ScsiPathId(self):
        if self.__id__ == 32:
            return 0
        elif self.__id__ == 33:
            return 0

    @ScsiPathId.setter
    def ScsiPathId(self, value):
        pass

    @property
    def Value(self):
        if self.__id__ == 153:
            return\
 u'Microsoft:Definition\\BDE5D4D6-E450-46D2-B925-976CA3E989B4\\Default'
        elif self.__id__ == 157:
            return u'Microsoft Synthetic SCSI Controller'
        elif self.__id__ == 161:
            return None
        elif self.__id__ == 165:
            return u'SCSI Controller'
        elif self.__id__ == 169:
            return u'Settings for the Microsoft Synthetic SCSI Controller.'
        elif self.__id__ == 173:
            return None
        elif self.__id__ == 177:
            return u'1'
        elif self.__id__ == 181:
            return True
        elif self.__id__ == 185:
            return True
        elif self.__id__ == 189:
            return u'Microsoft:bde5d4d6-e450-46d2-b925-976ca3e989b4\\Root'
        elif self.__id__ == 193:
            return u'1'
        elif self.__id__ == 197:
            return u'Controllers'
        elif self.__id__ == 201:
            return None
        elif self.__id__ == 205:
            return None
        elif self.__id__ == 209:
            return None
        elif self.__id__ == 213:
            return u'SCSI Controller'
        elif self.__id__ == 217:
            return None
        elif self.__id__ == 221:
            return u'1'
        elif self.__id__ == 225:
            return 6
        elif self.__id__ == 229:
            return 0
        elif self.__id__ == 235:
            return None
        elif self.__id__ == 56:
            return\
 u'Microsoft:Definition\\353B3BE8-310C-4CF4-839E-4E1B14616136\\Default'
        elif self.__id__ == 60:
            return u'Microsoft Physical Disk Drive'
        elif self.__id__ == 64:
            return None
        elif self.__id__ == 68:
            return u'Hard Drive'
        elif self.__id__ == 72:
            return u'Settings for the Microsoft Physical Hard Drive.'
        elif self.__id__ == 76:
            return None
        elif self.__id__ == 80:
            return u'1'
        elif self.__id__ == 84:
            return True
        elif self.__id__ == 88:
            return True
        elif self.__id__ == 92:
            return u'Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\\Root'
        elif self.__id__ == 96:
            return u'1'
        elif self.__id__ == 100:
            return u'Hard Drives'
        elif self.__id__ == 104:
            return None
        elif self.__id__ == 108:
            return None
        elif self.__id__ == 112:
            return None
        elif self.__id__ == 116:
            return u'Hard Drive'
        elif self.__id__ == 120:
            return None
        elif self.__id__ == 124:
            return u'1'
        elif self.__id__ == 128:
            return 22
        elif self.__id__ == 132:
            return 0
        elif self.__id__ == 138:
            return None

    @Value.setter
    def Value(self, value):
        pass

    @property
    def TargetName(self):
        if self.__id__ == 32:
            return\
 u'iqn.2010-10.org.openstack:volume-ccb39627-34fa-4f47-968b-6580d9d7ee2b'
        elif self.__id__ == 33:
            return\
 u'iqn.2010-10.org.openstack:volume-ccb39627-34fa-4f47-968b-6580d9d7ee2b'

    @TargetName.setter
    def TargetName(self, value):
        pass

    @property
    def DeviceInterfaceName(self):
        if self.__id__ == 32:
            return u''
        elif self.__id__ == 33:
            return\
 u'\\\\?\\scsi#disk&ven_iet&prod_virtual-disk#1&1c121344&0&000001#{53f56307-b6\
bf-11d0-94f2-00a0c91efb8b}'

    @DeviceInterfaceName.setter
    def DeviceInterfaceName(self, value):
        pass

    @property
    def ScsiPortNumber(self):
        if self.__id__ == 32:
            return 3
        elif self.__id__ == 33:
            return 3

    @ScsiPortNumber.setter
    def ScsiPortNumber(self, value):
        pass


    def __call__(self, *args):
        if len(args) == 0 and self.__id__ == 241:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="C887EED7-56F7-4DF6-BF80-0F25B5C79D8B"'
        elif len(args) == 0 and self.__id__ == 21:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="C887EED7-56F7-4DF6-BF80-0F25B5C79D8B"'
        elif len(args) == 0 and self.__id__ == 24:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="C887EED7-56F7-4DF6-BF80-0F25B5C79D8B"'
        elif len(args) == 0 and self.__id__ == 247:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="C887EED7-56F7-4DF6-BF80-0F25B5C79D8B"'
        elif len(args) == 0 and self.__id__ == 142:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_DiskDrive.CreationClassName="Msv\
m_DiskDrive",DeviceID="Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\\\\1",Sy\
stemCreationClassName="Msvm_ComputerSystem",SystemName="HV12OSDEMO1"'
        elif len(args) == 0 and self.__id__ == 141:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ResourceAllocationSettingData.In\
stanceID="Microsoft:C887EED7-56F7-4DF6-BF80-0F25B5C79D8B\\\\83F8638B-8DCA-4152\
-9EDA-2CA8B33039B4\\\\0"'
        elif len(args) == 0 and self.__id__ == 146:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="C887EED7-56F7-4DF6-BF80-0F25B5C79D8B"'
        elif len(args) == 0 and self.__id__ == 306:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="C887EED7-56F7-4DF6-BF80-0F25B5C79D8B"'


    def Item(self, strName='<PyOleMissing object at 0x040917C0>', iFlags=0):
        if self.__id__ == 152 and strName == u'InstanceID':
            v = CDispatch()
            v.__instance_id__ = 153
            return v
        elif self.__id__ == 156 and strName == u'ResourceSubType':
            v = CDispatch()
            v.__instance_id__ = 157
            return v
        elif self.__id__ == 160 and strName == u'HostResource':
            v = CDispatch()
            v.__instance_id__ = 161
            return v
        elif self.__id__ == 164 and strName == u'ElementName':
            v = CDispatch()
            v.__instance_id__ = 165
            return v
        elif self.__id__ == 168 and strName == u'Description':
            v = CDispatch()
            v.__instance_id__ = 169
            return v
        elif self.__id__ == 172 and strName == u'Parent':
            v = CDispatch()
            v.__instance_id__ = 173
            return v
        elif self.__id__ == 176 and strName == u'VirtualQuantity':
            v = CDispatch()
            v.__instance_id__ = 177
            return v
        elif self.__id__ == 180 and strName == u'AutomaticDeallocation':
            v = CDispatch()
            v.__instance_id__ = 181
            return v
        elif self.__id__ == 184 and strName == u'AutomaticAllocation':
            v = CDispatch()
            v.__instance_id__ = 185
            return v
        elif self.__id__ == 188 and strName == u'PoolID':
            v = CDispatch()
            v.__instance_id__ = 189
            return v
        elif self.__id__ == 192 and strName == u'Reservation':
            v = CDispatch()
            v.__instance_id__ = 193
            return v
        elif self.__id__ == 196 and strName == u'AllocationUnits':
            v = CDispatch()
            v.__instance_id__ = 197
            return v
        elif self.__id__ == 200 and strName == u'MappingBehavior':
            v = CDispatch()
            v.__instance_id__ = 201
            return v
        elif self.__id__ == 204 and strName == u'Address':
            v = CDispatch()
            v.__instance_id__ = 205
            return v
        elif self.__id__ == 208 and strName == u'OtherResourceType':
            v = CDispatch()
            v.__instance_id__ = 209
            return v
        elif self.__id__ == 212 and strName == u'Caption':
            v = CDispatch()
            v.__instance_id__ = 213
            return v
        elif self.__id__ == 216 and strName == u'ConsumerVisibility':
            v = CDispatch()
            v.__instance_id__ = 217
            return v
        elif self.__id__ == 220 and strName == u'Limit':
            v = CDispatch()
            v.__instance_id__ = 221
            return v
        elif self.__id__ == 224 and strName == u'ResourceType':
            v = CDispatch()
            v.__instance_id__ = 225
            return v
        elif self.__id__ == 228 and strName == u'Weight':
            v = CDispatch()
            v.__instance_id__ = 229
            return v
        elif self.__id__ == 234 and strName == u'Connection':
            v = CDispatch()
            v.__instance_id__ = 235
            return v
        elif self.__id__ == 154 and strName == u'InstanceID':
            v = CDispatch()
            v.__instance_id__ = 155
            return v
        elif self.__id__ == 158 and strName == u'ResourceSubType':
            v = CDispatch()
            v.__instance_id__ = 159
            return v
        elif self.__id__ == 162 and strName == u'HostResource':
            v = CDispatch()
            v.__instance_id__ = 163
            return v
        elif self.__id__ == 166 and strName == u'ElementName':
            v = CDispatch()
            v.__instance_id__ = 167
            return v
        elif self.__id__ == 170 and strName == u'Description':
            v = CDispatch()
            v.__instance_id__ = 171
            return v
        elif self.__id__ == 174 and strName == u'Parent':
            v = CDispatch()
            v.__instance_id__ = 175
            return v
        elif self.__id__ == 178 and strName == u'VirtualQuantity':
            v = CDispatch()
            v.__instance_id__ = 179
            return v
        elif self.__id__ == 182 and strName == u'AutomaticDeallocation':
            v = CDispatch()
            v.__instance_id__ = 183
            return v
        elif self.__id__ == 186 and strName == u'AutomaticAllocation':
            v = CDispatch()
            v.__instance_id__ = 187
            return v
        elif self.__id__ == 190 and strName == u'PoolID':
            v = CDispatch()
            v.__instance_id__ = 191
            return v
        elif self.__id__ == 194 and strName == u'Reservation':
            v = CDispatch()
            v.__instance_id__ = 195
            return v
        elif self.__id__ == 198 and strName == u'AllocationUnits':
            v = CDispatch()
            v.__instance_id__ = 199
            return v
        elif self.__id__ == 202 and strName == u'MappingBehavior':
            v = CDispatch()
            v.__instance_id__ = 203
            return v
        elif self.__id__ == 206 and strName == u'Address':
            v = CDispatch()
            v.__instance_id__ = 207
            return v
        elif self.__id__ == 210 and strName == u'OtherResourceType':
            v = CDispatch()
            v.__instance_id__ = 211
            return v
        elif self.__id__ == 214 and strName == u'Caption':
            v = CDispatch()
            v.__instance_id__ = 215
            return v
        elif self.__id__ == 218 and strName == u'ConsumerVisibility':
            v = CDispatch()
            v.__instance_id__ = 219
            return v
        elif self.__id__ == 222 and strName == u'Limit':
            v = CDispatch()
            v.__instance_id__ = 223
            return v
        elif self.__id__ == 226 and strName == u'ResourceType':
            v = CDispatch()
            v.__instance_id__ = 227
            return v
        elif self.__id__ == 230 and strName == u'Weight':
            v = CDispatch()
            v.__instance_id__ = 231
            return v
        elif self.__id__ == 232 and strName == u'VirtualSystemIdentifiers':
            v = CDispatch()
            v.__instance_id__ = 233
            return v
        elif self.__id__ == 236 and strName == u'Connection':
            v = CDispatch()
            v.__instance_id__ = 237
            return v
        elif self.__id__ == 55 and strName == u'InstanceID':
            v = CDispatch()
            v.__instance_id__ = 56
            return v
        elif self.__id__ == 59 and strName == u'ResourceSubType':
            v = CDispatch()
            v.__instance_id__ = 60
            return v
        elif self.__id__ == 63 and strName == u'HostResource':
            v = CDispatch()
            v.__instance_id__ = 64
            return v
        elif self.__id__ == 67 and strName == u'ElementName':
            v = CDispatch()
            v.__instance_id__ = 68
            return v
        elif self.__id__ == 71 and strName == u'Description':
            v = CDispatch()
            v.__instance_id__ = 72
            return v
        elif self.__id__ == 75 and strName == u'Parent':
            v = CDispatch()
            v.__instance_id__ = 76
            return v
        elif self.__id__ == 79 and strName == u'VirtualQuantity':
            v = CDispatch()
            v.__instance_id__ = 80
            return v
        elif self.__id__ == 83 and strName == u'AutomaticDeallocation':
            v = CDispatch()
            v.__instance_id__ = 84
            return v
        elif self.__id__ == 87 and strName == u'AutomaticAllocation':
            v = CDispatch()
            v.__instance_id__ = 88
            return v
        elif self.__id__ == 91 and strName == u'PoolID':
            v = CDispatch()
            v.__instance_id__ = 92
            return v
        elif self.__id__ == 95 and strName == u'Reservation':
            v = CDispatch()
            v.__instance_id__ = 96
            return v
        elif self.__id__ == 99 and strName == u'AllocationUnits':
            v = CDispatch()
            v.__instance_id__ = 100
            return v
        elif self.__id__ == 103 and strName == u'MappingBehavior':
            v = CDispatch()
            v.__instance_id__ = 104
            return v
        elif self.__id__ == 107 and strName == u'Address':
            v = CDispatch()
            v.__instance_id__ = 108
            return v
        elif self.__id__ == 111 and strName == u'OtherResourceType':
            v = CDispatch()
            v.__instance_id__ = 112
            return v
        elif self.__id__ == 115 and strName == u'Caption':
            v = CDispatch()
            v.__instance_id__ = 116
            return v
        elif self.__id__ == 119 and strName == u'ConsumerVisibility':
            v = CDispatch()
            v.__instance_id__ = 120
            return v
        elif self.__id__ == 123 and strName == u'Limit':
            v = CDispatch()
            v.__instance_id__ = 124
            return v
        elif self.__id__ == 127 and strName == u'ResourceType':
            v = CDispatch()
            v.__instance_id__ = 128
            return v
        elif self.__id__ == 131 and strName == u'Weight':
            v = CDispatch()
            v.__instance_id__ = 132
            return v
        elif self.__id__ == 137 and strName == u'Connection':
            v = CDispatch()
            v.__instance_id__ = 138
            return v
        elif self.__id__ == 57 and strName == u'InstanceID':
            v = CDispatch()
            v.__instance_id__ = 58
            return v
        elif self.__id__ == 61 and strName == u'ResourceSubType':
            v = CDispatch()
            v.__instance_id__ = 62
            return v
        elif self.__id__ == 65 and strName == u'HostResource':
            v = CDispatch()
            v.__instance_id__ = 66
            return v
        elif self.__id__ == 69 and strName == u'ElementName':
            v = CDispatch()
            v.__instance_id__ = 70
            return v
        elif self.__id__ == 73 and strName == u'Description':
            v = CDispatch()
            v.__instance_id__ = 74
            return v
        elif self.__id__ == 77 and strName == u'Parent':
            v = CDispatch()
            v.__instance_id__ = 78
            return v
        elif self.__id__ == 81 and strName == u'VirtualQuantity':
            v = CDispatch()
            v.__instance_id__ = 82
            return v
        elif self.__id__ == 85 and strName == u'AutomaticDeallocation':
            v = CDispatch()
            v.__instance_id__ = 86
            return v
        elif self.__id__ == 89 and strName == u'AutomaticAllocation':
            v = CDispatch()
            v.__instance_id__ = 90
            return v
        elif self.__id__ == 93 and strName == u'PoolID':
            v = CDispatch()
            v.__instance_id__ = 94
            return v
        elif self.__id__ == 97 and strName == u'Reservation':
            v = CDispatch()
            v.__instance_id__ = 98
            return v
        elif self.__id__ == 101 and strName == u'AllocationUnits':
            v = CDispatch()
            v.__instance_id__ = 102
            return v
        elif self.__id__ == 105 and strName == u'MappingBehavior':
            v = CDispatch()
            v.__instance_id__ = 106
            return v
        elif self.__id__ == 109 and strName == u'Address':
            v = CDispatch()
            v.__instance_id__ = 110
            return v
        elif self.__id__ == 113 and strName == u'OtherResourceType':
            v = CDispatch()
            v.__instance_id__ = 114
            return v
        elif self.__id__ == 117 and strName == u'Caption':
            v = CDispatch()
            v.__instance_id__ = 118
            return v
        elif self.__id__ == 121 and strName == u'ConsumerVisibility':
            v = CDispatch()
            v.__instance_id__ = 122
            return v
        elif self.__id__ == 125 and strName == u'Limit':
            v = CDispatch()
            v.__instance_id__ = 126
            return v
        elif self.__id__ == 129 and strName == u'ResourceType':
            v = CDispatch()
            v.__instance_id__ = 130
            return v
        elif self.__id__ == 133 and strName == u'Weight':
            v = CDispatch()
            v.__instance_id__ = 134
            return v
        elif self.__id__ == 135 and strName == u'VirtualSystemIdentifiers':
            v = CDispatch()
            v.__instance_id__ = 136
            return v
        elif self.__id__ == 139 and strName == u'Connection':
            v = CDispatch()
            v.__instance_id__ = 140
            return v
