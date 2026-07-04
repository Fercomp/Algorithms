# Time: O(n)
# Space: O(1)
def maxVowels(s, k):
    vowels = "aeiou"
    max_vowels_count = 0

    for i in range(k):
        if s[i] in vowels:
            max_vowels_count += 1
    curr_vowels_count = max_vowels_count

    for i in range(1, len(s) -k + 1):
        if s[i-1] in vowels:
            curr_vowels_count -= 1
        if s[i + k -1] in vowels:
            curr_vowels_count += 1
        max_vowels_count = max(max_vowels_count, curr_vowels_count)

    return max_vowels_count