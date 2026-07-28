# https://leetcode.com/problems/reverse-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    if not head or not head.next:
        return head
    
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