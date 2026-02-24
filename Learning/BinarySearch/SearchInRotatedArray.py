nums = [5,1,3]

def search(nums, target):
    l = 0
    r = len(nums) -1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[l] <= nums[mid]:
            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if target > nums[l]:
                r = mid - 1
            else:
                return -1

print(search(nums, 5))