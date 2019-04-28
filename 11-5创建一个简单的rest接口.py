"""
写一个简单的rest接口

"""
import cgi
from wsgiref.simple_server import make_server
import time

def notfound_404(environ,start_response):
    """参数名不可变"""
    start_response('404 Not found',[('content-type','text/plain')])
    return [b'404 not found']


class PathDispatcher:
    def __init__(self):
        self.pathmap={}   # 路由映射


    def __call__(self, environ,start_response):
        path = environ['PATH_INFO']
        params = cgi.FieldStorage(environ['wsgi.input'],
                                 environ=environ)
        method = environ['REQUEST_METHOD'].lower()
        environ['params'] = {key: params.getvalue(key) for key in params}
        handler = self.pathmap.get((method, path), notfound_404)
        return handler(environ, start_response)

    def register(self,method,path,function):
        """
        注册路由对应的处理方法
        :param method: 请求方法
        :param path:  请求路径
        :param function: view方法处理
        :return: 返回处理方法
        """
        self.pathmap[method.lower(),path] = function  # 以请求方法跟请求路径为元组作为key,虽然这里没有用()不过它还是为（）
        return function


_hello_resp = '''\
<html>
  <head>
     <title>Hello {name}</title>
   </head>
   <body>
     <h1>Hello {name}!</h1>
   </body>
</html>'''

def hello_world(environ, start_response):
    start_response('200 OK', [ ('Content-type','text/html')])
    params = environ['params']
    resp = _hello_resp.format(name=params.get('name'))
    yield resp.encode('utf-8')

_localtime_resp = '''\
<?xml version="1.0"?>
<time>
  <year>{t.tm_year}</year>
  <month>{t.tm_mon}</month>
  <day>{t.tm_mday}</day>
  <hour>{t.tm_hour}</hour>
  <minute>{t.tm_min}</minute>
  <second>{t.tm_sec}</second>
</time>'''

def localtime(environ, start_response):
    start_response('200 OK', [ ('Content-type', 'application/xml') ])
    resp = _localtime_resp.format(t=time.localtime())
    yield resp.encode('utf-8')

if __name__ == '__main__':
    dispather = PathDispatcher()
    dispather.register('GET','/hello',hello_world)
    dispather.register('GET','/time',localtime)

    httpd = make_server('',8080,dispather)
    print('servering on 8080')
    httpd.serve_forever()


"""

这是官网对wsgiref模块得一段代码

from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

# A relatively simple WSGI application. It's going to print out the
# environment dictionary after being updated by setup_testing_defaults
def simple_app(environ, start_response):
    setup_testing_defaults(environ)

    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response(status, headers)

    ret = [("%s: %s\n" % (key, value)).encode("utf-8")
           for key, value in environ.items()]
    return ret

with make_server('', 8000, simple_app) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()
"""