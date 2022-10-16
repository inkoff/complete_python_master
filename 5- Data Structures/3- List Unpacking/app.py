numbers = [1, 2, "3", 4, "five"]

# first = numbers[1]
# second = numbers[2]
# third = numbers[3]

# first, second, third = numbers
# print(first, second, third)

# first, second, *other = numbers
# print(other)

first, *other, last = numbers
print(first, last)
print(other)
