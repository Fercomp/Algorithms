class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = []


from collections import deque

def cloneGraph(node):
    c_node = Node(node.val, [])
    visited = { node }

    q_c = deque([c_node])
    q = deque([node])

    while q:
        v = q.popleft()
        v_c = q_c.popleft()

        for u in v.neighbors:
            if u.val not in visited:
                u_copy = Node(u.val, [])
                v_c.neighbors.append(u_copy)
                q.append(u)
                q_c.append(u_copy)
                visited.append(u)
    
    return c_node