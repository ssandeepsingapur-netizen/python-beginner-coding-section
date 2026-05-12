num = int(input("enter a number: "))
match num:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case 4:
        print("four")
    case 5:
        print("five")
    case _:
        print("number not in range")


age = int(input("enter your age: "))

match age:
    case age if age <18:
        print("you are a minor")
    case age if age >= 18 and age < 25:
        print("you are a young guy")
    case age if age >= 25 and age < 60:
        print("you are an adult")
    case age if age >= 60 and age < 100:
        print("you are a senior citizen")
    case _:
        print("invalid age")