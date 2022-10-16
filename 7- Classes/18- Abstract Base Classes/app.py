from abc import ABC, abstractmethod


class StreamOpenedError(Exception):
    pass


class Stream(ABC):
    def __init__(self) -> None:
        self.opened = False

    def open(self):
        if self.opened:
            raise StreamOpenedError("Stream is open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise StreamOpenedError("Stream is close")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("read file")


class NetStream(Stream):
    def read(self):
        print("read net")


class MemoryStream(Stream):
    def read(self):
        print("read memory")


stream = MemoryStream()
stream.open()
stream.read()
