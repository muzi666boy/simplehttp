#!/usr/bin/env python
# -*- coding: gbk -*-

""" simple index action """

from lib.application import WebApp

class Index(object):
    """ Index action  """
    def POST(self, name, **environ):
        """ do post request """
        WebApp.header('Content-type', 'text/plain')
        try:
            body_size = int(environ.get('CONTENT_LENGTH', 0))
        except (ValueError):
            body_size = 0
        body = environ['wsgi.input'].read(body_size)
        f = open("./stub.log", 'a+')
        print >> f, (name + " | " + body)
        return "success"

    def GET(self, name, **environ):
        """ do get request """
        return self.POST(name, **environ)

