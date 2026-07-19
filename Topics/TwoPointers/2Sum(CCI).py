# Time: O(n)
# Space: O(1)
def two_sum(nums, target):
    l, r = 0, len(nums) -1
    
    while l < r:
        if nums[l] + nums[r] == target: return True
        elif nums[l] + nums[r] > target: r -= 1
        else: l += 1
        
    return False