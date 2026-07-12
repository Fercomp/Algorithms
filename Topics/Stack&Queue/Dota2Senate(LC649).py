from collections import deque

def predictPartyVictory(senate):
    r, d = deque(), deque()
    for i in range(len(senate)):
        if senate[i] == "R":
            r.append(i)
        else:
            d.append(i)

    r_count, d_count = len(r), len(d)
    
    for i in range(len(senate)):
        if not r or not d:
            break

        if senate[i] == "R" and r[0] == i:
            d_count -= 1
            r.popleft()
            d.popleft()

        elif senate[i] == "D" and d[0] == i:
            r_count -= 1
            r.popleft()
            d.popleft()
        

    return "Radiant" if r_count > d_count else "Dire"

predictPartyVictory("DDRRR")