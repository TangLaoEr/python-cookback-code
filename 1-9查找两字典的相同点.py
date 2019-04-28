a={
    'x' : 1,
    'y' : 2,
    'z' : 3
}
b={
    'w' : 10,
    'x' : 11,
    'y' : 2
}

print(a.keys())
print(b.keys())

# 合并的健
print(a.keys() & b.keys())


print(a.keys() - b.keys())


print(a.items() & b.items())