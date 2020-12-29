point = {'x': 1, 'y': 2}

point = dict(x=1, y=2)

point['x'] = 10
point['z'] = 20

del point['x']

print(point)

print(point.get('a'))

# Looping over dictionaries
for key in point:
    print(key, point[key])

# Or

for key, value in point.items():
    print(key, value)
