
#! will always start with zero like string sequence
for number in range(3):
    print("Attempt: ", number+1)

#! starts with, does not in clude this number
for number in range(1, 4):
    print("Attempt: ", number)

#! last number is a step
#! increases by this number
for number in range(0, 10, 2):
    print(f"Even number: {number}")
