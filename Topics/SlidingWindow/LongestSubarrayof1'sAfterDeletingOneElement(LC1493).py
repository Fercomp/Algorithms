def longestSubarray(nums):
    if all(nums):
        return len(nums) - 1
    if not any(nums):
        return 0

    l, r = 0, 0
    deleted = False
    longest = 0

    while r < len(nums):
        if nums[r] == 1:
            r += 1

        else:
            if not deleted:
                deleted = True
                r += 1

            else:
                while nums[l] == 1:
                    l += 1
                l += 1
                r += 1

        longest = max(longest, r - l if not deleted else r - l - 1)
    
    return longest