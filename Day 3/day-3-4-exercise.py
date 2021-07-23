'''
Pizza Order
Instructions
Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.

Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1
'''

# Example Input
# size = "L"
# add_pepperoni = "Y"
# extra_cheese = "N"
# Example Output
# Your final bill is: $28.


size = input("Enter the size of Pizza,? S-Small, M-Medium, L-Large\n").upper()
add_pepperoni = input("Do you want to add pepperoni, Enter Y or N\n").upper()
extra_cheese = input("Do you want to add extra cheese, Y or N\n").upper()
# Method 1

bill = 0
if size == 'L':
    bill += 25
    if add_pepperoni == 'Y':
        bill += 3
    if extra_cheese == 'Y':
        bill += 1
elif size == 'M':
    bill += 20
    if add_pepperoni == 'Y':
        bill += 3
    if extra_cheese == 'Y':
        bill += 1
elif size == 'S':
    bill += 15
    if add_pepperoni == 'Y':
        bill += 2
    if extra_cheese == 'Y':
        bill += 1

print(f'Your final bill is ${bill}')


'''
# Method 2 from course

bill=0

if size=='S':
    bill+=15
elif size=='M':
    bill+=20
else:
    bill+=25

if add_pepperoni=='Y':
    if size=='S':
        bill+=2
    else:
        bill+=3

if extra_cheese=='Y':
    bill+=1

print(f'Your final bill is ${bill}')
'''