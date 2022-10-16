

class Point:
    default_color = "red"

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    @classmethod
    def zero(cls: object):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y}), {self.default_color}")


Point.default_color = "yellow"
point = Point.zero()
point.draw()

another = Point(3, 4)
another.default_color = "green"
another.draw()
