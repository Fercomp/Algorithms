# hackerrank.com/challenges/nested-list
import math

records = [["Alpha", 50], ["Beta", 20], ["Chi", 50], ["Randon", 20]]

# Time: O(n) + O(nlogn)
# Space: O(n)
students = []
lowest_score = math.inf
second_lowest_score = math.inf
for r in records:
    name = r[0]
    score = float(r[1])
    if score < lowest_score:
        second_lowest_score = lowest_score
        lowest_score = score
    elif score < second_lowest_score and score != lowest_score:
        second_lowest_score = score
    students.append((name, score))

# Filtering using lambda function as a parameter
filtered = filter(lambda x: x[1] == second_lowest_score, students)
sorted_students = sorted(filtered)
for s in sorted_students:
    print(s[0])