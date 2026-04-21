l = [1, [1, 2, 3], [[4]], 9]

def nested_array_sum(l):
    if isinstance(l, int):
        return l
    
    count = 0
    for i in range(len(l)):
        count += nested_array_sum(l[i])
    return count

print(nested_array_sum(l))