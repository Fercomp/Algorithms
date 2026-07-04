def greatest_in_line(grid, line, n):
    max_sum = 0
    current_sum = 0
    
    for i in range(n):
        if grid[line][i] == 0:
            max_sum = max(max_sum, current_sum)
            current_sum = 0
        else:
            current_sum += 1
    
    max_sum = max(max_sum, current_sum)
    return max_sum

def greatest_in_row(grid, row, n):
    max_sum = 0
    current_sum = 0
    
    for i in range(n):
        if grid[i][row] == 0:
            max_sum = max(max_sum, current_sum)
            current_sum = 0
        else:
            current_sum += 1

    max_sum = max(max_sum, current_sum)
    return max_sum

def greatest_in_diag1(grid, i, j, n):
    max_sum = 0
    current_sum = 0
    
    while i < n and j < n:
        if grid[i][j] == 0:
            max_sum = max(max_sum, current_sum)
            current_sum = 0
        else:
            current_sum += 1
        
        i += 1
        j += 1

    max_sum = max(max_sum, current_sum)
    return max_sum

def greatest_in_diag2(grid, i, j, n):
    max_sum = 0
    current_sum = 0
    
    while i < n and j >= 0:
        if grid[i][j] == 0:
            max_sum = max(max_sum, current_sum)
            current_sum = 0
        else:
            current_sum += 1
        
        i += 1
        j -= 1
        
    max_sum = max(max_sum, current_sum)
    return max_sum

while True:
    n = int(input())
    if n == 0:
        break

    grid = []
    for _ in range(n):
        row = list(map(int, input()))
        grid.append(row)

    max_sequence = 0

    for line in range(n):
        sequence = greatest_in_line(grid, line, n)
        max_sequence = max(sequence, max_sequence)

    for row in range(n):
        sequence = greatest_in_row(grid, row, n)
        max_sequence = max(sequence, max_sequence)

    for col in range(n):
        sequence = greatest_in_diag1(grid, 0, col, n)
        max_sequence = max(sequence, max_sequence)

    for row in range(1, n):
        sequence = greatest_in_diag1(grid, row, 0, n)
        max_sequence = max(sequence, max_sequence)

    for col in range(n):
        sequence = greatest_in_diag2(grid, 0, col, n)
        max_sequence = max(sequence, max_sequence)

    for row in range(1, n):
        sequence = greatest_in_diag2(grid, row, n-1, n)
        max_sequence = max(sequence, max_sequence)

    print(max_sequence)