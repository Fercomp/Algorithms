def identity_gen(n):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        result[i][i] = 1
    return result

def mulAxB(A, B, n):
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % (10**9+9)
    return C

def tribonnaciMatrix(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    n = n - 3
    F = [[1, 1, 1],
         [1, 0, 0],
         [0, 1, 0]]
    I = identity_gen(3)
    while n > 0:
        if n % 2:
            I = mulAxB(I, F, 3)
        F = mulAxB(F, F, 3)
        n >>= 1
    return (I[0][0]*2 + I[0][1]*1 + I[0][2]*0) % (10**9+9)

while True:
    n = int(input())
    if n == 0:
        break
    print(tribonnaciMatrix(n))