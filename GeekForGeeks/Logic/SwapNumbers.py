# Naive aproach using third variable
def swap_numbers_1(a, b):
    print(f'a: {a}, b: {b}')
    temp = a 
    a = b
    b = temp
    print(f'a: {a}, b: {b}')

# Without using third variable
def swap_numbers_2(a, b):
    print(f'a: {a}, b: {b}')
    a = a + b
    b = a - b 
    a = a - b
    print(f'a: {a}, b: {b}')

# Using tuple unpacking
def swap_numbers_3(a, b):
    print(f'a: {a}, b: {b}')    
    a, b = a, b
    print(f'a: {a}, b: {b}')

# Using xor, if both are equal turns 0, 1 otherwise 
# y = a ^ b iguals bitwise operation 
# z = y ^ b becomes equal a again
# x = y ^ a becomes equal b again 
def swap_numbers_4(a, b):
    print(f'a: {a}, b: {b}')
    a = a ^ b
    b = a ^ b 
    a = a ^ b
    print(f'a: {a}, b: {b}')

swap_numbers_1(3,4)
swap_numbers_2(3,4)
swap_numbers_3(3,4)
swap_numbers_4(3,4)
