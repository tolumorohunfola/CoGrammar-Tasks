# A program to calculate and output the triangle's area when the 3 lengths of the triangle are provided by the user.

import math # to calculate triangle area
# ask user to enter length of all three sides of triangle
length1 = float(input("Please enter the first length of your triangle: "))
length2 = float(input("Please enter the second length of your triangle: "))
length3 = float(input("Please enter the third length of your triangle: "))

# calculate area of triangle using formula
s = (length1 + length2 + length3) / 2
area = math.sqrt(s* (s-length1) * (s-length2) * (s-length3))

# print out the area of the triangle
print(f"The area of the triangle is {area}cm squared.")