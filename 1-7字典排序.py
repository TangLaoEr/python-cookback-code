from collections import OrderedDict


d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for i in d:
    print(i,d[i])


import json
# 需求转为json字符串，可以保持顺序
print(json.dumps(d))

