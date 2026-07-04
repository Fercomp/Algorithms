M = [
    [5, 5, 11],
    [1, 4, 7],
    [9, 2, 1],
    ]

def is_valid(n, m, i, j):
    return 0 <= i < n and 0 <= j < m

def subGridMax(M):
    n = len(M)
    m = len(M[0])
    result = [[0] * m for _ in range(n)]
    directions = [[0, 1], [1, 0], [1, 1]]
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            max_val = M[i][j]
            for dx, dy in directions:
                y = i + dy
                x = j + dx
                if is_valid(n, m, y, x):
                    # Very important, i need to look at the already
                    # computed solutions in result, not in M that holds
                    # the original values
                    max_val = max(max_val, result[y][x])
            result[i][j] = max_val
    return result

print(subGridMax(M))