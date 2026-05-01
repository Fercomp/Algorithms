words = ["abc", "fg", "hij", "klm", "nop", "qrs", "vwx"]

def alphabeticalSum(word):
    total_sum = 0
    for w in word:
        total_sum += ord('a') - ord(w) + 1
    return total_sum

def find_product(word, target):
    sum_to_word = {}
    for word in words:
        sum_to_word[alphabeticalSum(word)] = word

    l, r = 0, len(words)-1
    while l <= r:
        new_target = target / (sum_to_word[word[l]] * sum_to_word[word[r]])
        if new_target < 1:
            continue
        
        if new_target in sum_to_word:
            return [words[l], words[r], words[new_target]]
        
        
            