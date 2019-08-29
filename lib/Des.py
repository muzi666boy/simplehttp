#!/usr/bin/env python
# -*- coding: gbk -*-

""" simple des action """

from lib.DesUtils import DesUtils
from lib.application import WebApp

class Des(object):
    """ Index action  """
    def POST(self, name, **environ):
        """ do post request """
        f = open("./stub.log", 'a+')
        WebApp.header('Content-type', 'text/plain')
        try:
            body_size = int(environ.get('CONTENT_LENGTH', 0))
        except (ValueError):
            body_size = 0
        body = environ['wsgi.input'].read(body_size)
        print >> f, (name + " | " + body)
        try:
            desUtils = DesUtils()
            desUtils.input_key('12345678')
            clearText = desUtils.decode(body)
            print >> f, (name + " | " + clearText)
            return desUtils.encode("success")
        except Exception, e:
            print >> f, ("des decode exception", e)

    def GET(self, name, **environ):
        """ do get request """
        return self.POST(name, **environ)

