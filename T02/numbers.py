# A program to complete several calculations on 3 numbers input by the user.

# request that the user enters 3 different integers
int1 = int(input("Please enter an integer: "))
int2 = int(input("Please enter a different integer: "))
int3 = int(input("Please enter another different integer: "))

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