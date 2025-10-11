import math

# To determine if a number is prime we need to test if it can 
# be divided by any number lower than n
# T(n) = O(n)
def isPrime(n):
    # 0 and 1 are not primes; 2 is the only even prime
    if n < 2:
        return False
    if n == 2:
        return True
    # Test from 3 up to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Notice that if we have a number n, the highest divisor it can have 
# (other than itself) is sqrt(n).
# So we only need to test divisors up to sqrt(n).
def isPrime2(n):
    if n < 2:
        return False
    if n == 2:
        return True
    
    limit = int(math.sqrt(n)) + 1
    for i in range(2, limit):
        if n % i == 0:
            return False
    return True

# Optimization: we can skip even numbers, 
# since every even number greater than 2 is not prime.
def isPrime3(n):
    if n < 2:
        return False
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    limit = int(math.sqrt(n)) + 1
    # Skip even numbers by using step = 2
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True