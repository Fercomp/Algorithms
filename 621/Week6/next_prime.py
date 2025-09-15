import math
def is_prime(n):
    if n <= 2:
        return True
    if n % 2 == 0:
        return False
    l = int(math.sqrt(n)) + 1
    for i in range(3, l, 2):
        if n % i == 0:
            return False
    return True

n = int(input())
while True:
    if is_prime(n):
        print(n)
        break
    n+=1