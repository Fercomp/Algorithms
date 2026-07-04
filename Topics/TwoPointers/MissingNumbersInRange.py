arr = [6,9,12,15,18]
low = 9
hight = 13

def missing_numbers_in_range(arr1, low, hight):
    # Preciso fazer um list(), em volta do range() para virar uma lista
    arr2 = list(range(low, hight+1))
    arr1_ptr, arr2_ptr = 0, 0
    result = []
    
    while arr1_ptr < len(arr1) and arr2_ptr < len(arr2):
        if arr1[arr1_ptr] < arr2[arr2_ptr]:
            arr1_ptr += 1
            
        elif arr1[arr1_ptr] > arr2[arr2_ptr]:
            result.append(arr2[arr2_ptr])
            arr2_ptr += 1
            
        else:
            arr1_ptr += 1
            arr2_ptr += 1
            
    return result

print(missing_numbers_in_range(arr, low, hight)) # [10, 11, 13]