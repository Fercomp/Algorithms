# https://leetcode.com/problems/odd-even-linked-list

def oddEvenList(head):
    if not head:
        return head

    if not head.next:
        return head

    head_odd, head_even = head, head.next
    curr_odd, curr_even = head_odd, head_even

    while curr_even and curr_even.next:
        curr_odd.next = curr_even.next
        curr_odd = curr_odd.next
        
        curr_even.next = curr_odd.next
        curr_even = curr_even.next
    
    curr_odd.next = head_even
    return head_odd