# leetcode.com/problems/path-sum

def hasPathSum(root, targetSum):

    def path_sum(node, total_sum, target):
        # This problem has a small catch, I can't simply check the sum when node is None.
        # The path must go from root to a leaf node.
        # If a node has only one child, one recursive call will reach None,
        # but that does not mean we completed a valid root-to-leaf path.
        # So, I must confirm that the current node is a leaf,
        # which means both node.left and node.right are None.
        if not node:
            return False

        if not node.left and not node.right:
            return total_sum + node.val == target
        
        left = path_sum(node.left, total_sum + node.val, target)
        right = path_sum(node.right, total_sum + node.val, target)
        return left or right
    
    return path_sum(root, 0, targetSum)