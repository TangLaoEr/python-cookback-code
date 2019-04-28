# 用于匹配文件名
from fnmatch import fnmatch,fnmatchcase

print(fnmatch('tang.txt','*.txt'))


# 不区分大小写匹配
print(fnmatch('Tang.txt','tang.txt'))
print(fnmatchcase('Tang.txt','tang.txt'))


