"""
📌 Создайте класс Моя Строка, где:
    📌 будут доступны все возможности str
    📌 дополнительно хранятся имя автора строки и время создания (time.time)
"""
from datetime import datetime


class MyStr(str):
    """
    Modified str class with additional fields:
    * string author
    * time of creation.
    """
    def __new__(cls, value: str, author: str) -> str:
        """
        Modifies return of a string.

        In addition to input string, class also required name of the author.
        Creation time will be generated automatically.
        :param value:
        :param author:
        """
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = datetime.now().time().strftime("%H:%M:%S")
        return instance

    def __str__(self):
        """Returns all data like __repr__ call instead of __str__"""
        return f"String: {self!r}; Author: {self.author}; Creation time: {self.time}"


if __name__ == '__main__':
    s = MyStr("Hello world!", 'Dima')
    print(s)
