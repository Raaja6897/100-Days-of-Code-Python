# Days in Month
# You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.
# days_in_month(year=2022, month=2)
# And it will use this information to work out the number of days in the month, then return that as the output, e.g.:
# 28


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                # print("Leap Year")
                return True
            else:
                # print("Not leap year")
                return False
        else:
            # print("Leap year")
            return True
    else:
        # print("Not a leap year")
        return False


# Method 1
def days_in_month(year, month):
    if month>12 or month<1:
        return "Invalid month"
    result = is_leap(year)
    if result:
        month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return month_days[month - 1]
    else:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return month_days[month - 1]


# Method 2 from udemy

"""
def days_in_months(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month==2:
        return 29
    return month_days[month-1]
"""

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
