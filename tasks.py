def get_letter_count(string: str) -> dict:
    dict_letter = {}
    for i in string:
        if i in dict_letter:
            dict_letter[i] += 1
            continue
        dict_letter.update({i: 1})
    return dict_letter


print(get_letter_count('banana'))


def get_letter_count1(string: str) -> dict:
    dict_letter = {}
    for i in string:
        if i in dict_letter:
            dict_letter[i] += 1
        else:
            dict_letter[i] = 1
    return dict_letter


print(get_letter_count1('banana'))


def unique_numbers(numbers: list) -> list:
    unique_set = set(numbers)
    unique_list = list(unique_set)
    return unique_list


print(unique_numbers([1, 2, 2, 3, 4, 3, 5]))


def unique_numbers1(numbers: list) -> list:
    unique_list = []

    for number in numbers:
        if number not in unique_list:
            unique_list.append(number)
    return unique_list


print(unique_numbers1([1, 2, 2, 3, 4, 3, 5]))


def unique_numbers2(numbers: list) -> list:
    return list(dict.fromkeys(numbers))


print(unique_numbers2([1, 2, 2, 3, 4, 3, 5]))


def is_palindrome(string: str) -> bool:
    string = string.lower()
    string = string.replace(' ', '')

    return string == string[::-1]


print(is_palindrome("А роза упала на лапу Азора"))  # True
print(is_palindrome("python"))  # False


def fibonacci(n: int) -> list:
    fib_list = [0, 1]
    fib_amount = 0
    for i in range(2, n):
        fib_amount = fib_list[i - 1] + fib_list[i - 2]

        fib_list.append(fib_amount)

    return fib_list


print(fibonacci(5))  # [0, 1, 1, 2, 3]
print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def find_anagrams(word1: str, words: list) -> list:
    anagramma = []
    sorted_list = []
    word2 = sorted(word1)
    for word in words:
        sorted_list.append(sorted(word))
    for n, i in enumerate(sorted_list):
        if word2 == sorted_list[n]:
            anagramma.append(words[n])

    return anagramma


print(find_anagrams("listen", ["enlists", "google", "inlets", "banana", "silent"]))


# ['inlets', 'silent']


def square_evens(nums: list) -> list:
    return [num * num for num in nums if num % 2 == 0]


print(square_evens([1, 2, 3, 4, 5, 6]))
# [4, 16, 36]


def filter_strings(words: list[str]) -> list[str]:
    return [word for word in words if word and word[0].isupper() and len(word) >= 3]


print(filter_strings(["Cat", "dog", "Sun", "apple", "Sky", "no"]))
# ['Cat', 'Sun', 'Sky']

