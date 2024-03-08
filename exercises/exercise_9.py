# Your solution to Exercise 9

integer = int(input('Enter an integer: '))

digit_1 = integer // 100
digit_2 = (integer // 10) % 10
digit_3 = integer % 10

sum = digit_1 + digit_3

if sum > digit_2:
    print('>')
elif sum < digit_2:
    print('<')
else:
    print('=')