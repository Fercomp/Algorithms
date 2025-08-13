n, k = map(int, input().split())
nums = list(map(int, input().split()))

dic = dict()
c1 = 0
for i in range(k):
    if nums[i] in dic:
        c1 += 1
        dic[nums[i]] += 1
    else:
        dic[nums[i]] = 1
n1 = k - c1
r = [str(n1)]
n2 = 0
c2 = c1
for i in range(k, n):
    dic[nums[i - k]] -= 1
    if dic[nums[i - k]] == 1:
        c2 -= 1
    

    if nums[i] in dic:
        dic[nums[i]] += 1
        c2 += 1
    else:
        dic[nums[i]] = 1
    n2 = k - c2
    r.append(str(n2))

print(" ".join(r))