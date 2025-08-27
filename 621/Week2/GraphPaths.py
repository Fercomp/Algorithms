MOD = 10**9 + 7

def mult(A, B, n):
    # Create matriz with zeros without repeting references
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # For cell [i][j] do the dot product of i row and j column
            for k in range(n):
                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD
    return result

def identity(n):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        result[i][i] = 1
    return result

def matrix_power(M, k, n):
    # Create the identity that corespont to Mˆ0
    I = identity(n)
    # We repet the process always dividing k by 2
    while k > 0:
        # If is odd we update the identity
        if k & 1:
            I = mult(I, M, n)
        # If is even we just update M
        M = mult(M, M, n)
        # >>= is just to shift left and assign to k again
        k >>= 1
    return I

def graphPaths():
    n, m, k = map(int, input().split())
    M = [[0 for _ in range(n)] for _ in range(n)]
    
    for _ in range(m):
        a, b = map(int, input().split())
        M[a-1][b-1] = (M[a-1][b-1] + 1) % MOD
    
    Mk = matrix_power(M, k, n)
    print(Mk[0][n-1] % MOD)

graphPaths()