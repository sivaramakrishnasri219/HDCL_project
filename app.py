def is_leap_year(year):
    # A year is a leap year if divisible by 4 but not 100, or if divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

year_input = int(input("Enter a year: "))
if is_leap_year(year_input):
    print(f"{year_input} is a leap year.")
else:
    print(f"{year_input} is not a leap year.")