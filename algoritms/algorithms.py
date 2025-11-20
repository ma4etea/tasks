
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

def longest_palindrome(self, s: str) -> int:
    """Самый длинный полиндром"""

    letter_quantity_map = {}

    for letter in s:
        letter_quantity_map[letter] = letter_quantity_map.get(letter, 0) + 1

    result = 0
    center_used = False
    for quantity in letter_quantity_map.values():
        result += quantity // 2 * 2 #
        if quantity % 2 == 1 and not center_used:
            center_used = True

    return result + center_used


def insert_search(nums: list[int], target: int) -> int:
    left_index = 0
    right_index = len(nums) - 1

    # todo бинарный поиск
    while left_index <= right_index:
        mid_index = (right_index - left_index) // 2 + left_index

        if nums[mid_index] == target:
            return mid_index
        elif target > nums[mid_index]:
            left_index = mid_index + 1
        elif target < nums[mid_index]:
            right_index = mid_index - 1

    return left_index
