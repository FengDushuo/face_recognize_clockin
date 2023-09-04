#!/usr/bin/env python
# coding=utf-8

import os
import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.options import define, options
from handlers.workattendance import workattendanceHandler
from handlers.index import IndexHandler    
from handlers.user import UserHandler
from handlers.forgetpwd import SendEmailHandler
from handlers.modify import ModifyHandler
from handlers.listanddate import listanddateHandler
from handlers.register import RegisterHandler
from handlers.workerdo import workerdoHandler
from handlers.deleteinfo import deleteinfoHandler
from handlers.phonepic import phonepicHandler
from handlers.download import downloadHandler

define("port", default = 8000, help = "run on the given port", type = int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexHandler),          #index既是登录页面也是首页面
            (r'/index', IndexHandler),
            (r'/user', UserHandler),
            (r'/forgetpwd', SendEmailHandler),
            (r'/register',RegisterHandler),
            (r'/modify', ModifyHandler),
            (r'/workattendance', workattendanceHandler),
            (r'/workerdo', workerdoHandler),
            (r'/listanddate', listanddateHandler),
            (r'/deleteinfo', deleteinfoHandler),
            (r'/phonepic',phonepicHandler),
            (r'/download',downloadHandler)
        ]

        settings = dict(
        template_path = os.path.join(os.path.dirname(__file__), "templates"),
        static_path = os.path.join(os.path.dirname(__file__), "static"),
        cookie_secret = "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
        xsrf_cookies = False,
        login_url = '/',
        )
        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)

    print("Development server is running at http://localhost:%s" % options.port)
    print("Quit the server with Control-C")

    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()