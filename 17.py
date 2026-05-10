n =int(input("enter number")) 
try:
    divide = 10/n
    print(divide)
except (ZeroDivisionError,ValueError) as e:
    print("error we cannot divide by using this",e)


age = int(input("enetr age"))

try:
  if age>18:
    print("eligible")
except ValueError:
    print("valid input")





