"""
📌 Доработаем класс Архив из задачи 2.
📌 Добавьте методы представления экземпляра для программиста и для пользователя.
"""


class Archive:
    """Singleton pattern which saves all previous data in parallel archives."""
    instance = None

    def __new__(cls, *args, **kwargs):
        """
        Just returns values for the first call.

        First call returns entered values, all further function calls return entered values and save
        all previous inputs in parallel archives.
        :param args:
        :param kwargs:
        """
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.counts = []
            cls.instance.texts = []
        else:
            cls.instance.counts.append(cls.instance.count)
            cls.instance.texts.append(cls.instance.text)

        return cls.instance

    def __init__(self, count, text):
        self.count = count
        self.text = text

    def __str__(self):
        """
        Returns information about the created object in user-friendly way.

        Variable count_var stores an empty archive if it was first function call, otherwise stores
        an archive with entered numbers.
        Variable text_var stores an empty archive if it was first function call, otherwise stores
        an archive with entered text.
        :return:
        """
        count_var = self.instance.counts if self.instance.counts else "Empty"
        text_var = self.instance.texts if self.instance.texts else "Empty"
        return f"Value: {self.instance.count}, text: {self.instance.text} " \
               f"value archive: {count_var}, text archive: {text_var}"

    def __repr__(self):
        """Returns an information about the created object for programmers"""
        return f"Archive({self.instance.count}, '{self.instance.text}')"


if __name__ == '__main__':
    # d1 = Archive(1, 'aaa')
    d2 = Archive(2, 'bbb')
    # print(d2.text, d2.texts)
    # d3 = Archive(3, 'ccc')
    # print(d3.text, d3.texts)
    print(f"{d2 = }")
