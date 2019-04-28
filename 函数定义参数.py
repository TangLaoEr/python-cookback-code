x = 42

def spam(a, b=x):
    print(a,b)

print(spam(1))


x = 23
print(spam(2))