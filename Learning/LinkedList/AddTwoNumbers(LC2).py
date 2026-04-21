# https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    current = dummy
    carry = 0

    while l1 or l2:
        a = l1.val if l1 else 0
        b = l2.val if l2 else 0
        soma = a + b + carry
        q, r = divmod(soma, 10)
        carry = q
        current.next = ListNode(r)
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    if carry:
        current.next = ListNode(carry)
    
    return dummy.next