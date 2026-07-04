def duplicate_removal(arr):
    if len(arr) <= 1:
        return
    
    seeker, writter = 1, 1
    
    while seeker < len(arr):
        if arr[seeker] == arr[seeker - 1]:
            seeker += 1
            
        else:
            arr[writter] = arr[seeker]
            seeker += 1
            writter += 1
            
    return writter
            
arr = [1, 2, 2, 3, 3, 3, 5]
print(duplicate_removal(arr))