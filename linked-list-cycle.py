from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: Optional[ListNode]) -> bool:
    s = set()
    while head != None:
        if head in s:
            return True
        s.add(head)
        head = head.next
    return False


# Making Linked list
i = 2
head = ListNode(1)
temp = head
while i < 6:
    temp.next = ListNode(i)
    temp = temp.next
    i += 1

head.next.next.next.next.next = head.next.next.next
print(hasCycle(head))
