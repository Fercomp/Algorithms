# https://vjudge.net/problem/UVA-665

t = int(input())
for _ in range(t):
    _ = input()
    n, k = map(int, input().split())
    arr = [False] * n
    for _ in range(k):
        l = list(map(int, input().split()))
        o = input()
        i = l[0]
        if o == "=":
            for j in range(1, len(l)):
                arr[l[j]-1] = True
        else:
            u = set(l[1:])
            for i in range(1, n+1):
                if i not in u:
                    arr[i-1] = True      
    
    count = 0
    index = 0
    for i in range(n):
        if arr[i] == False:
            index = n
            count += 1
    if count == 1:
        print(index+1)
    else:
        print("0")
    print()