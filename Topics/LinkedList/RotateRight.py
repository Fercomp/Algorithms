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

def rotate(h, k):
    n = countLL(h)
    r = k % n
    i = n - r - 1
    
    a = h
    for _ in range(i-1):
        a = a.next
    n = a
    a = a.next
    n.next = None
        
    b = a
    while b.next != None:
        b = b.next
    b.next = h
    
    return a

rotate(h, 2)