"""
📌 Возьмите любые 1-3 задачи из прошлых домашних заданий.
   Добавьте к ним логирование ошибок и полезной информации.
   Также реализуйте возможность запуска из командной строки с передачей параметров.
"""
from random import randint
from typing import Callable
import logging

FORMAT = '{levelname} - {asctime} - {msg}'
logging.basicConfig(filename="guesser.log", encoding='utf-8', level=logging.INFO, style='{', format=FORMAT)
logger = logging.getLogger(__name__)


def logs(tries, guess_number, user_num, result, num2):
    logger.info(f"Try {tries} out of {num2}, Value to guess: {guess_number}, Entered value: {user_num}, Result: {result}")


def incoming_num(tries=5) -> Callable[[], None]:
    def guess_num():
        result = "Undefined"
        guess_number = randint(1, 100)
        for i in range(1, tries + 1):
            print(f"Попытка номер {i}:")
            try:
                user_num = int(input("Введите число от 1 до 100:\n>>> "))
            except ValueError:
                logger.error("Entered not an int value. Aborted...")
                print("Not an int num")
                break
            if user_num == guess_number:
                print("Вы угадали!")
                result = "You won!"
                logs(tries=i, guess_number=guess_number, user_num=user_num, result=result, num2=tries)
                break
            elif user_num < guess_number:
                print("Ваше число меньше")
                result = "User num is lesser"
            elif user_num > guess_number:
                print("Ваше число больше")
                result = "User num is greater"
            logs(tries=i, guess_number=guess_number, user_num=user_num, result=result, num2=tries)
        else:
            result = "No more tries"
            logs(tries=None, guess_number=guess_number, user_num=user_num, result=result, num2=tries)

    return guess_num


game = incoming_num()
game()

