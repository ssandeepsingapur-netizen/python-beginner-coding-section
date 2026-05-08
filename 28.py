num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

choice = input("Enter operation (+,-,*,/): ")

match choice:
    case "+":
        print("Result:", num1 + num2)

    case "-":
        print("Result:", num1 - num2)

    case "*":
        print("Result:", num1 * num2)

    case "/":
        print("Result:", num1 / num2)

    case _:
        print("Invalid Operation")