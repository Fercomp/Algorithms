i = 0
while True:
    count = 0
    n = int(input())
    if n == 0:
        break
    i+=1
    l = list(map(int, input().split()))
    for n in l:
        if n == 0:
            count -= 1
        else:
            count += 1

    print(f"Case {i}: {count}")