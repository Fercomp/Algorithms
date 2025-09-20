class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def countLL(head):
    if not head:
        return 0
    return 1 + countLL(head.next)

h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)
h.next.next.next.next = ListNode(5)

def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    size = countLL(h)
    t = size - n - 1

    
    

removeNthFromEnd(h, 1)