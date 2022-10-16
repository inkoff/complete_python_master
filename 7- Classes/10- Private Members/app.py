class Tag:
    def __init__(self) -> None:
        self.__tags = {}

    def add(self, tag: str):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag: str):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag: str, count: int):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = Tag()

cloud.add("Python")
cloud.add("Python")
cloud.add("Python")
cloud.add("Python")
# Ошибки доступа и их надо избежать
# print(cloud._Tag__tags["Python"])
# print(cloud.__tags["Python"])
print(cloud.__dict__)
