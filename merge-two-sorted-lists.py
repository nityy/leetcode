from typing import Optional

# Definition for singly-linked list.


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


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    h = ListNode()
    temp = h
    while list1 and list2:
        if (list1.val < list2.val):
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
        temp = temp.next
    if (list2):
        temp.next = list2
    if (list1):
        temp.next = list1
    return h.next


head1 = ListNode(1, ListNode(2, ListNode(4)))
head2 = ListNode(1, ListNode(3, ListNode(4)))
# head1 = None
# head2 = None
print(mergeTwoLists(head1, head2))
