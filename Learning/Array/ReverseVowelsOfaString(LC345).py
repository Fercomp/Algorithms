# leetcode.com/problems/reverse-vowels-of-a-string

def reverseVowels(s):
    vowels = set(["a", "e", "i", "o", "u"])
    left, right = 0, len(s) - 1
    s = list(s)
    while left <= right:
        if s[left].lower() not in vowels:
            left += 1
        elif s[right].lower() not in vowels:
            right -= 1
        else:
            s[right], s[left] = s[left], s[right]
            left += 1
            right -= 1

    return "".join(s)