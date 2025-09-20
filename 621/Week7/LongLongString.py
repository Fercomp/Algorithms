l = str(input())
n = int(input())

count = 1
nums = "123456789"
d = {}
for c in l:
    if c in nums:
        count = count * c + 1
        
    else c not in d:
        d[c] = count
        count += 1

print(r[n-1])