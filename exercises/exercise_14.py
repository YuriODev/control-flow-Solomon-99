number = int(input("Enter a number: "))
digit_1 = number // 1000
digit_2 = (number // 100) % 10
digit_3 = (number // 10) % 10
digit_4 = number % 10

is_Palindrome = digit_1 == digit_4 and digit_2 == digit_3

print(is_Palindrome)