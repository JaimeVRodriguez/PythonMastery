
letters = ['a', 'b', 'c']

# add
letters.append('d')
print(letters)
# place item at a specific index
letters.insert(0, '-')
print(letters)

# remove
letters.pop(0)
print(letters)

# specific item without knowing the index
letters.remove('b')
print(letters)