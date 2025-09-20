def is_one(a):
    count = 0
    if a[0] != "o":
        count += 1
    if a[1] != "n":
        count += 1
    if a[2] != "e":
        count += 1
    
    if count == 1 or count == 0:
        return True
    else:
        return False


n = int(input())
for _ in range(n):
    num = str(input())
    if len(num) == 5:
        print(3)
    else:
        if is_one(num):
            print(1)
        else:
            print(2)