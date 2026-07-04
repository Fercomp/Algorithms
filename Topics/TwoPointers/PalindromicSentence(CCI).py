# Time: O(n)
# Space: O(1)
def palindromic_sentence(sentence):
    l, r = 0, len(sentence) - 1
    while l <= r:
        if not sentence[l].isalpha():
            l += 1
        elif not sentence[r].isalpha():
            r -= 1
        else:
            if sentence[l].lower() != sentence[r].lower():
                return False
            else:
                l += 1
                r -= 1
    return True

print(palindromic_sentence('Bob wondered, "Now, bob?"'))