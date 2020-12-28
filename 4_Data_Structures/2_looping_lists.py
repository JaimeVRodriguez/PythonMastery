letters = ['a', 'b', 'c']

# Reads
# For every "letter" that is in list "letters"
# Print the "letter"
for letter in letters:
    print(letter)

# Creates read only tuple
# index and item of that index
for letter in enumerate(letters):
    print(letter)

for index, letter in enumerate(letters):
    print(index, letter)
