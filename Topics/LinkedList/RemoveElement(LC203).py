# https://leetcode.com/problems/remove-linked-list-elements

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, val):
    dummy = ListNode(0)
    dummy.next = head

    previous = dummy
    current = dummy.next

    while current:
        if current.val == val:
            previous.next = current.next
            current = current.next
        else:
            previous = current
            current = current.next

    return dummy.next