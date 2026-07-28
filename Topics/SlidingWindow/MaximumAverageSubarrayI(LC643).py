# https://leetcode.com/problems/maximum-average-subarray-i/

def findMaxAverage(nums, k):
    max_sum = sum(nums[:k])
    curr_sum = max_sum

    for idx in range(1, len(nums) -k + 1):
        curr_sum +=  (nums[idx + k -1] -nums[idx-1])
        max_sum = max(max_sum, curr_sum)

    return max_sum / k