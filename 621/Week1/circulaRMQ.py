n = int(input())
nums = list(map(int, input().split()))
m = int(input())
for i in range(m):
    command = list(map(int, input().split()))
    if len(command) == 2:
        l,r = command[0], command[1]
        if l < r:
            print(min(nums[l: r+1]))
        else:
            mina = min(nums[l:])
            minb = min(nums[:r+1]) 
            print(min(mina, minb))
    else:
        l,r,c = command[0],command[1],command[2]
        if command[0] <= command[1]:
           nums[l:r+1] = [x + c for x in nums[l:r+1]]
        else:
            nums[l:] = [x + c for x in nums[l:]]
            nums[:r+1] = [x + c for x in nums[:r+1]]

