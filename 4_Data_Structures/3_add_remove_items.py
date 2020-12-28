letters = ['a', 'b', 'c']

# Add items
# To end of list
letters.append('d')
print(letters)

# Specific position
letters.insert(0, '-')
print(letters)

# Remove items
# From end of list
letters.pop()
print(letters)

# From specific index
letters.pop(0)
print(letters)

# Specific item, first occurance
letters.remove('b')
print(letters)
