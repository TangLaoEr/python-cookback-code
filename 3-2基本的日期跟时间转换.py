
from datetime import timedelta,datetime
import time

import calendar  # 日历的


a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days)
print(c.seconds)

# print(c.hours)  没有这个属性


# 时间运算
d =  datetime(2019,12,18)
print(d+a)

