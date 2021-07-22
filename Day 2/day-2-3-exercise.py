# Example Input
# 56
# Example Output
# You have 12410 days, 1768 weeks, and 408 months left.
# if you live for 90 years

age=input("Enter your age\n")
days= (90-int(age))*365
months = (90-int(age))*12
week =(90-int(age))*52

print(f"You have {days} days {week} weeks and {months} months left")
