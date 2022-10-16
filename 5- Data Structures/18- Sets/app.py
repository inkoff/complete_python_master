# set - collections with out dublicates
numbers = [1, 1, 2, 2, 3, 4, 5, 5, 24]
first = set(numbers)
second = {1, 2, 4}
second.add(55)
second.remove(4)
print(len(second))
print(first)
# union союз
print(first | second)
# intersection пересечение
print(first & second)
# difference отличия
print(first - second)
# simmetric difference
print(first ^ second)
# set - unorder collection
# print(second[0])  # -> error

if 1 in first:
    print("yes")
