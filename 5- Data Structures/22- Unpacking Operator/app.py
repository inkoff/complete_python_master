numbers = [1, 2, 3]
print(*numbers)


values = list(range(5))
values = [*range(5)]
print(values)

strings = [*"Hello"]
print(strings)

first = [1, 2]
second = [3, 4]
print([*first, "a", *second])


first_d = {"a": 1, "b": 2}
second_d = {"a": 1, "c": 4}
print({**first_d, **second_d, "z": 12})
