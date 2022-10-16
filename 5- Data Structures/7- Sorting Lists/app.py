# numbers = [1, 5, 54, 4, 6, 7, 3, 21]
# # print(numbers)

# numbers.sort(reverse=False)
# # print(numbers)

# print(sorted(numbers))

items = [
    ("Product1", 10),
    ("Product2", 12),
    ("Product3", 9),
]


def sort_item_by_price(item):
    return item[1]


items.sort(key=sort_item_by_price)
print(items)
