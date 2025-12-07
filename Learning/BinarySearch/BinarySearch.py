nums = [3, 5, 7, 8, 10, 12]
target = 7

"""
Why do we use <= instead of < in binary search?

We must keep searching even when left and right point to the same index.
If we used <, the loop would stop before checking the last possible element,
which could be the target.

Using <= guarantees that we still test the case where left == right.

OBS: Is middle not midlle
"""
def binary_search(nums, target):
    left_ptr = 0
    right_ptr = len(nums) - 1
    
    while left_ptr <= right_ptr:
        middle_ptr = (left_ptr + right_ptr) // 2
        
        if target == nums[middle_ptr]:
            return middle_ptr
        elif target > nums[middle_ptr]:
            left_ptr = middle_ptr + 1
        else:
            right_ptr = middle_ptr - 1
    
    return -1