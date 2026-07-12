import math
sets = [
    [1, 2, 3],
    [3, 2, 1],
    [1, 4, 5],
    [1, 2]
    ]

elements_frequency = {}
for set in sets:
    for s in set:
        elements_frequency[s] = elements_frequency.get(s, 0) + 1

min_index = 0
min_soma = math.inf
for i in range(len(sets)):
    soma = 0
    for s in sets[i]:
        soma += elements_frequency[s]
    if soma < min_soma:
        min_soma = soma
        min_index = i

print(min_index)