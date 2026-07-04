class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)
h.next.next.next.next = ListNode(5)

# 2 -> 3 -> 4 -> 5
def reverseList(head):
    # Tree pointers
    previus = None
    current = head
    next = None
    
    while current:
        next = current.next
        current.next = previus
        previus = current
        current = next
    
    # Return previus because in the last iteration i set current to Null
    return previus    
    
def printH(h):
    if h == None:
        return 
    print(h.val)
    printH(h.next)