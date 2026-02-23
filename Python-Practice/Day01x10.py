n = 5

for i in range(n, 0, -1):

    for j in range(1, i + 1):
        print(j, end="")

    spaces = 2 * (n - i)
    for j in range(spaces):
        print("*", end="")

    for j in range(i, 0, -1):
        print(j, end="")

    print()
