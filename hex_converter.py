"""
Напишите программу, которая получает целое число и возвращает его
шестнадцатеричное строковое представление. Функцию hex используйте для
проверки своего результата.
"""
HEX = 16
ZERO = 0
n = int(input("Enter num to convert: "))

# Control:
print(f"Control: {hex(n)}")

# Option 1:
print(f"Option 1: {'%#x' % n}")

# Option 2:
hex_dict = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
res = []

while n > ZERO:
    res.append(hex_dict[n % HEX])
    n = n // HEX
res.reverse()
print(f"Option 2: 0x{''.join(res)}")
