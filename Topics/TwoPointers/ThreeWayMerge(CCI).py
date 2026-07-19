import math

# Time: O(n)
# Space: O(n)
def three_way_merge(arr1, arr2, arr3):
    idx0 = idx1 = idx2 = 0
    result = []

    while idx0 < len(arr1) or idx1 < len(arr2) or idx2 < len(arr3):
        a = arr1[idx0] if idx0 < len(arr1) else math.inf
        b = arr2[idx1] if idx1 < len(arr2) else math.inf
        c = arr3[idx2] if idx2 < len(arr3) else math.inf

        m = min(a, b, c)

        if not result or result[-1] != m:
            result.append(m)

        if a == m:
            idx0 += 1
        if b == m:
            idx1 += 1
        if c == m:
            idx2 += 1

    return result

# Time: O(2n)
# Space: O(n)
def three_way_merge2(arr1, arr2, arr3):
    
    def two_way_merge(arr1, arr2):
        idx0 = idx1 = 0
        result = []

        while idx0 < len(arr1) and idx1 < len(arr2):
            if arr1[idx0] <= arr2[idx1]:
                if not result or result[-1] != arr1[idx0]:
                    result.append(arr1[idx0])
                idx0 += 1
            else:
                if not result or result[-1] != arr2[idx1]:
                    result.append(arr2[idx1])
                idx1 += 1

        while idx0 < len(arr1):
            if not result or result[-1] != arr1[idx0]:
                result.append(arr1[idx0])
            idx0 += 1

        while idx1 < len(arr2):
            if not result or result[-1] != arr2[idx1]:
                result.append(arr2[idx1])
            idx1 += 1

        return result     
    
    m1 = two_way_merge(arr1, arr2)
    return two_way_merge(m1, arr3)