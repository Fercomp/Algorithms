d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12,
    "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22,"w": 23,
    "x": 24, "y": 25, "z": 26}

def get_sum(num):
    if num < 10:
        return num
    return num % 10 + get_sum(num // 10)

def get_ratio(name):
    total = 0
    for n in name:
        total += d.get(n, 0)
    return total

while True:
    try:
        name_a = str(input()).lower()
        name_b = str(input()).lower()
    except EOFError:
        break
    
    sum_a = get_ratio(name_a)
    sum_b = get_ratio(name_b)

    while sum_a >= 10:
        sum_a = get_sum(sum_a)
    
    while sum_b >= 10:
        sum_b = get_sum(sum_b)

    ratio = min(sum_a, sum_b) / max(sum_a, sum_b)

    print(f"{ratio * 100 :.2f} %")