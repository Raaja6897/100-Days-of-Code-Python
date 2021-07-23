'''
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.
'''

# Example Input
# weight = 85
# height = 1.75
# Example Output
# Your BMI is 28, you are slightly overweight.

weight = float(input("Enter your weight in kg\n"))
height = float(input("Enter your height in meter\n"))

bmi= round((weight/height**2),0)
bmi=int(bmi)

if bmi<18.5:
    print(f"Your bmi is {bmi}, you are underweight")
elif bmi<25:
    print(f"Your bmi is {bmi}, you are weight is normal")
elif bmi<30:
    print(f"Your bmi is {bmi}, you are slightly overweight")
elif bmi<35:
    print(f"Your bmi is {bmi}, you are obese")
else:
    print(f"Your bmi is {bmi}, you are clinically obese")