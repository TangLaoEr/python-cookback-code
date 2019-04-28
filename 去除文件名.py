import os
import re

os.chdir('/Users/mac/Desktop/ebook/python')
# print(os.listdir())
[os.rename(i,re.sub('\d{6}\s*','',i).strip()) for i in os.listdir()]
