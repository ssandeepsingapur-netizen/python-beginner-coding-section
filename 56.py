file = open("fruits.txt",mode= "w")
file.write("apple\nbanana\norange")
file.close()

file = open("fruits.txt",mode= "r")
data = file.readlines()
file.close()

print(data)