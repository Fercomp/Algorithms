def sum_d(n):
    if n < 10:
        return n
    return n % 10 + sum_d(n // 10)

while True:
    n = int(input())  
    if n == 0:
        break
    while n >= 10:
        n = sum_d(n)
    print(n)