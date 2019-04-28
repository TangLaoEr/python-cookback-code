import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock.sendto(b'hello world',('localhost',2000))


print(sock.recvfrom(1024))

