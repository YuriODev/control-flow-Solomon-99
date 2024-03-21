num1 = float(input('Enter the 1st number: '))
num2 = float(input('Enter the 2nd number: '))
operation = input('Enter the operation\n +, -, *, /, mod, pow, div: ')

if operation == '+':
    answer = num1 + num2

elif operation == '-':
    answer = num1 - num2
    
elif operation == '*':
    answer = num1 * num2
    
elif operation == '/':
    if num2 != 0:
        answer = num1 / num2
    else:
        answer = 'Division by 0!'

elif operation == 'mod':
    if num2 != 0:
        answer = num1 % num2
    else:
        answer = 'Division by 0!'

elif operation == 'pow':
    answer = num1 ** num2

elif operation == 'div':
    if num2 != 0:
        answer = num1 // num2
    else:
        answer = 'Division by 0!'

else:
    answer = 'Invalid operation'

print(answer)