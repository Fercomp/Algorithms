def isPalindrome(a, l, r):
    if l >= r:
        return True
    
    if a[l] != a[r]:
        return False

    return isPalindrome(a, l+1, r-1)

s = "acdfdca"
print(isPalindrome(s, 0, len(s) -1))