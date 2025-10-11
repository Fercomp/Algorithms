# Using While
# print("", end=) end is "\n" by default, so i change to ""
def print_alternate(numbers):
    index = 0
    while index < len(numbers):
        print(numbers[index], end="")
        index += 2
    print()

# Using For
# Range (start, end, step)
def print_alternate2(numbers):
    for i in range(0, len(numbers), 2):
        print(numbers[i], end="")
    print()

# Recursive approach
def print_alternate3(numbers, index=0):
    if index >= len(numbers):
        print()
        return
    else:
        print(numbers[index], end="")
        return print_alternate3(numbers, index + 2)

# Test
print_alternate([1,2,3,4,5,6,7])
print_alternate([1,2,3,4,5,6])
print_alternate2([2,9,5,6,7,8])
print_alternate2([2,9,5,6,7,8, 10])
print_alternate3([1,2,3,4])
print_alternate3([1,2,3])