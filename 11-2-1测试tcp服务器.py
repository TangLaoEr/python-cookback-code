import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect(('localhost',20000))

while True:
    sock.send(b'hello world')
    print(sock.recv(1024).decode('utf-8'),'from server')