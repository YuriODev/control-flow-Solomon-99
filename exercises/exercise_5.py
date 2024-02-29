import math

a = float(input('Coefficient a: '))
b = float(input('Coefficient b: '))
c = float(input('Coefficient c: '))

try:
    if a == b and b == c and a == 0:
        print('Infinite roots')
    else:
        x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        if x1 == x2:
            print(f'{x1:.2f}')
        else:
            print(f'{x1:.2f} and {x2:.2f}')
except ValueError:
    print("No roots")