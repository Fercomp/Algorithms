class Friend:
    def __init__(self, money, friendship):
        self.money = money
        self.friendship = friendship    

n, d = map(int, input().split())
friends = []
for _ in range(n):
    m, s = map(int, input().split())
    friends.append(Friend(m, s))
friends = sorted(friends, key=lambda x: x.money)

l = 0
r = 0
max_friendship = -1
current_friendship = 0
while r < len(friends):
    if friends[r].money - friends[l].money < d:
        current_friendship += friends[r].friendship
        max_friendship = max(max_friendship, current_friendship)
        r += 1
    else:
        max_friendship = max(current_friendship, max_friendship)
        current_friendship -= friends[l].friendship
        l += 1
print(max_friendship)