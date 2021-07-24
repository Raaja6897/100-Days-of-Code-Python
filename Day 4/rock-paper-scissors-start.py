import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

zero_rock = 0
one_paper = 1
two_scissors = 2

user=int(input("Enter 0 for Rock 1 for Paper 2 for Scissors\n"))
computer = random.randint(0,2)

if user==0:
    print("You chose")
    print(rock)
elif user==1:
    print("You chose")
    print(paper)
elif user==2:
    print("You chose")
    print(scissors)
else:
    print("Invalid number")



if user==0:
    if computer==0:
        print("draw")
    if computer==1:
        print(paper)
        print("Computer won")
    if computer==2:
        print(scissors)
        print("You won")

if user==1:
    if computer==0:
        print("You won")
    if computer==1:
        print("draw")
    if computer==2:
        # print(scissors)
        print("Computer won")


if user==2:
    if computer==0:
        print("Computer won")
    if computer==1:
        print("You won")
    if computer==2:
        print("draw")

# Method 2 from course

"""
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")
"""