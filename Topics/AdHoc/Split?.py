pins = list(map(int, list(input())))
columns = [[7], [4], [8, 2], [5, 1], [9, 3], [6], [10]]
is_split = False

if pins[0] == 1:
    print("No")
    exit()

for i in range(1, len(columns) - 1):
    all_down = True
    for j in columns[i]:
        if pins[j - 1] == 1:
            all_down = False
            break
        
    if not all_down:
        continue
    
    left_standing = False
    for k in range(0, i):
        for cell in columns[k]:
            if pins[cell - 1] == 1:
                left_standing = True
                break
                
    right_standing = False
    for k in range(i + 1, len(columns)):
        for cell in columns[k]:
            if pins[cell - 1] == 1:
                right_standing = True
                break
    
    if left_standing and right_standing:
        is_split = True
        break
        
if is_split:            
    print("Yes")
else:
    print("No")