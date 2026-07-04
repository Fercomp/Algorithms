nums = [1,2,3,4,5,6,7,8,9]
target = 4

def binary_search(nums, target, l ,r):
    if l > r:
        return -1
    mid = (l + r) // 2
    if nums[mid] == target:
        return mid
    if nums[mid] < target:
        return binary_search(nums, target, mid+1, r)
    else:
        return binary_search(nums, target, l, mid-1)

print(binary_search(nums, target, 0, len(nums)-1))