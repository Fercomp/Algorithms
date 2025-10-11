class Node:
    def __init__(self, val=0, children=[]):
        self.val = val
        self.children = children

root = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)

node2.children = [node5, node6, node7]
node8.children = [node9]
node4.children = [node8]
root.children = [node2, node3, node4]

#   Tree
#     1
#    /|\
#   2 3 4
# / | \  \
# 5 6 7   8
#          \
#           9

def height_of_tree(root):
    if root == None:
        return 0
    max_height = 0
    for c in root.children:
        max_height = max(max_height, height_of_tree(c))
    return max_height + 1

print(height_of_tree(root))

# Same tree represented in graph
from collections import defaultdict
edges = [(1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (2, 7), (4, 8), (8, 9)]
def create_tree(edges):
    t = defaultdict(list)
    for u, v in edges:
        t[u].append(v)
    return t

t = create_tree(edges)
def height_of_tree_2(t, r):
    if not t[r]:
        return 1
    max_height = 0
    for v in t[r]:
        max_height = max(max_height, height_of_tree_2(t, v))
    return max_height + 1

print(height_of_tree_2(t, 1))