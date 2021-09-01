
#! Constrained by the parameters
def multiply(x, y):
    return x * y

multiply(2, 3)

#! Not a set of parameters
def multiplyMult(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

answer = multiplyMult(2, 3, 4, 5)
print(answer)