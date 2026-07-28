# leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k

def maximumSubarraySum(nums, k):
    frequency = set()
    l = curr_sum = max_sum = 0

    for r in range(len(nums)):
        while nums[r] in frequency:
            frequency.remove(nums[l])
            curr_sum -= nums[l]
            l += 1

        curr_sum += nums[r]
        frequency.add(nums[r])
        
        if r - l + 1 > k:
            curr_sum -= nums[l]
            frequency.remove(nums[l])
            l += 1

        if r - l + 1 == k:
            max_sum = max(max_sum, curr_sum)

    return max_sum