# leetcode.com/problems/permutations/

nums = [1, 2, 3]

# Temos um total de n! permutações e para cada permutação temos que copiar o path pra result
# Time: O(n.n!)
# Também armazenamos n! listas cada lista contendo n elementos logo
# Space: O(n.n!)
def permute(nums):
    result = []
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])  # cópia
            return

        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False

    backtrack([])
    return result


nums = [1, 2, 3]
print(permute(nums))