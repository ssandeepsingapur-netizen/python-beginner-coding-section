def divExp(a, b):
    assert a>0 ,"value of a must be greater than 0"
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
        
        c = a / b
        return c
    
try:
    a = int(input("Enter a positive number for a: "))
    b = int(input("Enter a number for b: "))
    result = divExp(a, b)
    print(f"The result of {a} divided by {b} is: {result}")
except AssertionError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except ValueError:
    print("Invalid input. Please enter integers for a and b.")