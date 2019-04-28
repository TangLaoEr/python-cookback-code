from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])

sub = Subscriber('tanglaoer.qq.com','2012-10-18')

print(sub)
print(sub.addr)
print(sub.joined)

