class Tag:
    def __init__(self) -> None:
        self.tags = {}

    def add(self, tag: str) -> dict:
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag: str):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag: str, count: int):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


tag = Tag()

tag.add("Python")
tag.add("python")
tag.add("python")
tag.add("python")

print(tag.tags)
tag["Python"] = 22
tag["SEr"] = 22
print(tag["python"])

for T in tag:
    print(T)


# di = dict(python=23, js=2)

# print(di.get("python"))

# di["c"] = 1

# print(di)
