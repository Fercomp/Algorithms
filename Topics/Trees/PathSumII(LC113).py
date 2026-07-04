# leetcode.com/problems/path-sum-ii

# It's almost the same logic as Path Sum I, but now we need to store
# the full sequence whenever we find a valid root-to-leaf path.
# Time: O(n + k.h)
# Space: O(k.h)
def pathSum(root, targetSum):
    def dfs(root, current_sum, current_path, all_solutions):
        if not root:
            return

        current_path.append(root.val)

        if not root.left and not root.right:
            if root.val + current_sum == targetSum:
                # We need to save a copy of the current path.
                # If we append current_path directly, later recursive calls
                # will keep modifying the same list, so the stored result
                # would also be changed.
                all_solutions.append(current_path[:])
        else:
            l = dfs(root.left, current_sum + root.val, current_path, all_solutions)
            r = dfs(root.right, current_sum + root.val, current_path, all_solutions)

        # After exploring left and right, we backtrack in recursion.
        # We remove the current node from the path so the parent call
        # continues with the correct path state.
        current_path.pop()
    
    current_path = []
    all_solutions = []
    dfs(root, 0, current_path, all_solutions)
    return all_solutions