def equalPairs(grid):
    n = len(grid)
    cols_frequency = {}
    
    for i in range(n):
        col = []
        for j in range(n):
            col.append(str(grid[j][i]))
        col_id = "-".join(col)
        cols_frequency[col_id] = cols_frequency.get(col_id, 0) + 1
    
    row_frequency = {}
    for i in range(n):
        row = "-".join(list(map(str, grid[i])))
        row_frequency[row] = row_frequency.get(row, 0) + 1
    
    pairs = 0
    for key, value in cols_frequency.items():
        if key in row_frequency:
            pairs += value * row_frequency[key]
    
    return pairs

print(equalPairs([[11, 1], [1, 11]]))