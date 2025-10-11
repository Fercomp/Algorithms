# Iterative approach
def linear_search(numbers, x):
    for i in range(0, len(numbers)):
        if numbers[i] == x:
            return i
    return -1

# Recursive approach
def linear_search2(numbers, x, index=0):
    if index == len(numbers):
        return -1
    
    if numbers[index] == x:
        return index
    else:
        return  linear_search2(numbers, x, index+1)
    
# Test
print(linear_search([1,2,3,4,56,7], 56))
print(linear_search([4,8,2,1,9,99], 3))
print(linear_search([], 8))
print(linear_search([1,2,3,4,5,6], 6))
print(linear_search2([2,4,5,6,9],7))
print(linear_search2([], 8))