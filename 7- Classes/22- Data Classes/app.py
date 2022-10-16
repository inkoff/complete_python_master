from collections import namedtuple


# class Point:
#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y

#     def __eq__(self, o: object) -> bool:
#         return self.x == o.x and self.y == o.y


Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)
print(id(p1))
print(id(p2))
