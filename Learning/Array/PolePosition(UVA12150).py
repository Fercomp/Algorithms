# https://vjudge.net/problem/UVA-12150

while True:
    n = int(input())
    if n == 0:
        break
    # Initialize all positions with a dummy value
    start_positions = [-1] * n
    impossible = False
    for i in range(n):
        c, p = map(int, input().split())
        if not impossible:
            # calculate start position of car
            start = i + p
            # edge case position out of bounds
            if start < 0 or start >= n:
                impossible = True
            # edge case colision of cars
            elif start_positions[start] != -1:
                impossible = True
            else:
                start_positions[start] = c
    if impossible:
        print(-1)
    else:
        print(" ".join(map(str, start_positions)))