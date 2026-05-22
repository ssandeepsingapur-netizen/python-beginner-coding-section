row = int(input("enter number rows"))
columns =int(input("enter number coluns"))

for i in range(row):
        if i == 2:
              print("*")
              continue
        for i in range(columns):
            if i == 3:
                print("#" ,end=" ")
                continue



