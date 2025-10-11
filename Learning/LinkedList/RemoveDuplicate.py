class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
h = ListNode(1)
h.next = ListNode(1)
h.next.next = ListNode(1)
h.next.next.next = ListNode(2)


def deleteDuplicates(head):
    if head == None:
        return head
    
    dummy = ListNode(-1, head)
    cur = dummy
    
    while cur.next != None:
        if cur.val != cur.next.val:
            cur = cur.next
        else:
            b = cur
            while b.next != None and b.val == cur.val:
                b = b.next
            cur.next = b
        
    return head