def rotateLeft(d, arr):
    # Mod in over len(arr) and not len(arr) -1
    mod = len(arr)
    result = [0] * len(arr)
    for i in range(len(arr)):
        # We don't have any problem getting the negative mod
        result[(i - d) % mod] = arr[i]
    return result

arr = [2, 3, 4]
d = 6
print(rotateLeft(d, arr))