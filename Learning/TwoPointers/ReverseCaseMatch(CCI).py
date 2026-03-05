s = "hDarRAdH"

def isUpper(c):
    return ord('A') <= ord(c) <= ord('Z')
    
def isLower(c):
    return ord('a') <= ord(c) <= ord('z')

def reverse_case_match(s):
    l = 0
    n = len(s)
    r = n -1
    while l < n and r > 0:
        if isUpper(s[l]):
            l += 1
        elif isLower(s[r]):
            r -= 1
        else:
            if s[l].upper() != s[r]:
                return False
            l += 1
            r -= 1
    return True

print(reverse_case_match(s))