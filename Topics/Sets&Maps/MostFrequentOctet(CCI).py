connections = [
    ("203.0.113.10", "mike"),
    ("298.51.100.25", "bob"),
    ("292.0.2.5", "mike"),
    ("203.0.113.15", "bob2")
    ]

# Time: O(n)
# Space: O(1)
# The only intresting thing about this exercise, is that the Space complexity
# is O(1), because the biggest value the first octet can be is 255, so our map 
# has a fixed space size
def frequency_map(connections):
    ip_to_frequency = {}
    max_frequency = 0

    for ip, _ in connections:
        octet = ip.split(".")[0]
        ip_to_frequency[octet] = ip_to_frequency.get(octet, 0) + 1
        max_frequency = max(max_frequency, ip_to_frequency[octet])

    return max_frequency