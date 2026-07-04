def gcdOfStrings(self, str1: str, str2: str) -> str:
    if len(str1) < len(str2):
        smaller_string = str1
    else:
        smaller_string = str2

    for i in range(len(smaller_string), 0, -1):
        gcd = smaller_string[:i]
        
        n_str1, n_str2, n_gcd = len(str1), len(str2), len(gcd)
        if n_str1 % n_gcd == 0 and n_str2 % n_gcd == 0:

            q_str1, q_str2 = n_str1 // n_gcd, n_str2 // n_gcd
            if gcd * q_str1 == str1 and gcd * q_str2 == str2:
                return gcd

    return ""