class Point:
    color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y}), {self.color}")


Point.color = "yellow"
point = Point(1, 2)
point.draw()

another = Point(3, 4)
another.color = "green"
another.draw()
