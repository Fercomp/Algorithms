words = ["abc", "fg", "hij", "klm", "nop", "qrs", "vwx"]

def alphabeticalSum(word):
    return sum(ord(c) - ord('a') + 1 for c in word)

def find_product(words, target):
    word_to_sum = {word: alphabeticalSum(word) for word in words}
    sums = set(word_to_sum.values())

    for word1 in words:
        sum1 = word_to_sum[word1]

        if target % sum1 != 0:
            continue

        target2 = target // sum1

        for word2 in words:
            sum2 = word_to_sum[word2]

            if target2 % sum2 != 0:
                continue

            target3 = target2 // sum2

            if target3 in sums:
                return True

    return False