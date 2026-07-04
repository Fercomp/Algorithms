while True:
    try:
        count = 0
        curr = input()
        while curr != str(0):
            m = "".join(sorted(curr))
            curr = str(abs(int(curr) - int(m)))
            count += 1
        print(count)
        
    except EOFError:
        break