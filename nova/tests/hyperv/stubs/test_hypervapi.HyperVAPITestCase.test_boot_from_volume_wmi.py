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
            v.__instance_id__ = 30
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
            v.__instance_id__ = 27
        _WMI_count_3 += 1
        return v
    elif moniker ==\
 u'//HV12OSDEMO1/root/virtualization:Msvm_ConcreteJob.InstanceID="EC47481D-5C0\
C-416E-A7E4-2FFCDC2D9FBE"':
        ret_value = None
        global _WMI_count_4
        if not '_WMI_count_4' in globals():
            _WMI_count_4 = 0
        if _WMI_count_4 == 0:
            v = _wmi_object()
            v.__instance_id__ = 55
        elif _WMI_count_4 == 1:
            v = _wmi_object()
            v.__instance_id__ = 56
        _WMI_count_4 += 1
        return v


class _wmi_namespace(object):

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__

    @property
    def Msvm_VirtualSystemManagementService(self):
        if self.__id__ == 9:
            v = _wmi_class()
            v.__instance_id__ = 11
            return v
        elif self.__id__ == 27:
            v = _wmi_class()
            v.__instance_id__ = 33
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
            self._Msvm_ComputerSystem_count_0 += 1
            return v
        elif self.__id__ == 27:
            ret_value = None
            if not hasattr(self, '_Msvm_ComputerSystem_count_1'):
                self._Msvm_ComputerSystem_count_1 = 0
            if self._Msvm_ComputerSystem_count_1 == 0:
                v = _wmi_class()
                v.__instance_id__ = 28
            elif self._Msvm_ComputerSystem_count_1 == 1:
                v = _wmi_class()
                v.__instance_id__ = 31
            elif self._Msvm_ComputerSystem_count_1 == 2:
                v = _wmi_class()
                v.__instance_id__ = 35
            elif self._Msvm_ComputerSystem_count_1 == 3:
                v = _wmi_class()
                v.__instance_id__ = 38
            self._Msvm_ComputerSystem_count_1 += 1
            return v

    @Msvm_ComputerSystem.setter
    def Msvm_ComputerSystem(self, value):
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
    def MSFT_iSCSITargetPortal(self):
        if self.__id__ == 7:
            v = _wmi_class()
            v.__instance_id__ = 25
            return v

    @MSFT_iSCSITargetPortal.setter
    def MSFT_iSCSITargetPortal(self, value):
        pass

    def query(self, wql, instance_of=None, fields='[]'):
        if self.__id__ == 3 and wql == 'SELECT * FROM\
 MSiSCSIInitiator_SessionClass                     WHERE\
 TargetName=\'iqn.2010-10.org.openstack:volume-8957e088-dbee-4216-8056-978353a\
3e737\'':
            v = []
            return v


class _wmi_class(object):

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

    def __call__(self, fields='[]', **where_clause):
        if self.__id__ == 5:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 6
            v.append(v1)
            return v
        elif self.__id__ == 10 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_192ae3d3-d9de-4024-911b-f96784464895':
            v = []
            return v
        elif self.__id__ == 16 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_192ae3d3-d9de-4024-911b-f96784464895':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 17
            v.append(v1)
            return v
        elif self.__id__ == 11:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 12
            v.append(v1)
            return v
        elif self.__id__ == 28 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_192ae3d3-d9de-4024-911b-f96784464895':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 29
            v.append(v1)
            return v
        elif self.__id__ == 31 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_192ae3d3-d9de-4024-911b-f96784464895':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 32
            v.append(v1)
            return v
        elif self.__id__ == 35 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_192ae3d3-d9de-4024-911b-f96784464895':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 36
            v.append(v1)
            return v
        elif self.__id__ == 38 and where_clause.get('ElementName') ==\
 'openstack_unit_test_vm_192ae3d3-d9de-4024-911b-f96784464895':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 39
            v.append(v1)
            return v
        elif self.__id__ == 33:
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 34
            v.append(v1)
            return v

    def new(self, **kwargs):
        if self.__id__ == 13:
            v = _wmi_object()
            v.__instance_id__ = 14
            return v


class _wmi_method(object):

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__

    def __call__(self, *args, **kwargs):
        if len(args) == 3 and self.__id__ == 15 and str(args[0]) == '[]' and\
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
 TYPE="string"><VALUE>openstack_unit_test_vm_192ae3d3-d9de-4024-911b-f96784464\
