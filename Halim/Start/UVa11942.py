n = int(input())
print("Lumberjacks:")
for _ in range(n):
    l = list(map(int, input().split()))
    a = l[0] < l[1]
    
    b = True
    for i in range(1, 9):
        if a != (l[i] < l[i+1]):
            print("Unordered")
            b = False
            break
    if b:
        print("Ordered")