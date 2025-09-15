n = int(input())
l = list(map(int, input().split()))

dic = {}   # Stores frequencies of values (i + A[i]) seen so far
soma = 0   # Total number of valid pairs

for x in range(len(l)):
    # j is the "right side" of the condition: j - A[j]
    j = (x + 1) - l[x]

    # If this j matches any (i + A[i]) seen before, each occurrence
    # corresponds to a valid pair (i, j).
    soma += dic.get(j, 0)

    # Now compute the "left side" for this index to be used in the future:
    # i = index + 1, so we store i + A[i].
    i = (x + 1) + l[x]
    dic[i] = dic.get(i, 0) + 1

print(soma)