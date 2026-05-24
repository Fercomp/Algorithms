# cses.fi/problemset/result/17286461/

# Time: O(n)
# Space: O(1)
dna = input()
max_sequence = 0
current_sequence = 0
for i in range(len(dna)):
    if i > 0 and dna[i] != dna[i-1]:
        max_sequence = max(current_sequence, max_sequence)
        current_sequence = 0
    current_sequence += 1
    
print(max(current_sequence, max_sequence))