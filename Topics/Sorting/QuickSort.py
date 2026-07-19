def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    less, equal, grather = [], [], []
    pivot = arr[-1]
    
    for num in arr:
        if num < pivot:
            less.append(num)
        elif num > pivot:
            grather.append(num)
        else:
            equal.append(num)
            
    return quick_sort(less) + equal + quick_sort(grather)