ZERO = 0
ONE = 1
TWO = 2
THREE = 3
MAX_NUM = 100000

while True:
    n = int(input("Enter any number: "))
    if ZERO <= n < MAX_NUM:
        break

if n in range(ZERO, THREE):
    res = f"Number {n} is prime"

for i in range(TWO, n):
    if n % i == ZERO:
        res = f"Number {n} is composite"
        break
    else:
        res = f"Number {n} is prime"

print(res)
