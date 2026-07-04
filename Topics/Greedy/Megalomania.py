# atcoder.jp/contests/abc131/tasks/abc131_d

n = int(input())
jobs = []

for _ in range(n):
    time, deadline = map(int, input().split())
    jobs.append((time, deadline))
jobs.sort(key=lambda x: x[1])

total_time = 0
for time, deadline in jobs:
    if deadline >= time + total_time:
        total_time += time
    else:
        print("No")
        exit()
        
print("Yes")