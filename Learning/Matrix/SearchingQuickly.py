words_to_ignore = set()
while True:
    w = str(input())
    if w == "::":
        break
    words_to_ignore.add(w)

KWIC = []
while True:
    try:
        line = input().split()
    except EOFError:
        break
    
    for index, element in enumerate(line):
        if element.lower() not in words_to_ignore:
            KWIC.append((element.lower(), index, line))
    
order = sorted(KWIC, key= lambda x: x[0])
for element, index, line in order:
    line = list(map(str.lower, line))
    line[index] = element.upper()
    print(" ".join(line))