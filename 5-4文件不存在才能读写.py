#with open('text.txt','x') as f:
#    f.write('haha')  # 存在则报错
#

# 检测文件是否存在
import os
print(os.path.exists('text.txt'))