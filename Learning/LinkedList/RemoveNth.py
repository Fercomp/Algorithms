class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)
h.next.next.next.next = ListNode(5)

def removeNthFromEnd(head, n):
    count = 0
    count_p = head
    while count_p:
        count_p = count_p.next
        count += 1
    
    branch_point = count - n -1
    branch_p = head
    while branch_point > 0:
        branch_p = branch_p.next
        branch_point -= 1

    if n == 1:
        branch_p.next = None
    else:
        branch_p.next = branch_p.next.next
    return head

removeNthFromEnd(h, 2)