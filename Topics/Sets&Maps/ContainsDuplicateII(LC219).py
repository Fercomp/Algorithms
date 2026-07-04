# leetcode.com/problems/contains-duplicate-ii/

def containsNearbyDuplicate(nums, k: int):
    num_to_idx = {}
    for idx, num in enumerate(nums):
        if num in num_to_idx:
            if abs(idx - num_to_idx[num]) <= k:
                return True
        num_to_idx[num] = idx
    return False