from itertools import permutations

items = ['a','b','c']

# 所有长度的排列
# 排序
for p in permutations(items):
    print(p)


# 指定长度的排列
# 排序
for p in permutations(items,2):
    print(p)


# combinations 的使用,不排序
from itertools import combinations

# 元素的所有集合，不排序
for c in combinations(items,3):
    print(c)


# 指定长度,不排序
for c in combinations(items,2):
    print(c)


from itertools import combinations_with_replacement

# 允许同一元素选中多次,不排序
for c in combinations_with_replacement(items,3):
    print(c)
