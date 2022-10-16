# class Point:
#     def draw(self):
#         print("draw")


# point = Point()
# print(type(point))
# print(isinstance(point, Point))

# x = -1
# print(isinstance(x, int))
# s = "1"
# print(isinstance(s, (int, str, dict)))
# # type()
# print(s is int)
# point.draw()

class MyPointe:
    def draw(self):
        print("draw")


point = MyPointe()
point.draw()
print(type(point))
print(isinstance(point, MyPointe))
