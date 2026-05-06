N = int(input("Enter "))
commands = []
for x in range(N):
        commands.append(input().split())
output = []
for x in commands:
        if x[0] == 'insert':
            output.insert(int(x[1]), int(x[2]))
        elif x[0] == 'print':
            print(output)
        elif x[0] == 'remove':
            output.remove(int(x[1]))
        elif x[0] == 'append':
            output.append(int(x[1]))
        elif x[0] == 'sort':
            output.sort()
        elif x[0] == 'pop':
            output.pop()
        elif x[0] == 'reverse':
            output.reverse()