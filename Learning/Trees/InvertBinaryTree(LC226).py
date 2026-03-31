class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        def recursive_call(root):
            if not root:
                return
            root.left, root.right = root.right, root.left
            recursive_call(root.left)
            recursive_call(root.right)
        recursive_call(root)
        return root