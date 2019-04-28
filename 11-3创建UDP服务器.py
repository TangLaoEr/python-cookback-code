from socketserver import BaseRequestHandler,UDPServer
import time

class TimerHandler(BaseRequestHandler):
    def handle(self):
        print('got connection from',self.client_address)
        msg,sock = self.request

        resp = time.ctime()
        sock.sendto(resp.encode('utf-8'),self.client_address)


if __name__ == '__main__':
    serv = UDPServer(('',2000),TimerHandler)
    serv.serve_forever()


    
