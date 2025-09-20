# def fac(n, stop):
#     if n <= 1:
#         return 1
#     if n == stop:
#         return 1
#     return ((n % 10)  * (fac(n-1, stop) % 10)) % 10

# a, b = map(int, input().split())
# if a == 0 or b == 0:
#     print(0)
# else:
#     print(fac(b, a))

a, b = map(int, input().split())
if (a == 0 or b == 0) or (a - b >= 5):
    print(0)
elif a == b:
    print(1)
else:
    c = 1
    for i in range(a+1, b+1):
        c =  (c * (i % 10)) % 10
    print(c)