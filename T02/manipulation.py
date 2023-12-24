# A program print different versions of a sentence input by the user.

# request and save sentence input by the user
str_manip = input("Please enter a sentence: ")

# find and display length of user's sentence
print(f"The length of your sentence is {len(str_manip)} characters long.")

# replace ever occurrence of the last letter in the sentence with @
last_letter = str_manip[-1]
str_manip_last_letter_replaced = str_manip.replace(last_letter, "@")
print("Below is your sentence with each letter that is the same as the last letter of your sentence replaced with an @ sign: ")
print(str_manip_last_letter_replaced)

# print the last three characters in str_manip backwards
last_three_characters_backwards = str_manip[-1:-4:-1]
print(f"The last three characters in the sentence backwards are {last_three_characters_backwards}.")

# create a five letter word made of the first 3 characters and last two characters
five_letter_word = str_manip[0:3] + str_manip[-2:]
print(f"The new five letter word is {five_letter_word}.")