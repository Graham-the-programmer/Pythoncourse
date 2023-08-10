import math


def circumference_of_a_circle(radius):
    c = 2 * math.pi * radius
    print(f'Circumference = ', c)

# circumference_of_a_circle(20)

def area_of_circle(radius):
    A = math.pi * radius**2
    print(f'Area = ', A)

# area_of_circle(20)

def Volume_of_sphere(radius):
    V = (4/3) * math.pi * radius**3
    print(f'Volume of sphere =', V)


# Volume_of_sphere(10)

def area_perimeter_of_rectangle(height, length):
    area = height * length
    perimeter = (height*2) + (length*2)
    print(f'The area =', area)
    print(f'The perimeter =', perimeter )

# area_perimeter_of_rectangle(10, 20)

