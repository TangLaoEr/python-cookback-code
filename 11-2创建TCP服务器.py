"""
利用socketserver
"""

from socketserver import TCPServer,BaseRequestHandler

class EchoHandler(BaseRequestHandler):
    """重写handle"""
    def handle(self):
        print("客户端的地址:",self.client_address)

        while True:
            msg = self.request.recv(1024) # request表示他们之间的socket
            if not msg:
                break
            self.request.send(msg)

if __name__ == '__main__':
    serv = TCPServer(('127.0.0.1',20000),EchoHandler)
    serv.serve_forever()
