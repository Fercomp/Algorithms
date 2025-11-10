# The famous .join() function in python can be done in the following manner

def join(s, c):
    result_string = []
    for world in s:
        for w in world:
            result_string.append(w)
        if world != s[-1]:
            for char in c:
                result_string.append(char)
    return "".join(result_string)

print(join(["aba", "ca", "dabra"], "-"))