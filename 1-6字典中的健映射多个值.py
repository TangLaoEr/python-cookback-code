"""
一键对多值
d={
    'a' : [1, 2, 3],
    'b' : [4, 5]
 }
e={
    'a' : {1, 2, 3},
    'b' : {4, 5}
}
"""

from collections import defaultdict

d = defaultdict(list)  # 指定存储值得方式

# 健为有可无的情况下添加
d['a'].append(1)
d['a'].append(1)
d['b'].append(3)

for key,value in d.items():
    print(key,value)


s = defaultdict(set)  # 默认具有set的属性，去重


s['c'].add('1')
s['c'].add('1')
s['d'].add('3')
for key,value in s.items():
    print(key,value)