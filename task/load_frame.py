import os
import json
import base_type
import const

class task_instance(object):
    def loads(self, obj):
        self.obj = obj
        self._uri.scheme = ''
        self._uri.ip = obj['ip']
        self._uri.port = int(obj['port'])
        for k,v in obj.items():
            k = k.strip().lower()
            if self._uri.scheme =='' and k == 'service':
                if isinstance(v, str):
                    self._uri.scheme = v
                else:
                    self._uri.scheme = v[0]
            elif k == 'ip' or k == 'port':
                continue
            try:
                if k.index("_bin") > -1:
                    self.message_push_line(k)
                    if isinstance(v, str) and v[-1] != '\n':
                        self.message_push_line(v)
                    else:
                        self.message_push(v)
                else:
                    self.tag_set(k,v)
            except Exception as e:
                self.tag_set(k,v)
        pass
    def __init__(self, obj):
        # init #
        self.tags = {}
        self.messages = []
        self._uri = base_type.uri()
        # check & load #
        self.loads(obj)
    def dumps(self):
        self.obj['tags'] = self.tags
        self.obj['message'] = self.messages
        return json.dumps(self.obj)
    def tag_set(self, key, value = None):
        key = key.strip().lower()
        if not value:
            value = key
        self.tags[key] = value
        pass
    def tag_match(self, key, match):
        if not key:
            for k,v in self.tags.items():
                try:
                    if match(v):
                        return True
                except Exception as e:
                    pass
        else:
            try:
                if match(self.tags[key]):
                    return True
            except Exception as e:
                pass
        return False
    def tag_search(self, value):
        return self.tag_match(None, lambda v : v.index(value) > -1)
    def message_push_line(self, message):
        try:
            self.messages.append(str(message) + '\n')
        except Exception as e:
            pass
    def message_push(self, message):
        try:
            self.messages.append(message)
        except Exception as e:
            pass
    def url(self):
        return str(self._uri)
    def uri(self):
        return self._uri
    pass


class plugin_instance(object):
    WT = { 'scheme' : 'http',
           'service' : 'http'
           }
    WL = { }
    def __init__(self):
        pass
    def start(self, task):
        return True
    @staticmethod
    def work_type(key, value):
        if key and WT.has_key(key):
            return value == WT[key] or value in WT[key]
        else:
            for k,v in WT.items():
                if value == v or value in v:
                    return True
        return False
    @staticmethod
    def work_limit(self, key, value):
        if not key:
            print('ASSERT!!!!')
            print('ASSERT!!!!')
            print('ASSERT!!!!')
        if WL.has_key(key):
            return WL[key] 
        return True
    pass


class plugins_manager(object):
    def __init__(self, filter = None, filter_type = None):
        self.reload(filter,filter_type)
        pass
    def create_by_name(self ,name):
        # return self.core_dist[name]()
        return plugin_instance()
    def adapter_json(self, line):
        try:
            obj = json.loads(line)
            return task_instance(obj)
        except Exception as e:
            return None
    def reload(self, filter,filter_type):
        self.core_dict = {}
        ## in plugins folder ##
        # loading...
        # self.core_dist[filename] = file_call
        return True
    def show(self, filter,filter_type):
        return True


