def fizz_buzz(input):
    if input % 15 == 0:
        return 'FizzBuzz'
    elif input % 5 == 0:
        return 'Buzz'
    elif input % 3 == 0:
        return 'Fizz'
    return input


print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(13))
