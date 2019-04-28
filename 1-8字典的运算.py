"""
字典的操作
"""


prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 找出最小值
min_price = min(zip(prices.values(),prices.keys()))
print(min_price)

# 找出最大值
max_price = max(zip(prices.values(),prices.keys()))
print(max_price)


# 排序
prices_sorted = sorted(zip(prices.values(),prices.keys()))
print(prices_sorted)


prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names)) # OK
# print(max(prices_and_names)) # 报错，zip是生成器，只遍历一次

