import csv
from collections import namedtuple

#
#with open('stocks.csv') as f:
#    f_csv = csv.reader(f)
#    header = next(f_csv)
#    for row in f_csv:
#        print(row)


# 利用有名字典
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    heading = next(f_csv)
    Row = namedtuple('Row',heading)
    for r in f_csv:
        row = Row(*r)
        print(row.Symbol)

# 字典
with open('stocks.csv') as f:
    f_csv =csv.DictReader(f)
    for row in f_csv:
        print(row)

