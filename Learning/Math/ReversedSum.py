t = int(input())
for _ in range(t):
    a, b = input().split()
    n = len(a)
    m = len(b)
    biggest = max(n, m)
    result = [0] * (biggest + 1)
    if a == '0' and b == '0':
        print('0')
        continue

    for i in range(len(result) - 1):
        j = 0 if i > n-1 else int(a[i])
        k = 0 if i > m-1 else int(b[i])
        total = result[i] + j + k

        unity = total % 10
        decimal = total // 10
        result[i] = unity
        result[i + 1] += decimal
    
    last = len(result) - 1
    while last > 0 and result[last] == 0:
        last -= 1

    print("".join(map(str, result[:last+1])))