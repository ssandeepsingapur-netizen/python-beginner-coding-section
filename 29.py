row = 5

for i in range(row):
    for j in range(row - i - 1):#5-0-1,5-1-1,5-2-1,5-3-1,5-4-1
        print(" ", end= " ")
    for k in range(2 * i + 1):#1,3,5,7,9
        print("*", end= " ")
    print()