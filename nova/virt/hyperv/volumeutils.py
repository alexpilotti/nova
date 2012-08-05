# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright 2012 Pedro Navarro Perez
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
Helper methods for operations related to the management of volumes,
and storage repositories
"""

from nova import flags
from nova import log as logging
from nova import utils

from _winreg import (HKEY_LOCAL_MACHINE, KEY_ALL_ACCESS,
                     OpenKey, CloseKey, QueryValueEx)

LOG = logging.getLogger(__name__)
FLAGS = flags.FLAGS

class VolumeUtils(object):
        def __init__(self, time, driver, block_device):
            self._time = time
            self._driver = driver
            self._block_device = block_device
            self.attaching_volume_retry_count = FLAGS.hyperv_attaching_volume_retry_count
            self.wait_between_attach_retry = FLAGS.hyperv_wait_between_attach_retry
    
        def execute(self, *args, **kwargs):
            return utils.execute(*args, **kwargs)
        
        def _get_iscsi_initiator(self, cim_conn):
            """Get iscsi initiator name for this machine"""
            computer_system = cim_conn.Win32_ComputerSystem()[0]
            hostname = computer_system.name
            keypath = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\iSCSI\Discovery"
            try:
                key = OpenKey(HKEY_LOCAL_MACHINE, keypath, 0, KEY_ALL_ACCESS)
                temp = QueryValueEx(key, 'DefaultInitiatorName')
                initiator_name = str(temp[0])
                CloseKey(key) 
            except:
                LOG.info(_("The ISCSI initiator name can't be found. Choosing the default one"))
                computer_system = self.cim_conn.Win32_ComputerSystem()[0]
                initiator_name = "iqn.1991-05.com.microsoft:" + hostname.lower()
            return {
                'ip': FLAGS.my_ip,
                'initiator': initiator_name,
            }
        
        def _login_storage_target (self, target_lun, target_iqn, target_portal):
            """Add target portal, list targets and logins to the target"""
            separator = target_portal.find(':')
            target_address = target_portal[:separator]
            target_port = target_portal[separator + 1:]
            #Adding target portal to iscsi initiator. Sending targets
            self.execute('iscsicli.exe', 'AddTargetPortal', target_address, target_port, '*',
                          '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', close_fds=False)
            #Listing targets
            self.execute('iscsicli.exe', 'LisTargets', close_fds=False)
            #Sending login
            self.execute('iscsicli.exe', 'qlogintarget', target_iqn, close_fds=False)
            #Waiting the disk to be mounted. Research this
            self._time.sleep(self.wait_between_attach_retry)
            
        def _logout_storage_target(self, target_iqn):
            """ Logs out storage target through its session id """
            initiator_session = self._wmi_conn.query(
                    "SELECT * FROM MSiSCSIInitiator_SessionClass \
                    WHERE TargetName='" + target_iqn + "'")[0]
            session_id = initiator_session.SessionId
            self._execute_log_out(session_id)
            
        def _execute_log_out (self, session_id):
            """ Executes log out of the session described by its session ID """
            self.execute('iscsicli.exe', 'logouttarget', session_id, close_fds=False)
            
        def _volume_in_mapping(self, mount_device, block_device_info):
            block_device_list = [self._block_device.strip_dev(vol['mount_device'])
                                 for vol in
                                 self._driver.block_device_info_get_mapping(
                                     block_device_info)]
            swap = self._driver.block_device_info_get_swap(block_device_info)
            if self._driver.swap_is_usable(swap):
                block_device_list.append(
                    self._block_device.strip_dev(swap['device_name']))
            block_device_list += [self._block_device.strip_dev(ephemeral['device_name'])
                                  for ephemeral in
                                  self._driver.block_device_info_get_ephemerals(
                                      block_device_info)]
        
            LOG.debug(_("block_device_list %s"), block_device_list)
            return self._block_device.strip_dev(mount_device) in block_device_list