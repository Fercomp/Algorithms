"""
Knuth-Morris-Pratt (KMP) Algorithm Notes

Problem: String Searching
Find all occurrences of a shorter pattern string (P) within a longer text string (T).
The goal is to determine the number of substrings of T that match P.
"""

# The Problem and Naive Approach
# T = "aabbcabdeaba"  # Text string
# P = "ab"            # Pattern string

def naive_search(text, pattern):
    """
    Implements the naive string search approach.
    Compares the pattern P against every possible starting position in T.

    Complexity: O(|T| * |P|) in the worst case.
    """
    len_T = len(text)
    len_P = len(pattern)
    if len_T < len_P:
        return 0

    count = 0
    # The loop runs up to the last possible starting index for P in T
    for i in range(len_T - len_P + 1):
        # Slice comparison: O(|P|) time operation
        if text[i:i + len_P] == pattern:
            count += 1
    return count

# Example run:
T = "aabbcabdeaba"
P = "ab"
print(f"{naive_search(T, P)}") # Output: 3 (at indices 1, 6, 10)

# The naive algorithm is inefficient because of **redundant comparisons**.
# When a mismatch occurs, the naive approach only shifts the pattern by one 
# position and restarts the comparison from scratch, re-examining characters
# in T that we already know matched a part of P.

# Example Worst Case for Naive (O(|T| * |P|)):
# T = "AAAAAAB"
# P = "AAAAB" 
# At every position, we check 'AAAA', fail on the 5th character, shift 1, 
# and start checking 'AAAA' again.

# The KMP algorithm avoids this by pre-processing the pattern P 
# to calculate the largest possible, safe shift upon a mismatch.