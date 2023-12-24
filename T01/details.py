# A program to print out user's name, age and address once they input it.
"""
* Pseudo code*

request and save user name to a variable
request and save user age to a variable
request and save user house number to a variable
request and save user street name to a variable

print out sentence stating user name, age, house number and street name.
"""

user_name = input("Please enter your full name: ")
user_age = input("Please enter your age as a number of years: ")
user_house_number = input("Please enter your house number: ")
user_street_name = input("Please enter your street name: ")

print(f"This is {user_name}. They are {user_age} and lives at house number {user_house_number} on {user_street_name}.")