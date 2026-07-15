
def apply_in_array(arr, func):
    result = []
    for e in arr:
        result.append(func(e))
    return result

arr = [1, 2, 3, 4]
print(apply_in_array(arr, lambda x: x + 1))