from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        l = list()
        curr = self
        while curr:
            l.append(curr.val)
            curr = curr.next
        return str(l)


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    # Actual Solution starts
    curr = head
    newhead = None
    while curr:
        temp = curr.next
        curr.next = newhead
        newhead = curr
        curr = temp
    return newhead


i = 2
head = ListNode(1)
curr = head
while i < 6:
    curr.next = ListNode(i)
    curr = curr.next
    i += 1
emptyhead = None
print(reverseList(head))
print(reverseList(emptyhead))
