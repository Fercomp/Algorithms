t = int(input())
for i in range(1, t+1):
    n = int(input())
    nums = list(map(int, input().split()))
    if n == 1:
        print(f"Case {i}: 0 0")
        continue
    
    h = 0
    l = 0
    for j in range(n-1):
        if nums[j] > nums[j+1]:
            l += 1
        elif nums[j] < nums[j+1]:
            h += 1
    print(f"Case {i}: {h} {l}")