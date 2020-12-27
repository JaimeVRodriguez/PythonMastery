letters = ['a', 'b', 'c', 'd']

# Maxtrix - List of lists
matrix = [[0, 1], [2, 3]]

zeros = [0] * 5
# Prints [0, 0 , 0, 0, 0]

combined = zeros + letters

# Just like a split will not print last number in range
numbers = list(range(20))
numbers2 = list(range(1, 21))

chars = list('Hello World')

first = letters[0]
split = letters[1:]
alternate = numbers[::2]
reverse = numbers2[::-1]

print('-- Printing')
print(combined)
print(numbers)
print(numbers2)
print('-- Accessing')
print(first)
print(split)
print(alternate)
print(reverse)
print()
print(chars)
print(len(chars))
