def f1(L):
    print(L[0])
    return L[-1]

def f2(L):
    L.insert(0, L[0] + L[1])
    L[1] = 2 * f1(L)
    print(L.pop())
    return L[-1] + L[-2]


my_list = [2, 5]
print(f2(my_list))
print(my_list)