# A number is considered a leap year if its Divisible by 4 or its divisible by 400 for a century year

# lets start by asking an input from user

year = input("Enter year to check if its a leap year: ")

# Check if year is divisible by 4
if int(year) % 4 == 0:
    print("{} is a leap year ".format(year))
# check if its divisible by 400 for century years
elif int(year) % 400 == 0:
    print("{} is a leap year".format(year))
# Else number is not a leap year
else:
    print("{} is not a leap year".format(year))
