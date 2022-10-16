from pathlib import Path


path = Path(".")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

# list = [p for p in path.iterdir() if p.is_file()]
# print(list)
# list2 = [p for p in path.rglob("*.py")]
# print(list2)
list3 = [p for p in path.iterdir()]
# for p in list3:
#     print(p)


# print(*list3, sep="\n")
print(list3)
