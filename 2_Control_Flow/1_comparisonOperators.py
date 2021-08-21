
#! Similar to arithmetic
#! >, <, >=, <=, == (must be same type and "count")

temperature = 15
if temperature > 35:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")


# -------------------------

age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"

print(message)

#! Alternate using ternary operatory
age2 = 12
message2 = "Eligible" if age2 >= 18 else "Not eligible"
print(message2)