n = int(input())
people = []
for _ in range(n):
    p = str(input())
    people.append(p)

lyrics = ["Happy", "birthday", "to", "you",
          "Happy", "birthday", "to", "you",
          "Happy", "birthday", "to", "Rujia",
          "Happy", "birthday", "to", "you"]

n_p = len(people)
n_l = len(lyrics)
m = 1

if n_p > n_l:
    m = n_p // n_l + (1 if n_p % n_l > 0 else 0)
    
for i in range(16 * m):
    print(f"{people[i % n_p]}: {lyrics[i % n_l]}")