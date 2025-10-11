# To understand the algorithm, let's start with some properties:
# Let d be a common divisor of a and b. Then a = k1 * d and b = k2 * d for some integers k1 and k2.
# Subtracting the numbers: a - b = d * (k1 - k2). 
# Therefore, if d divides both a and b, it also divides (a - b).
# The reverse is also true: if d divides (a - b) and b, then it divides a.
# This gives the recursive relation: gcd(a, b) = gcd(a - b, b).
#
# slow_gcd uses repeated subtraction (inefficient for large numbers)
def slow_gcd(a, b):
    if b == 0:
        return a
    return slow_gcd(b, a - b)


# fast_gcd uses modulo operation (efficient version of Euclidean Algorithm)
def fast_gcd(a, b):
    if b == 0:
        return a
    return fast_gcd(b, a % b)