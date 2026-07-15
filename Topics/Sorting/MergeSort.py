def merge(arr1, arr2):    
    result = []
    idx_1, idx_2 = 0, 0
    while idx_1 < len(arr1) and idx_2 < len(arr2):
        if arr1[idx_1] < arr2[idx_2]:
            result.append(arr1[idx_1])
            idx_1 += 1
        else:
            result.append(arr2[idx_2])
            idx_2 += 1
    
    while idx_1 < len(arr1):
        result.append(arr1[idx_1])
        idx_1 += 1
    
    while idx_2 < len(arr2):
        result.append(arr2[idx_2])
        idx_2 += 1
        
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)
    
print(merge_sort([4, 12, 8, 9, 2]))