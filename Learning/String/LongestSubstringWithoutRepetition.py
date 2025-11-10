def lengthOfLongestSubstring(self, s: str) -> int:
    left = 0
    right = 0
    current_letters = dict()
    longest_sub = 0
    while right < len(s):
        current_letter = s[right]
        if current_letter not in current_letters:
            current_letters[current_letter] = right
        else:
            n = current_letters[current_letter] + 1
            for i in range(left, n):
                del current_letters[s[i]]
            left = n
            current_letters[current_letter] = right
        
        longest_sub = max(longest_sub, right - left + 1)
        right += 1
        
    return longest_sub