number = int(input("Enter the roulette number: "))

# if number == 0:
#     print("Green")
# elif number >= 1 and number <= 10:
#     if number % 2 == 0:
#         print("Black")
#     else:
#         print("Red")
# elif number >= 11 and number <= 18:
#     if number % 2 == 0:
#         print("Red")
#     else:
#         print("Black")
# elif number >= 19 and number <= 28:
#     if number % 2 == 0:
#         print("Black")
#     else:
#         print("Red")
# elif number >= 29 and number <= 36:
#     if number % 2 == 0:
#         print("Red")
#     else:
#         print("Black")
# else:
#     print("Out of range")

Output = "The bet will play!"

if number == 0:
    Output = "Green"
elif 1 <= number <= 10 or 19 <= number <= 28:
    Output = "Black" if number % 2 == 0 else "Red"
elif 11 <= number <= 18 or 29 <= number <= 36:
    Output = "Red" if number % 2 == 0 else "Black"
else:
    Output = "The bet will not play!"
print(Output)