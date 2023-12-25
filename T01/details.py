# A program to print out user's name, age and address once they input it.
"""
* Pseudo code*

request and save user name to a variable
request and save user age to a variable
request and save user house number to a variable
request and save user street name to a variable

print out sentence stating user name, age, house number and street name.
"""

# introduction to the program
print("This is a program to request and output your details, please type 'end' into any request for input to end the program.")

# defining a function in the case that the user wants to exit the program immediately.
def check_end_program(input_value):
    if input_value.lower() == 'end':
        print("This program has terminated as you have requested.") # prints termination message
        quit() # quit function to terminate the python program


# requests user's name
user_name = input("Please enter your first name: ")
#checking if the program should be ended
check_end_program(user_name)

# repeats the request for user input until a valid input is added
while user_name.isalpha() == False:
    user_name = input("Please enter your first name, it can not contain a number: ")
    #checking if the program should be ended
    check_end_program(user_name)


#requesting user age
user_age = input("Please enter your age as a number of years: ")
# checking if the program should be ended
check_end_program(user_age)

# while statement to ensure age input is valid
while user_age.isdigit() == False or float(user_age) < 0:
    user_age = input("Please enter your age as a number of years, it must be a positive number: ")
    #checking if the program should be ended
    check_end_program(user_age)


# requesting user house number
user_house_number = input("Please enter your house number: ")
#checking if the program should be ended
check_end_program(user_house_number)

# while statement to ensure user house input input is valid as house numbers can be a mix of letters and numbers but never just letters
while user_house_number.isalpha() or float(user_house_number) <=0:
    user_house_number = input("Please enter your house number, it must be a postiive number or a mix of numbers and letters: ")
    #checking if the program should be ended
    check_end_program(user_house_number)


#requesting user street name
user_street_name = input("Please enter your street name: ")
#checking if the program should be ended
check_end_program(user_street_name)

#while statement to ensure street name is a string
while user_street_name.isalpha() == False and " " not in user_street_name:
    user_street_name = input("Please enter a valid street name, it shouldn't contain digits: ")
    #checking if the program should be ended
    check_end_program(user_street_name)


print(f"This is {user_name.capitalize()}. They are {user_age} and they live at {user_house_number} {user_street_name.title()}.")