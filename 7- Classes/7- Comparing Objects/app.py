# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


# point = Point(1, 2)
# other = Point(1, 2)
# print(point == other) # False is memory location


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, o: object) -> bool:
        return self.x == o.x and self.y == o.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point(1, 2)
other = Point(1, 2)
print(point == other)
print(point > other)
