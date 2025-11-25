class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1: ListNode | None, list2: ListNode | None) -> list | None:

    dammy = ListNode()
    tail = dammy

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

    result = []
    node = dammy.next
    while node:
        result.append(node.val)
        node = node.next
    return result if result else None

print(merge_two_lists(ListNode(1, ListNode(2)), ListNode(3, ListNode(4))))
print(merge_two_lists(None, None))
print(merge_two_lists(None, ListNode(1, ListNode(2))))