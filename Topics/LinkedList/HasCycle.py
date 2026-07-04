class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    fast_pointer = head
    slow_pointer = head
    current_pointer = head
    while fast_pointer and slow_pointer:
        slow_pointer = current_pointer.next
        if slow_pointer:
            fast_pointer = slow_pointer.next
            if slow_pointer == fast_pointer:
                return False
        current_pointer = current_pointer.next
        
    return True