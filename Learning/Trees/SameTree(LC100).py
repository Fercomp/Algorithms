# https://leetcode.com/problems/same-tree/

def isSameTree(p, q):
    # Important test case, if bot are None return True
    # but if one of them is None and the other is not return false
    # if both are different we stil have work to do
    if not p and not q:
        return True
    elif not p and q or p and not q:
        return False
    
    if p.val == q.val:
        left = isSameTree(p.left, q.left)
        right = isSameTree(p.right, q.right)
        return left and right
    else:
        return False