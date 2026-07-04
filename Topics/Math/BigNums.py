def is_a_greater_than_b(a, b):
    # Numbers are stored in reverse order: "1234" represents 4321
    # Step 1: Compare lengths (longer number is always greater)
    if len(a) > len(b):
        return True
    elif len(a) < len(b):
        return False
    
    # Step 2: Compare digit by digit from the most significant one (last index)
    # We go from the end to the beginning, because the last character
    # represents the highest place value.
    n = len(a) - 1
    while n >= 0:
        if a[n] > b[n]:   # a has a larger digit at this place → greater
            return True
        if a[n] < b[n]:   # b has a larger digit at this place → a is smaller
            return False
        n -= 1
    
    # Step 3: If all digits are equal, the numbers are equal → not greater
    return False

def sum_a_b(a, b):
    # Numbers are stored in reverse order: "1234" means 4321
    a_size = len(a)
    b_size = len(b)
    
    min_size = min(a_size, b_size)
    max_size = max(a_size, b_size)
    
    # Result can have at most max_size + 1 digits (in case of carry overflow)
    result = [0] * (max_size + 1)
    
    # Step 1: Add digits that exist in both numbers
    for i in range(min_size):
        digit_sum = int(a[i]) + int(b[i]) + result[i]
        result[i] = digit_sum % 10          # current digit
        result[i+1] = digit_sum // 10       # carry
    
    # Step 2: Process the remaining digits of the longer number
    j = min_size
    if a_size < b_size:
        while j < max_size:
            digit_sum = int(b[j]) + result[j]
            result[j] = digit_sum % 10
            result[j+1] = digit_sum // 10
            j += 1
    elif a_size > b_size:
        while j < max_size:
            digit_sum = int(a[j]) + result[j]
            result[j] = digit_sum % 10
            result[j+1] = digit_sum // 10
            j += 1
    
    # Step 3: Remove leading zeros (highest digits)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    
    # Step 4: Print result as string (still reversed)
    print("".join(str(d) for d in result))