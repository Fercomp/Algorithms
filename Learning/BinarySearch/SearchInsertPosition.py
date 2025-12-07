# https://leetcode.com/problems/search-insert-position/description/?envType=problem-list-v2&envId=array

nums = [1,3,5,6]
target = 5

def searchInsert(nums, target):
    left_ptr = 0
    right_ptr = len(nums) - 1
    while left_ptr <= right_ptr:
        midlle_ptr = (right_ptr + left_ptr) // 2
        if nums[midlle_ptr] == target:
            return midlle_ptr
        elif nums[midlle_ptr] > target:
            right_ptr = midlle_ptr - 1
        else:
            left_ptr = midlle_ptr + 1

    # The only difference from binary search is that when we don't find the target,
    # the left pointer passes the right, so it's pointing to where the target
    # should be if it was in the array
    return left_ptr
    
print(searchInsert(nums, 7))