
def gcd_of_strings(str1: str, str2: str) -> str:
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



def missing_number(nums: list[int]) -> int:
    n = len(nums)

    total = n * (n + 1) // 2 # todo формула: сумма арифметической прогрессии
    nums_total = sum(nums)
    return total - nums_total
    # Напишите здесь свой код

def missing_number_xor(nums: list[int]) -> int:
    doc_path = "docs/xor.md"

    missing = len(nums)

    # todo Поиск пропавшего числа через XOR
    for index, num in enumerate(nums):
        missing = missing ^ index ^ num

    return missing

def two_sum(nums: list[int], target: int) -> list[int]:
    table_map = {}

    # todo решение через хэш таблицу
    for index, num in enumerate(nums):
        diff = target - num

        if diff in table_map:
            return [table_map[diff], index]

        table_map[num] = index

def longest_palindrome(s: str) -> int:
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

def move_zeroes(nums: list[int]) -> None:

    nums_len = len(nums)
    # todo двух указательный алгоритм
    insert_pointer = 0
    for num in nums:
        if num != 0:
            nums[insert_pointer] = num
            insert_pointer += 1

    while insert_pointer < nums_len:
        nums[insert_pointer] = 0
        insert_pointer += 1

def remove_stars(self, s: str) -> str:
    # todo техника "стэк"
    stack = []
    for l in s:
        if l == "*" and stack:
            stack.pop()
        else:
            stack.append(l)
    return "".join(stack)




class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

    dummy = ListNode()  # фиктивный узел
    tail = dummy  # конец нового списка

    # пока оба списка не закончились
    while list1 and list2:

        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next  # двигаем хвост

    # прикрепляем остаток
    tail.next = list1 if list1 else list2

    return dummy.next


def fib(n: int) -> int:

    # todo формула Бине ищет число фибо по номеру позиции, до 70 позиции безопасно
    phi = (1+5**0.5) / 2
    psi = (1-5**0.5) / 2

    fibo = (phi**n - psi**n) / 5**0.5
    return int(round(fibo))

range()