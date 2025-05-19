import dis

from bit_code import say_hello

dis.dis(say_hello)
print(say_hello.__code__.co_code)