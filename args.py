import sys


default = {}

class args():
    def __str__(self):
        return str(self.core)
    def __init__(self):
        self.core = {}
        self.load()
    def push(self, key, value):
        key = key.strip(' \t\r\n-=').lower()
        value = value.strip(' \t\r\n-=')
        self.core[key]=value
    def load(self):
        self.core = {}
        sys.argv;
        length = len(sys.argv)
        i = 0
        npos = 0
        while i<length:
            line = sys.argv[i]
            if len(line) == 0:
                i = i+1
                continue
            if line[0] != '-':
                i = i+1
                continue
            npos = line.find('=');
            if npos == -1:
                key = line[1:];
                if i + 1 < length and argv[i+1][0] != '-':
                    value = sys.argv[i+1];
                else:
                    value = '1'
                    i = i+1
                self.push(key,value)
                i = i+1
                continue
            else:
                value = line[npos+1:]
                key = line[0:npos]
                self.push(key,value)
            i = i+1
            continue
    def get(self, key):
        try:
            var = self.core[key]
        except Exception as e:
            var =  None
        if var == None:
            try:
                return default[key]
            except Exception as e:
                return None
        else:
            return var
    def print_items(self):
        for x,y in self.core.items():
            print( '{0}\t{1}'.format(x,y))






