# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

def pairSum(head):
    def reverse_first_half(head):
        slow = fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next

            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        return prev, slow

    prev, slow = reverse_first_half(head)
    max_sum = 0
    while prev and slow:
        max_sum = max(max_sum, prev.val + slow.val)
        prev = prev.next
        slow = slow.next

    return max_sum