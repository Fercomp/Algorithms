candidates = [2, 3, 6, 7]
target = 7

# def combination_sum(l, target, current_sum, current_r, r):
#     if current_sum > target:
#         return
    
#     if current_sum == target:
#         print(current_r)
#         return
    
#     for n in l:
#         current_r.append(n)
#         combination_sum(l, target, current_sum + n, current_r, r)
#         current_r.pop()

def combination_sum(l, n, i, target, r):
    if i == n:
        if target == 0:
            print(r)
        return
    
    if target == 0:
        print(r)
        return
    
    if target < 0:
        return
    
    r.append(l[i])
    combination_sum(l, n, i, target - l[i], r)
    r.pop()
    combination_sum(l, n, i + 1, target, r)

combination_sum(candidates, len(candidates), 0, target, [])