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
        elif _sleep_count_0 == 8:
            v = None
        elif _sleep_count_0 == 9:
            v = None
        elif _sleep_count_0 == 10:
            v = None
        elif _sleep_count_0 == 11:
            v = None
        elif _sleep_count_0 == 12:
            v = None
        elif _sleep_count_0 == 13:
            v = None
        elif _sleep_count_0 == 14:
            v = None
        elif _sleep_count_0 == 15:
            v = None
        elif _sleep_count_0 == 16:
            v = None
        elif _sleep_count_0 == 17:
            v = None
        elif _sleep_count_0 == 18:
            v = None
        elif _sleep_count_0 == 19:
            v = None
        elif _sleep_count_0 == 20:
            v = None
        elif _sleep_count_0 == 21:
            v = None
        elif _sleep_count_0 == 22:
            v = None
        _sleep_count_0 += 1
        return v


def gmtime(*p):
    if len(p) == 0:
        return 'time.struct_time(tm_year=2013, tm_mon=1, tm_mday=3,\
 tm_hour=20, tm_min=12, tm_sec=14, tm_wday=3, tm_yday=3, tm_isdst=0)'


def strftime(*p):
    if len(p) == 2 and p[0] == '%Y-%m-%dT%H:%M:%SZ' and str(p[1]) ==\
 'time.struct_time(tm_year=2013, tm_mon=1, tm_mday=3, tm_hour=20, tm_min=12,\
 tm_sec=14, tm_wday=3, tm_yday=3, tm_isdst=0)':
        return '2013-01-03T20:12:14Z'
