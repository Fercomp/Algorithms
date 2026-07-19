# If i know that two intervals have intersection we can get this
# intersection, from the maximum of the first value of both and 
# the minimun of the second value
def intersection(interval1, interval2):
    lower_bound = max(interval1[0], interval2[0])
    upper_bound = min(interval1[1], interval2[1])
    return [lower_bound, upper_bound]

# Time: O(n)
# Space: O(n)
def interval_intersection(arr1, arr2):
    arr1_ptr = 0
    arr2_ptr = 0
    result = []
    
    while arr1_ptr < len(arr1) and arr2_ptr < len(arr2):
        min_arr1, max_arr1, min_arr2, max_arr2 = arr1[arr1_ptr][0], arr1[arr1_ptr][1], arr2[arr2_ptr][0], arr2[arr2_ptr][1]
        
        # This interval don't intersect because arr1 interval is too low
        if max_arr1 < min_arr2:
            arr1_ptr += 1
        
        # This case, arr1 is much grather than arr2 interval
        elif min_arr1 > max_arr2:
            arr2_ptr += 1
        
        # This case we have an intersection
        else:
            intersec = intersection(arr1[arr1_ptr], arr2[arr2_ptr])
            result.append(intersec)
            
            # We add one to the interval that stops earlier
            if arr1[arr1_ptr][1] > arr2[arr2_ptr][1]:
                arr2_ptr += 1
            else:
                arr1_ptr += 1
    
    return result

arr1 = [[0,1], [4,6], [7,8]]
arr2 = [[2,3], [5,9], [10,11]]
print(interval_intersection(arr1, arr2))  # [[5, 6], [7, 8]]

arr1 = [[2, 4], [5, 8]]
arr2 = [[3, 3], [4, 7]]
print(interval_intersection(arr1, arr2))  # [[3, 3], [4, 4], [5, 7]]