from itertools import zip_longest

a = [1,2,3]
b = ['x','y','w','z']

for i in zip_longest(a,b):
    print(i)