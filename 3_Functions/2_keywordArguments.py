
#! Default by will be 1
#! If you want a differt increment by you must specify
def increment(number, by=1):
    return number + by

#! Keywords allow code to be more readable
# by is the parameter for those who may not know
result = increment(2, by=2)
result2 = increment(3)
result3 = increment(2, 5)

print(result)
print(result2)
print(result3)