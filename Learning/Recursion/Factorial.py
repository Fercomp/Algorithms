# Parameterized approach
def fac_p(n, acc = 1):
    if n == 0:
        print(acc)
        return 
    fac_p(n - 1, acc * n)

# Functional approach
def fac_f(n):
    if n < 1:
        return 1
    return n * fac_f(n-1)

fac_p(5)
print(fac_f(5))