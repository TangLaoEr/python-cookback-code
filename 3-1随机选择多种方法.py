import random

values = [1, 2, 3, 4, 5, 6]


# 每次取一个
print(random.choice(values))

# 返回一个长度为2的列表
print(random.sample(values,2))


# 打乱顺序
random.shuffle(values)  # 没有返回值
print(values)


# 生成随机整数
print(random.randint(0,10))  # 指定范围


# 生成随机数
print(random.random())