# Crivo de erastotenes é uma maneira de gerar todos os primos de 1 até n eficientemente
n = 100
nums = [i for i in range(n+1)]

import math
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True

result = []
for num in nums:
    if is_prime(num):
        result.append(num)
        for l in range(2 * num, n+1, num):
            nums[l] = 0

count = 1
for i in range(len(result) - 1):
    count *= result[i]
    if count * result[i + 1] > n:
        print(i)
        break

print(result)