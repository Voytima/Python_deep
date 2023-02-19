from datetime import datetime
from sys import argv

"""
📌 Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
📌 Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
📌 Для простоты договоримся, что год может быть в диапазоне [1, 9999].
📌 Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
📌 Проверку года на високосность вынести в отдельную защищённую функцию
"""
__all__ = ['date_checker']


def _year_checker(my_year: int) -> bool:
    if my_year % 4 == 0 and (my_year % 100 != 0 or my_year % 400 == 0):
        return True
    return False


def date_checker(my_date: str) -> bool:
    pattern = "%d.%m.%Y"
    try:
        dt = datetime.strptime(my_date, pattern)
        my_year = dt.year
        _year_checker(my_year)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    print(date_checker(input("Enter date in format DD.MM.YYYY:\n>>> ").replace('/', '.')))
