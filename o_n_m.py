
# new_case O(n*m)
def find_pairs(a: list[int], b: list[int], target: int) -> list[tuple[int, int]]:
    result = []
    a, b = set(a), set(b)
    for x in a:
        for y in b:
            if x + y == target:
                result.append((x, y))
    return result

print(find_pairs([1,2,3,4,5], [1,2,3], 5))

# new_case O(n+m)
def find_pairs_optimized(a: list[int], b: list[int], target: int) -> list[tuple[int, int]]:
    result = []
    set_b = set(b)  # Быстрый поиск элементов b — O(1) для каждого
    for x in a:
        complement = target - x
        if complement in set_b:
            result.append((x, complement))
    return result

print(find_pairs_optimized([1,2,3,4,5], [1,2,3], 5))



def mystery_function(lst):
    n = len(lst)
    for i in range(n):
        print(f"{n=}")
        j = 1
        print(f"{j=}")
        while j < n:
            print(f"{lst[i]=}, {lst[j]=}")
            j *= 2
        print(f"end:{i}")

mystery_function([1,2,3,4,5])