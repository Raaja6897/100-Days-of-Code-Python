'''
his is how you work out whether if a particular year is a leap year.

on every year that is evenly divisible by 4 **except** every year that is evenly divisible by 100 **unless** the year is also evenly divisible by 400

e.g. The year 2000:

2000 ÷ 4 = 500 (Leap)

2000 ÷ 100 = 20 (Not Leap)

2000 ÷ 400 = 5 (Leap!)

So the year 2000 is a leap year.

But the year 2100 is not a leap year because:

2100 ÷ 4 = 525 (Leap)

2100 ÷ 100 = 21 (Not Leap)

2100 ÷ 400 = 5.25 (Not Leap)
'''

# Example Input 1
# 2400
# Example Output 1
# Leap year.
# Example Input 2
# 1989
# Example Output 2
# Not leap year.

# Method 1
year=int(input("Enter the year\n"))

if year%4==0 and year%400==0:
    print("Leap year")
elif year%4==0 and year%100==0:
    print("Not leap year")
else:
    print("Leap Year")

'''
# Method 2

if year%4==0: # condition if year%4==0 then check for next 100
    if year%100==0: # if year%4==0 and year%100==0(if y%100!=0 it is leap year) then check for next 400
        if year%400==0: # if a year%4==0 and year%100==0 and year%400==0 it its a leap year else not leap year
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year") # if year%100!=0 it is leap year which is writen as else
else:
    print("Not leap year") # if year%4==0 is not True it is Not leap year

'''