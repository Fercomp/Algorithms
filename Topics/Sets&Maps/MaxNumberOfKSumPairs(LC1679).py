from collections import defaultdict

def maxOperations(nums, k):
    s = defaultdict(list)
    
    for idx, val in enumerate(nums):
        s[val].append(idx)
    
    operations = 0
    for val in nums:
        target = k - val
        
        if target in s:
            if val == target:
                if len(s[val]) >= 2:
                    s[val].pop()
                    s[val].pop()    
                    operations += 1
            
            else:
                if s[val] and s[target]:
                    s[val].pop()
                    s[target].pop()
                    operations += 1
    
    return operations

print(maxOperations([1,2,3,4], 5))