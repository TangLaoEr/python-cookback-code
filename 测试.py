from socket import socket,AF_INET, SOCK_STREAM
import hmac
import time

secret_key = b'tanglaoer'

def client_authenticate(connection,secret_key):
    """客户端认证"""
    message = connection.recv(32)
    hash_data = hmac.new(secret_key,message)
    digest = hash_data.digest()  # 提取加密后的摘要
    return connection.send(digest)



if __name__ == '__main__':
    sock = socket(AF_INET,SOCK_STREAM)

    sock.connect(('localhost',18000))
    client_authenticate(sock,secret_key)

    while True:
        time.sleep(2)
        sock.send(b'hello world')
        print(sock.recv(1024))
