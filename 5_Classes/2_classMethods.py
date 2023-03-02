class Point:
    default_color = 'red'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    @classmethod
    def one_two(cls):
        return cls(1, 2)

    def draw(self):
        print(f'Point ({self.x},{self.y})')


point = Point.zero()
point.draw()

point2 = Point.one_two()
point2.draw()