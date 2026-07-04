connections = [
    ("203.0.113.10", "mike"),
    ("298.51.100.25", "bob"),
    ("292.0.2.5", "mike"),
    ("203.0.113.15", "bob2")
    ]

# Time: O(n)
# Space: O(n)
def frequency_map(connections):
    d = dict()
    for _, user in connections:
        d[user] = d.get(user, 0) + 1
        
    max_frequency = 0
    max_user = None
    for key, value in d.items():
        if value > max_frequency:
            max_frequency = value
            max_user = key
            
    return max_user

# Time: O(n)
# Space: O(n)
def frequency_map_single_pass(connections):
    d = dict()
    max_frequency = 0
    max_user = None
    
    for _, user in connections:
        curr_frequency = d.get(user, 0) + 1
        
        if curr_frequency > max_frequency:
            max_frequency = curr_frequency
            max_user = user
            
        d[user] = curr_frequency
                
    return max_user