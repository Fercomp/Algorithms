def buildArray(target, n):
    result = []
    t_idx = 0

    for i in range(1, n+1):
        if t_idx > len(target) -1:
            break
    
        if i == target[t_idx]:
            result.append("Push")
            t_idx += 1

        else:
            result.append("Push")
            result.append("Pop")

    return result

print(buildArray([1, 3], 3))