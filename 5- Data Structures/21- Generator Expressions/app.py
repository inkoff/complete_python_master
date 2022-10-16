from sys import getsizeof
values = (x*2 for x in range(5000))
print(type(values))
for value in values:
    print(value)

print(getsizeof(values))
