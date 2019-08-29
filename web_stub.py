#!/usr/bin/env python
# -*- coding: gbk -*-
"""web stub"""

from wsgiref.simple_server import make_server
from lib.application import WebApp
from lib.Index import Index
from lib.Des import Des

urls = (
    ("/(.*)", "Index"),
)

app = WebApp(urls, globals())

if __name__ == '__main__':
    httpd = make_server('', 8071, app)
    sa = httpd.socket.getsockname()
    print 'http://{0}:{1}/'.format(*sa)
    httpd.serve_forever()
