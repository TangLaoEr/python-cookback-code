from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]


rows_by_name = sorted(rows,key=itemgetter('fname'))
print(rows_by_name)

rows_by_uid = sorted(rows,key=itemgetter('uid'))
print(rows_by_uid)

rows_by_lfname = sorted(rows,key=itemgetter('lname','fname'))
print(rows_by_lfname)


# 同样适合于min，max
print(min(rows,key=itemgetter('uid')))

print(max(rows,key=itemgetter('uid')))


# 还有另外一种方法，key=lambda表达式

