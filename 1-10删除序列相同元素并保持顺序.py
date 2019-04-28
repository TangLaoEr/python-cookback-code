# 案例一
# items里面的数据类型是不可变的数据类型
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))


# 案例二
# 可变的数据类型
def dedupe_dict(items,key=None):
    """:key为指定的方法"""
    seen = set()
    for item in items:
        val = item if key is None else key(item)   # 传给自定义的函数进行处理
        if val not in seen:
            yield val
            seen.add(val)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
result = list(dedupe_dict(a,key=lambda b:(b['x'],b['y'])))

print(result)

"""
通过set() 去重不能保持顺序
"""
