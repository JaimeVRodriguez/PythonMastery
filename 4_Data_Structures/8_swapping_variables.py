x = 10
y = 11

z = x
x = y
y = z

print('x: ', x)
print('y:', y)

# Condensed version
a, b = 10, 11

a, b = b, a
print('a: ', a)
print('b: ', b)
