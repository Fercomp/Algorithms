# leetcode.com/problems/longest-common-prefix

def longestCommonPrefix(strs):
    # Handle the edge case of an empty input list.
    if not strs:
        return ""

    # Find the length of the shortest string.
    # Your original method of sorting the lengths works, but using min()
    # with a generator is more direct and efficient.
    try:
        min_length = min(len(s) for s in strs)
    except ValueError:
        # This can happen if strs contains non-string items,
        # but more likely if strs = []. Handled above, but good practice.
        return ""

    # A list to build the prefix characters efficiently
    prefix_builder = []

    # Iterate vertically, column by column (character by character)
    for i in range(min_length):
        # Get the character to check from the first string
        char_to_compare = strs[0][i]

        # Compare this character against all other strings
        for j in range(1, len(strs)):
            if strs[j][i] != char_to_compare:
                # Mismatch found. Join and return the prefix built so far.
                return "".join(prefix_builder)

        # If the inner loop finished without returning, all characters matched.
        # Add the common character to our prefix.
        prefix_builder.append(char_to_compare)

    # If the outer loop finishes, the shortest string (or more) is the prefix
    return "".join(prefix_builder)