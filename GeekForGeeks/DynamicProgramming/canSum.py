# You are given an array of numbers and a target you need to say if is possible or 
# not to sum up that number
# Time: O(n ^ target)
# Space: O(target)
def can_sum(target, nums):
    if not target:
        return True
    if target < 0:
        return False
    
    result = False
    for n in nums:
        result = result or can_sum(target - n, nums)
    return result

def can_sum_memo(target, nums, m={}):
    if target in m:
        return m[target]
    if not target:
        return True
    if target < 0:
        return False
    
    result = False
    for n in nums:
        result = result or can_sum_memo(target - n, nums, m)

    m[target] = result
    return result
    
print(can_sum(6, [2, 5, 3, 4]))
print(can_sum(7, [2, 4]))
print(can_sum_memo(6, [2, 5, 3, 4]))
print(can_sum_memo(7, [2, 4]))