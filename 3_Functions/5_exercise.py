
# FizzBuzz
# Takes input returns Fizz, Buzz, FizzBuzz, or number depending on input

def fizzBuzz(userNumber):
    if userNumber % 15 == 0:
        return "FizzBuzz"
    elif userNumber % 5 == 0:
        return "Buzz"
    elif userNumber % 3 == 0:
        return "Fizz"
    
    return userNumber

print(fizzBuzz(9))
print(fizzBuzz(25))
print(fizzBuzz(15))
print(fizzBuzz(7))