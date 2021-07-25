# Read the question below the code:

import random

lowercase_letters=['a','b','c','d','e','f','g','h','i','j','k','l','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppercase_letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
special_character=['!','@','#','$','%','*','&','?','/','|']

password=[lowercase_letters, uppercase_letters, numbers, special_character]

# Method 1
"""
n_letter=int(input("Enter number of letter you want\n"))
n_number=int(input("Enter number of numbers you want\n"))
n_symbol=int(input("Enter number of symbols you want\n"))

password_gen=''
for _ in range(n_letter):
    password_gen+=(random.choice(password[random.randint(0,1)]))

for _ in range(n_number):
    password_gen+=random.choice(password[2])

for _ in range(n_symbol):
    password_gen+=random.choice(password[3])

print(f"Your generated password is {password_gen}")
"""

# Method 2
"""
n=int(input("Enter the number of letters you want in password\n"))
password_gen=''

for _ in range(n):
     password_gen += random.choice(password[random.randint(0,3)])

print(f"Your generated password is {password_gen}")
"""
# Method 3 Hard Level

n_letter=int(input("Enter number of letter you want\n"))
n_number=int(input("Enter number of numbers you want\n"))
n_symbol=int(input("Enter number of symbols you want\n"))

password_gen=''
for _ in range(n_letter):
    password_gen+=(random.choice(password[random.randint(0,1)]))

for _ in range(n_number):
    password_gen+=random.choice(password[2])

for _ in range(n_symbol):
    password_gen+=random.choice(password[3])

password_gen_list=[]
for l in password_gen:
    password_gen_list.append(l)
random.shuffle(password_gen_list)
print(f"Your generate password is {''.join(password_gen_list)}")

# Question:

"""
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
"""