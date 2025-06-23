




def unique_letters(text:str):

    return set([l.lower() for l in text if l.isalpha()])

# print(unique_letters("Hello, World!"))  # {'h', 'e', 'l', 'o', 'w', 'r', 'd'}


def compare_texts(a: str, b: str) -> tuple[set, set, set]:
    a = {l.lower() for l in a if l.isalpha()}
    b = {l.lower() for l in b if l.isalpha()}
    return a & b, a - b, b - a



# print(compare_texts("Apple Pie", "Peach"))
# 👉 ({'p', 'e'}, {'a', 'l', 'i'}, {'c', 'h'})


# print({1,2,3,4} & {3,4,5})
# print({1,2,3,4} ^ {3,4,5})
# print({1,2,3,4} - {2,3,4,5})
# print({1,2,3,4} | {3,4,5})


def weird_words(words1: list[str], words2: list[str]) -> tuple[set, set]:
    letters1 = {ch.lower() for word in words1 for ch in word if ch.isalpha()}
    letters2 = {ch.lower() for word in words2 for ch in word if ch.isalpha()}
    all_letters = letters1 | letters2
    symmetric_diff = letters1 ^ letters2
    return all_letters, symmetric_diff


# print(weird_words(["Hello", "World"], ["Python", "Code"]))
# 👉 ({все уникальные буквы}, {симметрическая разность})


def unique_digits(numbers: list[str]) -> set:
    return {n for string in numbers for n in string if n.isdecimal()}

print(unique_digits(["Room 404", "Call 123!", "No 007"]))
# 👉 {'0', '1', '2', '3', '4', '7'}
