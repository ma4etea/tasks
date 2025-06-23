




def unique_letters(text:str):

    return set([l.lower() for l in text if l.isalpha()])

# print(unique_letters("Hello, World!"))  # {'h', 'e', 'l', 'o', 'w', 'r', 'd'}


def compare_texts(a: str, b: str) -> tuple[set, set, set]:
    a = {l.lower() for l in a if l.isalpha()}
    b = {l.lower() for l in b if l.isalpha()}
    return a & b, a - b, b - a



print(compare_texts("Apple Pie", "Peach"))
# 👉 ({'p', 'e'}, {'a', 'l', 'i'}, {'c', 'h'})
