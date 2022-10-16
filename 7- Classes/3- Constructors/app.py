# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# point = Point(1, 2)
# point.draw()
# print(point.x)

class Point:
    def __init__(self, x, y) -> None:
        self.x = int(x)
        self.y = int(y)

    def draw(self) -> str:
        print(f"Point ({self.x},{self.y}).")


point = Point(1, 2)
print(point.x)
point.draw()
