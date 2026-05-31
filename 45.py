my_list = [2,4,5,6]
while True:
    print("\n menu")
    print("1 append element")
    print("2 Insert element")
    print("3 Remove element")
    print("4 Display length")
    print("5 pop element")
    print("6 clear list")
    print("7 display list")
    print("Exit")
    choice = int(input("enter your choice"))
    if choice == 1:
        val = int(input("enter the element"))
        my_list.append(val)
        print("updated list:", my_list)
    elif choice == 2:
        val = int(input("enter the element"))
        pos = int(input("enter the position(index)"))
        my_list.insert(pos,val)
        print("updated list:",my_list)
    elif choice == 3:
        val = int(input("enter element to remove"))
        if val in my_list:
            my_list.remove(val)
            print("updated list:",my_list)
        else:
            print("val is not in list")
    elif choice == 4:
        print("length of list",len(my_list))
    elif choice == 5:
        if len(my_list)>0:
            print("popped element is :",my_list.pop())
            print("updated list:",my_list)
        else:
            print("list is empty")
    elif choice == 6:
        my_list.clear()
    elif choice == 7:
        print("current list:",my_list)
    elif choice == 8:
        print("Existing program")
        break
    else:
        print("Invalid choice try again")
    

