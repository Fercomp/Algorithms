nums = [-1,0,1,2,-1,-4]
left = 0
right = len(nums) - 1

d = {}
for index, data in enumerate(nums):
    d[data] = index

tripplets = set()
while left < right:
    target = -(nums[left] + nums[right])
    desired_index = d.get(target, None)
    if desired_index != None:
        tripplets.add((left, right, desired_index))
        left += 1
        right -= 1
    elif target > nums[left]:
        left += 1
    else:
        right -= 1

print(tripplets)
        