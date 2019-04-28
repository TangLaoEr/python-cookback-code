"""
利用ipaddress模块
"""

import ipaddress

net = ipaddress.ip_network('123.45.67.64/27')

# 打印这个子网掩码下的所有IP地址
for i in net:
    print(i)

print('---'*20)


inet = ipaddress.ip_interface('123.45.67.73/27')
print(inet.network)  # 网络地址
print(inet.ip)  # ip地址 = 网络地址+主机号
print(inet.hostmask)
