s = list(input())
stack = [-1]
d = {}
for i in range(len(s)):
    if s[i] == "(":
        stack.append(i)
    else:
        stack.pop()
        if not stack:
            stack.append(i)
        else:
            lenght = i - stack[-1]
            d[lenght] = d.get(lenght, 0) + 1

if not d:
    print("0 1")
else:
    m = max(d.keys())
    print(f"{m} {d[m]}")