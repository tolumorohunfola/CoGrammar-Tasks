# This is a program to calculate the average of all numbers input by the user until they enter -1

import statistics # importing the statistics library to find average

print("This is a program to find the average of the numbers you input, enter -1 when prompted to finish adding numbers. If you would like to terminate the program, please type '-1'.")

# counts the number of times the user enters invalid input
number_of_value_errors = []

# try except to catch any incorrect inputs
try:
    # creating variable and requesting user to input their number of choice.
    number = float(input("Please enter a number: "))
    number_of_value_errors.append(0)
except ValueError:
    number_of_value_errors.append(1)
    number = 0


# creating a list to hold all the values that the user inputs while the program runs
list_of_numbers = []

# while statement to repeated list the numbers
while number != -1:
    if(number == 0 and number_of_value_errors[-1] == 1):
        print("You must enter a number, what you have entered is not valid.")
    else:
        # adding the current number to the list of numbers
        list_of_numbers.append(number)
        print(f"The number you input was {number}.")

    # requesting an update to the numbers variable and putting within a try except
    try:
        number = float(input("Please enter a number: "))
        number_of_value_errors.append(0)
    except ValueError:
        number_of_value_errors.append(1)
        number = 0

sum_of_value_errors = sum(number_of_value_errors)

# correcting the list to remove the 0s added when there is a value error
print(f"You didn't input a valid number on this number of occasions: {sum_of_value_errors}.")



# if statement to print end statement if -1 is the first number input
if len(list_of_numbers) != 0:
    average = statistics.mean(list_of_numbers)
    print(f"The list of numbers is: {list_of_numbers}")
    print(f"The average of all the numbers you input is: {average}")
else:
    print("The program has been terminated as no valid numbers were entered.")