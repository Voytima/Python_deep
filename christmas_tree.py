ONE = 1

n = int(input("How many layers of the tree: "))

for i in range(n):
    k1 = n - i - ONE
    k2 = n + i - ONE

    for j in range(k2 + ONE):
        if j >= k1:
            print("*", end="")
        else:
            print(" ", end="")

    print()
