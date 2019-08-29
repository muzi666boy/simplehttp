#!/usr/bin/env python
# -*- coding: gbk -*-

""" application framework """

import re

class WebApp(object):
    """simple web framework"""

    headers = []

    def __init__(self, urls, fvars):
        self._urls = urls
        self._fvars = fvars
        self._status = '200 OK'

    def __call__(self, environ, start_response):
        del self.headers[:]
        result = self._delegate(environ)
        start_response(self._status, self.headers)

        if isinstance(result, basestring):
            return iter([result])
        else:
            return iter(result)

    def _delegate(self, environ):
        path = environ['PATH_INFO']
        method = environ['REQUEST_METHOD']

        for pattern, name in self._urls:
            m = re.match('^' + pattern + '$', path)
            if m:
                args = m.groups()
                funcname = method.upper()
                klass = self._fvars.get(name)
                if hasattr(klass, funcname):
                    func = getattr(klass, funcname)
                    return func(klass(), *args, **environ)

        return self._notfound()

    def _notfound(self):
        self.status = '404 Not Found'
        self.header('Content-type', 'text/plain')
        return "Not Found\n"

    @classmethod
    def header(cls, name, value):
        """ set header """
        cls.headers.append((name, value))
