letters = ["a", "b", "c", "d"]
# print(letters[-1])
# letters[1] = "A"
# print(letters[0])
# print(letters[0:3])
# print(letters[-1])
# print(letters[-2:])
# print(letters[:-1])
# print(letters)


def add_even_number(i=int(input("Введите положительное число: "))):
    if i % 2:
        print(list(range(abs(i)))[::2])
        print(list(list(range(abs(i)-1))[::-2])[::-1] + [abs(i)])
    else:
        print(list(range(abs(i)+1))[::2])
        print(list(list(range(abs(i)))[::-2])[::-1])


add_even_number()
