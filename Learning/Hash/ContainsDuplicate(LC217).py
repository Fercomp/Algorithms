# leetcode.com/problems/contains-duplicate/

def containsDuplicate(nums):
    set_nums = set(nums)
    return len(set_nums) != len(nums)