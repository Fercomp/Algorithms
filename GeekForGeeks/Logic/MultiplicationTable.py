# Iterative approach
def multiplication_table(n):
    print("-=" * 10)
    for i in range(1, 11):
        # String interpolation
        print(f'{i} x {n} = {i * n}')

# Recursive approach
def multiplication_table2(n, i=1):
    if i > 10:
        return
    print(f'{i} x {n} = {i * n}')
    return multiplication_table2(n, i+1)



multiplication_table(1)
multiplication_table(2)
multiplication_table(10)
multiplication_table2(12)
multiplication_table2(1)