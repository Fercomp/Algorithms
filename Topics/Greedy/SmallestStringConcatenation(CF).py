# codeforces.com/problemset/problem/632/C

from functools import cmp_to_key
def compare(n1, n2):
    if n1 + n2 < n2 + n1:
        return -1
    else:
        return 1
    
s = []
n = int(input())
for i in range(n):
    s.append(input())
    
s = sorted(s, key=cmp_to_key(compare))
print("".join(s))