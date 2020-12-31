class Point:
    # default for all  points
    default_color = 'red'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f'Point ({self.x}, {self.y})')


point = Point(1, 2)
point.draw()

# Will chang that specific point but not the default for all points
point.default_color = 'green'

print(point.default_color)
print(Point.default_color)
