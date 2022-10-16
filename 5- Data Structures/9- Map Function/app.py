items = [
    ("Product1", 10),
    ("Product2", 12),
    ("Product3", 9),
]

# prices = []
# for item in items:
#     prices.append(item[1])

prices = list(map(lambda item: item[1], items))

print(prices)
