

list_ = ["1",2,3]
iterator = list_.__iter__()
a = iterator.__iter__()

list_.__next()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
# print(iterator.__next__())


