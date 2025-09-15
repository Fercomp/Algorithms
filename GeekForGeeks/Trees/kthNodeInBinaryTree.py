from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(7)
root.right = Node(9)
root.right.right = Node(11)
root.left = Node(6)
root.left.left = Node(3)
root.left.left.left = Node(1)
root.left.left.right = Node(4)

order = []
def kthNodeInBinaryTree(root, k):
    global order
    if not root:
        return -1
    l = kthNodeInBinaryTree(root.left, k)
    order.append(root.data)
    if len(order) == k+1:
        return order[k]
    r = kthNodeInBinaryTree(root.right, k)
    return max(l, r)
    
print(kthNodeInBinaryTree(root, 3))
print(order)