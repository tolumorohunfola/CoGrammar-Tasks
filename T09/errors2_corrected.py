# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" # RunTime Error: Lion needs to be within quotation marks
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth" # Logic Error: the str needs to be turned into a formatted string and the second and third variables within the string need to be swapped

print(full_spec) # Syntax Error: Missing parenthesis within print statement

