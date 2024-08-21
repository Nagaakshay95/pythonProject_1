#Task 6
#with if else condition
import math

formula = str(input("enter the formula:-"))

if formula == "circle":
    radius = float(input("enter the radius value:-"))

    print(radius)
    print(math.pi)

    area = math.pi * math.pow(radius, 2)
    print("Area of the circle:-", area)
    print(f"Area of the circle in fraction value:-{area:.2f}")

elif formula == "square":
    a = float(input("enter the area of square:-"))
    print(a)

    square=(a**2)

    print(f"Area of square:-{square:.2f}")
elif formula == "cube":
    b = float(input("enter the area of cube:-"))
    print(b)
    cube=(b**3)
    print(f"Area of square:-{cube:.2f}")
else:
    print("no formula to print")