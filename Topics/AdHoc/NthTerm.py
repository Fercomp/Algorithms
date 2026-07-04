def nth_term1(a1, a2, n):
    last = a1
    r = a2 - a1
    for i in range(n-1):
        last += r
    return last

def nth_term2(a1, a2, n):
    r = a2 - a1
    # We use (n - 1), because we need how many r have between
    # the first and the last number this is n-1
    return a1 + r * (n-1)

print(nth_term1(2,3,4))
print(nth_term2(2,3,4))