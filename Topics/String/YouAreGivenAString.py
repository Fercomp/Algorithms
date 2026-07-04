s = input()
grater_string = 0

n = len(s)
for t in range(n-1, 0, -1):
    older = set()
    for i in range(0, n-t+1):
        sub =  s[i:i+t]
        if sub in older:
            grater_string = t
            break
        
        older.add(sub)
        
    if grater_string > 0:
        break

print(grater_string)