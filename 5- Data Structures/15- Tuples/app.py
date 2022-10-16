point_0 = (1, 2)
point_1 = 1, 2
point_2 = 1,  # tuple
point_3 = 1  # int
point_4 = ()
print(type(point_0), type(point_1))
print(type(point_2), type(point_3))
print(type(point_4))

print(point_0 + point_1)
point_5 = (1, 2) + (3, 4)
print(point_5)
point_6 = (1, 2)*4
print(point_6)

point_7 = tuple([1, 2])
print(point_7)
point_8 = tuple("[1, 2]")
print(point_8)

point_9 = 1, 2, 3, 4, 5
print(point_9[0])
print(point_9[0:3])

point_10 = 1, 2
x, y = point_10
print(x, y)

if 1 in point_10:
    print("exist")

# immutable
# point_10[0] = 12
