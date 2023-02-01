from math import gcd
import fractions

"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с
числителем и знаменателем. Программа должна возвращать сумму и
*произведение дробей. Для проверки своего кода используйте модуль
fractions.
"""

first = (input("Числитель a: ") + '/' + input("Знаменатель b: "))
second = (input("Числитель a: ") + '/' + input("Знаменатель b: "))
operation = input("Choose math operation '+' or '*': ")

if operation == '*':
    res = f"{first} * {second} = {int(first.split('/')[0]) * int(second.split('/')[0])}/" \
          f"{int(first.split('/')[1]) * int(second.split('/')[1])}"

elif operation == '+':
    if int(first.split('/')[1]) == int(second.split('/')[1]):
        res = f"{first} + {second} = {int(first.split('/')[0]) + int(second.split('/')[0])}/{int(first.split('/')[1])}"
    else:
        cd = int(int(first.split('/')[1]) * int(second.split('/')[1]) /
                 gcd(int(first.split('/')[1]), int(second.split('/')[1])))
        rn = int(cd / int(first.split('/')[1]) * int(first.split('/')[0]) +
                 cd / int(second.split('/')[1]) * int(second.split('/')[0]))
        g2 = gcd(rn, cd)
        n = int(rn / g2)
        m = int(cd / g2)
        res = f"{first} + {second} = {n}/{m}" if n != m else n
else:
    res = 'Wrong math operation'
print(res)

# first = fractions.Fraction(int(input("Числитель a: ")), int(input("Знаменатель b: ")))
# second = fractions.Fraction(int(input("Числитель a: ")), int(input("Знаменатель b: ")))
# operation = input("Choose math operation '+' or '*': ")
#
# if operation == '+':
#     res = f"{first} * {second} = {first + second}"
# elif operation == '*':
#     res = f"{first} * {second} = {first * second}"
# else:
#     res = 'Wrong math operation'
# print(res)