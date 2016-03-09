
class uri(object):
    def __init__(self):
        self.scheme = ''
        self.ip = ''
        self.port = 0
    def __str__(self):
        if self.scheme:
            return "{0}://{1}:{2}".format(self.scheme, self.ip, self.port)
        else:
            return "{0}:{1}".format(self.ip, self.port)


