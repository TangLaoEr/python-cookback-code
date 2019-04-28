def frange(start, stop, increment):
    """自定义迭代方式"""
    x = start
    while x < stop:  # 跟range一样 左闭右开
        yield x
        x += increment


for i in frange(1,10,0.5):
    print(i)