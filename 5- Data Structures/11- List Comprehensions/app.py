items = [
    ("Product1", 10),
    ("Product2", 12),
    ("Product3", 9),
]
# prices = list(map(lambda item: item[1], items))
# filtred_prices = list(filter(lambda item: item[1] >= 10, items))

prices = [item[1] for item in items]
filtred_prices = [item for item in items if item[1] >= 10]

print(prices)
print(filtred_prices)
