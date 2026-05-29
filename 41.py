file = open("file txt" , "r")
lines = file.readlines()
file.close()

clean_lines = []
for line in lines:
    clean_lines.append(line.strip())
clean_lines.sort()
file2 = open("file2.txt","w")
for line in clean_lines:
    file2.write(line+"\n")
file2.close()
print("file sorted and saved is completed")
