def find_all_squares(nums):
    result = []
    num_to_idx = { num: idx for idx, num in enumerate(nums) }
    
    for idx, num in enumerate(nums):
        power = pow(num, 2)
        if power in num_to_idx:
            result.append([idx, num_to_idx[power]])
        num_to_idx[power] = idx
        
    return result