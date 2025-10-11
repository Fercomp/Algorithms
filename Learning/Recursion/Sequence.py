def all_sequences(l, i, n, r=""):
    if i == n:
        print(r)
        return

    r += l[i]
    all_sequences(l, i+1, n, r)
    r = r[:-1]
    all_sequences(l, i+1, n, r)

def all_combination_different_letters(l, i, n, r=""):
    if i == n:
        print(r)
        return
    
    for j in l:
        r += j
        all_combination_different_letters(l, i+1, n, r)
        r = r[:-1]
        all_combination_different_letters(l, i+1, n, r)

def all_combination_allow_equal_letters(l, i, n, r=""):
    if i == n:
        print(r)
        return
    
    for j in l:
        r += j
        all_combination_allow_equal_letters(l, i, n, r)
        
        all_combination_allow_equal_letters(l, i+1, n, r)


s = "abcde"
all_combination_allow_equal_letters(s, 0, len(s))