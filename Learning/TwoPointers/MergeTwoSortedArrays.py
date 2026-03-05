arr1 = [1, 4, 4]
arr2 = [2, 3, 5]

def merge_two_sorted_arrays(arr1, arr2):
    ptr1 = 0
    ptr2 = 0
    result = []
    while ptr1 < len(arr1) and ptr2 < len(arr2):
        if arr1[ptr1] < arr2[ptr2]:
            result.append(arr1[ptr1])
            ptr1 += 1
        else:
            result.append(arr2[ptr2])
            ptr2 += 1
    
    while ptr1 < len(arr1):
        result.append(arr1[ptr1])
        ptr1 += 1
        
    while ptr2 < len(arr2):
        result.append(arr2[ptr2])
        ptr2 += 1
    
    return result

print(merge_two_sorted_arrays(arr1, arr2))  # [1, 2, 3, 4, 4, 5]