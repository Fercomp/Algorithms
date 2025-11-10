# The famous split funtion can be implemented as following

def split(s, c):
    result_strings = []
    current_string = []
    arr_s = list(s)
    arr_s.append(" ")
    for i in arr_s:
        if i == c:
            splited_string = "".join(current_string)
            result_strings.append(splited_string)
            current_string = []
        else:
            current_string.append(i)
    return result_strings

print(split("maconha jiromba hula", " "))