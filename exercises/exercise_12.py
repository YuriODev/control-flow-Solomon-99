number = int(input("Enter a number: "))
# digit_1 = number // 1000
# digit_2 = (number // 100) % 10
# digit_3 = (number // 10) % 10
# digit_4 = number % 10

digit_1,digit_2,digit_3,digit_4 = number // 1000, (number // 100) % 10,(number // 10) % 10,number % 10

digit_1 = '*' if digit_1 % 2 == 0 else str(digit_1)
digit_2 = '*' if digit_2 % 2 == 0 else str(digit_2)
digit_3 = '*' if digit_3 % 2 == 0 else str(digit_3)
digit_4 = '*' if digit_4 % 2 == 0 else str(digit_4)
answer = digit_1 + digit_2 + digit_3 + digit_4
print(answer)