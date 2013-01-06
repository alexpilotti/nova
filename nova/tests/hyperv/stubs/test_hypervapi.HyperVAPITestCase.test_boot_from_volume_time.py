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
        return None


def gmtime(*p):
    if len(p) == 0:
        return 'time.struct_time(tm_year=2013, tm_mon=1, tm_mday=3,\
 tm_hour=20, tm_min=11, tm_sec=26, tm_wday=3, tm_yday=3, tm_isdst=0)'


def strftime(*p):
    if len(p) == 2 and p[0] == '%Y-%m-%dT%H:%M:%SZ' and str(p[1]) ==\
 'time.struct_time(tm_year=2013, tm_mon=1, tm_mday=3, tm_hour=20, tm_min=11,\
 tm_sec=26, tm_wday=3, tm_yday=3, tm_isdst=0)':
        return '2013-01-03T20:11:26Z'
