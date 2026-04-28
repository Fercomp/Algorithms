inp = input()
d = {}
stack = []
last_invalid = -1

for idx in range(len(inp)):
    j = i[idx]

    if j == "(":
        stack.append(idx)
    else:
        if not stack:
            last_invalid = idx
        else:
            stack.pop()
            if not stack:
                length = idx - last_invalid
            else:
                length = idx - stack[-1]

            d[length] = d.get(length, 0) + 1

if not d:
    print("0 1")
else:
    m = max(d.keys())
    print(m, d[m])