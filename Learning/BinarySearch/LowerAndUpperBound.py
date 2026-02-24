# Lower bound is the firs element that is grather than or equal >= target
nums = [1,3,5,6,11,12,13,15]
target = 7
# If you pay attention this is just a transition questions
def lowerBound(nums, target):
    l = 0
    r = len(nums) - 1
    while r > l + 1:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            r = mid
        else:
            l = mid
    return nums[r]

# The upper bound is the first position after the last ocurrence of x, 
# or first index grater > target

print(lowerBound(nums, target))
        