nums = [2, 3, 5, 8, 0]
nums1 = [1, 5, 6, 8, 11]
nums2 = [1, 5, 6, 11, 8]
nums3 = [11, 8, 6, 5, 1]
nums4 = [11, 8, 6, 1, 5]

def check_is_sorted(nums):
    if len(nums) <= 1:
        return True
    
    increasing_order = nums[0] < nums[1]
    for i in range(len(nums) - 1):
        if (increasing_order and nums[i] > nums[i + 1]) or (not increasing_order and nums[i] < nums[i+1]):
            return False
    
    return True

print(check_is_sorted(nums))  # False
print(check_is_sorted(nums1)) # True
print(check_is_sorted(nums2)) # False
print(check_is_sorted(nums3)) # True
print(check_is_sorted(nums4)) # False