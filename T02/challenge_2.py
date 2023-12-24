# A program to outut the user's favourite restaurant and number once they have input it into the program

# store the name of a user's favourite restaurant
string_fav = input("Please type in the name of your favourite restaurant: ")

# stores user's favourite number
int_fav = int(input("Please type in your favourite number: "))

print(f"Your favourite restaurant is named {string_fav}.")
print(f"Your favourite number is {int_fav}.")

casting_the_int_to_a_string = int(string_fav)
#This will generate an error as the user is likely to type a name of a restaurant which would usually be a string. If this tries to convert into an int, it will generate a value error as it is unable to perform that error due to the data type of the value.