letters = ["a", "b", "c"]
T_letters = ("a", "b", "c")

for letter in enumerate(letters):
    print(letter)

for letter in enumerate(letters):
    print(letter[0], letter[1])

for index, letter in enumerate(letters):
    print(index, letter)

for index, letter in enumerate(T_letters):
    print(index, letter)
