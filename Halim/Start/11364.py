t = int(input())
for i in range(t):
    n = int(input())
    stores = sorted(list(map(int, input().split())))
    print(2 * (stores[-1] - stores[0]))