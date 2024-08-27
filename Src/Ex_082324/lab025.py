#task 8
#Write a program that classifies a triangle based on its side lengths.
#Given three input values representing the lengths of the sides,
#determine if the triangle is equilateral (all sides are equal),
#isosceles (exactly two sides are equal), or scalene (no sides are equal).
#Use an if-else statement to classify the triangle.

l1 = float(input("enter the length1:\n"))
l2 = float(input("enter the length2:\n"))
l3 = float(input("enter the length3:\n"))

if l1 == l2 and l1 == l3 and l2 == l3:
    print("your entered value is equilateral triangle")
elif l1 == l2 or l1 == l3 or l2 == l3:
    print("your entered value is isosceles triangle")
else:
    print("your entered value is scalene triangle")
