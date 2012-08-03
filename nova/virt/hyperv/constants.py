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
Constants used in ops classes
"""

from nova.compute import power_state

HYPERV_POWER_STATE = {
    3: power_state.SHUTDOWN,
    2: power_state.RUNNING,
    32768: power_state.PAUSED,
    32769: power_state.SUSPENDED    
}

REQ_POWER_STATE = {
    'Enabled': 2,
    'Disabled': 3,
    'Reboot': 10,
    'Reset': 11,
    'Paused': 32768,
    'Suspended': 32769,
}

WMI_JOB_STATUS_STARTED = 4096
WMI_JOB_STATE_RUNNING = 4
WMI_JOB_STATE_COMPLETED = 7
