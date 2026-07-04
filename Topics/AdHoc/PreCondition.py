s = input()
t = input()

def check(s, t):
    for i in range(1, len(s)):
        if s[i].isupper() and s[i-1] not in t:
            return False
    return True

if check(s, t):
    print("Yes")
else:
    print("No")