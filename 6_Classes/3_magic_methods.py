class Point:
    # default for all  points
    default_color = 'red'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def draw(self):
        print(f'Point ({self.x}, {self.y})')


point = Point(1, 2)

print(point)
