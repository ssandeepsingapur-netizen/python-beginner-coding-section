file1 = open("file1.txt" ,mode = "r")
lines = file1.readlines()
file1.close()

clean_lines = []
for line in lines:
    clean_lines.append(line)
    clean_lines.sort()

file2 = open("file4.txt", mode = "w")
for line in clean_lines:
    files = file.write(line+"\n")
print("file saved and sorted")