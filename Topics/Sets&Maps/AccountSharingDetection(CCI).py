connections = [
    ("203.0.113.10", "mike"),
    ("298.51.100.25", "bob"),
    ("292.0.2.5", "mike"),
    ("203.0.113.15", "bob2")
    ]

# Time: O(nˆ2)
# Space: O(1)
def brute_force(connections):
    n = len(connections)
    for i in range(n):
        for j in range(i+1, n):
            if connections[i][1] == connections[j][1]:
                return connections[i][1]
            
# Time: O(n)
# Space: O(n)
def set_solution(connections):
    seen = set()
    for _, user in connections:
        if user in seen:
            return user
        seen.add(user)