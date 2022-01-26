// Definition for singly-linked list.
class ListNode {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function (head) {
    const s = new Set();
    while (head != null) {
        if (s.has(head)) {
            return true;
        }
        s.add(head);
        head = head.next;
    }
};

var i = 2;
head = new ListNode(1);
temp = head;
while (i < 6) {
    temp.next = new ListNode(i);
    temp = temp.next;
    i++;
}
head.next.next.next.next.next = head.next.next;
console.log(hasCycle(head));