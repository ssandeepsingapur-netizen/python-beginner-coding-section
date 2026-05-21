class student:
    def __init__(self, name):
        self.name = name
        print(self.name)       
        

def fun():
    s1 = student("john")
    return 


 
fun()  

str = "hello world"
for i in range(len(str)):
    if i == 0:
        print(str[i].upper(), end="")
    elif i == 6:
        print(str[i].upper(), end="")
    else:
        print(str[i], end="")