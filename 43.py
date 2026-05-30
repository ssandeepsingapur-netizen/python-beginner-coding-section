N = int(input("Enter the value N:"))
fib = [ ]
for i in range(N):
    if i == 0:
        fib.append(0)
    elif i == 1:
        fib.append(1)
    else:
        fib.append((i-1)+(i-2))
        print("fibonnaci sequence:",fib)