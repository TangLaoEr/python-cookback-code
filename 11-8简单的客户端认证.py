"""
客户端跟服务器都知道一个共同的秘钥
1、服务器给客户端发送一个随机的字节消息（这里例子中使用了 os.urandom() 返回值）。
2、客户端和服务器同时利用hmac和一个只有双方知道的密钥来计算出一个加密哈希值。
3、然后客户端将它计算出的摘要发送给服务器， 服务器通过比较这个值和自己计算的是否一致来决定接受或拒绝连接。
4、摘要的比较需要使用 hmac.compare_digest() 函数。 使用这个函数可以避免遭到时间分析攻击
"""

import os
import hmac
from socket import socket,AF_INET, SOCK_STREAM
secret_key = b'tanglaoer'


#def client_authenticate(connection,secret_key):
#    """客户端认证"""
#    message = connection.recv(32)
#    hash_data = hmac.new(secret_key,message)
#    digest = hash_data.digest()  # 提取加密后的摘要
#    return connection.send(digest)


def server_authenticate(connection,secret_key):
    """服务器认证"""
    message = os.urandom(32)  # 产生32位随机值

    # 发生随机值给客户端
    connection.send(message)

    # 计算哈希值
    hash_data = hmac.new(secret_key,message)

    # 生成摘要
    digest = hash_data.digest()

    # 接收客户端发来的摘要
    response = connection.recv(len(digest))

    return hmac.compare_digest(digest,response)






def echo_handler(client_sock):
    """处理客户请求"""
    if not server_authenticate(client_sock,secret_key):
        client_sock.close()
        print('客户端认证失败')
        return

    print('认证成功')
    while True:
        msg = client_sock.recv(1024)
        print('接收的数据:%s'%msg)
        if not msg:
            break
        client_sock.sendall(msg)


def echo_server(address):
    s = socket(AF_INET,SOCK_STREAM)
    s.bind(address)
    s.listen(5)
    while True:
        client_sock,addr = s.accept()
        echo_handler(client_sock)


if __name__ == '__main__':
    echo_server(('',18000))

"""
from socket import socket,AF_INET, SOCK_STREAM
import hmac
import time

secret_key = b'tanglaoer'

def client_authenticate(connection,secret_key):
    #客户端认证
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
"""


