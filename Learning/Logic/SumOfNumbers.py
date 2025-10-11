def sum_of_numbers(n):
    total_sum = 0
    for i in range(1, n+1):
        total_sum += i
    return total_sum

def sum_of_numbers2(n):
    return int((1 + n) * n / 2)

def sum_of_numbers3(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_numbers3(n-1)

print(sum_of_numbers(5))
print(sum_of_numbers2(5))
print(sum_of_numbers3(5))