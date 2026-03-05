def parity_sorting(arr):
    l, r = 0, len(arr) - 1
    
    while l < r:
        if arr[l] % 2 == 0:
            l += 1
            
        elif arr[r] % 2 != 0:
            r -= 1

        else:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
            
arr = [1, 2, 3, 4, 5]
parity_sorting(arr)
print(arr)  # [2, 4, 1, 3, 5]