# Read the question below the code

scores=list(map(int, input("Enter the scores\n").split()))
# print(scores)

high_score=0
for score in scores:
    if score>high_score:
        high_score = score

print(f'The highest score in the class is: {high_score}')


# Question
"""
Highest Score
Instructions
You are going to write a program that calculates the highest score from a List of scores.

e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important you are not allowed to use the max or min functions. The output words must match the example. i.e

The highest score in the class is: x

Example Input
78 65 89 86 55 91 64 89
In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]

Example Output
The highest score in the class is: 91
"""