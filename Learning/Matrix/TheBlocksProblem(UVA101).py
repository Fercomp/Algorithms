# https://vjudge.net/problem/UVA-101

def remove_stacked_blocks(a, i, blocks):
    # Always looking to the last bloks[-1]
    while blocks[i][-1] != a:
        aux = blocks[i].pop()
        blocks[aux].append(aux)

def get_stacked_blocks(a, i, blocks):
    result = []
    while blocks[i][-1] != a:
        aux = blocks[i].pop()
        result.append(aux)
    aux = blocks[i].pop()
    result.append(aux)
    return result

def add_pile(i, pile, blocks):
    while pile:
        aux = pile.pop()
        blocks[i].append(aux)    

def find_block(a, blocks):
    for i in range(len(blocks)):
        for j in range(len(blocks[i])):
            if blocks[i][j] == a:
                return (i, j)
    return None, None

def move_onto(a, ia, b, ib, blocks):
    remove_stacked_blocks(a, ia, blocks)
    remove_stacked_blocks(b, ib, blocks)
    aux = blocks[ia].pop()
    blocks[ib].append(aux)
    
def move_over(a, ia, ib, blocks):
    remove_stacked_blocks(a, ia, blocks)
    aux = blocks[ia].pop()
    blocks[ib].append(aux)

def pile_onto(a, ia, b, ib, blocks):
    pile = get_stacked_blocks(a, ia, blocks)
    remove_stacked_blocks(b, ib, blocks)
    add_pile(ib, pile, blocks)
    
def pile_over(a, ia, ib, blocks):
    pile = get_stacked_blocks(a, ia, blocks)
    add_pile(ib, pile, blocks)
    
def print_blocks(blocks):
    for i in range(len(blocks)):
        if len(blocks[i]) == 0:
            print(f"{i}:")
        else:
            line = " ".join(map(str, blocks[i]))
            print(f"{i}: {line}")

n = int(input())
# List are ok because during this i always pop from the right
# if i needed to pop from the beginning i would prefer deque
blocks = [[i] for i in range(n)]
while True:
    command = input().split()
    if len(command) == 1:
        break
    c1, a, c2, b = command[0], int(command[1]), command[2], int(command[3])
    ia, ja = find_block(a, blocks)
    ib, jb = find_block(b, blocks)
    if ia == ib:
        continue

    if c1 == "move" and c2 == "onto":
        move_onto(a, ia, b, ib, blocks)
    elif c1 == "move" and c2 == "over":
        move_over(a, ia, ib, blocks)
    elif c1 == "pile" and c2 == "onto":
        pile_onto(a, ia, b, ib, blocks)
    elif c1 == "pile" and c2 == "over":
        pile_over(a, ia, ib, blocks)

print_blocks(blocks)