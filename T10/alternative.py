# A program to read a string and make each alternate character into an upper case character and each other alternate character a lower case character.

print("This is a program to read a string and output it with alternating upper and lower case characters and words. To terminate the program, type 'end' when input is requested.")

# requesting input from the user
user_string = input("Please input your sentence: ")
# checking if they requested for the program to be terminated.
if user_string.lower().strip() == "end":
    print("The program has been terminated as requested.")
    quit()
# requesting input from user until it is valid. Input is invalid if the string is empty or the string doesn't contain letters or letters and spaces
# while not (user_string.isalpha() and user_string.find(" ")) or (user_string.isalpha() == False) or len(user_string) == 0:  # * original version*************************************
while len(user_string) == 0: # * send help *
    # break statements
    if user_string.isalpha(): # * send help*
        break
    if (user_string.isalpha() and user_string.isspace()): # * I'm having trouble with this, it allows in numbers for some reason!!!
        break
    print("Your sentence must only include letters and spaces, please do not include punctuation.")
    user_string = input("Please input your sentence: ")
    # checking if they requested for the program to be terminated.
    if user_string.lower().strip() == "end":
        print("The program has been terminated as requested.")
        quit()


# user_string = "I am learning to code"
print(f"The original string: {user_string}.")

# alternating character version
up_down_char_string = ""

for character_index in range(len(user_string)):
    # if the character is an even number, changes it to uppercase and if not changes to lowercase
    if character_index % 2 == 0:
        amended_character = user_string[character_index].upper()
    else:
        amended_character = user_string[character_index].lower()
    # adds amended character to the up_down_char_string
    up_down_char_string += str(amended_character)

print(f"The amended string with characters in alternate cases: {up_down_char_string}.")

# alternating word version

# creating a list of all the words in the string
list_of_words = user_string.split()
up_down_word_list = []

for word_number in range(len(list_of_words)):
    # if the word is an even number in the string, changes it to lowercase and if not changes to uppercase
    if word_number % 2 == 0:
        up_down_word_list.append(list_of_words[word_number].lower())
    else:
        up_down_word_list.append(list_of_words[word_number].upper())

up_down_word_string = " ".join(up_down_word_list)

print(f"The amended string with words in alternate cases: {up_down_word_string}.")
