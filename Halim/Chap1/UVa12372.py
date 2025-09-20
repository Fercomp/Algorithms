t = int(input())
for i in range(1, t+1):
    a, b, c = map(int, input().split())

    if a > 20 or b > 20 or c > 20:
        print(f"Case {i}: bad")
    else:
        print(f"Case {i}: good")