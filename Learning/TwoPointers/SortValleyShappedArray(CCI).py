arr1 = [8, 4, 2, 6]
arr2 = [1, 2]
arr3 = [2, 2, 1, 1]

def sort_valley_shapped_array(arr):
    l = 0
    r = len(arr) - 1
    result = []
    
    while l <= r:
        if arr[l] >= arr[r]:
            result.append(arr[l])
            l += 1
            
        else:
            result.append(arr[r])
            r -= 1
            
    return list(reversed(result))

print(sort_valley_shapped_array(arr1)) # [2, 4, 6, 8]
print(sort_valley_shapped_array(arr2)) # [1, 2]
print(sort_valley_shapped_array(arr3)) # [1, 1, 2, 2]