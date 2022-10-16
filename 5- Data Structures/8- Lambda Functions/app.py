items = [
    ("Product1", 10),
    ("Product2", 12),
    ("Product3", 9),
]


# def sort_item_by_price(item):
#     return item[1]


# items.sort(key=sort_item_by_price)
items.sort(key=lambda item: item[1])
print(items)
