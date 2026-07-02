# leetcode.com/problems/product-of-array-except-self

def productExceptSelf(nums):
    prefix = [0] * len(nums)
    sufix = [0] * len(nums)
    acc = 1
    for i in range(len(nums)):
        acc *= nums[i]
        prefix[i] = acc
        
    acc = 1
    for i in range(len(nums)-1, -1, -1):
        acc *= nums[i]
        sufix[i] = acc
    
    for i in range(len(nums)):
        pre = prefix[i-1] if i > 0 else 1
        suf = sufix[i+1] if i < len(nums) else 1
        nums[i] = pre * suf
        
    return nums

print(productExceptSelf([0, 0]))