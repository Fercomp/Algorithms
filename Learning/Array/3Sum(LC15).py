# leetcode.com/problems/3sum/
nums = [-4, -1, -1, 0, 1, 2]

# Time: O(nˆ3)
# Space: O(k), k is the number of triplets
def brute_force_three_sum(nums):
    result = set()
    for i in range(len(nums) - 2):
        for j in range(i+ 1, len(nums) - 1):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    # We cannot add lists to a set because they are mutable
                    # and therefore not hashable. For that reason, we need to
                    # convert them to tuples first.
                    result.add(tuple(sorted([nums[i], nums[j], nums[k]])))
    return [list(x) for x in result]

print(brute_force_three_sum(nums))

# Time: O(nˆ2)
# Space: O(n + k), k is the number of triplets
def hashing_three_sum(nums):
    result = set()
    for i in range(len(nums)):
        target = -nums[i]
        s = set()
        for j in range(i+1, len(nums)):
            desired = target - nums[j]
            if desired in s:
                result.add(tuple(sorted([nums[i], nums[j], desired])))
            s.add(nums[j])
    
    return [list(x) for x in result]

print(hashing_three_sum(nums))

# Time: O(nˆ2)
# Space: O(1)
def optimized_three_sum(nums):
    result = []
    nums.sort()
    
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        if nums[i] > 0:
            break
        
        l, r = i + 1, len(nums) - 1
        
        while l < r:
            soma = nums[i] + nums[l] + nums[r]
            
            if soma == 0:
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1
                    
            elif soma < 0:
                l += 1
            else:
                r -= 1  
    return result

print(optimized_three_sum(nums))