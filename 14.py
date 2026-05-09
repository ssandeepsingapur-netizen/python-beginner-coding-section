n = 10
l = []

for i in range(n):
    val = int(input("enter any numbers"))
    l.append(val)

print(l)
print(l.insert(2,15))
print(l.remove(4))
print(l.pop(1))
print(l.index(10))
print(l.count(5))
print(l.sort())
