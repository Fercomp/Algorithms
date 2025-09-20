t = int(input())
for i in range(1, t+1):
    n = int(input())
    nums = list(map(int, input().split()))
    
    mile = 0
    juice = 0
    for j in nums:
        mile += j // 30 + 1
        juice += j // 60 + 1
    
    mile *= 10
    juice *= 15
    if mile < juice:
        print(f"Case {i}: Mile {mile}")
    elif mile > juice:
        print(f"Case {i}: Juice {juice}")
    else:
        print(f"Case {i}: Mile Juice {mile}")