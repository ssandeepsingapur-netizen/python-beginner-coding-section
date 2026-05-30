import math
n= int(input("enter the number  of element"))
numbers = []
for i in range(n):
    num = float(input("enter element{i+1}:"))
    numbers.append(num)

mean = sum(numbers)/n
variance = sum((x-mean)**2 for x in numbers)

std_deviation = math.sqrt(variance)

print("Mean:",mean)
print("Variance:",variance)
print("standard_deviation:",std_deviation)