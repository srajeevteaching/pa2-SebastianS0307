# Programmer: Sebastian Silguero
# Course: CS151, Dr. Rajeev
# Date: September 29th, 2021
# Programming Assignment: 2
# Program Inputs: User will input month and year
# Program Outputs: Number of days in that month and if the year is a leap year

# User input month
month = input("Please enter a month: ")
year = int(input("Please enter a year (0000): "))

# If statement determines how many days are in a month
if month == "January":
    print("There are 31 days in the month of " + month + "!")
elif month == "March":
    print("There are 31 days in the month of " + month + "!")
elif month == "April":
    print("There are 30 days in the month of " + month + "!")
elif month == "May":
    print("There are 31 days in the month of " + month + "!")
elif month == "June":
    print("There are 30 days in the month of " + month + "!")
elif month == "July":
    print("There are 31 days in the month of " + month + "!")
elif month == "August":
    print("There are 31 days in the month of " + month + "!")
elif month == "September":
    print("There are 30 days in the month of " + month + "!")
elif month == "October":
    print("There are 31 days in the month of " + month + "!")
elif month == "November":
    print("There are 30 days in the month of " + month + "!")
elif month == "December":
    print("There are 31 days in the month of " + month + "!")

# Function to check leap year and determine days in February

def leapYear(year):
    if ((year % 400 == 0) or
            (year % 100 != 0) and
            (year % 4 == 0)):
        print(str(year) + " is a leap year")
        if month == "February":
            print("There are 29 days in the month of " + month + "!")
    else:
        print(str(year) + " is not a leap year")


# Calling the function
leapYear(year)