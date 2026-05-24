# www.luogu.com.cn/problem/P2240

n, t = map(int, input().split())

piles_ratios = []
for _ in range(n):
    m, v = map(int, input().split())
    ratio = v / m
    piles_ratios.append((ratio, m))

piles_ratios.sort(reverse=True)
total = 0
for pile in piles_ratios:
    if t == 0:
        break
    m = min(pile[1], t)
    total += m * pile[0]
    t -= m

print(f"{total:.2f}")