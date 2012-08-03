# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 Cloudbase Solutions Srl
# All Rights Reserved.
#
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

"""
Management base class for Hyper-V operations.
"""
from nova import log as logging
from nova import flags
import constants

LOG = logging.getLogger(__name__)

class BaseOps(object):
    def __init__(self, wmi):
        self._wmi = wmi
        self.__conn = None
        self.__conn_v2 = None
        self.__conn_cimv2 = None
                
    @property
    def _conn(self):
        if self.__conn is None:
            self.__conn = self._wmi.WMI(moniker='//./root/virtualization')
        return self.__conn
        
    @property
    def _conn_v2(self):
        if self.__conn_v2 is None:
            self.__conn_v2 = self._wmi.WMI(moniker='//./root/virtualization/v2')
        return self.__conn_v2
            
    @property
    def _conn_cimv2(self):
        if self.__conn_cimv2 is None:
            self.__conn_cimv2 = self._wmi.WMI(moniker='//./root/cimv2')
        return self.__conn_cimv2        
        