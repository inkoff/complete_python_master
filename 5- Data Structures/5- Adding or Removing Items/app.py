letters = ["a", "b", "c"]

# Add
letters.append("d")
letters.insert(0, "z")
letters.insert(5, "e")
print(letters)

# Remove
letters.pop(0)
print(letters)
letters.pop()
print(letters)
letters.remove("d")
print(letters)
del letters[0]
print(letters)
del letters[0:1]
print(letters)
letters.clear()
print(letters)
