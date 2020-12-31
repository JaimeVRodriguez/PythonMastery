try:
    age = int(input('Age: '))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError) as ex:
    print('Input was not a valid age. ')
    print('Error Message: ', ex)
else:
    print('No exceptions were thrown')
