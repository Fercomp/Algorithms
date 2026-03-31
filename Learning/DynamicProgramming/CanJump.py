
def can_jump(nums):
    dp = [False] * len(nums)
    dp[0] = True
    for index, num in enumerate(nums):
        if dp[index] == True:
            for i in range(1, num+1):
                if index + i < len(nums):
                    dp[index + i] = True
    return dp[-1]

print(can_jump([2,3,1,1,4]))
print(can_jump([3,2,1,0,4]))
print(can_jump([0,2,3]))