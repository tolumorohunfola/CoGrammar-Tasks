# A program to print out a statement based on the age input by the user.

# request and store user's age
age = int(input("Please enter your age: "))

# assuming user can not be over 100
if age > 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill.")
elif age < 13:
    print("Your qualify for the kiddie discount.")
elif age == 21:
    print("Congrats on your 21st!")
else:
    print("Age is but a number.")