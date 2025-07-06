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

# Test
print_alternate([1,2,3,4,5,6,7])
print_alternate([1,2,3,4,5,6])
print_alternate2([2,9,5,6,7,8])
print_alternate2([2,9,5,6,7,8, 10])