# Your solution to Exercise 8

input_Number = int(input('Enter a 3-digit number: '))

digit = int(input('Enter a digit: '))

in_Number = (digit == input_Number % 10) or (digit == (input_Number // 10) % 10) or (digit == input_Number // 100)

print(in_Number)