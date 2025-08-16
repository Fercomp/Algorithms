'''
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    list3 = ListNode()
    head = list3
    while list1 != None and list2 != None:
        if list1 < list2:
            list3.next = list1
            list1 = list1.next
        else:
            list3.next = list2
            list2 = list2.next
        list3 = list3.next
    if list1 != None:
        list3.next = list1
    elif list2 != None:
        list3.next = list2

    return head.next