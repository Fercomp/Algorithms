# Time: O(n)
# Space: O(1)
def smaller_prefixes(arr):
    n = len(arr)
    slow_pointer, fast_pointer, slow_sum, fast_sum = 0
    
    while fast_pointer < n:
        slow_sum += arr[slow_pointer]
        fast_sum += arr[fast_pointer] + arr[fast_pointer + 1]
        
        if slow_sum >= fast_sum:
            return False
        
        slow_pointer += 1
        fast_pointer += 2
        
    return True