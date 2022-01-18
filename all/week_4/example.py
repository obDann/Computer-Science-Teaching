def f1(x):
    return x + 1

def f2(y, x):
    z = f1(y)
    print(y + x)
    return z + x

def f3(x, y):
    c = x
    x = f1(y)
    y = f1(x)
    z = f2(c, y) % 5
    return y, z, x

x = f3(4, 5)
print(x)