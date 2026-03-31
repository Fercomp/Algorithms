from itertools import permutations

def solve(nums):
    for p in permutations(nums):
        a,b,c,d,e = p        
        for o1 in range(3):
            r1 = a+b if o1==0 else a-b if o1==1 else a*b
            for o2 in range(3):
                r2 = r1+c if o2==0 else r1-c if o2==1 else r1*c
                for o3 in range(3):
                    r3 = r2+d if o3==0 else r2-d if o3==1 else r2*d
                    for o4 in range(3):
                        r4 = r3+e if o4==0 else r3-e if o4==1 else r3*e
                        if r4 == 23:
                            return "Possible"
    return "Impossible"


while True:
    nums = list(map(int, input().split()))
    if nums == [0,0,0,0,0]:
        break
    print(solve(nums))