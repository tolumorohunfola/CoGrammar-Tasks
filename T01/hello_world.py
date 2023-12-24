# A program to print out user's name and age once they input it and then print out 'Hello World!'
"""
* Pseudo code outlining how to solve the first task*

request and save user's name to variable
print out user's name

request and save user's age to variable
print out user's age

print out the string 'Hello World!' on a new line
"""

# requesting user's name
user_name = input("Please enter your name: ")

# if statement to check if user name is a number by using isalpha string method
if user_name.isalpha():
    # prints user's name if valid
    print(f"Your name is {user_name}.")
else:
    # prints statement if user name is not valid
    print("Your name should not contain a number, therefore there is no output.")


# try except statement in case user inputs invalid age
try:
    user_age = int(input("Please enter your age: "))
    if user_age >= 0:
        print(f"Your age is {user_age}.")
    else:
        print("Your age can not be a negative number, therefore there is no output.")
except ValueError:
    print("Your age must be a whole number, therefore there is no output.")

print("Hello World!")