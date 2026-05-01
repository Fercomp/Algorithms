# leetcode.com/problems/3sum/
nums = [-4, -1, -1, 0, 1, 2]

# Time: O(nˆ3)
# Space: O(k), k is the number of triplets
def brute_force_tree_sum(nums):
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

print(brute_force_tree_sum(nums))


# Time: O(nˆ2)
# Space: O(n + k), k is the number of triplets
def hashing_tree_sum(nums):
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

print(hashing_tree_sum(nums))