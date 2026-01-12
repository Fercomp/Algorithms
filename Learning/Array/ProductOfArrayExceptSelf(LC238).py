# leetcode.com/problems/product-of-array-except-self

def productExceptSelf(nums):
    total = 1
    zeros = 0
    first_zero_index = -1

    for i in range(len(nums)):
        if nums[i] == 0 and zeros == 1:
            nums
            return [0] * len(nums)

        if nums[i] == 0:
            zeros += 1
            first_zero_index = i
            continue
        
        total *= nums[i]
    
    result = [0] * len(nums)
    if zeros:
        result[first_zero_index] = total
    else:
        for i in range(len(nums)):
            result[i] = total // nums[i]
    return result