# leetcode.com/problems/palindrome-partitioning


s = "aab"

def is_palindrome(s):
    if not s:
        return False
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def partition(s):
    all_partitions = []
    left = 0
    right = len(s) - 1
    while left <= right:
        a, b, c  = s[left:right+1], s[left+1:right+1], s[left:right]
        if is_palindrome(a):
            all_partitions.append(a)
        if is_palindrome(b):
            all_partitions.append(b)
        if is_palindrome(c):
            all_partitions.append(c)
        left += 1
        right -= 1
    return all_partitions