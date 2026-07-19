s = "supercalifragilisticexepialdocious"
def sorting_by_frequency(s):
    arr = list(s)
    frequency = dict()
    
    for i in arr:
        frequency[i] = frequency.get(i, 0) + 1
        
    arr.sort(key=lambda x: (frequency[x], x), reverse=True)
    return "".join(arr)

print(sorting_by_frequency(s))
        