895</VALUE></PROPERTY><PROPERTY NAME="ExternalDataRoot"\
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
="Msvm_ComputerSystem",Name="BAA72B74-BBD6-4F0B-88B0-4E3C8242C817"'
            v += (v1,)
            v1 = None
            v += (v1,)
            v1 = 0
            v += (v1,)
            return v
        elif len(args) == 2 and self.__id__ == 20 and args[0] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="BAA72B74-BBD6-4F0B-88B0-4E3C8242C817"' and\
 str(args[1]) == '[u\'<INSTANCE CLASSNAME="Msvm_MemorySettingData"><PROPERTY\
 NAME="__PATH" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>\\\\\\\\HV12OSDEMO1\\\\root\\\\virtualization:Msvm_Memor\
ySettingData.InstanceID="Microsoft:BAA72B74-BBD6-4F0B-88B0-4E3C8242C817\
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
 TYPE="string"><VALUE>Msvm_MemorySettingData.InstanceID="Microsoft:BAA72B74-BB\
D6-4F0B-88B0-4E3C8242C817\\\\\\\\4764334d-e001-4176-82ee-5594ec9b530e"</VALUE>\
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
 TYPE="string"><VALUE>Microsoft:BAA72B74-BBD6-4F0B-88B0-4E3C8242C817\\\\476433\
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
="Msvm_ComputerSystem",Name="BAA72B74-BBD6-4F0B-88B0-4E3C8242C817"' and\
 str(args[1]) == '[u\'<INSTANCE\
 CLASSNAME="Msvm_ProcessorSettingData"><PROPERTY NAME="__PATH"\
 CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>\\\\\\\\HV12OSDEMO1\\\\root\\\\virtualization:Msvm_Proce\
ssorSettingData.InstanceID="Microsoft:BAA72B74-BBD6-4F0B-88B0-4E3C8242C817\
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
 TYPE="string"><VALUE>Msvm_ProcessorSettingData.InstanceID="Microsoft:BAA72B74\
-BBD6-4F0B-88B0-4E3C8242C817\\\\\\\\b637f346-6a0e-4dec-af52-bd70cb80a21d\
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
 TYPE="string"><VALUE>Microsoft:BAA72B74-BBD6-4F0B-88B0-4E3C8242C817\\\\b637f3\
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
        elif len(args) == 1 and self.__id__ == 37 and args[0] == 3:
            v = ()
            v1 = None
            v += (v1,)
            v1 = 32775
            v += (v1,)
            return v
        elif len(args) == 1 and self.__id__ == 53 and args[0] ==\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="BAA72B74-BBD6-4F0B-88B0-4E3C8242C817"':
            v = ()
            v1 =\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ConcreteJob.InstanceID="EC47481D\
-5C0C-416E-A7E4-2FFCDC2D9FBE"'
            v += (v1,)
            v1 = 4096
            v += (v1,)
            return v


class _wmi_object(object):

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__

    @property
    def RequestStateChange(self):
        if self.__id__ == 36:
            v = _wmi_method()
            v.__instance_id__ = 37
            return v

    @RequestStateChange.setter
    def RequestStateChange(self, value):
        pass

    @property
    def DestroyVirtualSystem(self):
        if self.__id__ == 34:
            v = _wmi_method()
            v.__instance_id__ = 53
            return v

    @DestroyVirtualSystem.setter
    def DestroyVirtualSystem(self, value):
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
        if self.__id__ == 17:
            ret_value = None
            if not hasattr(self, '_path__count_0'):
                self._path__count_0 = 0
            if self._path__count_0 == 0:
                v = CDispatch()
                v.__instance_id__ = 21
            elif self._path__count_0 == 1:
                v = CDispatch()
                v.__instance_id__ = 24
            self._path__count_0 += 1
            return v
        elif self.__id__ == 32:
            v = CDispatch()
            v.__instance_id__ = 54
            return v

    @path_.setter
    def path_(self, value):
        pass

    @property
    def ResourceSubType(self):
        if self.__id__ == 41:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_0'):
                self._ResourceSubType_count_0 = 0
            if self._ResourceSubType_count_0 == 0:
                v = u'Microsoft Virtual Keyboard'
            elif self._ResourceSubType_count_0 == 1:
                v = u'Microsoft Virtual Keyboard'
            elif self._ResourceSubType_count_0 == 2:
                v = u'Microsoft Virtual Keyboard'
            self._ResourceSubType_count_0 += 1
            return v
        elif self.__id__ == 42:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_1'):
                self._ResourceSubType_count_1 = 0
            if self._ResourceSubType_count_1 == 0:
                v = u'Microsoft Virtual PS2 Mouse'
            elif self._ResourceSubType_count_1 == 1:
                v = u'Microsoft Virtual PS2 Mouse'
            elif self._ResourceSubType_count_1 == 2:
                v = u'Microsoft Virtual PS2 Mouse'
            self._ResourceSubType_count_1 += 1
            return v
        elif self.__id__ == 43:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_2'):
                self._ResourceSubType_count_2 = 0
            if self._ResourceSubType_count_2 == 0:
                v = u'Microsoft S3 Display Controller'
            elif self._ResourceSubType_count_2 == 1:
                v = u'Microsoft S3 Display Controller'
            elif self._ResourceSubType_count_2 == 2:
                v = u'Microsoft S3 Display Controller'
            self._ResourceSubType_count_2 += 1
            return v
        elif self.__id__ == 44:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_3'):
                self._ResourceSubType_count_3 = 0
            if self._ResourceSubType_count_3 == 0:
                v = u'Microsoft Synthetic Diskette Drive'
            elif self._ResourceSubType_count_3 == 1:
                v = u'Microsoft Synthetic Diskette Drive'
            elif self._ResourceSubType_count_3 == 2:
                v = u'Microsoft Synthetic Diskette Drive'
            self._ResourceSubType_count_3 += 1
            return v
        elif self.__id__ == 45:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_4'):
                self._ResourceSubType_count_4 = 0
            if self._ResourceSubType_count_4 == 0:
                v = None
            elif self._ResourceSubType_count_4 == 1:
                v = None
            elif self._ResourceSubType_count_4 == 2:
                v = None
            self._ResourceSubType_count_4 += 1
            return v
        elif self.__id__ == 46:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_5'):
                self._ResourceSubType_count_5 = 0
            if self._ResourceSubType_count_5 == 0:
                v = u'Microsoft Serial Controller'
            elif self._ResourceSubType_count_5 == 1:
                v = u'Microsoft Serial Controller'
            elif self._ResourceSubType_count_5 == 2:
                v = u'Microsoft Serial Controller'
            self._ResourceSubType_count_5 += 1
            return v
        elif self.__id__ == 47:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_6'):
                self._ResourceSubType_count_6 = 0
            if self._ResourceSubType_count_6 == 0:
                v = u'Microsoft Serial Port'
            elif self._ResourceSubType_count_6 == 1:
                v = u'Microsoft Serial Port'
            elif self._ResourceSubType_count_6 == 2:
                v = u'Microsoft Serial Port'
            self._ResourceSubType_count_6 += 1
            return v
        elif self.__id__ == 48:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_7'):
                self._ResourceSubType_count_7 = 0
            if self._ResourceSubType_count_7 == 0:
                v = u'Microsoft Serial Port'
            elif self._ResourceSubType_count_7 == 1:
                v = u'Microsoft Serial Port'
            elif self._ResourceSubType_count_7 == 2:
                v = u'Microsoft Serial Port'
            self._ResourceSubType_count_7 += 1
            return v
        elif self.__id__ == 49:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_8'):
                self._ResourceSubType_count_8 = 0
            if self._ResourceSubType_count_8 == 0:
                v = u'Microsoft Emulated IDE Controller'
            elif self._ResourceSubType_count_8 == 1:
                v = u'Microsoft Emulated IDE Controller'
            elif self._ResourceSubType_count_8 == 2:
                v = u'Microsoft Emulated IDE Controller'
            self._ResourceSubType_count_8 += 1
            return v
        elif self.__id__ == 50:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_9'):
                self._ResourceSubType_count_9 = 0
            if self._ResourceSubType_count_9 == 0:
                v = u'Microsoft Emulated IDE Controller'
            elif self._ResourceSubType_count_9 == 1:
                v = u'Microsoft Emulated IDE Controller'
            elif self._ResourceSubType_count_9 == 2:
                v = u'Microsoft Emulated IDE Controller'
            self._ResourceSubType_count_9 += 1
            return v
        elif self.__id__ == 51:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_10'):
                self._ResourceSubType_count_10 = 0
            if self._ResourceSubType_count_10 == 0:
                v = u'Microsoft Synthetic Mouse'
            elif self._ResourceSubType_count_10 == 1:
                v = u'Microsoft Synthetic Mouse'
            elif self._ResourceSubType_count_10 == 2:
                v = u'Microsoft Synthetic Mouse'
            self._ResourceSubType_count_10 += 1
            return v
        elif self.__id__ == 52:
            ret_value = None
            if not hasattr(self, '_ResourceSubType_count_11'):
                self._ResourceSubType_count_11 = 0
            if self._ResourceSubType_count_11 == 0:
                v = u'Microsoft Synthetic Display Controller'
            elif self._ResourceSubType_count_11 == 1:
                v = u'Microsoft Synthetic Display Controller'
            elif self._ResourceSubType_count_11 == 2:
                v = u'Microsoft Synthetic Display Controller'
            self._ResourceSubType_count_11 += 1
            return v

    @ResourceSubType.setter
    def ResourceSubType(self, value):
        pass

    @property
    def Version(self):
        if self.__id__ == 6:
            return u'6.2.9200'

    @Version.setter
    def Version(self, value):
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
    def JobState(self):
        if self.__id__ == 55:
            return 4
        elif self.__id__ == 56:
            ret_value = None
            if not hasattr(self, '_JobState_count_1'):
                self._JobState_count_1 = 0
            if self._JobState_count_1 == 0:
                v = 7
            elif self._JobState_count_1 == 1:
                v = 7
            self._JobState_count_1 += 1
            return v

    @JobState.setter
    def JobState(self, value):
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
        elif self.__id__ == 40 and wmi_result_class ==\
 'MSVM_ResourceAllocationSettingData':
            v = []
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
            v1 = _wmi_object()
            v1.__instance_id__ = 52
            v.append(v1)
            return v
        elif self.__id__ == 39 and wmi_result_class ==\
 'Msvm_VirtualSystemSettingData':
            v = []
            v1 = _wmi_object()
            v1.__instance_id__ = 40
            v.append(v1)
            return v

    def GetText_(self, iObjectTextFormat='<PyOleMissing object at\
 0x04091890>', iFlags=0, objWbemNamedValueSet=None):
        if self.__id__ == 19 and iObjectTextFormat == 1:
            return u'<INSTANCE CLASSNAME="Msvm_MemorySettingData"><PROPERTY\
 NAME="__PATH" CLASSORIGIN="___SYSTEM"\
 TYPE="string"><VALUE>\\\\HV12OSDEMO1\\root\\virtualization:Msvm_MemorySetting\
Data.InstanceID="Microsoft:BAA72B74-BBD6-4F0B-88B0-4E3C8242C817\\\\4764334d-e0\
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
 TYPE="string"><VALUE>Msvm_MemorySettingData.InstanceID="Microsoft:BAA72B74-BB\
D6-4F0B-88B0-4E3C8242C817\\\\4764334d-e001-4176-82ee-5594ec9b530e"</VALUE></PR\
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
 TYPE="string"><VALUE>Microsoft:BAA72B74-BBD6-4F0B-88B0-4E3C8242C817\\4764334d\
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
ingData.InstanceID="Microsoft:BAA72B74-BBD6-4F0B-88B0-4E3C8242C817\\\\b637f346\
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
 TYPE="string"><VALUE>Msvm_ProcessorSettingData.InstanceID="Microsoft:BAA72B74\
-BBD6-4F0B-88B0-4E3C8242C817\\\\b637f346-6a0e-4dec-af52-bd70cb80a21d\\\\0"</VA\
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
 TYPE="string"><VALUE>Microsoft:BAA72B74-BBD6-4F0B-88B0-4E3C8242C817\\b637f346\
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
 TYPE="string"><VALUE>openstack_unit_test_vm_192ae3d3-d9de-4024-911b-f96784464\
895</VALUE></PROPERTY><PROPERTY NAME="ExternalDataRoot"\
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


class CDispatch(object):

    @property
    def __id__(self):
        if not hasattr(self, '__instance_id__'):
            self.__instance_id__ = 1
        return self.__instance_id__

    def __call__(self, *args):
        if len(args) == 0 and self.__id__ == 21:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="BAA72B74-BBD6-4F0B-88B0-4E3C8242C817"'
        elif len(args) == 0 and self.__id__ == 24:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="BAA72B74-BBD6-4F0B-88B0-4E3C8242C817"'
        elif len(args) == 0 and self.__id__ == 54:
            return\
 u'\\\\HV12OSDEMO1\\root\\virtualization:Msvm_ComputerSystem.CreationClassName\
="Msvm_ComputerSystem",Name="BAA72B74-BBD6-4F0B-88B0-4E3C8242C817"'
