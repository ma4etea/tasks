def count_even(param):
    return sum(1 for x in param if x % 2 == 0)
    #return len([even for even in param if even % 2 == 0])



even1 = count_even([1, 2, 3, 4, 5, 6])  # → 3
print(even1)


def remove_duplicates(param):
    string = ''
    for symbol in param:
        if symbol not in string:
            string += symbol
    return string


remove_duplicates("hello")      # → "helo"
remove_duplicates("aabbccdd")   # → "abcd"
remove_duplicates("abcabcabc")  # → "abc"

print(remove_duplicates("hello") , remove_duplicates("aabbccdd"), remove_duplicates("abcabcabc"))

fff = 'lldd'
print('l' not in fff)