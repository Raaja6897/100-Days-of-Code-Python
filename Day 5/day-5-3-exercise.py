# Read the question below the code:
# Method 1
total=0
for i in range(1,101):
    if i%2==0:
        total+=i
print(total)
# Method 2
total_j=0
for j in range(0,101,2):
    total_j+=j
print(total_j)

# Question:

"""
Adding Evens

Instructions:
You are going to write a program that calculates the sum of all the even numbers from 1 to 100. 
Thus, the first even number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output. 
It should just print the final total and not every step of the calculation.
"""