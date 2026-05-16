N = int(input("enter a number: ")) #heart pattern
for i in range(N):
    for j in range(N):
        if (i == 0 and j % 3 != 0) or (i == 1 and j % 3 == 0) or (i - j == 2) or (i + j == 8):
            print("*", end="")
        else:
            print(" ", end="")
    print()