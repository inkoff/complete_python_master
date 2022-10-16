items = [
    ("Product1", 10),
    ("Product2", 12),
    ("Product3", 9),
]
filtred_prices = list(filter(lambda item: item[1] >= 10, items))
print(filtred_prices)
