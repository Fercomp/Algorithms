def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)
        
while True:
    n = int(input())
    if n == 0:
        break
    while n > 10:
        n = sum_digits(n)
    print(n)