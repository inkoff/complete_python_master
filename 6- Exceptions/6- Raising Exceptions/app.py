def calculate(age):
    if age <= 0:
        raise ValueError("The age can't be a zero or less")
    return 10/age


try:
    calculate(-1)
except ValueError as error:
    print(error)
