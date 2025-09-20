from collections import deque

dealer = deque()
non_dealer = deque()

l = []
is_d = False
while True:
    l = list(map(str, input().split()))
    if l[0] == "#":
        break
    for c in l:
        if is_d:
            dealer.append(c)
        else:
            non_dealer.append(c)
        is_d = not is_d

n = 1
is_face = False
q = deque()
for i in range(n):
    if is_d:
        c = dealer.pop_left()
    else:
        c = non_dealer.pop_left()
    q.append(c)
    n-=1

    if c[1] == "A":
        n = 4
    elif c[1] == "K":
        n = 3
    elif c[1] == "Q":
        n = 2
    elif c[1] == "J":
        n = 1
    if c[1] in "AKQJ":
        is_face = True
        is_d = not is_d
        continue

    if n == 0:
        is_d = not is_d
        if is_face:
            is_face = False
            if is_d:
                dealer = q + dealer
            if not is_d:
                non_dealer = q + non_dealer
        n += 1

print(f"{1 if is_d else 2} {len(dealer) if is_d else len(non_dealer)}")