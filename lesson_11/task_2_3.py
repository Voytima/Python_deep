"""
📌 Создайте класс Архив, который хранит пару свойств. Например, число и строку.
📌 При создании нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в
пару списков-архивов.
📌 list-архивы также являются свойствами экземпляра.
📌 Добавьте к задачам 1 и 2 строки документации для классов.
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


if __name__ == '__main__':
    d1 = Archive(1, 'aaa')
    d2 = Archive(2, 'bbb')
    print(d2.text, d2.texts)
    d3 = Archive(3, 'ccc')
    print(d3.text, d3.texts)
    print(d1.__doc__)


