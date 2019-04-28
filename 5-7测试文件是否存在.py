import os

os.path.isfile('/etc/passwd')

os.path.isdir('/tmp/data')

# 是否是链接
os.path.islink('/usr/local/bin/python3')


# 链接的真实路径
os.path.realpath('/usr/local/bin/python3')  # /usr/local/bin/python3.7


def wrapper(func):
    def innder(*args,**kwargs):
        return func(*args,**kwargs)
    return innder


@wrapper
def test(a,b):
    print(a + b)


test(1,2)
print(test.__name__)