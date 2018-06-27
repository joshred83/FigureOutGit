# Create a Mad Libs program that reads in test files and lets the user add their own text
# anywhere the word ADJECTIVE, NOUN, ADVERB, OR VERB appears in the text file.
#
# The program would find each occurrence and prompt the user to replace them.
#
# The result should be printed to the screen and saved to a new text file.


import os
import re

try:
    os.chdir('./Mad Libs files')

except FileNotFoundError:
    os.makedirs('./Mad Libs files')
    os.chdir('./Mad Libs files')

file_in = open('mad.txt', 'r')
file_out = open('libs.txt', 'w')

re_adjective = re.compile('ADJECTIVE')
re_noun = re.compile('NOUN')
re_adverb = re.compile('ADVERB')
re_verb = re.compile('VERB')

text = file_in.read().split(' ')

for i in range(len(text)):

    if re_adjective.search(text[i]):
        new_word = input('Enter an adjective:')
        text[i] = re_adjective.sub(new_word, text[i])

    if re_noun.search(text[i]):
        new_word = input('Enter a noun:')
        text[i] = re_noun.sub(new_word, text[i])

    if re_adverb.search(text[i]):
        new_word = input('Enter an adverb:')
        text[i] = re_adverb.sub(new_word, text[i])

    if re_verb.search(text[i]):
        new_word = input('Enter a verb:')
        text[i] = re_verb.sub(new_word, text[i])

text = str.join(' ', text)

print(text)


file_out.write(text)

file_in.close()
file_out.close()
