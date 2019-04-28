import os

# 返回文件名
print(os.path.basename(__file__))


# 返回目录绝对路径
print(os.path.dirname(__file__))


# 路径分隔
print(os.path.split(__file__))


# 路径拼接
print(os.path.join('/tmp','hahah.cv'))