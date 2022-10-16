import csv

# file = open("data.csv", "w")
# file.close()

# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["id", "name", "price"])
#     writer.writerow([1000, "str1", 5])
#     writer.writerow([1001, "str2", 5])
#     writer.writerow([1003, "str3", 5])

with open("data.csv") as file:
    reader = csv.reader(file)
    # print(list(reader))
    for r in reader:
        print(r)
