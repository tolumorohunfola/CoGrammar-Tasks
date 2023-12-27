# A program to complete several calculations on 3 numbers input by the user.

# Introducing program
print("This is a program to complete calculations on 3 numbers you input. To terminate the program type 'end' when input is requested.")

# function to request integer
def request_integer(number):
    integer = input(f"Please enter your {number} whole number: ")
    # while statement in case user doesn't type an integer
    while integer.isdigit() == False:
        # if statement in case user requests end of program
        if integer.lower() == 'end':
            print("The program has been terminated as requested.")
            quit()
        print("Your input is not valid.")
        integer = input(f"Please enter your {number} whole number: ")
    
    return int(integer)


# request that the user enters 3 different integers
int1 = request_integer('first')
int2 = request_integer('second')
int3 = request_integer('third')

# creating a list out of the 3 integers
list_of_integers = [int1, int2, int3]
# print sum of all 3 integers
sum_of_all_integers = sum(list_of_integers)
print(f"The sum of all of the numbers you input is {sum_of_all_integers}")

# print out the first number minus the second number
first_number_minus_second_number = list_of_integers[0] - list_of_integers[1]
print(f"The first number minus the second number is {first_number_minus_second_number}.")

# print out the third number multiplied by the first number
third_number_multiplied_by_first_number = list_of_integers[2] * list_of_integers[0]
print(f"The product of the third and first number is {third_number_multiplied_by_first_number}.")

# print out the sum of all three numbers divided by the third number
sum_of_all_integers_divided_by_third_number = sum_of_all_integers / list_of_integers[2]
print(f"The sum of all three numbers divided by the third number is {sum_of_all_integers_divided_by_third_number}.")