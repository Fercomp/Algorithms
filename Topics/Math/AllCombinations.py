n = 4
for i in range(2**n):
    '''
    0 → will full with zeros to the left
    {n} → will have n digits
    b → convert number to binary
    '''
    print(format(i, f"0{n}b"))

letters = ["H", "O", "M", "E"]
n = len(letters)
for i in range(2**n):
    '''
    Generate all the combinations of array
    iterate through all masks 
    create a list with only the letters that are 1 in the mask 
    '''
    mask = format(i, f"0{n}b")
    if mask != "0000": # Don't show the empty combination
        print("".join([letters[j] for j in range(n) if mask[j] == "1"]))