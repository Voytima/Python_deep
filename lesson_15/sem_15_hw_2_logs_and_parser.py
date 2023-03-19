"""
📌 Возьмите любые 1-3 задачи из прошлых домашних заданий.
   Добавьте к ним логирование ошибок и полезной информации.
   Также реализуйте возможность запуска из командной строки с передачей параметров.
-----------------------------------------------------------------------------------------------------
📌 Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
📌 Возвращается строка в нижнем регистре.
"""
import argparse
from string import ascii_letters
import logging

FORMAT = '{levelname} - {asctime} - {funcName} - {msg}'
logging.basicConfig(filename="str_filter.log", encoding='utf-8', level=logging.INFO, style='{', format=FORMAT)
logger = logging.getLogger(__name__)


def text_filter(string: str) -> str:
    result = ''.join(c for c in string if c in set(ascii_letters + ' '))
    logger.info(f"Initial str: {string}, converted str: {result}")
    return result.lower()


def parser():
    parser = argparse.ArgumentParser(description="Удаление из текста всех символов кроме букв латинского алфавита и "
                                                 "пробелов")
    parser.add_argument('-s', '--string', default='It works!1!!11')
    args = parser.parse_args()
    return text_filter(args.string)


# print(text_filter("C'mon-c'mon, тудуду, be positive!11!1"))
print(parser())
