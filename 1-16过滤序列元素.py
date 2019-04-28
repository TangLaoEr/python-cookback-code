myList = [1, 4, -5, 10, -7, 2, 3, -1]


# 方案一：
print([n for n in myList if n > 0])


# 方案二
pos = (i for i in myList if i > 0)  # 返回一个生成器

for i in pos:
    print(i,end=' ')
print('-'*20)


# 方案三
fi_f = filter(lambda x:x>0,myList)
for i in fi_f:
    print(i, end=' ')
print('='*20)


from itertools import compress

counts = [0, 3, 10, 4, 1, 7, 6, 1]
more5 = [n > 5 for n in counts]
print(more5)

myList = [0, 3, 10, 4, 1, 7, 6, 1]   # 返回对应为true的元素
for i in compress(myList,more5):
    print(i,end=' ')