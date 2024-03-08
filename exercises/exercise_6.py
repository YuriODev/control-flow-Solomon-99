import math
Ax, Ay = int(input("Enter Ax: ")), int(input("Enter Ay: "))

Bx, By = int(input("Enter Bx: ")), int(input("Enter By: "))

if math.sqrt(Ax**2 + Ay**2) > math.sqrt(Bx**2 + By**2):
    print("A is further from the origin.")
elif math.sqrt(Ax**2 + Ay**2) < math.sqrt(Bx**2 + By**2):
    print("B is further from the origin.")
else:
    print("A and B are at the same distance from the origin.")