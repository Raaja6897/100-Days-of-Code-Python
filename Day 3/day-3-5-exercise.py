'''
Love Calculator
💪 This is a Difficult Challenge 💪
Instructions
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:

"Your score is **z**."

e.g.

name1 = "Angela Yu"

name2 = "Jack Bauer"

T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."

Example Input 1
name1 = "Kanye West"
name2 = "Kim Kardashian"
Example Output 1
Your score is 42, you are alright together.
Example Input 2
name1 = "Brad Pitt"
name2 = "Jennifer Aniston"
Example Output 2
Your score is 73.
'''


# Method 1
name1 = input("Enter name 1\n").lower()
name2 = input("Enter name 2\n").lower()
full_name = name1 + name2

full_name_count_1 = full_name.count('t')
full_name_count_1 += full_name.count('r')
full_name_count_1 += full_name.count('u')
full_name_count_1 += full_name.count('e')

full_name_count_2 = full_name.count('l')
full_name_count_2 += full_name.count('o')
full_name_count_2 += full_name.count('v')
full_name_count_2 += full_name.count('e')

tot_score = str(full_name_count_1) + str(full_name_count_2)
tot_score = int(tot_score)

if tot_score < 10 or tot_score > 90:
    print(f"Your score is {tot_score}, you go together like coke and mentos.")
elif tot_score <= 40 or tot_score <= 50:
    print(f"Your score is {tot_score}, you are alright together.")
else:
    print(f"Your score is {tot_score}")

'''
# Method 2
name1 = input("Enter name 1\n")
name2 = input("Enter name 2\n")
combine_name = name1 + name2
lower_case_string=combine_name.lower()

t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')

true = t+r+u+e

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')

love= l+o+v+e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score>=40) and (love_score>90):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")

'''



