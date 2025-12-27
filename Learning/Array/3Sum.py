nums = [0, 0, 0, 0]
nums = [-4, -1, -1, 0, 1, 2]

def tree_sum(nums):
    result = []
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        target = -nums[i]
        left, right = i+1, len(nums)-1
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while right > left and nums[right-1] == nums[right]:
                    right-=1
                right-=1 
    return result

print(tree_sum(nums))