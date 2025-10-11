def closest_and_divisible(n, m):
    # First we need to get the integer division of n by m, because this gives 
    # how many m fit in a n

    i = n // m

    # Then we multiply by m again to know closest multiple of m to n
    # this will always be lower than n
    l = i * m

    # l is the lower closes, now we need the upper closest 
    u = (i + 1) * m

    # Finaly we check who is closes the upper bound or the lower bound
    if abs(i - l) > abs(i - u):
        return u
    else:
        return l

print(closest_and_divisible(-15, 4))
print(closest_and_divisible(17, 3))