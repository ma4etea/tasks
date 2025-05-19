a = 4

def func1(n):
    n += 1
    return n

print(func1(a))
print(a)

list1 = [1,2,3]

def func2(list2):
    list2.append(4)
    list2[0] = 5
    return list2

print(func2(list1))
print(list1)