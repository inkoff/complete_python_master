class Text(str):
    def dublicate(self):
        return self + self


dubl = Text("Py")

print(dubl.dublicate())


class LogList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


list = LogList()

list.append("1")
