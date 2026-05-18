n =int(input("enter the number of tuple element : "))

tuple = ()
for i in range(n):
    element = int(input("enter the element: "))
    tuple += (element,)
print("the tuple is:", tuple)
print("The smallest element in the tuple is:", min(tuple))
print("The largest element in the tuple is:", max(tuple))
print("The sum of all elements in the tuple is:", sum(tuple))
print("The average of all elements in the tuple is:", sum(tuple)/len(tuple))
