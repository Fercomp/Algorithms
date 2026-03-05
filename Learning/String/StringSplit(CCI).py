def string_split(s, c):
    result_strings = []
    current_string = []
    arr_s = list(s)
    # This is just for when s ends then i will run line 10
    # one more time, to add the last current_string to result
    arr_s.append(c)
    
    for i in arr_s:
        if i == c:
            splited_string = "".join(current_string)
            if splited_string:
                result_strings.append(splited_string)
            current_string = []
            
        else:
            current_string.append(i)

    return result_strings

print(string_split("aaa a    aa", " "))           # ['aaa', 'a', 'aa']