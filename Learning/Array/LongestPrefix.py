def longestCommonPrefix(self, strs: List[str]) -> str:
    """
    Finds the longest common prefix string amongst a list of strings.

    This method works by "vertical scanning." It first handles the
    edge case of an empty list. It then finds the length of the
    shortest string, as the prefix cannot be longer than this.

    It iterates character by character (from index 0 to min_length - 1).
    In each iteration, it compares the character from the first string
    (strs[0][i]) with the character at the same position in all
    other strings.

    - If a mismatch is found, the prefix built so far is returned.
    - If the loop completes, the entire prefix is common.
    """
    # 1. Handle the edge case of an empty input list.
    if not strs:
        return ""

    # 2. Find the length of the shortest string.
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

    # 5. If the outer loop finishes, the shortest string (or more) is the prefix
    return "".join(prefix_builder)