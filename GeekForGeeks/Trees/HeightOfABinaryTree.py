from collections import deque

# Binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)

# Recusrive approach
def heightOfBinaryTree(root):
    if root == None:
        return 0
    
    l = heightOfBinaryTree(root.left)
    r = heightOfBinaryTree(root.right)
    return 1 + max(l, r)

def bfs_heightOfBinaryTree(root):
    if not root:
        return 0
    level = 0
    q = deque([root])
    while q:
        for _ in range(len(q)):
            v = q.popleft()
            if v.left:
                q.append(v.left)
            if v.right:
                q.append(v.right)
        level += 1
    return level

def iterative_heightOfBinaryTree(root):
    if not root:
        return 0
    
    s = deque([(root, 1)])
    max_height = 0
    while s:
        v, h = s.popleft()
        max_height = max(max_height, h)
        if v.left:
            s.append((v.left, h+1))
        if v.right:
            s.append((v.right, h+1))
    return max_height
    
        
print(heightOfBinaryTree(root))
print(bfs_heightOfBinaryTree(root))
print(iterative_heightOfBinaryTree(root))