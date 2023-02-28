from lesson_7.sem_task_7_4 import file_maker

"""
✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.
"""


def rnd_file_maker(extension: dict):
    for extension, count in extension.items():
        file_maker(extension=extension, count=count)


if __name__ == '__main__':
    ext = {
        'bin': 3,
        'zip': 2
    }
    rnd_file_maker(ext)
