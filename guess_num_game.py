from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ONE = 1
TEN = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)
counter = TEN

while counter:
    user_num = int(input("Guess the number from 0 to 1000: "))
    print()

    if user_num == num:
        print("You are the winner!")
        break
    elif user_num > num:
        counter -= ONE
        print("Guess number is lower!")
        print(f"{counter} tries left")
        print()
    else:
        counter -= ONE
        print("Guess number is greater!")
        print(f"{counter} tries left")
        print()
else:
    print("No more tries left...")
