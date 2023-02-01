"""
Напишите программу банкомат.
📌 Начальная сумма равна нулю
📌 Допустимые действия: пополнить, снять, выйти
📌 Сумма пополнения и снятия кратны 50 у.е.
📌 Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
📌 После каждой третей операции пополнения или снятия начисляются проценты - 3%
📌 Нельзя снять больше, чем на счёте
📌 При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
📌 Любое действие выводит сумму денег
"""
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
print(f"Welcome to 'CashToBash ATM'\nCurrent deposit is {balance}\n")
operation = int(input("Choose operation:\n1.Deposit\n2.Withdraw\n3.Exit\n>>> "))

while operation != THREE:
    if operation == ONE:
        if balance > RICH_LIMIT:
            balance -= balance * RICH_PERCENTS
        while True:
            print("_____Minimal deposit should be equal to 50$_____")
            print(f"\nCurrent{balance = :.2f}$\n")
            amount = int(input("Please, enter deposit sum: "))
            if not amount % FIFTY:
                break
        balance += amount
        counter += 1
        print(f"\nCurrent{balance = :.2f}$\n")
        operation = int(input("Choose operation:\n1.Deposit\n2.Withdraw\n3.Exit\n>>> "))

    if operation == TWO and balance != ZERO:
        while True:
            if balance > RICH_LIMIT:
                balance -= balance * RICH_PERCENTS
            print("_____Minimal withdraw should be equal to 50$, withdraw percents - 1.5%_____\n")
            print(f"\nCurrent{balance = :.2f}$\n")
            amount = int(input("Please, enter withdraw sum: "))
            if not amount % FIFTY:
                break
        if (balance - (amount + amount * WITHDRAW_PERCENTS)) < ZERO:
            print("\nNot enough money on deposit")
            print(f"\nCurrent{balance = :.2f}$\n")
            operation = int(input("Choose operation:\n1.Deposit\n2.Withdraw\n3.Exit\n>>> "))
        else:
            if amount * WITHDRAW_PERCENTS <= LOWER_PERCENTS_LIMIT:
                balance -= (amount + LOWER_PERCENTS_LIMIT)
            elif amount * WITHDRAW_PERCENTS >= UPPER_PERCENTS_LIMIT:
                balance -= (amount + UPPER_PERCENTS_LIMIT)
            else:
                balance -= (amount + amount * WITHDRAW_PERCENTS)
            counter += 1
            print(f"\nCurrent{balance = :.2f}$\n")
            operation = int(input("Choose operation:\n1.Deposit\n2.Withdraw\n3.Exit\n>>> "))
    else:
        print(f"\nCurrent{balance = :.2f}$\n")
        operation = int(input("Choose operation:\n1.Deposit\n2.Withdraw\n3.Exit\n>>> "))
    if not counter % THREE:
        balance += balance * BONUS_PERCENTS
else:
    print("\nHave a nice day!")
