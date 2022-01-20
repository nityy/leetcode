# Building an iterator for a linked list
# Along with string representation of linked list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head) -> None:
        self.head = head

    def __str__(self) -> str:
        l = list()
        curr = self.head
        while curr:
            l.append(curr.val)
            curr = curr.next
        return str(l)

    def __next__(self):
        if self.head == None:
            raise StopIteration
        v = self.head.val
        self.head = self.head.next
        return v

    def __iter__(self):
        return self


# Making Linked list
i = 2
head = ListNode(1)
temp = head
while i < 6:
    temp.next = ListNode(i)
    temp = temp.next
    i += 1
ll = LinkedList(head)

# Printing linked list
print(ll)

# Testing linked list as a iterator
for v in ll:
    print(v)
