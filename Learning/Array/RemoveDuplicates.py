# Remove duplicates in place from sorted array
nums = [1, 1, 2, 3, 4, 5, 5, 5, 9] # desired [1,2,3,4,5,9,_,_,_]

def remove_duplicates(nums):
    left_pointer = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[left_pointer]:
            left_pointer += 1
            nums[i], nums[left_pointer] = nums[left_pointer], nums[i]
        else:
            continue
        
remove_duplicates(nums)
print(nums)