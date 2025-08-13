'''
Mike has a string s consisting of only lowercase English letters.
He wants to change exactly one character from the string so that the resulting one is a palindrome.
A palindrome is a string that reads the same backward as forward, for example strings
"z", "aaa", "aba", "abccba" are palindromes, but strings "codeforces", "reality", "ab" are not.

Input
The first and single line contains string s (1 ≤ |s| ≤ 15).

Output
Print "YES" (without quotes) if Mike can change exactly one character so that the resulting string
is palindrome or "NO" (without quotes) otherwise.
'''

def mike_string():
    mike_string = list(input())
    i,j = 0, len(mike_string) - 1
    count = 0
    while i < j:
        if mike_string[i] != mike_string[j]:
            count += 1
        i += 1
        j -= 1

    if count == 1:
        print("YES")
    elif count == 0 and len(mike_string) % 2 == 1:
        print("YES")
    else:
        print("NO")

mike_string()