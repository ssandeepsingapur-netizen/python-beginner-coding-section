def divExp(a,b):
    assert a>0 ,"value of a must be greter than 0"

    if b == 0:
        raise ZeroDivisionError("value of most greate than zero")

    else:
        c = a/b
        return c


try:
    a = int(input("enter the value of a"))
    b = int(input("enter the value of b"))
    result =divExp(a,b)
    print("Result:",result)
except AssertionError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except ValueError:
    print("invalid input")