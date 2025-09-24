s = 0
while True:
    s += 1
    n = int(input())
    if n == 0:
        break   

    isFirst = False
    nums = list(map(int, input().split()))
    m = int(sum(nums) / n)
    count = 0
    for i in nums:
        count += abs(i - m)

    print(f"Set #{s}")
    print(f"The minimum number of moves is {int(count / 2)}.")
    print()