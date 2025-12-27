# leetcode.com/problems/remove-element

nums = [3,2,3,3,1,4,5,3]
target = 3

def removeElement(nums, val):
    current = 0
    index = 0
    while index < len(nums):
        if nums[index] != val:
            nums[current] = nums[index]
            index += 1
            current += 1
        else:
            index += 1
    return current