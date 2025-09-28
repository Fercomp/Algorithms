# UVa 10324 - Zeros and Ones
#
# The first time I tried a naive approach: 
# for each query, just check all elements from i to j to see if they are equal. 
# But since the string can be very large (up to 1,000,000 chars) and there can be many queries, this
# solution runs in O(j - i) per query and leads to Time Limit Exceeded.
#
# Optimized approach:
# Instead of checking the whole range each time, 
# we preprocess the string into an auxiliary array that records when a change happens. 
#
# Example:
#   Original string: 00101000111
#   Aux array:       00123444555
#
# Explanation:
# - We start with count = 0.
# - Every time the bit changes, we increment count.
# - At each position, we store the current count.
#
# With this, all positions belonging to the same "block" of equal characters have the same value in the auxiliary array.
#
# So, to answer a query [i, j]:
#   - If aux[i] == aux[j], then all characters between i and j are equal.
#   - Otherwise, there was at least one change, so they are not equal.
#
# Each query now runs in O(1), after O(n) preprocessing. Space complexity is O(n).

s = 0
while True:
    # Input can end with EOF
    try:
        l = input()
    except EOFError:
        break

    # Or input can end with an empty line
    if l.strip() == "":
        break

    n = int(input())
    s += 1
    print(f"Case {s}:")

    # Build the auxiliary array (change counter)
    l_count = []
    current = l[0]
    count = 0
    for c in l:
        if c != current:
            current = c
            count += 1
        l_count.append(count)

    # Answer queries in O(1)
    for _ in range(n):
        x, z = map(int, input().split())
        i, j = min(x, z), max(x, z)
        if l_count[i] != l_count[j]:
            print("No")
        else:
            print("Yes")