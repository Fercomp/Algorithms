class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    carry = 0
    l3 = ListNode()
    head = l3
    while l1 != None and l2 != None:
        a = l1.val if l1 else 0
        b = l2.val if l2 else 0
        result = (a + b + carry) % 10
        carry = (a + b + carry) // 10
        l3.val = result
        l3.next = ListNode()
        l3 = l3.next
        if l1.next:
            l1 = l1.next
    if carry != 0:
        l3.next = ListNode(carry)
        l3 = l3.next
    return head

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = addTwoNumbers(l1, l2)