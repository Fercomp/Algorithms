def string_join(s, c):
    result_string = []
    for world in s:
        for w in world:
            result_string.append(w)
        if world != s[-1]:
            for char in c:
                result_string.append(char)
    return "".join(result_string)

print(string_join(["abra", "ca", "dabra"], "-")) # abra-ca-dabra