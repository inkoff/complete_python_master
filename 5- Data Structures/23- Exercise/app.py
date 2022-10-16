sentence = "This is a common interview question"

repite = {}
for char in sentence:
    if char in repite:
        repite[char] += 1
    else:
        repite[char] = 1
# print(repite)
print(sorted(repite.items(), key=lambda kv: kv[1], reverse=True))
