# https://leetcode.com/problems/remove-duplicates-from-sorted-list

import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next        

def deleteDuplicates(head):
    dummy = ListNode(-math.inf)
    dummy.next = head
    previous = dummy
    current = head
    
    while current:
        if current.val == previous.val:
            previous.next = current.next
        else:
            previous = current
        current = current.next
        
    return dummy.next