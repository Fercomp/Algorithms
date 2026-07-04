# leetcode.com/problems/house-robber/description/

def rob(nums):
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    for i in range(1, n):
        not_take = dp[i-1]
        aux = 0
        if i-2>=0:
            aux = dp[i-2]
        take = nums[i] + aux
        dp[i] = max(take, not_take)

    return dp[-1]

nums = [2,7,9,3,1]
print(rob(nums))