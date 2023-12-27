# A program to print out a statement based on the age input by the user.

print("This is a program to provide output based on age. If you would like to terminate the program, please type 'end' when input is requested.")
# request and store user's age unless invalid
age = input("Please enter your age: ")
while age.isdigit() == False:
    #if statement to terminate program if requested
    if age.lower() == 'end':
        print("The program has been terminated as requested.")
        quit()
    # flagging that input is invalid and requesting new age input
    print("Your input is not valid.")
    age = input("Please enter your age: ")

# casting age to input
age = int(age)

# assuming user can not be over 100 and printing statements based on age of user
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