def longestCommonPrefix(self, strs: List[str]) -> str:
    sizes = sorted([len(i) for i in strs])
    min_size = sizes[0]
    output = []
    for i in range(min_size):
        current_letter = strs[0][i]
        for j in range(1, len(strs)):
            if strs[j][i] != current_letter:
                return "".join(output)
        output.append(current_letter)
    return "".join(output)