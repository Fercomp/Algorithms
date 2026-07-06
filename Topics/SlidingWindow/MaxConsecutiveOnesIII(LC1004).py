def longestOnes(nums, k):
    l, r = 0, 0
    count = 0

    while r < len(nums):
        if nums[r] == 1:
            r += 1

        else:
            if k > 0:
                k -= 1
                r += 1 

            else:
                while nums[l] == 1:
                    l += 1
                k += 1
                l += 1
                
        count = max(count, r - l)
    return count