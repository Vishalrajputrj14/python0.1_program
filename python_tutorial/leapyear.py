def is_leap_year(year):
    # Leap year rule:
    # 1. Divisible by 4
    # 2. Not divisible by 100 unless also divisible by 400
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

# User input
year = int(input("Enter a year: "))

# Check and display result
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")