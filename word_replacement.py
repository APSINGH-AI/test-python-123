sentence = input('Enter the sentence :')
print('The sentence is ', sentence, 'and it \'s length is ', len(sentence) )
word1 = input('Enter the word to replace')
word2 = input('Enter the word to replace with ')

dkia =sentence.replace(word1, word2)
print(dkia)

for ch in dkia:
    print(ord(ch))


for ch in  dkia:
    print(chr(ord(ch)))
    






# --------------------------------------------
# Project: Python Word Replacement Program
# --------------------------------------------

# Concepts Covered:
# 1. input() - Taking input from the user.
# 2. len() - Finding the length of a string.
# 3. Escape Sequence (\') - Printing a single quotation mark.
# 4. replace() - Replacing an existing word with another word.
# 5. for loop - Iterating through each character of a string.
# 6. ord() - Converting a character into its Unicode value.
# 7. chr() - Converting a Unicode value back into a character.

# Purpose:
# This project was created to practise Python string operations,
# loops, built-in functions, and character conversions.

# Learning Status:
# Beginner Python Practice Project.
