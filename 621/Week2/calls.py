def multAxB(A, B, mod):
    result = [[0, 0], [0, 0]]
    result[0][0] = (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod
    result[0][1] = (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod
    result[1][0] = (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod
    result[1][1] = (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod
    return result

def power(k, M, mod):
    result = [[1, 0], [0, 1]]
    while k:
        if k % 2 == 1:
            result = multAxB(result, M, mod)
        M = multAxB(M, M, mod)
        k //= 2
    return result

def fib(n, mod):
    if n == 0 or n == 1:
        return 1 % mod
    M = [[1, 1], [1, 0]]
    res = power(n - 1, M, mod)
    return res[0][0] % mod

t = 1
while True:
    n, b = map(int, input().split())
    if n == 0 and b == 0:
        break

    f = fib(n + 1, b)
    calls = (2 * f - 1) % b

    print(f"Case {t}: {n} {b} {calls}")
    t += 1