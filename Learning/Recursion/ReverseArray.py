def reverse_p(arr, n, r):
    if n < 0:
        print(r)
        return
    
    r.append(arr[n])
    reverse_p(arr, n-1, r)

def reverse_f(arr, n, r):
    if n < 0:
        return r
    
    r.append(arr[n])
    return reverse_f(arr, n-1, r)

# This approach doesn't need an auxiliary array and is in O(n/2)
def reverse_p2(arr, l, r):
    if l >= r:
        print(arr)
        return
    
    aux = arr[l]
    arr[l] = arr[r]
    arr[r] = aux
    reverse_p2(arr, l+1, r-1)

nums = [2, 3, 4, 5, 6]
reverse_p2(nums, 0, len(nums)-1)