l = [1, 2, 0, 3, 2, 0]
def sum_k(nums, partial_nums, partial_sum, target, size, i):
    if i == size:
        if target == partial_sum:
            print(partial_nums)
        return
    
    partial_nums.append(nums[i])
    sum_k(nums, partial_nums, partial_sum + nums[i], target, size, i+1)
    partial_nums.pop()
    sum_k(nums, partial_nums, partial_sum, target, size, i+1)


def first_sum_k(nums, partial_nums, partial_sum, target, size, i):
    if i == size:
        if target == partial_sum:
            print(partial_nums)
            return True
        return False
    
    partial_nums.append(nums[i])
    if first_sum_k(nums, partial_nums, partial_sum + nums[i], target, size, i+1):
        return True
    
    partial_nums.pop()
    if first_sum_k(nums, partial_nums, partial_sum, target, size, i+1):
        return True
    
    return False

def number_of_sum_k(nums, partial_nums, partial_sum, target, size, i):
    if i == size:
        if target == partial_sum:
            print(partial_nums)
            return 1
        return 0
    
    partial_nums.append(nums[i])
    a = number_of_sum_k(nums, partial_nums, partial_sum + nums[i], target, size, i+1)
    
    partial_nums.pop()
    b = number_of_sum_k(nums, partial_nums, partial_sum, target, size, i+1)
    
    return a + b

#sum_k(l, [], 0, 2, len(l), 0)
#first_sum_k(l, [], 0, 2, len(l), 0)
print(number_of_sum_k(l, [], 0, 2, len(l), 0))