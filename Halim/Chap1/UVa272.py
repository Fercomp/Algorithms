import sys

open_quote = True 

# Read the line of input indefinitely until finds the EOF or the CRL + C
for line in sys.stdin:
    result = []
    for ch in line:
        if ch == '"':
            if open_quote:
                result.append("``")
            else:
                result.append("''")
            open_quote = not open_quote
        else:
            result.append(ch)
    print("".join(result), end="")