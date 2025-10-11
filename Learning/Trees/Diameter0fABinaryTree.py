class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.left.left = TreeNode(7)
root.left.right = TreeNode(9)

# Time = O(n)
# Space = O(log(n)) <= x <= O(n) worst case degenerate tree, best case balanced tree
res = 0
def height_of_tree(root):
    if not root:
        return 0
    l = height_of_tree(root.left)
    r = height_of_tree(root.right)
    # Don't need to ad 1 because the height is relative the edges
    global res
    res = max(res, l + r)
    return max(l, r) + 1
height_of_tree(root)
print(res)