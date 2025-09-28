while True:
    h, u, d, f = map(int, input().split())
    if h == 0:
        break

    distance = 0
    is_day = True
    count = 0
    while distance <= h and distance >= 0:
        if is_day:
            fatigue = (f / 100 * count * u)
            count += 1
            if u - fatigue > 0:
                distance += u - fatigue
        else:
            distance -= d
        is_day = not is_day
    
    if distance > 0:
        print(f"success on day {count}")
    else:
        print(f"failed on day {count}")
