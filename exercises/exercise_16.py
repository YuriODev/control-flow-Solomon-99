day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

leap_year = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

if day == 1:
    if month == 1:
        day = 31
        month = 12
        year -= 1
    elif month == 3:
        day = 29 if leap_year else 28
        month = 2
    elif month == 5 or month == 7 or month == 10 or month == 12:
        day = 30
        month -= 1
    elif month == 2 or month == 4 or month == 6 or month == 8 or month == 9 or month == 11:
        day = 31
        month -= 1
else:
    day -= 1


output = f"{day:02d}.{month:02d}.{year}" #2 digits


print(output)
