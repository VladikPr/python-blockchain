# 1: Create a list of names and use a for loop to output the length of each name(len()).
# 2: Add an if check inside the loop to only output names longer than 5 characters.
# 3: Add another if check to see whether a name includes a "n" or "N" character.
# 4: Use a while loop to empty the list of names(via pop())

names_list = ['Maximillian', 'Vladyslav', 'Benjamin',
              'William', 'Lucas', 'Noah', 'Alexander', 'Nathan']

for name in names_list:
    name_length = len(name)
    if name_length > 5 and ('n' in name or 'N' in name):
        print(f'Name: {name}, length: {name_length} characters')

while len(names_list) != 0:
    names_list.pop()
else:
    print('Done! The names list is empty.')
