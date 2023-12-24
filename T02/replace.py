# A program to print different versions of a sentence created by the program

# saves sentence 
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# reprint sentence using replace function to replace ! with a space
corrected_sentence = sentence.replace("!", " ")
print(corrected_sentence)

# reprint the sentence completely in upper case using upper function
upper_case_sentence = corrected_sentence.upper()
print(upper_case_sentence)

#reprint the sentence in reverse using slices
reversed_sentence = corrected_sentence[::-1]
print(reversed_sentence)