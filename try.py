try:
    print(1/1)
finally:
    print('finally')

try:
    print(1 / 1)
    # print(1/0)
finally:
    print('finally')

print("---------------------------------------------------------------------------")

try:
    print(1 / 1)
    # print(1/0)
except ZeroDivisionError:
    print('ex')
else:
    print('else')


