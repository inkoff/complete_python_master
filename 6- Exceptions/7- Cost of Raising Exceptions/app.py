from timeit import timeit

code1 = """
def calculate(age):
    if age <= 0:
        raise ValueError("The age can't be a zero or less")
    return 10/age


try:
    calculate(-1)
except ValueError as error:
    print(error)
"""
code2 = """
def calculate(age):
    if age <= 0:
        raise ValueError("The age can't be a zero or less")
    return 10/age


try:
    calculate(-1)
except ValueError as error:
    pass
"""
code3 = """
def calculate(age):
    if age <= 0:
        None
    return 10/age


x = calculate(-1)
if x == None:
    pass
"""
# print(timeit(code1, number=1000))
print(timeit(code2, number=1000))
print(timeit(code3, number=1000))
