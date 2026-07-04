n, c = map(int, input().split())
times = list(map(int, input().split()))

cashiers = [0] * n
result = []

def set_cashier(cashiers, time):
    index = cashiers.index(0)
    cashiers[index] = time
    return index

for time in times:
    if 0 in cashiers:
        index = set_cashier(cashiers, time)
        
    else:
        min_time = min(cashiers)
        for j in range(n):
            cashiers[j] -= min_time
        index = set_cashier(cashiers, time)
        
    result.append(str(index + 1))
    
print(" ".join(result))