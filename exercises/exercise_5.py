#___________MY OG SOLUTION___________#

# import math

# a = float(input('Coefficient a: '))
# b = float(input('Coefficient b: '))
# c = float(input('Coefficient c: '))

# try:
#     if a == b and b == c and a == 0:
#         print('Infinite roots')
#     else:
#         d = b ** 2 - (4 * a * c)
#         x1 = (-b + math.sqrt(d)) / (2 * a)
#         x2 = (-b - math.sqrt(d)) / (2 * a)
#         if d < 0:
#             print('No real roots')
#         elif x1 == x2:
#             print(f'{x1:.2f}')
#         elif ValueError:
#             print('No real roots')
#         else:
#             print(f'{x1:.2f} and {x2:.2f}')
# except ValueError:
#     print("No roots")

#___________MY 2nd SOLUTION___________#

# a = float(input('Coefficient a: '))
# b = float(input('Coefficient b: '))
# c = float(input('Coefficient c: '))

# output = "No roots."

# d = (b ** 2) - (4 * a * c)

# x1 = (-b + (d ** 0.5)) / (2 * a)
# x2 = (-b - (d ** 0.5)) / (2 * a)
# if d < 0:
#     output = 'No roots'
# elif d == 0:
#     output = f'{x1:.2f}'
# elif a == b == c == 0:
#     output = 'Infinite roots'
# elif a == 0 and b != 0 and c != 0:
#     output = f'{-c / b}'
    
# elif x1 == x2:
#     output = f'{x1:.2f}'
# else:
#     output = f'{x1:.2f} and {x2:.2f}'
# print(output)

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
output = "No roots."

if a == 0 and b == 0 and c == 0:
    output = "Infinite roots."
elif a == 0:
    if b != 0:
        output = f"{-c / b}"
elif b == 0:
    if c != 0:
        if -c / a >= 0:
            x1 = (-c / a) ** 0.5
            x2 = -(-c / a) ** 0.5
            output = f"{x1} and {x2}"
    else:
        output = "0"
else:
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        output = f"{x1} and {x2}"
    elif d == 0:
        x = -b / (2 * a)
        output = f"{x}"
print(output)

#____________SOLUTION 5.py____________#

# a = float(input("Enter coefficient a: "))
# b = float(input("Enter coefficient b: "))
# c = float(input("Enter coefficient c: "))

# output = "No roots."

# if a == 0:
#     if b != 0:
#         output = f"{-c / b}"
# elif b == 0:
#     if c != 0:
#         if -c / a >= 0:
#             x1 = (-c / a) ** 0.5
#             x2 = -(-c / a) ** 0.5
#             output = f"{x1} and {x2}"
#     else:
#         output = "No roots"
# else:
#     d = b ** 2 - 4 * a * c
#     if d > 0:
#         x1 = (-b + d ** 0.5) / (2 * a)
#         x2 = (-b - d ** 0.5) / (2 * a)
#         output = f"{x1} and {x2}"
#     elif d == 0:
#         x = -b / (2 * a)
#         output = f"{x}"

# print(output)

#___________EMAIL SOLUTION___________#

# A = float(input())
# B = float(input())
# C = float(input())

# # find the discriminant
# D = B * B - 4 * A * C

# # if A is zero, the equation is linear: Bx + C = 0
# if A == 0:
#     # Bx = -C => x = -C / B
#     if B != 0:
#         print(-C / B)
#     # if B is zero, there are no roots

# elif D == 0:  # case with zero discriminant
#     # exactly one root
#     print(-B / (2 * A))

# elif D > 0:  # case with positive discriminant
#     r1 = (-B + D ** 0.5) / (2 * A)
#     r2 = (-B - D ** 0.5) / (2 * A)
#     print(r1, r2)

# # if the discriminant is negative, there are no real roots
# else:
#     print("No roots")