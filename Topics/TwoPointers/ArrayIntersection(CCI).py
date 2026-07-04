# Time: O(n)
# Space: O(n)
def array_intersection(arr1, arr2):
    pointer_1, pointer_2 = 0, 0
    
    result = []
    while pointer_1 < len(arr1) and pointer_2 < len(arr2):
        if arr1[pointer_1] == arr2[pointer_2]:
            result.append(arr1[pointer_1])
            pointer_1 += 1
            pointer_2 += 1
        elif arr1[pointer_1] < arr2[pointer_2]:
            pointer_1 += 1
        else:
            pointer_2 += 1
            
    return result
            
print(array_intersection([1, 2, 3], [1, 3, 5])) # [1, 3]
print(array_intersection([1, 1, 1], [1, 1]))    # [1, 1]