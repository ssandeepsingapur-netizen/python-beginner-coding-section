
file = open("demo.txt", "w")
file.write("hello sndy how are you?")
file.close()


file = open("demo.txt", "r")
data = file.read()
file.close()
print(data)

file = open("demo.txt", "a")
file.write(" I am fine.")
file.close()

file = open("demo.txt", "r")

data = file.read()

new_data = data.replace(" ", "")

print(new_data)

file.close()
