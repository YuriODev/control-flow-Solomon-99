alex_age = int(input())
tatyana_age = int(input())

# print('Tatyana is the eldest' * (tatyana_age > alex_age))

# print('Alex and Tatyana are of the same age.' * (tatyana_age == alex_age))

# print('Alex is the eldest' * (alex_age > tatyana_age))

if alex_age > tatyana_age:
    print("Alex is the eldest.")
elif alex_age < tatyana_age:
    print("Tatyana is the eldest.")
else:
    print("Alex and Tatyana are of the same age.")