n = int(input())
if n == 0:
    print(1)
else:
    dic = {0: 6, 1: 8, 2: 4, 3: 2}
    l = n % 4
    print(dic[l])