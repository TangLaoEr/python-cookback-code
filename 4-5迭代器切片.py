"""
由于迭代器事先并不知道长度，无法用常规的切片
"""

def count(n):
    while True:
        yield n
        n += 1

# c = count(1)
# print(c[10:20]) # 报错


# 利用itertools.islise()

import itertools

c = count(1)
for x in itertools.islice(c,10,20):  # 打印11-20 然后关闭，就算生成器死循环也关闭 (10,20]  左开右闭
    print(x)