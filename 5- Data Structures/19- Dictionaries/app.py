# point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
print(point["x"])
print(point["y"])
print(point["x"])
point["x"] = 12
point["z"] = 21
point["a"] = 25
print(point)


if "a" in point:
    print(point["a"])
print(point.get("a", 23))

del point["a"]
print(point)

for x in point:
    print(x)
for key in point:
    print(key)
for key in point:
    print(key, point[key])
for x in point.items():
    print(x)
for key, value in point.items():
    print(key, value)
