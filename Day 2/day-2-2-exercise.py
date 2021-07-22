'''
PEMDAS ORDER OF IMPORTANCE
()
**
* /
+ -
'''

#BMI Calculator
#Example Input
#weight = 80 in kg
#height = 1.75 in m
# Example Output
# 80 ÷ (1.75 x 1.75) = 26.122448979591837
# 26

weight= float(input("Enter your weight in kg\n"))
height= float(input("Enter your height in meter\n"))

bmi=(weight//(height*height))

print(bmi)
