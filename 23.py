a=int(input("enter the number"))
b =int(input("enter the number"))
try:
    divide = a/b
    print(divide)
except ZeroDivisionError:
    print("Not possible divide")

except ValueError:
    print("Give  only numbers")#

def fun(a,b):
    if a==b:
        print("this recursion function")
    elif a>=b:
        a = a-b
       
        print(a,b)
        return fun(a,b)
    elif a<=b:
        b= b-a
        print(a,b)
        return fun(a,b)
    

fun(5,4)

