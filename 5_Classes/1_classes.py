
class Point:
    default_color = 'red'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f'Point ({self.x},{self.y})')

point = Point(1, 2)
point.default_color = 'blue'
print(point.default_color)
point.draw()

point2 = Point(3, 4)
print(point2.default_color)
point2.draw()
