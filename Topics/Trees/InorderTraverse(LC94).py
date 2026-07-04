# leetcode.com/problems/binary-tree-inorder-traversal

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(self, root):
    result = []
    # Classic technique to create a function inside another function
    def recursive_call(root):
        if not root:
            return
        
        recursive_call(root.left)
        # The only difficult part is understanding that we need to visit the left first,
        # then append the current node. Recursively, the left subtree will be added,
        # and then we visit the right subtree.
        result.append(root.val)
        recursive_call(root.right)
        
    recursive_call(root)
    return result