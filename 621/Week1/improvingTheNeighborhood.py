'''
When a family purchases a house, they will be gifted with the services of one school and one park in the neighborhood. 
However, to make the most of the services, they will not gift the same school or park to two different families.
 
In other words, if a family buys a house, the construction company will provide them with the gift of a school and a park within a distance of no more than 𝐷
 from their purchased house. From each cell in the map, a family can only move left, right, up or down to an adjacent cell. The distance between two consecutive cells is 1
. Families are only allowed to walk on "Transitable Spaces" when moving between their cells.

These recent changes have made the construction company concerned, as it seems that with these restrictions, there may be houses that cannot be sold because they cannot fulfill the promotion.
That is why they have come to seek your help. Given the map of the neighborhood, which marks the accessible locations, the locations of the new houses, the locations of the parks and schools, and the distance 𝐷
, your task is to determine the maximum number of new houses that can be sold.

Input
The first line of input contains three integers separated by a space 𝑅, 𝐶, and 𝐷
representing the number of rows, the number of columns in the map, and the maximum distance a family wills to walk when going from the house to school, or from house to park, respectively. Each of the next 𝑅
lines contains a string consisting of exactly 𝐶
characters. Each character will be one of '.', '#', 'H', 'S', or 'P'. Representing a transitable space in the neighborhood, an untransitable space in the neighborhood, a new house, a new school, and a new park. Respectively.

Output
Print a line with a single integer number, the maximum number of new houses the construction can sell.
'''

i = list(input().split())
r, c, d = i[0], i[1], i[2]
adj = []

for x in range(int(r)):
    line = list(input())
    adj.append(line)

from collections import deque
q = deque()
for a in range(r):
    for b in range(c):
        if adj[a][b] == 'H':
            deque.append((a,b))



print(adj)