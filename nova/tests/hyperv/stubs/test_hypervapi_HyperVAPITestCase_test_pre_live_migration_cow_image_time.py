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


def sleep(seconds=0):
    if seconds == 0.1:
        ret_value = None
        global _sleep_count_0
        if not '_sleep_count_0' in globals():
            _sleep_count_0 = 0
        if _sleep_count_0 == 0:
            v = None
        elif _sleep_count_0 == 1:
            v = None
        elif _sleep_count_0 == 2:
            v = None
        elif _sleep_count_0 == 3:
            v = None
        elif _sleep_count_0 == 4:
            v = None
        elif _sleep_count_0 == 5:
            v = None
        elif _sleep_count_0 == 6:
            v = None
        elif _sleep_count_0 == 7:
            v = None
        _sleep_count_0 += 1
        return v
