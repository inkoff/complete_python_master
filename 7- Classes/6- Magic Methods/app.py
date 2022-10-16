class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y}), {self.default_color}")


point = Point(1, 2)
print(point)
