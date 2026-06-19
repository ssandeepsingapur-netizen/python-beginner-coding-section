x = int(input("enter a number:"))
shoe_size = []
for i in range(x):
    shoe_size.append(int(input("enter shoe size:")))

N = int(input("enter number of customers:"))
xi = []
for i in range(N):
    xi.append(int(input("enter price of shoe:")))
    print(shoe_size[i],xi[i])

print(sum(xi))