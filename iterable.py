

list_ = ["1",2,3]
iterator = list_.__iter__()

print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
# print(iterator.__next__())

letter1 = "a"
letter2 = "b"

print(letter1.__hash__())
print(letter2.__eq__("b"))

print(hash("key"))