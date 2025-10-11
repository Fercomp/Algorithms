# Rememeber, maximum sum of subsequences
# Obs: this problem don't even make sence because we could only sum all elements
# or if could have negative numbers just discard the negatives
s = [1, 2, 3, 4, 5]

# Basic recursion without dp
def max_sub_sequences(s, i=0, r=[]):
    if len(s) == i:
        return 0
    
    r.append(s[i])
    taken =  max_sub_sequences(s, i + 1, r)
    r.pop()
    not_taken = max_sub_sequences(s, i + 1, r)
    return s[i] + max(taken, not_taken)

# Now the problem states to find all subsequences with no adjacents elements
# This makes more sence, because you cannot take a greedy approach and need to test
# every subsequence
# Time complexity: 0(2^n)
# Space complexity: O(n)
def no_adj_max_sub_sequences(s, i=0, r=[]):
    if i >= len(s):
        return 0
    
    r.append(s[i])
    # taken is when i take the current element and sum with the next non adjacent 
    taken = s[i] + no_adj_max_sub_sequences(s, i+2, r)
    r.pop()
    # not taken is when i don't take the current and just consider the problem for the rest
    not_taken = no_adj_max_sub_sequences(s, i+1, r)
    return max(taken, not_taken)

# Optimization using dp
def no_adj_max_sub_seq(s, i=0, d={})
    if i >= len(s):
        return 0

    if i in d:
        return d[i]
    
    r.append(s[i])
    if i+2 in d:
        taken = d[i+2]
    else:
        taken = s[i] + no_adj_max_sub_seq(s, i+2, d)
    
    r.pop()
    if i+1 in d:
        not_taken = d[i+1]
    else:
        not_taken = no_adj_max_sub_seq(s, i+1, d)
    d[i] = max(taken, not_taken)
    return d[i]


print(no_adj_max_sub_sequences(s))