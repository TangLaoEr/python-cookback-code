import ipaddress

net = ipaddress.ip_network('123.45.67.64/27')


for i in net:
    print(i)