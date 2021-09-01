
numbers = [1, 2, 3]
numbers2 = [1, 2, 3, 4, 5, 6, 7]
"""
Not as clean to assign
first = numbers[0]
second = numbers[1]
"""

#! Must match the number of items in list
first, second, third = numbers
print(first, second, third)

#! If only want a certain amount, "pack" the rest
one, two, *rest = numbers2
print(one, two)
print(rest)
