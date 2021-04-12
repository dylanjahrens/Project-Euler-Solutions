'''
Using names.txt, a 46K text file containing over five-thousand first names
begin by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its
alphabetical position in the list to obtain a name score.
What is the total of all the name scores in the file?
'''

import string

f = open('PE_22_names.txt', 'r')
names = f.read()

names_list = names.split(',')
alpha_list = sorted(names_list)

letter_value_index = list(string.ascii_uppercase)

total_value = 0


for name in alpha_list:

    name_value = 0
    letters = list(name)
    
    for letter in letters:
        if letter == '"':
            value = 0
        else:
            value = int(letter_value_index.index(letter)) + 1
            #add 1 because indexing starts at 0 (a = 0, b = 1)
        name_value += value
        name_value_multiplied = name_value * (int(alpha_list.index(name)) + 1)
    
    total_value += name_value_multiplied

print('Total Name Scores:', total_value)
