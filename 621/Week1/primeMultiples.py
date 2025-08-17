
def prime_multiples1():
    n, k = map(int, input().split())
    primes = list(map(int, input().split()))
    data = set()

    for i in primes:
        count = i
        while count <= n:
            data.add(count)
            count += i
    print(len(data))

# This algorithm is O(n.k) the problem is that n is to large, we can't 
# iterate trought all the numbers 
# Exclusion inclusion principle

n, k = map(int, input().split())
primes = list(map(int, input().split()))

masks = []
for i in range(2 ** k):
    bitmask = format(i, f'0{k}b')
    masks.append(list(map(int, list(bitmask))))
    
total = 0
for mask in masks:
    if sum(mask) % 2 == 0:
        m = -1
    else:
        m = 1
        
    c = 1
    for j, bit in enumerate(mask):
        r = bit * primes[j]
        if r != 0:
            c *= r
        if c != 1:
            div = n // c
            total += m * div
print(total)

n, k = map(int, input().split())
primes = list(map(int, input().split()))

total = 0
for mask in range(1, 1 << k):  
    lcm = 1
    bits = 0
    for j in range(k):
        if mask & (1 << j):
            bits += 1
            lcm *= primes[j]
            if lcm > n:
                break
    else:
        if bits % 2:
            total += n // lcm
        else:
            total -= n // lcm

print(total)