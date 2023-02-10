"""
📌 Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные
операции - функции. Дополнительно сохраняйте все операции поступления и
снятия средств в список
"""
from typing import Callable

ZERO = 0
ONE = 1
TWO = 2
THREE = 3
FIFTY = 50
WITHDRAW_PERCENTS = 0.015
BONUS_PERCENTS = 0.03
RICH_PERCENTS = 0.1
LOWER_PERCENTS_LIMIT = 30
UPPER_PERCENTS_LIMIT = 600
RICH_LIMIT = 5_000_000

balance = ZERO
counter = ZERO

logs = []
print(f"Welcome to 'CashToBash ATM'\nCurrent deposit is {balance}\n")


def balance_checker(money: float) -> float:
    if money > RICH_LIMIT:
        money -= money * RICH_PERCENTS
    return money


def operation_type(btn: int) -> str:
    return 'deposit' if btn == 1 else 'withdraw' if btn == 2 else 'exit'


def balance_deposit(plus_money: int) -> Callable[[int], str] | float:
    global balance
    global counter

    if plus_money % FIFTY:
        return operation_type
    balance += plus_money
    logs.append(f"Deposit: + {plus_money}. Current balance: {balance}")
    counter += 1
    return balance


def deposit_balance_printer():
    global balance
    print("_____Minimal deposit should be equal to 50$_____")
    print(f"\nCurrent{balance = :.2f}$\n")


def balance_withdraw(minus_money: int) -> Callable[[int], str] | float:
    global balance
    global counter

    if minus_money % FIFTY:
        return operation_type

    if (balance - (minus_money + minus_money * WITHDRAW_PERCENTS)) < ZERO:
        print("\nNot enough money on deposit")
        return operation_type
    else:
        if minus_money * WITHDRAW_PERCENTS <= LOWER_PERCENTS_LIMIT:
            balance -= (minus_money + LOWER_PERCENTS_LIMIT)
            logs.append(f"Withdraw: - {minus_money}. Current balance: {balance}")
            counter += 1
            return balance
        elif minus_money * WITHDRAW_PERCENTS >= UPPER_PERCENTS_LIMIT:
            balance -= (minus_money + UPPER_PERCENTS_LIMIT)
            logs.append(f"Withdraw: - {minus_money}. Current balance: {balance}")
            counter += 1
            return balance
        else:
            balance -= (minus_money + minus_money * WITHDRAW_PERCENTS)
            logs.append(f"Withdraw: - {minus_money}. Current balance: {balance}")
            counter += 1
            return balance


def withdraw_balance_printer():
    global balance
    print("_____Minimal withdraw should be equal to 50$, withdraw percents - 1.5%_____\n")
    print(f"\nCurrent{balance = :.2f}$\n")


def balance_printer():
    print(f"\nCurrent{balance = :.2f}$\n")


button = operation_type(int(input("Choose operation:\n1.Deposit\n2.Withdraw\n3.Exit\n>>> ")))

while button != 'exit':

    if button == 'deposit':
        balance = balance_checker(balance)
        deposit_balance_printer()

        balance_deposit(int(input("Please, enter deposit sum: ")))

        balance_printer()
        button = operation_type(int(input("Choose operation:\n1.Deposit\n2.Withdraw\n3.Exit\n>>> ")))

    if button == 'withdraw' and balance != ZERO:
        balance = balance_checker(balance)
        withdraw_balance_printer()

        balance_withdraw(int(input("Please, enter withdraw sum: ")))

        balance_printer()
        button = operation_type(int(input("Choose operation:\n1.Deposit\n2.Withdraw\n3.Exit\n>>> ")))

    if not counter % THREE:
        balance += balance * BONUS_PERCENTS
else:
    print("\nHave a nice day!")
    if logs:
        print(f"Operation logs:\n{logs}")
