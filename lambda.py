from cProfile import label
from functools import reduce

nums = [1, 2, 3, 4, 5]
nums1 = list(map(lambda x: x*10, nums))
print(nums1)
# Результат: [10, 20, 30, 40, 50]


words = ["apple", "banana", "avocado", "grape", "apricot", "melon", "A", ""]
words1 = list(filter(lambda x: x if x and x[0].lower() == "a" else None, words))
words2 = list(filter(lambda x: x.lower().startswith("a"), words))

print(words1)
print(words2)

# Результат: ["apple", "avocado", "apricot"]


words_sorted = ["apple", "banana", "fig", "kiwi", "grape", "avocado"]
words_sorted1 = sorted(words_sorted, key=lambda x: len(x))
print(words_sorted1)

# Ожидаемый результат: ['fig', 'kiwi', 'apple', 'grape', 'banana', 'avocado']


words_sorted = ["apple", "banana", "fig", "kiwi", "grape", "avocado", "a", ""]
words_sorted1 = sorted(words_sorted, key=lambda x: x[-1] if len(x) > 0 else x)
words_sorted2 = sorted(words_sorted, key=lambda x: x[-1:])

print(words_sorted1)
print(words_sorted2)

# Ожидаемый результат: ['banana', 'apple', 'grape', 'fig', 'avocado', 'kiwi']
# (т.к. последние буквы: a, e, e, g, o, i → отсортированы: a, e, e, g, i, o)


words = ["apple", "banana", "fig", "kiwi", "grapefruit", "pear"]
words1 = max(words, key=lambda x: len(x))

print(words1)

print(max([1,2,234,525,6346]))
print(max([1.2,2.2,234,525,6346.435]))

# Ожидаемый результат: "grapefruit"


words = ["Apple", "banana", "Orange", "ice", "Umbrella", "Egg", "owl", "grape", "kivi"]
words1 = list(filter(lambda x: x.lower().startswith(('a','e','i','o','u')) and len(x) > 4 , words))
print(words1)

# Ожидаемый результат: ["Apple", "Orange", "Umbrella"]



nums = [2, 3, 4]

num = reduce(lambda x, y: x*y, nums)

print(num)

# Ожидаемый результат: 24 (2 * 3 * 4)


names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
result = list(zip(names, scores))
print(result)

# Ожидаемый результат:
# ["Alice: 85", "Bob: 92", "Charlie: 78"]


list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list(map(lambda x: x[0]+x[1], zip(list1, list2)))
result1 = list(map(lambda x, y: x + y, list1, list2))
print(result)
print(result1)
# Результат: [5, 7, 9]


words = ["apple", "banana", "cherry"]

result = list(map(lambda x: f"{x[0]}: {x[1]}", enumerate(words)))
print(result)
# Результат: ["0: apple", "1: banana", "2: cherry"]




words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]


result = list(filter(lambda even_fruit: 1 if even_fruit[0] % 2 == 0 else None, enumerate(words)))
result1 = list(map(lambda x: x[1], result))

print(result1)
# Ожидаемый результат: ['apple', 'cherry', 'elderberry']

