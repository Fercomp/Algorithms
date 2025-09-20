import math
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True

    if n % 2 == 0:
        return False
    
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    nums = [i for i in range(100)]

    result = []
    for num in nums:
        if is_prime(num):
            result.append(num)

    total = 1
    count = 0
    for num in result:
        total *= num
        if total > n:
            break
        count += 1
    print(count)