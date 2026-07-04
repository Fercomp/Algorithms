first = input().strip()
second = input().strip()

def get_frequency(string):
    result = [0] * 26
    stars = 0
    
    for ch in string:
        if ch == "*":
            stars += 1
        else:
            result[ord(ch) - ord('a')] += 1
            
    return result, stars

f_first, _ = get_frequency(first)
f_second, stars = get_frequency(second)

missing = 0

for i in range(26):
    if f_first[i] > f_second[i]:
        missing += f_first[i] - f_second[i]

if missing <= stars:
    print("A")
else:
    print("N")