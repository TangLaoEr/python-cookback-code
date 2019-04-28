
str.replace()


import re
re.sub()
re.subn()  # 返回一个元组


datepat = re.compile()
datepat.sub(function_name,text) # 第一个参数可为函数，接收一个参数，为正则匹配对象，有group()方法
