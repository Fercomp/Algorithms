from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(6)
root.right.left = TreeNode(3)
root.right.right = TreeNode(7)
'''
    5
    /\
   4  6
      /\
     3  7
'''

def isValidBST(root):
    if not root:
        return True
    
    is_valid_left = isValidBST(root.left)
    is_valid_right = isValidBST(root.right)
    if not is_valid_left or not is_valid_right:
        return False

    if root.left and root.right:
        return root.left.val < root.val < root.right.val
    elif root.left and not root.right:
        return root.left.val < root.val
    elif not root.left and root.right:
        return root.val < root.right.val
    else:
        return True

print(isValidBST(root))