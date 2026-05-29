class complex:
    def __init__(self,real,image):
        self.real = real
        self.image = image
    
    def add(self,other):
        real_part = self.real+other.real
        image_part = self.image+other.image
        return complex(real_part,image_part)

    def display(self):
        print(f"{self.real}+{self.image}")

N = int(input("Enter number of complex numbers (N>=2):"))
if N<2:
    print("please enter atleast 2 complex number")
else:
    complex_list = []
    for i in range(N):
        print(f"enter complex number{i+1}:")
        r = int(input("real_part:"))
        im = int(input("imaginary_part"))
        complex_list.append(complex(r,im))
    
    result = complex_list[0]
    for i in range(1,N):
        result = result.add(complex_list[i])
    print("sum of complex numbers")
    result.display()

