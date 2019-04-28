"""
两个函数
strftime()
strptime()
"""

from time import strftime,strptime

from datetime import datetime


# 字符串转时间
text = "2018-12-13"
print(datetime.strptime(text,"%Y-%m-%d"))  # 指定字符串的格式


# 时间转字符串
t = datetime.now()
print(datetime.strftime(t,'%x%X'))  # x 表示年月日，X表示时分秒



