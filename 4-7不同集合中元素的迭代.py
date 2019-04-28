from itertools import chain

a = [1, 2, 3, 4]
b = ['x', 'y', 'z']


# 主要是省内存，比 a + b 的方式更加节省内存
for i in chain(a,b):
    print(i)


