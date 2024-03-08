number = int(input("Enter the roulette number: "))

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