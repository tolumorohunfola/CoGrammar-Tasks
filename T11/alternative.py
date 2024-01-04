# A program to read a string and make each alternate character into an upper case character and each other alternate character a lower case character.

print("This is a program to read a string and output it with alternating upper and lower case characters and words. To terminate the program, type 'end' when input is requested.")

def request_user_sentence():
    # requesting input from the user
    user_string = input("Please input your sentence: ")
    # checking if they requested for the program to be terminated.
    if user_string.lower().strip() == "end":
        print("The program has been terminated as requested.")
        quit()
    return user_string

#function to check if the string is valid
def is_string_valid(user_string):
    # splits the string into a list of words
    split_sentence = user_string.split()
    # define invalid variable as 0. It will stay at this value unless there are invalid characters.
    invalid = 0
    # iterate over the list of words and add 1 to 
    for word in split_sentence:
        if word.isalpha() == False:
            # reassigning invalid variable to 1 if any of the words have invalid characters
            invalid = 1
    # returns answer to whether string is valid
    if invalid == 0:
        return True # returns true if the user's string was never invalid
    else:
        return False # returns false if any of the words in the string were invalid



# requesting input from user until it is valid. Input is invalid if the string is empty or only has spaces or includes non-letter characters
user_string = request_user_sentence()

# loops unless the input is valid and prints out what is wrong with the input if input is invalid.
while len(user_string.strip()) == 0 or is_string_valid(user_string) == False: 
    if len(user_string) == 0:
        print("You did not input anything so your input was not valid. Your sentence must include letters.")
    elif len(user_string.strip()) == 0:
        print("You must include letters in your sentence, spaces by themselves do not count as a sentence.")
    else:
        print("Your sentence must only include letters and spaces, please do not include punctuation.")
    user_string = request_user_sentence()



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
