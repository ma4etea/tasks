"""1. List comprehension

Задача:
Получить список квадратов нечётных чисел от 1 до 10.

👉 Напиши одной строкой с использованием for."""
print([n ** 2 for n in range(1, 11) if n % 2 != 0])  # List comprehension

"""2. Set comprehension

Задача:
Получить множество первых букв всех слов в списке ["apple", "banana", "pear", "apricot", "blueberry"].

👉 Используй {... for ...}"""
print({l[0] for l in ["apple", "banana", "pear", "apricot", "blueberry", ""] if len(l) > 0})

"""3. Generator expression

Задача:
Посчитать сумму всех трёхзначных чисел, делящихся на 7.

👉 Используй sum(...) и (for ...)"""
print((sum((n for n in range(100, 999 + 1) if n % 7 == 0))))

"""
4. Вложенные list comprehensions

Задача:
Получить список всех пар (x, y), где x от 1 до 3, y от 1 до 2.

👉 Результат: [(1,1), (1,2), (2,1), (2,2), (3,1), (3,2)]"""

print(  [(x,y) for x in range(1, 3 + 1) for y in range(1, 2 + 1)]  )


"""5. Set comprehension с фильтрацией

Задача:
Получить множество уникальных цифр из списка строк:
["a1b2", "c3", "44", "b5a7"]

👉 Только цифры, без повторов."""


print({n for string in ["a1b2", "c3", "44", "b5a7"] for n in string if n.isdecimal()})