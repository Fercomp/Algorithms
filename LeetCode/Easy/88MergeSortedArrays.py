
l1 = [1,2,6,9,10,0,0,0]
l2 = [3,5,11]

e = len(l1) - 1
k = len(l1) - len(l2) - 1
j = len(l2) - 1
while j >= 0:
    if l1[k] < l2[j]:
        l1[e] = l2[j]
        j -= 1
    else:
        l1[e] = l1[k]
        l1[k] = 0
        k-=1
    e-=1
print(l1)