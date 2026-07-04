arr = [1, 7, 2, 3, 3, 5, 3]
pivot = 4

def quick_sort_partition(arr, pivot):
    l = 0
    r = len(arr) - 1
    while l < r:
        if arr[l] < pivot:
            l += 1
        elif arr[r] >= pivot:
            r -= 1
        else:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
            
quick_sort_partition(arr, pivot)
print(arr)