class complex:
    def __init__(self,real,image):
        self.real = real
        self.image = image
    
    def add(self,other):
        real_part = self.real+other.real
        imaginary_part =self.image+other.image
        return complex(real_part,imaginary_part)
    def show(self):
        print(f"{self.real}+{self.image}")

N = int(input("enter elemnt for complex"))
if N<2:
    print("enter number atlest 2")
else:

    complex_list = []
    for i in range(N):
        print(f"enter complex elemnt {i+1}")
        r= int(input("enter the real part"))
        im = int(input("enter imaginary part"))
        complex_list.append(complex(r,im))

    result = complex_list[0]
    for i in range(1,N):
        result = result.add(complex_list[i])
    
print("sum of complex number")
result.show()