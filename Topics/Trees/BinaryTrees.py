from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node2.left = node3
node2.right = node4
node3.left = node5

'''
   2
  / \
 3   4
/
5
'''

# Current -> Left -> Right
def pre_order_traverse(tree):
    if tree is None:
        return
    print(tree.data, end=" ")
    pre_order_traverse(tree.left)
    pre_order_traverse(tree.right)

# Left -> Current -> Right
def in_order_traverse(tree):
    if tree is None:
        return 
    in_order_traverse(tree.left)
    print(tree.data, end=" ")
    in_order_traverse(tree.right)

# Left -> Right -> Current
def pos_order_traverse(tree):
    if tree is None:
        return
    pos_order_traverse(tree.left)
    pos_order_traverse(tree.right)
    print(tree.data, end=" ")

# BFS for trees
def level_order_traverse(root):
    q = deque()
    q.append(root)
    while q:
        n = q.popleft()
        print(n.data, end=" ")
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)

print("Pre order:  ", end=" ")
pre_order_traverse(node2)
print()
print("In order: ", end=" ")
in_order_traverse(node2)
print()
print("Pos order: ", end=" ")
pos_order_traverse(node2)
print()
print("Level order: ", end=" ")
level_order_traverse(node2)