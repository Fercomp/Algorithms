class Student:
    def __init__(self, math, id, english=0):
        self.math = math
        self.id = id
        self.english = english
        
n, x, y, z = map(int, input().split())
students = []
result = []
math_grades = list(map(int, input().split()))
for i in range(n):
    s = Student(math_grades[i], i+1)
    students.append(s)
    
english_grades = list(map(int, input().split()))
for i in range(n):
    students[i].english = english_grades[i]
    
students.sort(key=lambda x: (-x.math, x.id))
for i in range(x):
    result.append(students[i].id)
students = students[x:]

students.sort(key=lambda x: (-x.english, x.id))
for i in range(y):
    result.append(students[i].id)
students = students[y:]

students.sort(key=lambda x: (-x.math - x.english, x.id))
for i in range(z):
    result.append(students[i].id)

result.sort()
for i in range(len(result)):
    print(result[i])