import random

# Method 1
name=input("Give me everybody's name separated by ','\n").split(',')
list_name=[]
list_name.extend(name)
r=random.randint(0,len(list_name)-1)
print(f"{list_name[r].removeprefix(' ')} is going to buy the meal today")
"""
# Method 2
import random

# Split string method
names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

#Write your code below this line 👇

#Get the total number of items in list.
num_items = len(names)
#Generate random numbers between 0 and the last index.
random_choice = random.randint(0, num_items - 1)
#Pick out random person from list of names using the random number.
person_who_will_pay = names[random_choice]

#print(person_who_will_pay + " is going to buy the meal today!")
# or Using choice() function
person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to buy the meal today!")
"""

# Question
"""
Who's Paying
Instructions
You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name

Example Input
Angela, Ben, Jenny, Michael, Chloe
Note: notice that there is a space between the comma and the next name.

Example Output
Michael is going to buy the meal today!
"""