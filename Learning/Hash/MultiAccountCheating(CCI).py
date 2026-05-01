users = [
    ("mike", ["203.0.3.10", "208.51.0.5", "52.0.2.5"]),
    ("bob1", ["111.0.0.10", "222.0.0.5", "222.0.0.8"]),
    ("bob2", ["222.0.0.5", "222.0.0.8", "111.0.0.10"])
]

def multiAccountCheating(users):
    ips_set = set()
    for _, ips in users:
        canonical_key = "".join(sorted(ips))
        if canonical_key in ips_set:
            return True
        ips_set.add(canonical_key)
    return False

print(multiAccountCheating(users))