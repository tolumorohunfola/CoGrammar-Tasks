# A program to calculate and output the triangle's area when the 3 lengths of the triangle are provided by the user.


#* I'm having trouble fixing this to accept decimal numbers such as 2.3*******************************************

import math # to calculate triangle area

# printing intro statemnet and how to terminate program
print("This is a program to calculate the area of a triangle when you input the lengths of the 3 sides as requested. To terminate the program, please type 'end'.")

# defining function to get length from user including exception handling
def request_length(number):
    # ask user to enter length of one side of the triangle 
    length = input(f"Please enter the {number} length of your triangle: ")

    # a while loop to ensure the length input by the user is valid (over 0 and a number)
    while length.isdecimal() == False or float(length) <= 0:
        # checking if input is 'end' first so the program can be terminated if so
        if length.lower() == "end":
            print("The program has been terminated as you have input 'end'.")
            quit()
        length = input(f"Your input is not valid. It must be a positve number. Please enter the {number} length of your triangle: ")
    #returning length converted into float
    return float(length)

#calling request length function to get all 3 lengths from user
length1 = request_length("first")
length2 = request_length("second")
length3 = request_length("third")

# calculate area of triangle using formula
s = (length1 + length2 + length3) / 2
area = math.sqrt(s* (s-length1) * (s-length2) * (s-length3))

# print out the area of the triangle
print(f"The area of the triangle is {round(area, 2)}cm squared.")