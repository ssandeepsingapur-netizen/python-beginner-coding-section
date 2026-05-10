import math

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiple(a,b):
    return a*b
def divide(a,b):
    return a/b

num = int(input("enter number"))
a = int(input("enter first number"))
b =int(input("enter second number"))


if num == 1:
    result = add(a,b)
    print(result)
elif num ==2:
    result = sub(a,b)
    print(result)
elif num == 3:
    result = multiple(a,b)
    print(result)

elif num == 4:
    try:
        result =  divide(a,b)
        print(result)
    except ZeroDivisionError:
        print("we cannot divide by using zero")
