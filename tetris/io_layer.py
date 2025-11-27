from typing import Protocol, List

class Reader(Protocol):
    def read_all(self) -> List[str]:
        ...

class Writer(Protocol):
    def write_lines(self, lines: List[str]) -> None:
        ...

class FileReader:
    def __init__(self, file_path: str):
        self.file_path = file_path
    def read_all(self) -> List[str]:
        with open(self.file_path, 'r', encoding = "utf-8") as file:
            return file.readlines()

class FileWriter:
    def write_lines(self, lines: List[str]) -> None:
        for line in lines:
            print(line)



