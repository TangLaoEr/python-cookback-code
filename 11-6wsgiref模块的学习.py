from wsgiref.simple_server import make_server


def wsgi_app(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/plain')])
    resp = []
    resp.append(b'Hello World\n')
    resp.append(b'Goodbye!\n')
    return resp
if __name__ == '__main__':
    httpd =  make_server('',8080,wsgi_app)
    httpd.serve_forever()
