class complex:
    def __init__(self,real,image):
        self.real = real
        self.image = image
    def add(self,other):
        real_part = self.real+other.real
        imginary_part = self.image+other.image
        return complex(real_part,imginary_part)
    def display(self):
        print(f"{self.real}+{self.image}")

N = int(input("enter value must be greater than 2"))
if N<2:
    print("atleast enter the two number ")
else:
    complex_list = []
    for i in range(N):
        print(f"enter the complex number {i+1}")
        r = int(input("enter real_part"))
        im = int(input("enter imaginary part"))
        complex_list.append(complex(r,im))

    result =complex_list[0]
    for i in range(1,N):
        result = result.add(complex_list[i])
    print("sum of complex numbers:")
    result.display()

