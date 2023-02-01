TWO = 2
SIX = 6
TEN = 10
ELEVEN = 11

for x in range(TWO, ELEVEN):
    for y in range(TWO, SIX):
        print(f'\t\t\t{y} X {x} = {y * x}', end='')
    print('')
print()
for i in range(TWO, ELEVEN):
    for j in range(SIX, TEN):
        print(f'\t\t\t{j} X {i} = {j * i}', end='')
    print('')
