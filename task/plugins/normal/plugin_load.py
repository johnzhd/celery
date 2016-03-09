import os
import imp


class loader(object):
    def __init__(self, filter = None, filter_type = None):
        self.core_dict = {}
        self.path = os.path.split(os.path.realpath(__file__))[0] + '/'
        self.reload(filter, filter_type)
    def reload(self, filter = None, filter_type = None):
        for n in os.listdir(self.path):
            name, ext = os.path.splitext(n)
            if ext.lower() != 'py':
                continue
            full_path = self.path + n
            core = self.load_single(name, full_path)
            if filter and not core.work_type(filter_type, filter):
                del core
                continue
            self.core_dict[name] = core
        pass
    def show(self):
        return self.core_dict.keys()
    def load_single(self, name, filename):
        try:
            module = imp.load_source(name, filename)
            if hasattr(module,'plugin_instance'):
                return module
        except Exception as e:
            pass
        return None



