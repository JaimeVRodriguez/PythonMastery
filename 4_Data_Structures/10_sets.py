numbers = [1, 1, 2, 3, 4]
# Set is like a list with no repeating items
uniques = set(numbers)
second = {1, 5}


print(uniques)

print(uniques | second)  # In either set
print(uniques & second)  # In both sets
print(uniques - second)  # Removes what is in the first set from the second
print(uniques ^ second)  # Returns numbers that are not in both
