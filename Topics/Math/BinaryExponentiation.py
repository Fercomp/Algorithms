# T(n) = T(n - 1) + c, O(n)
def naiveExponentiation(n, k):
    if k == 0:
        return 0
    if k == 1:
        return n
    return n * naiveExponentiation(n, k - 1)

# T(n) = T(n/2) + c, O(log(n))
def binaryExponentiation(n, k):
    if k == 0:
        return 1
    if k == 1:
        return n
    
    if k % 2:
        aux = binaryExponentiation(n, (k-1)/2)
        return n * aux * aux
    else:
        aux = binaryExponentiation(n, k/2)
        return aux * aux

# Iterative without recursion overhead
def binaryExponentiation2(n, k):
    result = 1
    while k > 0:
        if k % 2:
            result *= n
        n = n * n
        k >>= 1
    return result

# Applications
# Effective computation of large exponents modulo a number
# relation (a⋅b mod m) = ((a mod m)⋅(b mod m)) mod m can be proven so 
def moduloExponentiation(n, k, m):
    result = 1
    while k > 0:
        if k % 2:
            result *= n % m
        n = (n * n) % m
        k >>= 1
    return result
        
print(binaryExponentiation2(3, 3))
print(naiveExponentiation(3, 5))
print(binaryExponentiation(3, 5))
    