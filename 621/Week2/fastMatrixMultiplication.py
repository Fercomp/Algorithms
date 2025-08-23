# Naive exponential T(k) = T(k-1) + c = O(n)
def naive_exponential(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    
    return n * naive_exponential(n, k-1)

# Divide and conquer approach T(n) = T(n/2) + T(n/2) = O(log(n))
def divide_and_conquer(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    if k % 2 == 0:
        a = divide_and_conquer(n, k / 2)
        return a * a
    else:
        a = divide_and_conquer(n, (k-1) / 2)
        return n * a * a

# Basicaly a manual multiplication of 3x3 Matrix
def multAxB(A, B):
    result = [[0,0],[0,0]]
    result[0][0] = A[0][0]*B[0][0] + A[0][1]*B[1][0]
    result[0][1] = A[0][0]*B[0][1] + A[0][1]*B[1][1]
    result[1][0] = A[1][0]*B[0][0] + A[1][1]*B[1][0]
    result[1][1] = A[1][0]*B[0][1] + A[1][1]*B[1][1]
    return result

def power(k, M):
    result = [[1,0],[0,1]]
    while k:
        if k % 2 == 1:
            result = multAxB(result, M)
        M = multAxB(M, M)
        k >>= 1
    return result
  
def fib(n):
    if n == 0 or n == 1:
        return 1
    M = [[1, 1], [1, 0]]
    F = [[1, 0], [0, 0]]
    res = power(n - 1, M)
    multAxB(res, F)

    return res[0][0] % 1000000009

print(fib(7))