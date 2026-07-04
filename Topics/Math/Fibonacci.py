def fibonnaci(n):
    if n <= 1:
        return n
    return fibonnaci(n - 1) + fibonnaci(n - 2)

def mulAxB(A, B):
    result = [[0,0],[0,0]]
    result[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    result[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1]
    result[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    result[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1]
    return result
    
def fibonnaciMatrix(k):
    k = k - 1
    I = [[1, 0], [0, 1]]
    M = [[1, 1], [1, 0]]
    while k > 0:
        if k % 2:
            I = mulAxB(I, M)
        M = mulAxB(M, M)
        k >>= 1
    return I[0][0]
     
print(fibonnaci(9))
print(fibonnaciMatrix(9))
print(fibonnaci(10))
print(fibonnaciMatrix(10))