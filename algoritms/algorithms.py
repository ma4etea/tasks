
def gcd_of_strings(self, str1: str, str2: str) -> str:
    # Напишите здесь свой код
    if str1 + str2 != str2 + str1:
        return ""

    dividend = len(str1)  # 30
    devisor = len(str2)  # 18

    # todo Алгоритм Евклида
    while devisor != 0:
        common_division = devisor
        devisor = dividend % devisor  # 30 % 18 = 12, 18 % 12 = 6, 12 % 6 = 0
        dividend = common_division

    return str1[:common_division]



def missing_number(self, nums: list[int]) -> int:
    n = len(nums)

    total = n * (n + 1) // 2 # todo формула: сумма арифметической прогрессии
    nums_total = sum(nums)
    return total - nums_total
    # Напишите здесь свой код

def missing_number_xor(self, nums: list[int]) -> int:
    doc_path = "docs/xor.md"

    missing = len(nums)

    # todo Поиск пропавшего числа через XOR
    for index, num in enumerate(nums):
        missing = missing ^ index ^ num

    return missing

def two_sum(self, nums: list[int], target: int) -> list[int]:
    table_map = {}

    # todo решение через хэш таблицу
    for index, num in enumerate(nums):
        diff = target - num

        if diff in table_map:
            return [table_map[diff], index]

        table_map[num] = index