# def multiply(x, y):
#     return x*y


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(1, 2, 3, 4))


# x = tuple([12, 2, 3, 4])
# print(x, type(x))
