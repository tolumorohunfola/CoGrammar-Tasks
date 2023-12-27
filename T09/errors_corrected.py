# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") # Syntax Error: Missing Parenthesis after print
print ("\n") # Syntax Error: unneeded indentation before print statement and missing parenthesis after print

    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" # Syntax Error: unneeded indentation before variable assignment and RunTime Error: incorrect ==, when it should be = for variable assignment
age = int(age_Str) # Syntax Error: unneeded indentation before variable assignment and RunTime Error: Value Error as the age_Str variable can not be converted to an int, so I've removed the 'years old' part of the assignment in the line before
print("I'm " + str(age) + " years old.") # Syntax Error: unneeded indentation before print statement and RunTime Error: age needs to be cast to string for this to work and Logic Error: to make the sentence easily readable, there needs to be spaces before and after the age is printed

    # Variables declaring additional years and printing the total years of age
years_from_now = "3" # Syntax Error: unneeded indentation before variable assignment
total_years = age + int(years_from_now) # "3" # Syntax Error: unneeded indentation before variable assignment and RunTimeError: years from now needs to be cast to an int for this line to work

print("The total number of years: " + str(total_years)) # Syntax Error: Missing parenthesis within print statement and RunTime Error: the answer_years variable is not defined, it should be the total_years variable and should be cast to a string to avoid an error. Logic Error: total_years should not be within quotation marks

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12  + 6 # RunTime Error: total variable not defined, looks like it was meant to be total_years variable instead and Logic Error: the calculation should also add 6 months
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old") # Syntax Error: missing parenthesis within print statement and RunTime Error: total_months variable needs to be cast to a string to avoid error

#HINT, 330 months is the correct answer

