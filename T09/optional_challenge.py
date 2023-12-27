# A program with two compilation errors, a runtime and logic error

print("This is a program with two compilation errors. One runtime and one logic error. Type 'end' when input is required to terminate the program.")

sentence = input("Please input a sentence: ")
# if statement to check if program was terminated
if sentence.lower() == 'end':
    print("The program has been terminated as requested.")
    quit()

# while statement to continue to request input until valid sentence is input
while len(sentence) == 0:
    print("Your failed to input a sentence. ")
    sentence = input("Please input a sentence: ")
    # if statement to check if program was terminated
    if sentence.lower() == 'end':
        print("The program has been terminated as requested.")
        quit()

# assigning variable with length of sentence and printing it
length_of_sentence = len(sentence)
print(f"The length of your sentence is {length_of_sentence} characters in total.")

# for statement to print each character in the sentence and which number it was in the list of characters in the sentence.
for character in range(length_of_sentence + 1 ): # RunTime Error: index error as it will continue to run past the length of the sentence (needs to remove the -1)
    print(f"Character number {character} in your sentence is {sentence[character]}") # Logical Error: the character numbers output are one behind what they should be. character number 1 not 0 should be the first character in the sentence