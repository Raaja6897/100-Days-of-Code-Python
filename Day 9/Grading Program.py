student_score = {
    "Harry": 81,
    "Ron": 78,
    "Hermoine": 99,
    "Draco": 74,
    "Neville": 62
}

for student in student_score:
    score=student_score[student]
    if score >90:
        student_score[student]="Outstanding"
    elif score >80 and score <=90:
        student_score[student]="Exceeds Expectations"
    elif score >70 and score <=80:
        student_score[student]="Acceptable"
    elif score <=70:
        student_score[student]="Fail"

print(student_score)