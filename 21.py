N = int(input())
l = []
for i in range(N):
    val =input("enter number")
    l.append(val)
print(l)
l.pop()
l.append(5)
l.append(12)
print(l)