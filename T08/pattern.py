import math # to round down using math.floor()
# write code to output the star pattern shown below: using an if-else statement
# in combination with a single for loop

# output should be:
# *         1 - 1
# **        2 - 2
# ***       3 - 3
# ****      4 - 4
# *****     5 - 5
# ****      4 - 6
# ***       3 - 7
# **        2 - 8
# *         1 - 9

print("Thank you for choosing to use our program to see your pattern!")

# requests the user's choice of how long the pattern will be.
upper_limit_of_range = int(input("Please enter a single digit, odd number between and including 1 and 9 which will be the number of lines that the pattern is: ")) # *will try error handling when I refactor

if upper_limit_of_range > 9 or upper_limit_of_range < 1 or upper_limit_of_range % 2 == 0:
    upper_limit_of_range = 9
    print("As your input was not within the valid range, the pattern will be 9 lines long.")
    # creates a default version of the upper limit of the range in the for loop below and notifies user
else:
    print(f"Thank you for choosing, the pattern will be {upper_limit_of_range} lines long.")

stars = "*" # sets the original string of stars with only 1 star in the string


for number in range(0, upper_limit_of_range):
    print(stars)
    if number < math.floor(upper_limit_of_range / 2):
        # adds one star to the string of stars if the number in the range is less than half of the range
        stars += "*"
    else:
        # removes the last star in the string of stars if the number in the range higher or equal to half of the range.
        stars = stars[:-1]
