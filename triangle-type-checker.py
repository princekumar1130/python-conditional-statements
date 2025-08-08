import math

# Input three sides of a triangle
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

# First, check if the triangle is valid
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Valid Triangle")

    # Type of triangle based on sides
    if a == b == c:
        print("It is an Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("It is an Isosceles Triangle")
    else:
        print("It is a Scalene Triangle")

    # Check if it's a right-angled triangle using Pythagoras theorem
    sides = sorted([a, b, c])  # sort so hypotenuse is last
    if math.isclose(sides[2]**2, sides[0]**2 + sides[1]**2):
        print("It is also a Right-angled Triangle")
    else:
        print("It is not a Right-angled Triangle")
else:
    print("Not a valid Triangle")
