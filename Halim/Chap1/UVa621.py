t = int(input())
for _ in range(t):
    a = str(input())
    if a == "1" or a == "4" or a == "78":
        print("+")
    elif a[-2:] == "35":
        print("-")
    elif a[0] == "9" and a[-1] == "4":
        print("*")
    elif a[0:3] == "190":
        print("?")