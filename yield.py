from datetime import datetime
from itertools import count
from time import strftime
from typing import Generator, Tuple


def simple_gen():
    yield 1
    yield 2
    yield 3


for value in simple_gen():
    print(value)

print("--------------------------------------")
print("def countdown(n):")


def countdown(n):
    while n > 0:
        yield n
        n -= 1


for num in countdown(5):
    print(num)

print("--------------------------------------")
print("def even_countdown(n):")


def even_countdown(n):
    while n > 0:
        if n % 2 == 0: yield n
        n -= 1


for num in even_countdown(10):
    print(num)

print("--------------------------------------")
print("def accumulator(n):")
def accumulator() -> Generator:
    amount = 0
    while True:
        amount += yield amount


gen = accumulator()
next(gen)  # активируем генератор
print(gen.send(5))  # 5
print(gen.send(3))  # 8
print(gen.send(10))  # 18


print("--------------------------------------")
print("def smart_accumulator(n):")
def smart_accumulator() -> Generator[int, Tuple[str, int], None]:
    amount = 0
    while True:
        command, value_num = yield amount
        if command == "add":
            amount += value_num
        elif command == "mul":
            amount *= value_num

gen = smart_accumulator()
next(gen)                     # запускаем

print(gen.send(("add", 5)))   # 5
print(gen.send(("add", 2)))   # 7
print(gen.send(("mul", 3)))   # 21
print(gen.send(("add", -1)))  # 20



print("--------------------------------------")
print("def event_logger(n):")
def event_logger() -> Generator[int, str, None]:
    log_sting = ""
    count_event = 0
    while True:

        log_sting = (yield f"[{datetime.now().strftime('%H:%M:%S')} Event: {log_sting} -> {count_event}]")
        count_event += 1


gen = event_logger()
next(gen)

print(gen.send("user_logged_in"))  # [12:34:56] Event: user_logged_in → 1
print(gen.send("file_uploaded"))   # [12:35:02] Event: file_uploaded → 2
print(gen.send("logout"))          # [12:35:10] Event: logout → 3


print("--------------------------------------")
print("def limited_accumulator(n):")
def limited_accumulator(max_count: int) -> Generator[None, int, int]:
    total = 0
    for _ in range(max_count):
        value_num = yield
        total += value_num
    return total


gen = limited_accumulator(3)
next(gen)

gen.send(10)     # 1-е число
gen.send(5)      # 2-е число

try:
    gen.send(2)
except StopIteration as e:
    print(e.value)  # ← здесь будет итоговая сумма: 17


