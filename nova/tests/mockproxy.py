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

class Mock(object):
    def _get_next_value(self, name):
        c = self._access_count.get(name)
        if c is None:
            c = 0
        else:
            c = c + 1
        self._access_count[name] = c
        return self._values[name][c]

    def _get_next_ret_value(self, name, params):
        d = self._access_count.get(name)
        if d is None:
            d = {}
            self._access_count[name] = d
        c = d.get(params)
        if c is None:
            c = 0
        else:
            c = c + 1
        d[params] = c
        return self._values[name][params][c]        
        
    def __init__(self, values):
        self._values = values
        self._access_count = {}

    def __getattr__(self, name):
        if name.startswith('__') and name.endswith('__'):
            return object.__getattribute__(self, name)
        else:
            if isinstance(self._values[name],  dict):
                def newfunc(*args, **kwargs):
                    params = str(args) + str(kwargs)
                    return self._get_next_ret_value(name, params)
                return newfunc
            else:
                return self._get_next_value(name)

    def __str__(self):
        return self._get_next_value('__str__')

    def __iter__(self):        
        return  getattr(self._get_next_value( '__iter__'), '__iter__')()

    def __getitem__(self,key):
        return self._get_next_ret_value( '__getitem__', str(key))
        
        
class MockProxy(object):
    def __init__(self, wrapped):
        self._wrapped = wrapped
        self._recorded_values = {}

    def _get_proxy_object(self, obj):
        if hasattr(obj, '__dict__') or isinstance(obj, tuple) or isinstance(obj, list) or isinstance(obj, dict):        
            p = MockProxy(obj)        
        else:
            p = obj
        return p

    def __getattr__(self, name):
        if name in ['_wrapped']:
            return object.__getattribute__(self, name)
        else:
            attr = getattr(self._wrapped, name)
            if hasattr(attr, '__call__'):
                def newfunc(*args, **kwargs):
                    result = attr(*args, **kwargs)
                    p = self._get_proxy_object(result)                    
                    self._add_recorded_ret_value(name,  str(args) + str(kwargs), p)
                    return p
                return newfunc
            elif hasattr(attr, '__dict__'):
                p = MockProxy(attr)
            else:
                p = attr
            self._add_recorded_value(name, p)
            return p

    def _add_recorded_ret_value(self, name, params, val):
        d = self._recorded_values.get(name)
        if d is None:
            d = {}
            self._recorded_values[name] = d       
        l = d.get(params)
        if l is None:
            l = []
            d[params] = l
        l.append(val)
                        
    def _add_recorded_value(self, name, val):
        if not self._recorded_values.has_key(name):
            self._recorded_values[name] = []
        self._recorded_values[name].append(val)
                
    def get_mock(self):
        values = {}
        for k, v in self._recorded_values.items():            
            if isinstance(v, dict):
                d = {}
                values[k] = d
                for k1, v1 in v.items():
                    l = []
                    d[k1] = l
                    for i1 in v1:                
                        if isinstance(i1, MockProxy):
                            l.append(i1.get_mock())
                        else:
                            l.append(i1)                
            else:
                l = []
                values[k] = l            
                for i in v:
                    if isinstance(i, MockProxy):
                        l.append(i.get_mock())
                    elif isinstance(i, dict):
                        d = {}
                        for k1, v1 in v.items():
                            if isinstance(v1, MockProxy):
                                d[k1] = v1.get_mock()
                            else:
                                d[k1] = v1
                        l.append(d)
                    elif isinstance(i, list):
                        l1= []
                        for i1 in i:
                            if isinstance(i1, MockProxy):
                                l1.append(i1.get_mock())
                            else:
                                l1.append(i1)
                        l.append(l1)
                    else:
                        l.append(i)
        return Mock(values)

    def __str__(self):
        s = str(self._wrapped)
        self._add_recorded_value('__str__', s)        
        return s

    def __iter__(self):
        it = []
        for i in self._wrapped:
            it.append(self._get_proxy_object(i))
        self._add_recorded_value('__iter__', it)    
        return iter(it) 

    def __getitem__(self,key):
        p = self._get_proxy_object(self._wrapped[key])
        self._add_recorded_ret_value('__getitem__', str(key), p) 
        return p
