# vim: tabstop=4 shiftwidth=4 softtabstop=4

#  Copyright 2012 Cloudbase Solutions Srl
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

import inspect


class MockProxy(object):
    def __init__(self, wrapped, id_sequence=None):
        self._wrapped = wrapped
        self._recorded_values = {}
        self._recorded_values_ret = {}
        self._types = {}

        if not id_sequence:
            self._id_sequence = [1]
        else:
            self._id_sequence = id_sequence
            self._id_sequence[0] += 1
        self._instance_id = self._id_sequence[0]

    def _get_proxy_object(self, obj):
        if isinstance(obj, list):
            p = [self._get_proxy_object(i) for i in obj]
        elif isinstance(obj, tuple):
            p = tuple(self._get_proxy_object(i) for i in obj)
        elif isinstance(obj, dict):
            p = {}
            for k, v in obj.items():
                p[self._get_proxy_object(k)] = self._get_proxy_object(v)
        elif hasattr(obj, '__dict__'):
            p = MockProxy(obj, self._id_sequence)
        else:
            p = obj
        return p

    def __getattr__(self, name):
        if name in ['_wrapped', '_instance_id', '_id_sequence']:
            return object.__getattribute__(self, name)
        else:
            attr = getattr(self._wrapped, name)
            if inspect.isfunction(attr) or inspect.ismethod(attr) or \
                    inspect.isbuiltin(attr):
                def newfunc(*args, **kwargs):
                    result = attr(*args, **kwargs)
                    p = self._get_proxy_object(result)
                    params = self._serialize_args(args, kwargs)
                    self._add_recorded_ret_value(name, params, p)
                    return p
                return newfunc
            else:
                p = self._get_proxy_object(attr)
            self._add_recorded_value(name, p)
            return p

    def __setattr__(self, name, value):
        if name in ['_wrapped', '_recorded_values', '_recorded_values_ret',
                '_types', '_instance_id', '_id_sequence']:
            object.__setattr__(self, name, value)
        else:
            setattr(self._wrapped, name, value)

    def _add_recorded_ret_value(self, name, params, val):
        l = self._recorded_values_ret.get(name)
        if l is None:
            l = []
            self._recorded_values_ret[name] = l
        l1 = [r for r in l if r[0] == params]
        if l1:
            l2 = l1[0][1]
        else:
            l2 = []
            l.append((params, l2))
        l2.append(val)

    def _add_recorded_value(self, name, val):
        if not name in self._recorded_values:
            self._recorded_values[name] = []
        self._recorded_values[name].append(val)

    def _serialize_args(self, *args, **kwargs):
        return (args[0], tuple(args[1].items()))

    def __str__(self):
        s = str(self._wrapped)
        self._add_recorded_ret_value('__str__', ((), ()), s)
        return s

    def __len__(self):
        l = len(self._wrapped)
        self._add_recorded_ret_value('__len__', ((), ()), l)
        return l

    def __iter__(self):
        it = []
        for i in self._wrapped:
            it.append(self._get_proxy_object(i))
        self._add_recorded_ret_value('__iter__', ((), ()), it)
        return iter(it)

    def __getitem__(self, key):
        p = self._get_proxy_object(self._wrapped[key])
        self._add_recorded_ret_value('__getitem__', ((str(key),), ()), p)
        return p

    def __call__(self, *args, **kwargs):
        c = self._wrapped(*args, **kwargs)
        p = self._get_proxy_object(c)
        params = self._serialize_args(args, kwargs)
        self._add_recorded_ret_value('__call__', params, p)
        return p
