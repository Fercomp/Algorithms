def is_lower(c):
    return ord("a") <= ord(c) <= ord("z")

def is_uper(c):
    return ord("A") <= ord(c) <= ord("Z")

def is_num(c):
    return ord("0") <= ord(c) <= ord("9")

def is_alpha_numeric(c):
    return is_lower(c) or is_uper(c) or is_num(c)

def to_upper(c):
    if is_uper(c):
        return c
    alpha_index = ord(c) - ord('a')
    upper_code = ord("A") + alpha_index
    return chr(upper_code)