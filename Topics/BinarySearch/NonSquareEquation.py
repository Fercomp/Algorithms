def sum_of_digits(n):
    s = 0
    while n > 0:
        n, r = divmod(n, 10)
        s += r
    return s

n = int(input())
