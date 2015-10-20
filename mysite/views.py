#coding:utf8
__author__ = 'adair'
import tornado.web

class DemoRequest(tornado.web.RequestHandler):

    def get(self):
        self.write('Trying')