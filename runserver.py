#coding:utf8
__author__ = 'adair'
from tornado import web,ioloop
from mysite.urls import urls
from mysite.setting import port,ip
if __name__ == '__main__':
    try:
        app=web.Application(urls)
        app.listen(port,ip)
        io=ioloop.IOLoop().current()
        print('listening')
        io.start()
    except Exception as e:
        print(e)