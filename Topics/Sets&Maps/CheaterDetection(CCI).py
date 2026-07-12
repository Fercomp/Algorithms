from collections import defaultdict

answers = ["a", "b", "c", "c"]
m = 5
students = [
    (4, 10, ["a", "b", "c", "d"]),
    (1, 6,  ["a", "b", "c", "d"]),
    (3, 8,  ["a", "b", "d", "d"]),
    (5, 11, ["a", "b", "c", "d"]),
    (9, 7,  ["a", "b", "c", "d"]),
    (6, 16, ["a", "b", "d", "d"])
]

def cheater_detection(answers, m, students):
    row_to_answers = defaultdict(lambda: defaultdict(list))

    def get_wrong_answers(student_ans):
        wrong_answers = []
        for i in range(len(answers)):
            if student_ans[i] != answers[i]:
                wrong_answers.append(student_ans[i])
            else:
                wrong_answers.append("*")
                
        return "".join(wrong_answers)

    for id, desk, ans in students:
        if ans == answers:
            continue
        row = (desk -1) // m
        d = row_to_answers[row]
        wrong_answers = get_wrong_answers(ans)
        d[wrong_answers].append(id)

    result = []
    for value in row_to_answers.values():
        for k, v in value.items():
            if len(v) > 1:
                result.append(v)
    return result

print(cheater_detection(answers, m, students))