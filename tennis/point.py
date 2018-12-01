class Point(object):
    def __init__(self, **kwargs):
        self._server = kwargs['server']
        self._receiver = kwargs['receiver']

    def server(self):
        return self._server

    def receiver(self):
        return self._receiver