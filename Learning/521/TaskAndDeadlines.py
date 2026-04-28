n = int(input())

l = []
for i in range(n):
    d, f = map(int, input().split())
    l.append((d, f))

l = sorted(l, key=lambda x: x[0])
current_time = 0
reward = 0
for i in l:
    current_time += i[0]
    reward += i[1] - current_time

print(reward)