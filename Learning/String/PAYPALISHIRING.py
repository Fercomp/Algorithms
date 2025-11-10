def convert(s, numRows):
    vertical = numRows
    diagnol = numRows - 2
    cuts = []
    count = 0
    
    arr = list(s)
    n = len(arr)
    rest = n % numRows
    arr += ['#'] * rest
    
    is_vertical = True
    while count < len(arr):
        if is_vertical:
            cuts.append(arr[count:count+vertical])
            count += vertical
        else:
            aux = arr[count:count+diagnol]
            aux += ['#']
            aux = ['#'] + aux
            aux.reverse()
            cuts.append(aux)
            count += diagnol
        is_vertical = not is_vertical
    
    final = []
    for j in range(numRows):
        for i in range(len(cuts)):
            final.append(cuts[i][j])
    final_string = "".join(final).replace("#", "")
    return final_string
    
print(convert("A", 1))