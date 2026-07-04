# https://leetcode.com/problems/balanced-binary-tree/

def height(root):
    if not root:
        return 0
        
    return 1 + max(height(root.left), height(root.right))

def isBalanced(root):
    if not root:
        return True
    
    l_height = height(root.left)
    r_height = height(root.right)

    # See if both height doesen't exceed the difference by one    
    if 0 <= abs(l_height - r_height) <= 1:
        l_balanced = isBalanced(root.left)
        r_balanced = isBalanced(root.right)
        return l_balanced and r_balanced
    else:
        return False