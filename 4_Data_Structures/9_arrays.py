from array import array

numbers = array('i', [1, 2, 3])

numbers.append(4)
numbers.insert(0, 0)


print(numbers)

# Since typecode 'i' is for intergers
# Only integers can be inserted into this specific array
