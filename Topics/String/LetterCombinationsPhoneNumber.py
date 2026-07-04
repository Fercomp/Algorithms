def get_char(i, offset):
    a = ord('a')
    return chr(a + 3 * (i-1) + offset)

def letterCombinations(digits, i, result, global_result):
    if i == len(digits):
        global_result.append("".join(result))
        return

    for j in range(3):
        d = get_char(int(digits[i]), j)
        result.append(d)
        letterCombinations(digits, i+1, result, global_result)
        result.pop()
    
digits = "23"
global_result = []
letterCombinations(digits, 0, [], global_result)
print(global_result)
