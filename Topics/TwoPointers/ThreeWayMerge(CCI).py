arr1 = [2, 3, 3, 4, 5, 7]
arr2 = [3, 3, 9]
arr3 = [3, 3, 9]

def merge_two(arr1, arr2):
    ptr1 = 0
    ptr2 = 0
    result = [min(arr1[ptr1], arr2[ptr2])]
    while ptr1 < len(arr1) and ptr2 < len(arr2):
        if arr1[ptr1] < arr2[ptr2]:
            if arr1[ptr1] != result[-1]:
                result.append(arr1[ptr1])
            ptr1 += 1
        else:
            if arr2[ptr2] != result[-1]:
                result.append(arr2[ptr2])
            ptr2 += 1
    
    while ptr1 < len(arr1):
        if arr1[ptr1] != result[-1]:
            result.append(arr1[ptr1])
        ptr1 += 1
        
    while ptr2 < len(arr2):
        if arr2[ptr2] != result[-1]:
            result.append(arr2[ptr2])
        ptr2 += 1
    
    return result


def three_way_merge(arr1, arr2, arr3):
    first_list = merge_two(arr1, arr2)
    second_list = merge_two(first_list, arr3)
    return second_list

print(three_way_merge(arr1, arr2, arr3))